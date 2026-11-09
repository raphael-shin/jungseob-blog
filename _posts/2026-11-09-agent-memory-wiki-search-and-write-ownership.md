---
layout: post
title: 에이전트 위키의 효과와 공동 편집의 함정
date: 2026-11-09 22:58:23 +0900
created: '2026-11-09T22:58:23+09:00'
source: https://www.anthropic.com/research/components-of-agent-memory
source_title: The components of agent memory
author: jungseob
source_author: Lance Martin
source_published: '2026-11-06'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 위키를 평가했다. 검색과 비교했다. 누락도 발견했다. 작성법을 바꿨다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://www-cdn.anthropic.com/images/4zrzovbb/website/6ab2663a2c0bd6a41409d90136a59a5d72995ea5-1200x630.jpg
  alt: Anthropic 에이전트 메모리 글의 대표 이미지
---

## TL;DR

- 위키의 효과는 과제마다 달랐다.
- 작성 책임 분리와 원문 보존으로 누락을 줄였다.

## 위키의 효과와 사실 누락을 함께 측정한다

Anthropic은 에이전트가 작업 사이에 기록을 다시 읽고 기억을 정리하는 과정을 dreaming이라 부른다. 기억을 원래 대화와 대조해 오류를 고치거나 관련 문서를 연결한 위키를 만든다. Stainless 내부 문서 약 35만 개로 만든 평가에서는 25개 질문을 사용했다. 검색만 쓸 때 점수는 53%였고, 위키와 검색을 함께 쓰면 최대 61%였다. 위키만 사용한 최고 점수는 48%여서 원문 검색을 대체하지 못했다.

위키가 항상 도움이 된 것은 아니다. 한 문서에서 필요한 사실을 찾을 수 있는 과제에서는 검색 대비 뚜렷한 이득이 없었다. 다른 과제에서는 위키가 원본 문서보다 커졌다. 여러 문서의 정보를 연결할 때 얻는 효과와 별개로, 위키 자체를 만들고 최신 상태로 유지하는 계산 비용도 든다. 이 결과는 Anthropic의 특정 과제 평가이며 모든 업무에서 같은 개선을 보장하지 않는다.

계약 자료를 정리한 실험에서는 여러 에이전트가 같은 표를 수정하면서 서로의 내용을 덮어썼다. 부정확한 요약도 겹쳐 결과물에 평가 대상 사실 57개 중 41개만 남았다. 계약마다 별도 페이지를 두고 한 에이전트가 담당하게 바꿨다. 계약 조건도 요약 대신 원문 그대로 보존했다. 수정한 위키로 만든 결과물은 57개 기준을 모두 충족했다. 작성 책임 분리와 내용 보존 방식을 함께 바꾼 결과다.

## 참고 자료

[Anthropic의 에이전트 메모리 실험](https://www.anthropic.com/research/components-of-agent-memory)
