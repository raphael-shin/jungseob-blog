---
layout: post
title: "OpenAI는 비용 절감 모드에 들어갔을 수 있다"
date: "2026-11-28 10:47:19 +0900"
created: "2026-11-28T10:47:19+09:00"
source: "https://micjm.com/blog/openai-is-in-cost-control-mode/"
source_title: "OpenAI may be in cost control mode"
author: jungseob
source_author: "micjm"
source_published: "2026-11-26"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "OpenAI의 Astra 6.2와 Sol 6.2는 비용을 아끼는 쪽으로 조정된 것으로 보인다. 우리 대결 데이터에서 두 모델은 작업당 출력 토큰과 추론 토큰이 전작보다 줄었고 상대 모델에 비해 생각을 덜 하는 이상치가 됐다."
tags:
  - knowledge
  - blog
  - AI
  - web
  - OpenAI
  - 비용
  - 평가
  - 벤치마크
---

## TL;DR

- OpenAI의 Astra 6.2와 Sol 6.2는 비용을 아끼는 쪽으로 조정된 것으로 보인다. 우리 데이터에서 작업당 출력 토큰과 추론 토큰이 줄었다.
- 같은 대결의 상대와 비교하면 전작인 Astra 6과 Sol 6.1은 평범했지만 6.2 두 모델은 추론을 훨씬 덜 하는 이상치다.
- 감소는 통계적으로 유의미하다. p값은 출력에서 Sol 0.0055와 Astra 0.022이고 추론에서 Sol 0.00013과 Astra 0.0064다.

## 출력 토큰과 추론 토큰이 줄었다

OpenAI가 최근 내놓은 Astra 6.2와 Sol 6.2는 널리 혹평을 받았다. 무슨 일이 있었을까. 우리 데이터로 보면 두 모델은 비용을 아끼는 쪽으로 조정된 것으로 보인다. 구체적으로는 작업당 출력 토큰과 작업당 추론 토큰이 줄었다. 추론 토큰은 모델이 답을 내기 전에 생각하는 데 쓰는 토큰이다.

GPT-6에서 GPT 6.2로 오면서 비용이 어떻게 변했는지 차트로 그렸다. 가로축은 실제 작업으로 맞붙이는 우리 대결 시스템에서 GPT 모델이 상대 모델에 비해 돈을 얼마나 썼는지의 비율이다. 세로축은 우리 리더보드의 Elo 점수다. Elo는 맞대결 승패로 실력을 매기는 점수다. 차트에 나타난 이동은 유의미하고 신뢰 구간을 넣어 그려도 마찬가지다.

## 무엇이 달라졌나

상대 모델과 비교하면 Astra와 Sol은 추론을 훨씬 덜 하는 것으로 보인다. 같은 대결에서 모델이 상대보다 얼마나 추론하는지를 그리면 기준선 위는 더 많이, 아래는 더 적게 추론한다는 뜻이다. Astra 6과 Sol 6.1은 꽤 평범한 모델이었다. 그런데 Astra 6.2와 Sol 6.2는 이상치가 됐다. 출력 토큰에서도 같은 효과가 보인다.

이 변화는 유의미한가. 출력 감소의 p값은 Sol이 0.0055이고 Astra가 0.022다. 추론 감소의 p값은 Sol이 0.00013이고 Astra가 0.0064다. p값은 이런 차이가 우연히 나올 확률을 뜻하고 작을수록 우연으로 보기 어렵다. 결론적으로 Astra와 Sol은 전작에 비해 비용에 맞춰 조정된 것으로 보인다. 그 정도가 커서 두 모델은 생각을 덜 하는 이상치가 됐다.
