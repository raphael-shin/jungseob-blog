---
layout: post
title: Inkitt의 PR 에이전트가 중복 이벤트와 재시도를 다루는 방법
date: 2026-11-05 23:01:27 +0900
created: '2026-11-05T23:01:27+09:00'
source: https://medium.com/inkitt-tech/how-we-built-a-one-shot-pr-creator-at-inkitt-e1b8dbc52cda
source_title: How we built a one-shot PR creator at Inkitt
author: jungseob
source_author: Agi Letkiewicz Tanner
source_published: '2026-08-26'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: Inkitt의 PR 자동화 사례다. 중복 실행을 막는다. 재시도 횟수를 제한한다. 검토는 사람이 맡는다.
tags:
- knowledge
- blog
- web
- ai-agents
image:
  path: https://cdn-images-1.medium.com/max/1024/1*i7e783IUxz7dr_Z-dqjrAg.png
  alt: Inkitt PR 자동화 원문 대표 그림
---

## TL;DR

- 실행 상태를 저장하고 조건부 쓰기로 중복 실행을 막는다.
- CI 전체 완료를 API로 확인하고, 초안 PR의 검토 준비 전환은 사람이 맡는다.

## 실행 상태와 외부 작업을 한곳에서 관리한다

Inkitt의 PR 생성기는 Slack 요청이나 Linear 라벨을 받아 작은 코드 변경을 초안 PR로 만든다. 명세 작성, 구현, 검증은 필요할 때 생성되는 컨테이너가 하나씩 맡는다. 실행 상태는 데이터베이스의 한 행에 저장된다. 중간에 멈춰도 그 상태에서 이어갈 수 있으며, 다음 행동을 정하는 핵심 함수는 현재 상태와 이벤트만 입력받는다.

## 같은 이벤트가 두 번 와도 실행은 한 번만 시작한다

웹훅은 같은 이벤트를 여러 번 전달할 수 있다. Inkitt는 브랜치 확보, PR 번호 기록, 다음 재시도처럼 한 번만 수행해야 하는 동작을 조건부 데이터베이스 쓰기로 선점한다. 경쟁에서 진 실행은 새 컨테이너를 시작하지 않고 멈춘다. 검증 실패, CI 수정, 병합 충돌 해결에도 각각 두 번의 시도 한도를 둔다.

CI 이벤트 하나를 받았을 때는 GitHub API로 관련 작업 전체가 끝났는지 다시 확인한다. 개별 작업의 종료 이벤트를 PR 전체의 완료로 취급하면 다음 단계가 일찍 시작될 수 있기 때문이다. 완성된 변경도 초안 PR로 열리며, CI와 스테이징 확인 뒤 사람이 검토 준비 상태로 전환한다. 자동화가 맡는 범위와 사람이 책임을 넘겨받는 시점이 실행 절차에 들어 있다.

## 참고 자료

[Inkitt의 PR 생성기 설계 기록](https://medium.com/inkitt-tech/how-we-built-a-one-shot-pr-creator-at-inkitt-e1b8dbc52cda)
