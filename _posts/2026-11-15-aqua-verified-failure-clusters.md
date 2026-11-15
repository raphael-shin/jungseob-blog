---
layout: post
title: AQuA가 에이전트 실패 후보를 검증하는 방법
date: 2026-11-15 23:06:44 +0900
created: '2026-11-15T23:06:44+09:00'
source: https://developers.googleblog.com/the-outer-loop-insights-first-an-ambient-quality-agent-that-diagnoses-your-production-agent/
source_title: 'The Outer Loop, Insights First: An Ambient Quality Agent That Diagnoses
  Your Production Agent'
author: jungseob
source_author: Dima Melnyk, Elia Secchi
source_published: '2026-10-08'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 대화와 배포 코드로 실패 후보를 검증한다.
tags:
- knowledge
- blog
- web
- ai-agents
image:
  path: https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Gemini_Generated_Image_2g9cog2g9c.2e16d0ba.fill-1200x600.jpg
  alt: AQuA 원문 대표 이미지
---

## TL;DR

- 실패 후보를 별도 모델로 검증한다.
- 배포 코드와 연결하되 표본 검증의 한계를 구분한다.

## 실패 후보를 실제 대화와 대조한다

Google의 AQuA는 운영 중인 에이전트의 대화 기록을 읽고 반복되는 실패를 찾는다. HTTP 응답이 정상이어도 좌석 확인을 건너뛸 수 있다. 검토 모델이 지적한 문제들을 같은 실패 원인끼리 묶은 뒤, 별도 모델이 묶음마다 최대 세 개의 전체 대화 기록과 대조한다. 여행 에이전트의 대화 32개를 재생한 실험에서는 후보 아홉 묶음 중 세 묶음을 기각했다. 사용자가 명시적으로 요청한 동작을 오류로 판단하거나 서로 다른 문제를 합친 경우였다.

남은 문제의 원인을 조사할 때는 현재 개발 코드가 아니라 배포 시점에 저장한 소스 사본을 읽는다. 좌석 오류에서는 사용자가 좌석 번호를 직접 말할 때 확인 도구를 호출하라는 지시가 빠져 있었다. 진단은 해당 파일과 줄을 가리키고 서버는 그 위치의 존재를 검사한다. 코드 밖의 문제라면 대화의 해당 단계를 지목한다. AQuA 자체는 수정을 적용하거나 풀 리퀘스트를 열지 않는다.

일부 대화만 검증하므로 묶음의 크기는 우선순위를 정하는 대략적인 근거다. 실행 기록에는 검증 한도를 넘긴 후보와 평가 오류도 남겨 정상 처리와 구분한다. 무작위 표본은 드문 실패를 놓칠 수 있고, 사용자 발화를 재생해도 당시 외부 시스템의 상태까지 복구하지는 못한다. 운영 전체의 품질을 확인한 실험은 아니다.

## 참고 자료

[Google의 AQuA 설계와 검증 사례](https://developers.googleblog.com/the-outer-loop-insights-first-an-ambient-quality-agent-that-diagnoses-your-production-agent/)
