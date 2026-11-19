---
layout: post
title: "머스크, Grok Bot 안에서 Grok 4.8을 시험한다"
date: "2026-11-19 19:49:36 +0900"
created: "2026-11-19T19:49:36+09:00"
source: "https://x.com/firesidealpha/status/2123203404365480234"
source_title: "Elon Musk reveals Grok 4.8 is in the RL phase"
author: jungseob
source_author: "Fireside Alpha (@firesidealpha, 일론 머스크 발언 클립)"
source_published: "2026-11-19"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "X 계정 Fireside Alpha가 올린 일론 머스크의 49초 발언 클립을 정리한다. 머스크는 xAI가 지금 Grok 4.8을 강화학습 단계에서 만들고 있고, Grok Bot 안에서 주기적으로 조용한 출시를 한다고 말한다. 그래서 Grok Bot 사용자가 겪는 것은 때때로 쓸모를 시험 중인 여러 버전의 Grok이고, 사용자 문제를 풀었는지 못 풀었는지가 다시 Grok을 고치는 데이터가 된다. 그는 이것을 Grok Bot을 계속 낫게 하는 데이터 플라이휠이라고 부른다. 같은 계정이 앞서 올린, 학습 스택을 처음부터 다시 썼다는 발언도 함께 짚는다."
image:
  path: "https://pbs.twimg.com/amplify_video_thumb/2123203177302589440/img/uTZuGCtMrKWmio_D.jpg"
  alt: "일론 머스크 Grok 4.8 발언 클립 썸네일"
tags:
  - knowledge
  - blog
  - AI
  - GrokBot
  - xAI
---

## TL;DR

- 머스크는 xAI가 지금 Grok 4.8을 만들고 있고, 모델이 강화학습(RL) 단계에 있다고 말한다. 강화학습은 사전 학습을 마친 모델을 보상 신호로 다듬는 단계다.
- 그는 xAI가 Grok Bot 안에서 주기적으로 조용한 출시(soft release)를 한다고 밝힌다. 그래서 Grok Bot 사용자가 겪는 것은 때때로 쓸모를 시험 중인 여러 버전의 Grok이다.
- 시험의 기준은 사용자 문제를 풀었느냐다. 풀었는지 못 풀었는지가 다시 Grok을 고치는 데이터가 되고, 그는 이것을 Grok Bot을 계속 낫게 하는 좋은 데이터 플라이휠이라고 부른다.
- 같은 계정이 2분 앞서 올린 클립에서 머스크는 xAI가 6~8개월 동안 학습, 강화학습, 추론 스택 전체를 C와 일부 C++로 처음부터 다시 썼고, 세계 최고의 학습 스택일 수 있다고 말한다. 이 노트는 그 클립 영상은 보지 않고 게시물에 옮겨진 인용만 읽었다.

## 무슨 영상인가

X 계정 Fireside Alpha가 한국 시간 2026년 11월 19일 올린 48.8초짜리 영상 클립이다. 일론 머스크가 말하는 장면이지만 어느 행사나 인터뷰에서 나온 발언인지는 게시물에 나오지 않는다. 이 노트는 게시물 본문에 옮겨진 인용과, 영상 음성을 직접 받아 Whisper로 받아쓴 전사를 대조해 읽었다. 두 글은 거의 같다. 다만 게시물은 말을 조금 다듬었다. 예를 들어 머스크가 "그 데이터로 문제를 풀었는지 못 풀었는지"라고 말한 대목을, 받아쓴 전사는 일부를 흐리게 잡았다. 게시물은 이 영상이 같은 계정의 앞선 게시물을 인용하는 형태라, 그 앞선 클립의 인용도 함께 읽었다. 앞선 클립의 영상 자체는 열지 않았다.

## Grok 4.8과 조용한 출시

머스크는 긴 답이 되겠다며 말을 꺼낸다. xAI는 지금 Grok 4.8을 작업하고 있고 모델은 강화학습 단계에 있다. 그리고 xAI는 Grok Bot에서 주기적으로 일종의 조용한 출시를 한다. 조용한 출시는 새 버전을 크게 알리지 않고 일부 사용자에게 먼저 내보내는 방식이다. 그래서 그의 말로는 Grok Bot을 쓰는 사람이 겪는 것은 때때로 쓸모를 판단하려고 시험 중인 여러 버전의 Grok이다.

