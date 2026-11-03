---
layout: post
title: Astra는 Qwen의 수학 점수를 어떻게 높였나
date: 2026-11-03 22:56:58 +0900
created: '2026-11-03T22:56:58+09:00'
source: https://honnibal.dev/blog/astra-read-write-misleading
source_title: The 'Astra can read and write weights to improve Qwen' post is massively
  misleading
author: jungseob
source_author: Matthew Honnibal
source_published: '2026-11-03'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 가중치만 보고 게임을 맞힌 실험과 파이썬으로 Qwen의 반복 출력을 고친 실험의 조건을 비교한다.
tags:
- knowledge
- blog
- AI
- web
image:
  path: https://honnibal.dev/social.png
  alt: Matthew Honnibal의 블로그 대표 이미지
---

## TL;DR

- Astra는 작은 신경망이 어떤 게임을 배웠는지 가중치를 읽고 맞혔다.
- Qwen 실험에서는 연습 문제의 출력까지 살펴 반복을 줄였다. 같은 접근으로 Gemma의 산술 오류를 고치는 데는 성공하지 못했다.

## 가중치만 보고 게임을 맞힌 실험

연구진은 벽돌깨기와 팩맨을 비롯한 네 게임에 각각 신경망을 훈련했다. 모두 같은 크기의 격자에서 같은 다섯 가지 행동을 고르므로 입력과 출력의 개수만 세어서는 게임을 구분할 수 없다. Astra는 격자와 행동에 관한 설명, 가중치 17,253개를 숫자로 받았다. 게임 이름이나 선택지를 주지 않았는데도 도구 없이 네 게임을 모두 맞혔다.

Matthew Honnibal은 이 결과를 읽을 때 실험마다 Astra가 무엇을 볼 수 있었는지 따져 본다. 예컨대 작은 자동차가 경사로에서 멈춘 문제를 고칠 때는 실패 장면을 기록한 에피소드 하나를 미리 보여 줬다. 게임 정책을 처음부터 작성하는 과제에서는 가중치의 초깃값이 모두 0이었다. 완성된 정책의 동작을 숫자에서 읽어 내는 일과 원하는 동작을 숫자로 구현하는 일은 서로 다른 능력을 시험한다.

## Qwen에서는 답이 끝나지 않는 이유를 추적했다

Qwen3.5-0.8B를 고칠 때 Astra는 파이썬으로 가중치를 조사하고 연습 문제를 입력해 출력을 확인했다. 원래 모델은 처음 푼 96문제 가운데 85문제에서 같은 말을 반복하다가 토큰 한도에 닿았다. Astra는 반복과 관련된 신호를 두 층에서 찾아 그 성분을 줄였다. 순전파를 50회 허용한 조건에서 MATH-500 점수는 7.9%에서 48.1%로 올랐다.

비교 대상인 Gemma 3 270M은 답을 쓰다가 토큰 한도에 닿는 비율이 8.5%였다. 틀린 답에는 산술 실수나 잘못된 대수 전개가 섞여 있었고, 가중치를 바꿔도 뚜렷한 점수 향상은 없었다. 두 결과를 함께 보면 Qwen에서 확인한 개선의 범위가 드러난다. 이미 풀 수 있던 문제에서 답을 끝내도록 반복을 줄인 것이며, 가중치 수정으로 새로운 수학 능력을 더할 수 있는지는 별도의 실험이 필요하다.

## 참고 자료

[Matthew Honnibal의 실험 조건 비교](https://honnibal.dev/blog/astra-read-write-misleading)

[MIT CSAIL 연구진의 실험 설계와 결과표](https://rikiyat.github.io/blog/weight-space-programming/)
