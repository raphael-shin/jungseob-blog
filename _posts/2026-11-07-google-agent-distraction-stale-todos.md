---
layout: post
title: 낡은 TODO가 코딩 에이전트를 다른 일로 이끈다
date: 2026-11-07 23:01:20 +0900
created: '2026-11-07T23:01:20+09:00'
source: https://developers.googleblog.com/agent-distraction/
source_title: Agent Distraction
author: jungseob
source_author: Sam Saccone, Madhuri Garikapati
source_published: '2026-11-06'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: Google이 TODO를 따라간 에이전트를 분석했다. 요청 밖 작업도 있었다. 처리 비용과 대기 시간이 늘었다. 삭제 전에는
  주석의 의도를 확인했다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Agent_Distraction_Cover_1600x900_.2e16d0ba.fill-1200x600.png
  alt: Google의 Agent Distraction 글 대표 이미지
---

## TL;DR

- TODO가 요청 밖 작업을 유발했다.
- 주석 삭제 전에는 변경 이력을 확인했다.

## 주석이 요청 밖의 작업으로 이어지는 경로

Google은 사내 코딩 에이전트가 읽은 TODO와 연결된 버그 상태를 대조했다. TODO는 나중에 처리할 일을 표시하는 코드 주석이다. 파일을 읽은 세션의 13%에서 버그 번호가 붙은 TODO나 FIXME가 나타났다. 관련 주석을 만난 경우의 6%에서 후속 행동이 발생했고, 그중 83%는 사용자가 요청하지 않은 버그를 대상으로 했다.

요청 밖의 추적 가운데 41%는 이미 닫힌 버그를 향했다. 열린 버그를 따라간 경우도 57%였다. 아직 해결되지 않은 문제라도 현재 요청의 범위에는 없을 수 있다. 개발자와 작업 종류 등을 통제한 분석에서 이런 추적은 토큰 77%, 대기 시간 105% 증가와 연관됐다. 이는 Google 내부의 관찰 분석이며, 주석을 지우면 같은 비율로 비용이 줄어든다는 실험 결과는 아니다.

Google은 정리 에이전트로 해결되거나 폐기된 버그 참조를 찾았다. 닫힌 티켓이라는 이유만으로 주석을 삭제하지는 않았다. 버그와 파일의 변경 이력을 함께 확인해 주석에 담긴 의도까지 더는 유효하지 않을 때 삭제안을 검토에 보냈다. 여섯 달 동안 수천 개를 제거했고 사람 검토자의 승인율은 95%를 넘었다. 이 승인율은 정리안에 대한 평가이며, 코딩 작업 전체의 정확도를 뜻하지 않는다.

## 참고 자료

[Google Developers Blog: Agent Distraction](https://developers.googleblog.com/agent-distraction/)
