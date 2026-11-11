---
layout: post
title: 'GenDB-V: 정답 보장이 빠른 속도까지 보장할까'
date: 2026-11-11 23:01:10 +0900
created: '2026-11-11T23:01:10+09:00'
source: https://databasearchitects.blogspot.com/2026/11/next-level-benchmarking-overfitting.html
source_title: Next-Level Benchmarking Overfitting
author: jungseob
source_author: Thomas Neumann; Jiale Lao (author response)
source_published: '2026-11-07'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 시험 데이터에는 지름길이 있다. 코드는 예상 위치부터 확인한다. 정답과 속도는 검증 범위가 다르다. 새 작업으로 평가할 계획이다.
tags:
- knowledge
- blog
- web
- software-engineering
---

## TL;DR

- GenDB-V의 일부 조회는 시험 데이터의 배치 규칙을 이용한다.
- 정확성 증명과 미공개 작업의 성능 평가는 별개다.

## 시험 데이터의 규칙을 이용한 빠른 조회

GenDB-V는 AI가 데이터베이스 구현과 정확성 증명을 함께 만드는 연구다. Thomas Neumann의 비판은 속도 비교에 집중한다. 질의마다 미리 만든 보조 자료구조가 조회 시간을 줄인다. 사전 준비를 줄인 plain-array 방식에도 시험 데이터 생성기인 dbgen의 규칙을 이용하는 코드가 있다. 따라서 빠른 시험 결과만으로 일반적인 데이터 처리 성능을 판단하기 어렵다.

공개된 Q18 조회 코드에서 고객 키 k를 찾을 때는 배열의 k−1 위치에 있는 값부터 확인한다. 주문 키는 생성 규칙으로 예상 위치를 계산한다. 두 경우 모두 배열 범위와 실제 키가 맞는지 검사한 뒤 반환한다. 예상이 틀리면 배열을 처음부터 순서대로 검색한다. 잘못된 위치의 값을 그대로 반환하는 방식은 아니다. 다만 생성 규칙에서 벗어난 데이터는 빠른 경로의 이점을 잃는다.

## 정확성 증명과 성능 검증의 범위

연구 저자 Jiale Lao는 댓글 답변에서 고객의 실제 작업에 맞춘 특화와 생성기의 우연한 규칙에 맞춘 최적화를 구분했다. 후자는 제한하겠다고 밝혔다. 자주 쓰는 질의용 구현은 범용 엔진을 보완하는 용도다. 별도의 범용 엔진 생성 방식도 있지만, 저자가 손으로 만든 미공개 질의에서는 아직 Umbra보다 느렸다. 정확성 증명이 여러 작업에서의 우수한 속도를 뜻하지는 않는다.

저자가 제안한 다음 실험은 최적화한 엔진을 고정한 뒤 다른 에이전트가 새 작업을 만드는 방식이다. 고정된 엔진의 성능을 먼저 측정하고 이후 개선한다. 다음 평가에서는 다시 새 작업을 쓴다. 이는 공개된 시험에 익숙해진 효과와 처음 보는 작업으로 전이되는 성능을 구분하려는 계획이다. 아직 그 격차가 줄었다는 결과는 아니다.

## 참고 자료

[Thomas Neumann의 비판과 연구 저자의 답변](https://databasearchitects.blogspot.com/2026/11/next-level-benchmarking-overfitting.html)

[GenDB-V Q18 조회 코드](https://github.com/GenLang-V/GenDB-V/blob/a85741904b9fe6338827ea19d5b932fc389c07cc/results/tpch-sf100/gendb-v-plain-array-storage/queries/q18/code/lookup.rs)
