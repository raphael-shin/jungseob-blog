---
layout: post
title: Performance Factory의 진단 반박과 복구 확인
date: 2026-11-20 23:02:07 +0900
created: '2026-11-20T23:02:07+09:00'
source: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/
source_title: How OpenAI’s Performance Factory keeps ChatGPT fast
author: jungseob
source_author: Okay Zed, Cyrus Forbes
source_published: '2026-11-19'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 진단과 복구 검증을 다룬다.
tags:
- knowledge
- blog
- web
- software-engineering
---

## TL;DR

- 진단을 반박하고 복구를 확인한다.
- 평가에서는 정답 유출을 막는다.

## 진단을 반박하고 복구까지 확인한다

OpenAI의 Performance Factory는 성능 저하 알림을 받아 원인을 조사하고 수정안을 제안한다. 작업 상태와 근거는 개별 에이전트의 대화 밖에 저장한다. 검토나 배포를 기다릴 때는 실행을 멈추고 관련 이벤트가 도착하면 재개한다. 수정 코드의 병합 여부는 엔지니어가 결정한다.

첫 설명이 그럴듯해도 조사를 끝내지 않는다. 별도 세션이 진단을 반박하며, 의심한 변경을 적용받지 않은 요청도 느려졌는지 확인한다. 이미지 다운로드 실패 사례에서는 원인으로 지목한 내부 서비스가 복구됐는데도 실패가 계속됐다. 검토자는 설명이 불충분하다고 판단해 조사를 다시 열었다.

배포 뒤에는 이전 성능 수준으로 돌아왔는지 다시 확인한다. 개선이 없으면 원인 조사로 되돌리고, 일부만 회복되면 남은 성능 저하를 새 작업으로 분리한다. 제안한 변경이 불필요하게 복잡하거나 새 문제를 만들기도 했다. 수정안에도 별도 반박 검토를 추가했지만, 캐시 도입처럼 데이터 신선도에 영향을 주는 결정에는 엔지니어의 판단이 필요하다.

조사 스킬을 바꿀 때는 과거 장애로 평가하되 정답 유출을 막는다. 이전 조사 메모와 장애 보고서, 앞선 실행 결과는 볼 수 없게 한다. 복구 뒤 수집한 증거도 원인을 드러낼 수 있어 주의해야 한다. 발생 시점을 맞혀도 엉뚱한 배포를 탓할 수 있으므로 시점과 원인 추론을 따로 채점한다. 보고서의 이해도는 별도로 평가한다.

## 참고 자료

[OpenAI의 Performance Factory 설계](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/)
