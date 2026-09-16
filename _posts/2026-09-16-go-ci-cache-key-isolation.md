---
layout: post
title: 병렬 Go CI를 느리게 만든 공유 캐시 키
date: '2026-09-16'
created: '2026-09-16T23:04:15+09:00'
source: https://www.cloudx.ai/posts/setup-go
source_title: Scaling Golang CI by Replacing actions/setup-go
author: jungseob
source_author: Lukas Schwab and Peter Downs
source_published: '2026-09-16'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: CloudX의 Go CI 사례를 통해 원격 캐시 키의 충돌, 실행별 갱신과 테스트 재사용 조건을 살펴본다.
tags:
- knowledge
- blog
- go
- github-actions
- caching
image:
  path: https://www.cloudx.ai/images/posts/setup-go/setup-go-hero.png
  alt: CloudX의 병렬 Go CI 캐시 구조를 다룬 원문 대표 이미지
---

## TL;DR

- 병렬 작업이 같은 원격 캐시 키를 쓰면, 한 작업이 남긴 불완전한 캐시를 다른 작업이 반복해서 복원할 수 있다.
- 작업별 접두사와 실행별 저장 키는 캐시 분리와 갱신을 함께 다룬다.
- 테스트 패키지 실행 횟수의 감소와 전체 CI 시간의 감소는 서로 다른 지표다.

## lint가 남긴 캐시를 test가 계속 받았다

CloudX의 병렬 Go CI에서는 lint와 test 작업이 같은 원격 캐시 키를 사용했다. lint가 먼저 저장하면 테스트 결과가 충분히 담기지 않은 캐시가 남았고 뒤의 test 작업은 이를 반복해서 복원했다. 실행을 마친 워커에 새 결과가 쌓여도 다음 워커가 받는 원격 캐시는 그대로여서 불필요한 재실행이 이어졌다.

이 현상은 [GitHub Actions 캐시의 저장 규칙](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching)과 연결된다. 기존 키에 저장한 내용은 수정할 수 없으며 새 내용을 보관하려면 새 키가 필요하다. 정확히 일치하는 키가 없을 때는 `restore-keys`로 부분 일치를 찾고 성공한 작업이 새 캐시를 저장한다. 부분 일치 후보가 여럿이면 가장 최근 캐시를 복원한다. 따라서 캐시 복원 성공 여부만으로 이번 작업에 필요한 결과가 충분히 들어 있는지 판단할 수는 없다.

## 작업 종류와 실행마다 저장 키를 나눈다

[CloudX의 공개 구현](https://github.com/cloudx-io/setup-go)은 `cache-key-prefix`로 작업별 캐시를 분리한다. test와 lint가 서로 다른 접두사를 사용하고 운영체제·아키텍처·Go 버전·브랜치·의존성 해시 뒤에는 `run_id`를 붙인다. 새 실행은 새 키에 저장하면서 복원할 때는 접두사로 이전 실행의 캐시를 찾는다. 같은 브랜치와 의존성 해시를 우선하고 없으면 더 넓은 브랜치·의존성 범위로 탐색한다. 실패한 작업의 최종 상태는 저장하지 않는다.

이때 복원한 파일에서 무엇을 다시 쓸지는 Go 도구가 판단한다. [Go 공식 문서](https://pkg.go.dev/cmd/go#hdr-Build_and_test_caching)에 따르면 빌드 캐시는 소스 파일과 컴파일러, 컴파일 옵션의 변경을 반영한다. `GOCACHE`는 이 결과를 보관하는 디렉터리이고 `go env GOCACHE`로 위치를 확인할 수 있다. 원격 저장소는 파일 묶음을 옮기고 Go는 개별 결과의 재사용 가능성을 확인하므로 두 캐시의 키가 같은 수준의 정보를 표현할 필요는 없다.

## 성능 수치는 비교 기준부터 확인한다

CloudX가 공개한 차트 설명은 테스트 작업 중앙값이 131초에서 41초로 줄었다는 내용이다. 이 값으로 계산한 감소율은 약 69%다. 하지만 같은 글의 앞선 설명에는 느려진 중앙값을 180초로 적어 두었다. 두 기준의 집계 구간 차이는 분명하지 않아 180초에서 41초로 줄면서 69% 개선됐다고 연결하지 않는다.

또 다른 수치는 4,011개 커밋을 대상으로 캐시 키에 따른 재사용을 모델링한 결과다. 캐시 없이 실행할 테스트 패키지 수는 526,166회에서 71,928회로 약 86% 감소했다. 이는 실제 전체 CI 시간이나 청구액이 같은 비율로 줄었다는 뜻은 아니다. CloudX는 캐시 객체가 늘면서 복원 시간과 저장 용량도 부담이 되어 정리 절차를 추가했다.

## 테스트 재사용이 성립하는 조건

Go의 테스트 결과 캐시는 `go test ./...`처럼 패키지를 명시하는 모드에서 성공한 결과에 적용된다. 인자 없이 실행하는 `go test`는 이 결과 캐시를 사용하지 않는다. 재사용에는 같은 테스트 바이너리와 허용된 플래그 조합이 필요하고 모듈 안에서 읽은 파일이나 참조한 환경변수가 바뀌면 캐시 일치 조건도 달라진다. `-count=1`은 테스트 결과 재사용을 명시적으로 끈다. 따라서 원격 캐시 구성을 바꾸기 전에 실제 테스트 명령의 캐시 조건도 함께 확인해야 한다.

CloudX 구현은 저장 직전에 오래 사용하지 않은 `GOCACHE` 파일을 정리하며 기본 유예 시간은 2시간이다. 오래된 파일을 모두 다음 실행으로 옮기는 비용을 줄이는 선택이다. 다만 이 구현의 정리 정책과 Go 자체의 정리를 혼동해서는 안 된다. [Go 공식 문서](https://pkg.go.dev/cmd/go#hdr-Build_and_test_caching)는 최근 사용하지 않은 캐시 데이터를 주기적으로 삭제한다고 명시한다. CI에서 복원하는 파일 묶음의 크기는 별도로 측정해야 한다.

## 참고 자료

[Scaling Golang CI by Replacing actions/setup-go — CloudX](https://www.cloudx.ai/posts/setup-go)

[cloudx-io/setup-go 구현과 캐시 정책](https://github.com/cloudx-io/setup-go)

[GitHub Actions: Dependency caching reference](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching)

[Go command: 테스트 실행과 캐시](https://pkg.go.dev/cmd/go)
