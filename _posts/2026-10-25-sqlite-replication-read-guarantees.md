---
layout: post
title: "분산 SQLite에서 복구·쓰기 합의·읽기 보장을 구분하기"
date: "2026-10-25 23:03:33 +0900"
created: "2026-10-25T23:03:33+09:00"
source: "https://philipotoole.com/twelve-years-of-distributed-sqlite/"
source_title: "Twelve years of distributed SQLite"
author: jungseob
source_author: "Philip O’Toole"
source_published: "2026-10-23"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "rqlite 개발자의 회고와 공식 읽기 일관성 문서로 살펴본 복제의 서로 다른 보장."
tags: [knowledge, blog, web]
---

## TL;DR

- 장애 후 복구와 클러스터를 통한 운영 지속은 서로 다른 요구다.
- rqlite의 쓰기 합의가 기본 Weak 읽기의 최신성까지 보장하지는 않는다.
- 더 강한 읽기 보장은 과반수 확인과 반영 대기 비용을 수반한다.

## 복구와 계속 운영하기는 다른 요구다

Philip O’Toole의 회고에서 rqlite는 작은 관계형 저장소를 어느 노드에 둘지 결정하기 어려웠던 문제에서 출발했다. SQLite 앞에 Raft 로그를 두고 쓰기를 복제하는 구조다. 쓰기는 리더를 거쳐 과반수의 승인을 받아야 하며, 네트워크 분할로 소수가 된 쪽은 쓰기를 거절한다. 모든 노드가 독립적으로 쓰도록 만든 시스템은 아니다.

Litestream은 다른 질문을 다룬다. 단일 노드의 SQLite 변경 로그를 외부 저장소로 보내 장애 후 복구할 수 있게 하는 접근이다. 클러스터를 계속 운영하는 대신 복원 절차를 받아들이는 선택이다. 회고는 복구를 기다릴 수 있는 경우와 그렇지 않은 경우를 구분하며, 분산 SQLite라는 이름만으로 서로 대체 가능한 제품처럼 비교하지 않는다.

## 쓰기 합의가 모든 읽기를 보장하지는 않는다

rqlite의 공식 읽기 일관성 문서를 대조하면 기본값인 Weak는 노드가 자신을 리더로 판단하는지만 확인한다. 리더가 아니면 요청을 리더에게 전달한다. 그러나 교체된 옛 리더가 잠시 자신을 리더로 믿는 구간에는 오래된 값을 반환할 수 있다. 쓰기를 합의로 복제한다는 설명만으로 기본 읽기까지 선형화 가능하다고 이해하면 안 된다.

Linearizable 읽기는 리더가 과반수와 통신하고, 기록해 둔 커밋 위치까지 SQLite에 반영됐는지도 기다린다. 그 뒤에 읽으므로 Weak보다 네트워크 지연을 더 부담한다. 반대로 None은 클러스터 연결을 확인하지 않고 해당 노드의 데이터만 읽는다. 장애 허용성과 응답 속도를 논할 때는 복제 방식뿐 아니라 실제로 선택한 읽기 보장도 함께 봐야 한다.

## 참고 자료

[Twelve years of distributed SQLite](https://philipotoole.com/twelve-years-of-distributed-sqlite/)

[rqlite 공식 문서 — Read Consistency](https://rqlite.io/docs/api/read-consistency/)
