---
layout: post
title: 두 번 만드는 비용이 바뀌면 기술 선택도 바뀐다 - Shopify의 네이티브 복귀
date: '2026-09-11'
last_modified_at: '2026-09-12T12:17:45+09:00'
author: jungseob
categories:
- 지식 노트
tags:
- ai-agents
- engineering
description: Shopify의 네이티브 전환을 구현 비용과 검증 구조의 변화로 읽는다.
source: https://shopify.engineering/back-to-native
source_title: Native is now the future of mobile at Shopify
source_author: Mustafa Ali (Shopify)
source_published: '2026-09-10'
published: true
render_with_liquid: false
image:
  path: https://cdn.shopify.com/b/shopify-brochure2-assets/74f109ae9b0c3034a78a3b63294ae2e6.png
  alt: 원문 대표 이미지 · Native is now the future of mobile at Shopify
---

## TL;DR

- Shopify는 플랫폼별 중복 구현 비용이 줄면서 Swift·Kotlin으로 전환하기로 했다. React Native가 제공했던 이익 자체를 부정한 결정은 아니다.
- 새 코드베이스를 만들되 Helix로 작업을 작은 검증 단위로 나눴다. 전체 재작성과 작은 단위의 검토는 함께 사용할 수 있다.
- 업무 로직을 UI에서 분리한 CLI가 검증 병목을 줄인다. 전환의 성과는 코드 생성량보다 앱 품질과 실제 개발 속도로 판단한다.

## Source

[Native is now the future of mobile at Shopify](https://shopify.engineering/back-to-native)

## Knowledge

### 공유 구현의 이익이 줄어든 조건

Shopify는 React Native가 중복 구현과 플랫폼 간 기능 차이를 줄여줬다고 평가한다. 이후 에이전트가 반대 플랫폼의 코드를 참고해 구현하고 공통 명세·테스트로 차이를 좁히면서 계산이 달라졌다. 네이티브의 플랫폼 접근성과 적은 의존 계층이 상대적으로 매력적이 됐다. 두 코드베이스를 유지하는 비용이 사라진 것은 아니다.

2020년의 선택은 같은 기능을 두 번 만들지 않고 개발자가 스택을 넘나들며 기능 차이를 맞추는 시간을 줄이려는 것이었다. 새 전환에서는 프로토타입으로 재작성 속도를 확인했다. 기존 구현을 참조할 수 있고 과거 구조의 제약을 벗어날 수 있다는 이유로 새 코드베이스를 택했다. 성공했던 선택도 비용의 전제가 바뀌면 다시 검토할 수 있다.

### 새로 만들면서도 작은 단위로 검증한다

Shopify는 기존 앱을 참조해 새 코드베이스를 만드는 방식을 택했다. 그러나 한 번에 전체 구현을 맡기는 시도는 유지하기 어려운 코드를 만들었다. Helix는 화면의 작업을 작은 체크포인트로 나누고 테스트, 시각 검토, 두 코드 리뷰어와 사람의 승인을 거친다. 이전 검토의 피드백도 다음 작업에 반영한다.

여기서 재작성의 범위와 검토의 크기는 별개다. 가령 결제 화면 전체를 새로 만들더라도 주소 입력과 결제 수단 선택을 각각 검토할 수 있다. 이 가상 예에서 각 단계의 통과 조건은 기존 화면과 같은 행동을 하는지다. 작은 단위라면 오류가 어느 변경에서 생겼는지 찾기 쉽고 수정 결과도 빨리 확인할 수 있다. 새로 시작한다는 결정이 한 번에 완성품을 승인한다는 뜻은 아니다.

### 코드 수정 뒤의 대기 시간을 줄인다

시뮬레이터를 스크린샷이나 접근성 트리로 조작하는 과정은 검증 병목이었다. Shopify는 업무 로직을 UI에서 분리해 데스크톱에서 실행하고 CLI로 상태와 행동을 제어했다. 시뮬레이터가 필요하면 원격 모드로 연결한다. 원문 시점에 Shop은 12주 만에 네이티브로 재출시됐고 다른 앱은 전환 중이었다. 전체 전환의 장기 성과가 확정된 결과는 아니다.

검증 경로를 나눈다는 생각은 프레임워크를 유지하는 팀에도 적용할 수 있다. 예를 들어 할인 계산은 화면 없이 확인하고 실제 버튼의 조작 가능성은 화면에서 확인하는 식이다. 전자는 빠른 반복에 적합하고 후자는 사용자 경험의 오류를 찾는다. 이 예시는 Shopify의 별도 실측이 아니라 구조를 이해하기 위한 설명이다. 검증을 빠르게 만들면서도 어떤 오류를 각 경로가 책임지는지 분명히 해야 한다.


## 더 생각해보기

- 지금 기술 선택을 지탱하는 비용 가정 중 무엇이 달라졌는가?
- 화면 없이 실행할 수 없는 업무 로직은 어디에 남아 있는가?
