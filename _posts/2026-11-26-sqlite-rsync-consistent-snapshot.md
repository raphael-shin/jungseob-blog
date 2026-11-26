---
layout: post
title: sqlite3_rsync의 일관된 스냅샷 복사
date: 2026-11-26 23:04:34 +0900
created: '2026-11-26T23:04:34+09:00'
source: https://www.sqlite.org/rsync.html
source_title: Database Remote-Copy Tool For SQLite
author: jungseob
source_author: SQLite
source_published: unknown
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 복사 시점과 버전 호환 조건을 구분한다.
tags:
- knowledge
- blog
- web
- software-engineering
---

## TL;DR

- 복사 시작 시점을 보존한다.
- 버전 호환성을 확인해야 한다.

## 파일 복사와 트랜잭션 스냅샷의 차이

SQLite 공식 문서의 `sqlite3_rsync`는 실행 시작 시점의 원본을 일관된 복제본으로 만든다. 복사 중에도 원본에는 쓰기 작업을 계속할 수 있고 복제본에서는 읽기가 가능하다. 다만 실행 도중 원본에 생긴 변경은 이번 복사에 포함되지 않으며, 복제본에 쓰는 작업은 허용되지 않는다. 일반 `rsync`는 트랜잭션을 이해하지 못하므로 서로 다른 시점의 조각을 섞어 손상된 복사본을 만들 수 있다.

전송량을 줄이는 방식은 페이지 해시 비교다. 복제본이 페이지나 페이지 묶음의 해시를 보내면 원본은 다른 부분을 전송한다. 묶음이 다르면 더 세밀한 해시를 요청한다. 차이가 작을수록 유리하지만 처음부터 두 파일이 크게 다르면 해시 교환 비용 때문에 전체 파일보다 전송량이 커질 수도 있다. 테이블과 인덱스 내용은 같아도 헤더는 일부 달라질 수 있으므로 파일 전체의 바이트 일치를 보장하는 복사는 아니다.

원격 복사에는 양쪽의 실행 파일과 SSH 연결이 필요하며, 한 번에 데이터베이스 하나만 동기화한다. 양쪽 모두 원격일 수는 없다. 문서에는 로컬 3.50.0 이상과 원격 3.49.1 이하의 조합에서 협상 버그로 멈출 가능성이 명시돼 있다. 양쪽을 최신 버전으로 맞추기 어렵다면 `--protocol 1`이 우회 방법이다. 이는 문서에 기록된 호환 조건이며 여기서 직접 실행해 검증한 결과는 아니다.

## 참고 자료

[공식 문서](https://www.sqlite.org/rsync.html)
