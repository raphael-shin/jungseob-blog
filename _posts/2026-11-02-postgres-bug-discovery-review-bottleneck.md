---
layout: post
title: PostgreSQL의 버그 발견 증가가 검토 병목으로 이어진 이유
date: 2026-11-02 23:05:53 +0900
created: '2026-11-02T23:05:53+09:00'
source: https://neon.com/blog/postgres-19-is-late-and-its-ais-fault
source_title: Postgres 19 is late, and it's AI's fault
author: jungseob
source_author: Robert Haas
source_published: '2026-10-21'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: AI의 버그 발견 증가와 PostgreSQL의 수정·검토 부담.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://cdn.neonapi.io/public/images/pages/blog/postgres-19-is-late-and-its-ais-fault/cover.jpg
  alt: PostgreSQL 19 출시 지연을 다룬 Neon 원문 대표 이미지
---

## TL;DR

- AI의 버그 발견 증가가 수정안의 사람 검토까지 없애지는 않는다.
- PostgreSQL은 베타에서 일부 기능을 철회하고 안정성 검증을 계속했다.
- 커밋 증가만으로 AI의 인과적 기여를 측정할 수는 없다.

## 발견은 빨라졌지만 검토는 남는다

PostgreSQL 커미터 Robert Haas는 LLM이 버그를 찾는 속도와 사람이 수정안을 검토하는 속도의 차이를 지적한다. AI가 패치를 만들어도 정확성과 프로젝트 기준 준수는 사람이 확인해야 한다. 구버전의 보안 문제와 버그 대응에 검토 시간이 쏠리면서 새 버전의 기능을 점검하고 철회할지 판단하는 일도 늦어졌다는 설명이다.

Haas의 집계에서 4월 8일부터 9월 25일까지 출시 준비 브랜치의 커밋은 전년 724건에서 올해 1,169건으로 늘었다. 직전 버전으로 되돌려 적용한 수정 커밋도 248건에서 433건으로 증가했다. 다만 커밋 수는 버그 수나 AI 기여율이 아니다. 이 수치는 작업량 증가의 단서이며 AI가 지연을 얼마나 유발했는지 분리한 실험 결과는 아니다.

## 공식 발표로 확인되는 기능 철회

PostgreSQL 19 Beta 1은 SQL/PGQ, 기간 일부를 지정하는 UPDATE·DELETE, 파티션 병합·분할을 새 기능으로 소개했다. Beta 4 발표에서는 이 기능들을 철회 목록에 넣었다. 공식 설명은 신뢰성과 예측 가능한 출시 일정을 지키기 위해 개발·검토 시간을 더 확보한다는 것이다. 이 결정 자체와 Haas의 AI 영향 해석은 구분해서 읽어야 한다.

기능 철회가 베타 전체의 중단을 뜻하지는 않는다. Beta 4에는 REPACK의 충돌·권한 문제 수정과 WAIT FOR의 교착상태 수정 등 다른 작업도 포함됐다. 발표문은 테스트 결과가 최종 출시 시점을 결정한다고 명시했다. 기능을 남길지와 언제 안정판을 낼지를 사용자의 워크로드 검증 결과에 따라 판단하는 절차다.

Haas는 단기 지연보다 오래된 결함을 처리하면서 새 기능 개발을 이어갈 수 있을지를 미해결 과제로 남긴다. 버그가 많이 발견됐다는 이유로 코드 품질이 나빠졌다고 단정하지도 않는다. 사람의 검토를 더 많이 통과하는 방법까지 해결되어야 발견 속도의 향상이 출시 속도의 향상으로 연결될 수 있다.

## 참고 자료

[Robert Haas: Postgres 19 is late, and it’s AI’s fault](https://neon.com/blog/postgres-19-is-late-and-its-ais-fault)

[PostgreSQL 19 Beta 1](https://www.postgresql.org/about/news/postgresql-19-beta-1-released-3313/)

[PostgreSQL 19 Beta 4](https://www.postgresql.org/about/news/postgresql-19-beta-4-released-3386/)
