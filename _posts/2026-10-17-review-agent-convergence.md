---
layout: post
title: "리뷰 에이전트의 반복을 끝내는 운영 규칙"
date: "2026-10-17 23:03:30 +0900"
created: "2026-10-17T23:03:30+09:00"
source: "https://claude.dev/blog/solving-code-review-at-anthropic/"
source_title: "How the Claude Code team does code review"
author: jungseob
source_author: "Addy Osmani, Morgan Westlee Lunt, and Qing Wang"
source_published: "2026-10-15"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Claude Code 팀의 리뷰 횟수 제한과 장애 기반 평가 방식."
tags: [knowledge, blog, web]
---

## TL;DR

- 리뷰 횟수와 버그 탐지율을 함께 추적한다.
- 변경분 재검토와 중복 지적 억제로 반복을 줄인다.
- 반복 중단 기준은 승인 조건을 대체하지 않는다.

## 리뷰가 끝나지 않는 이유

Claude Code 팀에서는 에이전트가 작성하고 다른 에이전트가 검토한 PR이 밤새 50회 넘게 수정과 리뷰를 반복했다. 뒤늦게 나온 지적 상당수는 처음부터 있던 코드에 관한 것이었다. 사람이라면 넘겼을 사소한 지적도 작성 에이전트는 수정하기 때문에 새 커밋과 다음 리뷰가 계속 생겼다.

팀은 버그 탐지율과 함께 통과까지 필요한 리뷰 횟수를 추적한다. 세 차례 뒤에는 작성자에게 접근법을 재고하도록 요청한다. 초기 몇 차례 이후에는 변경분만 다시 검토하고, 이미 낸 지적을 반복하지 않는다. 한 줄씩 고치게 하기보다 버그 유형을 짚어 같은 문제가 있는 다른 위치도 함께 수정하게 한다.

## 탐지 성능과 불필요한 수정 비용

평가는 실제 장애를 일으킨 PR과 후속 수정·되돌림으로 구성한다. 해당 코드를 아는 엔지니어가 버그와 위치를 확인하고 리뷰어를 매일 평가한다. 댓글에 대한 수정·오류 반박·의도된 동작·중요하지 않음의 반응도 분류한다. 정상 PR에 해로운 수정을 유발할 지적을 내는지 따로 검사하므로 발견 개수만 늘리는 최적화를 견제한다.

이 운영 방식은 실제 버그 탐지를 우선하면서 반복 비용을 줄이는 Claude Code 팀의 사례다. 기존 코드의 버그는 별도 야간 리뷰로도 찾는다. 세 차례라는 기준은 자동 승인 조건이 아니며, 열린 지적은 수정하거나 이유를 남겨 해소해야 한다. 사람의 승인이 필요한 변경을 에이전트 승인으로 대체할 수도 없다.

## 참고 자료

[How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/)
