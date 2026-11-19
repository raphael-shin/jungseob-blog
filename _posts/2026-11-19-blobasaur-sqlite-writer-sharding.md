---
layout: post
title: Blobasaur의 SQLite 쓰기 분산과 만료 처리
date: 2026-11-19 23:05:25 +0900
created: '2026-11-19T23:05:25+09:00'
source: https://zerodha.tech/blog/high-performance-distributed-blob-storage/
source_title: Distributed, high-performance blob storage on SQLite
author: jungseob
source_author: Sarat Chandra
source_published: '2026-11-19'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 파일별 쓰기 대기열과 만료 정리의 잠금 경합을 다룬다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://zerodha.tech/static/images/blobasaur-og.png
  alt: Blobasaur 저장소
---

## TL;DR

- SQLite 파일마다 쓰기 대기열을 분리한다.
- 만료 정리도 일반 쓰기와 같은 대기열을 쓴다.

## SQLite 파일마다 쓰기 담당자를 둔다

Zerodha는 거래 화면의 차트 설정과 작업 공간을 저장하던 SSDB를 Blobasaur로 교체했다. 금융 거래 데이터와 달리 이 설정은 최근 쓰기의 일부 손실을 허용할 수 있었다. SQLite의 WAL 모드에서도 파일 하나에는 동시에 하나의 쓰기만 가능하다. Blobasaur는 키를 여러 SQLite 파일로 분산하고, 파일마다 전용 쓰기 담당자와 크기가 제한된 대기열을 둔다. 대기열의 요청은 묶어서 커밋한다.

만료 데이터 정리도 같은 쓰기 담당자를 거쳐야 했다. 처음에는 별도 연결에서 만료 행을 한꺼번에 삭제했는데, 이 작업이 쓰기 잠금을 차지하면서 일반 요청을 지연시켰다. 정리 작업을 기존 쓰기 대기열로 보내고 회당 삭제량을 기본 1,000행으로 제한하자 지연 급증이 사라졌다. 읽을 때 이미 만료 행을 걸러내므로 물리적 삭제를 나눠 수행해도 만료된 값이 노출되지는 않는다.

이 설계의 성능에는 내구성과 운영 기능의 제약이 따른다. WAL의 synchronous=NORMAL 설정에서는 커밋마다 디스크 동기화를 하지 않아 전원 장애나 운영체제 충돌 때 최근 쓰기를 잃을 수 있다. 선택적인 비동기 모드는 메모리 대기열에 넣은 시점에 성공을 응답한다. 노드 사이의 슬롯 배치는 고정이며 자동 장애 전환도 없다. 노드 내부 파일 수를 바꾸는 작업 역시 서버를 중단한 뒤 수행한다.

## 참고 자료

[Zerodha의 Blobasaur 설계](https://zerodha.tech/blog/high-performance-distributed-blob-storage/)