시험의 기준은 그가 분명히 말한다. 사용자의 문제를 풀고 있는가다. 그리고 그 문제를 풀었는지 못 풀었는지에 대한 데이터를 써서 Grok을 고친다. 그는 이것으로 Grok Bot을 시간이 갈수록 계속 낫게 하는 좋은 데이터 플라이휠을 갖췄다고 말한다. 데이터 플라이휠은 제품을 쓸수록 데이터가 쌓이고 그 데이터로 제품이 나아져 더 많이 쓰이는 순환을 말한다.

## 앞선 클립: 학습 스택을 처음부터 다시 쓰다

이 영상이 인용하는 같은 계정의 앞선 게시물은 2분쯤 먼저 올라왔다. 게시물에 옮겨진 인용에 따르면 머스크는 xAI가 학습, 강화학습, 추론 스택 전체를 처음부터 다시 썼다고 말한다. 그 전에는 구글에서 나온 일종의 무료 소프트웨어인 JAX와 SGLang을 썼는데, 그가 보기에 구글이 안에서 쓰는 것에 훨씬 못 미친다. 그래서 평범한 무료 소프트웨어로는 세계 최고 수준의 AI를 만들 수 없다는 게 그의 말이다.

다시 쓴 스택은 하드웨어에서 최고 성능을 끌어내려고 하드웨어에 최대한 가깝게, 주로 C와 일부 C++로 썼다. 그는 소프트웨어 추상화 층이 많을수록 코드 성능이 떨어지고 제3자 소프트웨어는 안에서 무슨 일이 일어나는지 알기 어려운 블랙박스가 되기 쉽다고 말한다. 그리고 이 일이 보통 기준으로는 아주 빠르게, 6~8개월에 걸쳐 일어나고 있으며 이제 소프트웨어가 아주 좋아져 xAI가 세계 최고의 학습 스택을 가졌을 수도 있다고 말한다. 그 결과는 앞으로 나올 모델에서 보게 될 거라고 덧붙인다.

## 읽을 때 생각할 점

49초짜리 클립이고 어떤 자리에서 어떤 질문에 답한 것인지 맥락이 없다. Grok 4.8의 일정, 조용한 출시의 범위, "세계 최고의 학습 스택"은 모두 xAI를 이끄는 머스크의 말이고 확인된 사실이 아니다. 출처 계정 Fireside Alpha는 발언 클립을 모아 올리는 계정이라 원본 영상의 출처도 게시물에 나오지 않는다.

그래도 이 발언에는 실무에서 짚어 볼 점이 있다. Grok Bot 사용자가 자기도 모르게 시험 중인 모델을 쓸 수 있다는 뜻이기 때문이다. 이 블로그의 [Grok Bot 토큰 청구서 노트](https://raphael-shin.github.io/jungseob-blog/posts/maestro-grok-bot-token-bill-12-settings/)나 [XCreators의 Grok Bot 안내서 노트](https://raphael-shin.github.io/jungseob-blog/posts/xcreators-grok-bot-guide-for-creators/)처럼 Grok Bot을 업무에 쓰는 이야기를 읽을 때, 같은 이름 아래에서도 모델이 바뀔 수 있다는 점을 함께 고려해야 한다. 같은 일을 해도 결과가 달라질 수 있고 평가를 다시 돌려야 할 이유가 된다. "문제를 풀었는가"를 데이터로 삼는 순환은 [YC Lightcone 노트](https://raphael-shin.github.io/jungseob-blog/posts/yc-lightcone-rise-of-ai-coworkers-grok-bot/)에서 Grok Bot 팀이 사용자 피드백으로 작은 버그를 자동으로 고친다고 한 이야기와도 이어진다. 학습 스택을 낮은 층부터 다시 쓴다는 대목은 [Inside xAI 노트](https://raphael-shin.github.io/jungseob-blog/posts/ghori-relentless-inside-xai/)와 함께 읽을 만하다.

내 일에 가져올 질문은 이렇다. 우리가 쓰는 AI 도구는 같은 이름 아래에서 모델이 바뀔 때 알려 주는가? 우리 작업의 평가 세트는 그런 변화를 잡을 만큼 자주 돌아가는가? 우리 제품은 "사용자 문제를 풀었는가"를 데이터로 모으고 있는가?

## 참고 자료

[X: Fireside Alpha, Elon Musk reveals Grok 4.8 is in the RL phase (2026-11-19)](https://x.com/firesidealpha/status/2123203404365480234): 게시물 본문, 인용된 앞선 게시물의 글, 48.8초 영상의 음성을 Whisper로 받아쓴 전사를 읽고 정리했다.
