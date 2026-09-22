---
layout: post
title: "Linear의 CI 개선과 테스트 격리를 푸는 조건"
date: "2026-09-22"
created: "2026-09-22T23:02:58+09:00"
source: "https://linear.app/now/ci-bottleneck-reworked"
source_title: "AI coding has made CI a bottleneck, so we reworked ours to keep up"
author: jungseob
source_author: "Mufeez Amjad"
source_published: "2026-09-21"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Linear의 CI 개선을 준비 비용, 파일 분할, 모듈 상태 공유의 조건으로 살펴본다."
tags: [knowledge, blog, testing, ci, performance]
image:
  path: "https://webassets.linear.app/images/ornj730p/production/eba763cf034ad5e7b5d75ceec7ba560dd2aea5cb-2400x1350.png?q=95&auto=format&dpr=2"
  alt: "Linear CI 최적화 원문 대표 이미지"
---

## TL;DR

- Linear는 늘어난 테스트를 처리하면서 PR 대기와 테스트당 러너 시간을 함께 줄였다.
- 파일 분할은 작업량을 나누지만 준비 비용도 반복한다. 실제 대기 시간과 누적 실행 시간을 구분해서 측정해야 한다.
- Linear는 안전한 파일만 모듈 상태를 공유하고 나머지는 격리를 유지했다.

## 기다리는 시간과 사용하는 시간을 함께 줄이기

Linear의 테스트 묶음은 연초보다 거의 네 배로 커졌다. PR의 CI 대기는 6분 초과에서 5분 남짓으로 줄었고 테스트당 러너 시간도 약 절반이 됐다. 병렬 분할로 대기를 줄여도 준비 작업이 반복되면 총비용은 커질 수 있어 두 지표를 함께 추적했다.

테스트 뒤에 실행하던 캐시 표시 기록을 병합의 필수 경로에서 빼자 대기가 42초 줄었다. 몇 초짜리 검사 7개는 작업 2개 안에서 동시에 실행해 준비 비용을 줄였다. `node_modules` 복원은 약 28초로 필요한 패키지만 설치하는 약 7.5초보다 느려서 제거했다. [Linear의 개선 사례](https://linear.app/now/ci-bottleneck-reworked)

## 파일을 나누는 단위와 시간 지표

Vitest의 기본 샤딩은 개별 테스트 사례가 아닌 파일을 여러 실행에 나누어 배정한다. 파일 수가 같아도 각 파일에 들어 있는 테스트 수와 실행 시간은 다를 수 있다. 큰 파일 하나에 작업이 몰렸다면 샤드 수만 늘려도 그 파일이 끝나는 시간을 기다리게 된다. [공식 성능 문서](https://vitest.dev/guide/improving-performance.html#sharding)의 분할 단위를 보면 파일 크기와 실행 시간의 분포를 함께 살펴야 하는 이유를 알 수 있다.

같은 문서에서 `Duration`의 단계별 비율은 벽시계 시간에 대한 비율이 아니라 추적한 단계 시간의 합을 기준으로 한다. 여러 워커가 동시에 실행되므로 그 합은 실제 경과 시간보다 클 수 있다. `import`는 테스트 파일과 모듈의 평가를, `setup`은 준비 파일의 실행을 따로 집계한다. 테스트 자체보다 환경 생성과 반복 import가 오래 걸리는 경우에는 테스트 코드의 속도만 살펴서는 원인을 찾기 어렵다.

## 상태 공유로 줄인 반복 작업과 남겨 둔 격리

Linear는 큰 테스트 파일을 나누고 준비 비용을 줄인 뒤 샤드를 늘렸다. 이어 안전한 파일만 `isolate: false` 프로젝트에 넣어 모듈 상태를 공유했다. API 샤드의 누적 러너 시간은 실행당 약 32.8분에서 22분으로 줄었다. 참여 표시와 상태 정리를 명시했고 안전하게 분리하지 못한 가짜 타이머·공유 상태 사용 파일은 격리 프로젝트에 남겼다.

[Vitest의 격리 설정](https://vitest.dev/config/isolate.html)은 기본값이 `true`다. 이를 끄면 같은 워커의 파일들이 환경과 모듈 상태를 공유하므로 파일마다 깨끗한 상태를 전제로 하는 테스트에서는 실행 조건이 달라진다. `projects`를 나누면 일부 파일에만 격리 해제를 적용할 수 있다. 공식 성능 문서도 부작용에 의존하지 않고 상태를 제대로 정리하는 경우를 조건으로 삼으며 `vmThreads`에서는 격리를 끌 수 없다고 명시한다.

여기서 확인할 대상은 공유 모듈을 매번 다시 평가하는 비용과 테스트가 남기는 상태다. 성능 문서는 import 단계가 반복된 모듈 그래프 평가로 커지는 경우를 별도로 설명한다. 파일들이 그 상태를 공유해도 올바르게 동작하는지에 따라 적용 범위가 달라진다. Linear의 시간 절감은 그들이 선택한 파일과 준비 절차에서 관찰한 결과이며 다른 테스트 묶음의 절감률이나 격리 해제의 안전성을 보장하지 않는다.

## 참고 자료

[Linear 원문](https://linear.app/now/ci-bottleneck-reworked)

[Vitest — Improving Performance](https://vitest.dev/guide/improving-performance.html)

[Vitest — isolate](https://vitest.dev/config/isolate.html)
