---
layout: post
title: Postgres 워크플로의 복구와 외부 API의 중복 실행
date: '2026-09-15'
created: '2026-09-15T23:04:35+09:00'
source: https://www.infoq.com/articles/durable-workflows-postgres/
source_title: Implementing Durable Workflows on Postgres Without an External Orchestrator
author: jungseob
source_author: Raman Varma
source_published: '2026-09-14'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: Postgres에 워크플로 진행 상태를 저장하는 구조와 외부 API 재시도에 남는 멱등성의 경계를 살펴본다.
tags:
- knowledge
- blog
- postgresql
- durable-execution
- idempotency
image:
  path: https://res.infoq.com/articles/durable-workflows-postgres/en/headerimage/Implementing-Durable-Workflows-on-Postgres-Without-an-External-Orchestrator-header-1789129413946.jpg
  alt: Postgres 기반 워크플로 원문의 대표 이미지
---

## TL;DR

- Kestrel은 Postgres의 실행 행, 체크포인트와 리스로 워크플로를 복구한다.
- 체크포인트의 유일성만으로 외부 API 작업의 중복 실행까지 막을 수는 없다.
- 재시도 키의 보관 기간과 작업의 복구 기간도 함께 맞춰야 한다.

## 실행 상태를 데이터베이스에 남긴다

Kestrel은 장애 분석, 수정안 생성, 사람의 승인, GitOps PR 생성으로 이어지는 자동화의 진행 상태를 Postgres에 저장한다. 애플리케이션 서버가 실행 행을 가져오면서 상태와 소유자, 리스 만료 시각을 짧은 트랜잭션으로 함께 기록한다. 작업 중에는 리스를 갱신하고 만료된 실행은 주기적인 sweeper가 다시 큐에 넣는다.

PostgreSQL의 `FOR UPDATE SKIP LOCKED`는 다른 트랜잭션이 잠근 행을 기다리지 않고 건너뛴다. 여러 소비자가 같은 큐에서 작업을 가져올 때 잠금 경합을 줄이는 방식이다. 다만 조회 결과에서 잠긴 행이 빠지므로 전체 데이터의 일관된 모습을 읽는 일반 조회에는 맞지 않는다. 행 잠금을 건너뛰더라도 테이블 수준의 잠금까지 사라지지는 않는다. 이 범위는 [PostgreSQL 공식 문서](https://www.postgresql.org/docs/18/sql-select.html#SQL-FOR-UPDATE-SHARE)에 명시되어 있다.

## 완료한 단계와 외부 작업 사이의 빈틈

단계별 출력에는 `(execution_id, step_id)` 기본 키를 둔다. 재시작한 워커는 저장된 결과가 있으면 해당 단계를 건너뛰고 중복된 체크포인트 삽입은 제약조건으로 막는다. 승인 대기나 예약 시각도 메모리 대신 행으로 남긴다. 리스가 짧으면 아직 살아 있는 워커의 작업을 다른 워커가 가져갈 수 있고 길면 장애 복구가 늦어진다.

여기서 체크포인트 중복 방지와 외부 작업의 중복 방지는 구분해야 한다. 예를 들어 외부 API 호출은 성공했지만 결과를 Postgres에 저장하기 전에 프로세스가 종료됐다고 가정하자. 다음 워커가 보는 데이터베이스에는 완료 기록이 없으므로 같은 호출을 다시 시도할 수 있다. 뒤늦게 결과 행의 중복 삽입을 막아도 이미 일어난 외부 동작을 취소하지는 못한다. 이는 위 실행 순서에서 도출되는 실패 시나리오이며 원문이 설명하는 체크포인트만으로 전체 과정의 exactly-once를 보장한다고 읽어서는 안 되는 이유다.

## 재시도를 외부 API까지 연결한다

[Stripe의 멱등 요청 문서](https://docs.stripe.com/api/idempotent_requests)는 이 경계를 다루는 구체적인 사례다. 클라이언트가 같은 작업의 재시도에 동일한 키를 보내면, 서버는 최초 요청의 상태 코드와 본문을 보관했다가 다시 반환한다. 성공 결과뿐 아니라 `500` 오류도 재사용한다. 따라서 연결 오류가 났다는 이유만으로 새 키를 만들어 다시 요청하면, 같은 작업이라는 식별 정보가 끊어진다.

키의 수명에도 조건이 있다. Stripe는 생성 후 최소 24시간이 지난 키를 정리할 수 있으며 삭제된 키를 재사용하면 새 요청으로 처리한다. 같은 키에 다른 매개변수를 보내는 경우에는 오류를 반환한다. 입력 검증 실패나 실행 중인 요청과의 충돌처럼 엔드포인트 실행이 시작되지 않은 경우는 결과를 저장하지 않는다. 워크플로의 복구 기간과 API가 키를 보관하는 기간을 함께 고려해야 한다는 결론은 이 계약에서 나온다.

## 운영 비용과 적용 범위

Kestrel의 선택은 외부 호출이 많고 동시성이 크지 않은 자동화에 맞춰져 있다. 실행·단계·승인 데이터를 SQL로 연결해 조사할 수 있지만 폴링 연결 수와 큐 테이블의 잦은 갱신은 관리 대상으로 남는다. 원문은 연결 풀링, 폴링 지연과 jitter, autovacuum과 부분 인덱스를 다룬다. 엄격한 FIFO나 수천 워커의 초저지연 분배가 필요하면 별도 엔진을 검토할 여지가 있다. 처리량 수치는 재현 조건이 부족해 일반적인 성능 보장으로 옮기지 않는다.

## 참고 자료

[Implementing Durable Workflows on Postgres Without an External Orchestrator — Raman Varma](https://www.infoq.com/articles/durable-workflows-postgres/)

[PostgreSQL 18: SELECT의 잠금 절](https://www.postgresql.org/docs/18/sql-select.html#SQL-FOR-UPDATE-SHARE)

[Stripe API: Idempotent requests](https://docs.stripe.com/api/idempotent_requests)
