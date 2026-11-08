---
layout: post
title: D1이 생성 실패를 복구하고 중앙 DB 부하를 줄이는 법
date: 2026-11-08 23:02:26 +0900
created: '2026-11-08T23:02:26+09:00'
source: https://blog.cloudflare.com/d1-control-plane/
source_title: 'Under the hood, off the hot path: How D1 scales to millions of databases'
author: jungseob
source_author: David Laban, Lambros Petrou
source_published: '2026-10-13'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: D1은 생성 실패를 복구한다. 주기적으로 상태를 대조한다. 조회 정보는 분산 저장한다. 중앙 DB의 부하를 줄인다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://blog.cloudflare.com/_emdash/api/media/file/01M4TZKNBC5XJ3T8WNHET65CMR.png
  alt: Cloudflare D1 설계 글의 대표 이미지
---

## TL;DR

- 새 ID로 재시도하고 남은 객체는 정리한다.
- 분산 저장한 조회 정보도 복구한다.

## 생성 중단을 복구하고 조회 경로를 분리한다

Cloudflare D1은 SQLite 기반 데이터베이스 서비스다. 데이터베이스마다 저장과 실행을 담당하는 Durable Object를 먼저 초기화한다. 그다음 중앙 Postgres에 대응 정보를 저장하면 생성이 확정된다. 초기화가 끝나기 전에 등록하면 조회 요청이 준비되지 않은 객체로 향할 수 있다. 반대로 초기화부터 전체를 트랜잭션으로 묶으면 먼 지역의 응답을 기다리는 동안 Postgres 연결을 붙잡게 된다.

초기화 후 Postgres 기록이 실패하면 새 데이터베이스 ID와 객체 ID로 재시도한다. 같은 데이터베이스 ID를 재사용하면 여러 객체가 자신을 소유자로 여길 수 있기 때문이다. 각 객체는 약 30초 간격에 시간차를 두고 중앙의 상태를 확인한다. 이 주기적 확인이 하트비트다. 실패한 시도에서 남은 객체는 자신의 데이터베이스가 등록되지 않았음을 확인하고 삭제 상태로 바뀐다.

조회에 필요한 대응 정보는 분산 저장소 Workers KV에서 읽는다. 캐시에서 빠져도 KV 자체 저장소가 응답하므로 중앙 Postgres로 요청이 몰리지 않는다. KV에서 정보를 찾지 못할 때는 Hyperdrive의 캐시와 Postgres 읽기 복제본으로 넘어간다. KV 갱신 실패는 하트비트가 나중에 바로잡는다. 삭제된 객체는 자체 저장 상태로 요청을 거부하므로 오래된 KV 정보가 요청을 통과시켜도 실행하지 않는다.

## 참고 자료

[Cloudflare의 D1 설계 원문](https://blog.cloudflare.com/d1-control-plane/)
