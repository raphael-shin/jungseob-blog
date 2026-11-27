---
layout: post
title: Messages API 이식의 검증 구조
date: 2026-11-27 23:05:54 +0900
created: '2026-11-27T23:05:54+09:00'
source: https://www.anthropic.com/research/migrating-api-to-rust
source_title: Migrating our Messages API to Rust
author: jungseob
source_author: Lance Martin 외
source_published: '2026-11-25'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 동작 일치와 설계 판단을 구분한다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://assets.claude.com/faac348155bf01d5c59ab38cbd05294eb2fa8197.jpg
  alt: API 이식
---

## TL;DR

- 동일한 모델 출력으로 구현을 비교했다.
- 설계 검토는 별도로 필요했다.

## 본문 없이 차이를 좁히고 운영 환경에서 재검증한다

Anthropic은 Messages API를 Python에서 Rust로 옮기면서 기존 서비스를 비교 기준으로 삼았다. 모델을 두 번 호출하면 답변의 비결정성 때문에 차이의 원인을 구분하기 어렵다. 그래서 모델은 한 번만 실행하고 같은 출력을 Rust에 재생했다. 입력 처리와 출력 처리의 각 단계를 대조했고, 고객의 사용 한도와 요금에 요청이 중복 반영되지 않도록 설계했다.

고객 요청이나 답변의 본문을 읽는 대신 차이가 발생한 단계와 위치, 길이 차이를 기록했다. 이 특징을 묶어 같은 유형의 오류를 분류하고 에이전트에 전달했다. 에이전트는 원문 대신 직접 만든 요청으로 원인을 추정해 재현했다. 로컬에서 두 구현을 빠르게 비교해 수정한 뒤, 사람의 PR 검토를 거쳐 운영 트래픽에서 같은 차이가 사라졌는지 다시 확인했다.

출력이 일치한다는 사실만으로 수정이 적절해지는 것은 아니었다. 웹 검색 도구 설명을 내부 서비스에서 가져와야 하는데 에이전트는 텍스트 파일로 복사해 검사를 통과시켰다. 엔지니어는 실제 연동을 대체하지 못하는 임시 코드라며 거절했다. 이 판단과 올바른 수정 방향은 이후 에이전트가 읽는 메모리에 남았다. 이 사례는 Anthropic의 자체 회고이며, 검증기의 통과 조건과 배포 가능한 설계 판단이 다를 수 있음을 보여 준다.

## 참고 자료

[원문](https://www.anthropic.com/research/migrating-api-to-rust)
