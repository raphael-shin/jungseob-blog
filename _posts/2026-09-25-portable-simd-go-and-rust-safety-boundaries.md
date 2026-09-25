---
layout: post
title: "Go와 Rust의 SIMD 추상화, CPU 차이와 안전성을 다루는 방식"
date: "2026-09-25"
created: "2026-09-25T23:04:58+09:00"
source: "https://go.dev/blog/simd-experiment"
source_title: "Platform-independent SIMD in Go"
author: jungseob
source_author: "David Chase, Junyang Shao"
source_published: "2026-09-24"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Go의 실험적 SIMD와 Rust Fearless SIMD 1.0의 이식성·분기·안전성 설계를 비교한다."
tags: [knowledge, blog, performance, simd]
image:
  path: "https://go.dev/doc/gopher/gopher5logo.jpg"
  alt: "Go 공식 블로그의 Gopher 대표 이미지"
---

## TL;DR

- Go의 실험적 `simd`는 벡터 폭을 타입에서 분리하고, 컴파일러가 만든 특수화 구현을 실행 환경에 맞춰 선택한다.
- Fearless SIMD는 경계값 의미가 일정한 연산과 플랫폼별 결과를 허용하는 빠른 연산을 구분한다. 안전성은 작은 공통 구현의 정확성을 전제로 한다.
- 이식 가능한 API에서도 미지원 연산과 에뮬레이션을 확인해야 한다. Go의 실험 단계와 Fearless SIMD의 코어·매크로 버전도 서로 구분된다.

## Go는 벡터 폭과 실행 분기를 컴파일러로 옮긴다

Go 1.27의 실험적 `simd`는 CPU마다 다른 벡터 폭과 마스크 표현을 감춘다. `archsimd`가 아키텍처별 기능을 노출하는 데 비해 공통 연산과 에뮬레이션을 제공한다. `Float32s`처럼 폭을 고정하지 않은 타입을 쓰고 `Len()`으로 처리할 원소 수를 구한다. 원문의 내적 예제는 남은 원소를 부분 로드로 처리한다. [Go 공식 원문](https://go.dev/blog/simd-experiment)

컴파일러는 SIMD 타입을 사용하는 함수·변수·타입의 특수화 버전을 만든다. 필요한 경계에서 시작 시 감지한 SIMD 수준에 맞는 구현을 선택한다. 특수화 함수끼리는 직접 호출하므로 계산 내부의 반복 분기 비용을 피한다. 코드 복제와 분기 위치를 조정하는 설계이며 모든 프로그램의 속도 향상을 보장하는 수치는 아니다.

## Rust는 연산 의미와 안전성의 근거를 나눈다

[Shnatsel의 Fearless SIMD 1.0 소개](https://linebender.org/blog/fearless-simd-1-0/)는 같은 이름의 연산도 플랫폼마다 경계값 결과가 다를 수 있다는 문제를 다룬다. 원소 재배열이나 부동소수점 최댓값에는 일관된 결과를 주는 정밀 버전과 플랫폼 차이를 허용하는 빠른 버전이 있다. 경계값이 나오지 않는다는 전제가 있을 때 후자를 선택할 수 있다. 하드웨어 고유 폭과 고정 폭을 모두 지원하며 필요한 부분만 플랫폼 명령으로 내려갈 수도 있다.

안전성 설계는 `kernel!` 매크로와 안전한 타입 변환 모듈에 집중한다. 컴파일러의 target feature 지원으로 대부분의 SIMD 명령을 안전하게 호출하고 포인터 기반 로드·스토어는 재사용하는 래퍼로 모은다. 프로젝트가 제시하는 메모리 안전성의 근거는 이 공통 구성 요소가 올바르다는 조건이다. 코드 곳곳의 개별 `unsafe` 블록 대신 작은 기반 구현을 감사하도록 범위를 좁힌다. 이를 독립적인 보안 감사가 끝났다는 뜻으로 읽어서는 안 된다.

## 미지원 기능과 안정화 범위는 여전히 남는다

Go에서는 `GOEXPERIMENT=simd`로 기능을 켠다. 원문 시점의 1.27에는 `ReduceSum`이 없으며 다음 릴리스에 추가할 계획이다. `ToArch()`로 특정 아키텍처 구현을 보충할 수 있지만 다른 플랫폼과 에뮬레이션 경로도 작성해야 한다. `GODEBUG=simd=0`은 하드웨어가 있어도 에뮬레이션을 강제하므로 해당 경로를 점검할 수 있다.

Fearless SIMD는 코어 1.0과 별도로 `#[simd]`를 제공하는 매크로 패키지 0.1을 발표했다. 함수마다 인라이닝을 조정하는 부담을 줄이지만 사용 편의성은 더 바뀔 수 있는 영역이다. 프로젝트는 코어 안정성과 3년 보안 업데이트를 약속하며 표준 `std::simd`가 안정화돼도 멀티버저닝 같은 역할이 남는다고 본다. 두 발표는 하나의 코드를 여러 CPU에서 실행하는 방법을 넓히지만 실험적 API와 라이브러리의 유지보수 약속은 같은 보장이 아니다.

## 참고 자료

[Go — Platform-independent SIMD in Go](https://go.dev/blog/simd-experiment)

[Linebender — Fearless SIMD v1.0 is here](https://linebender.org/blog/fearless-simd-1-0/)
