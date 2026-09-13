---
layout: post
title: Pandas의 한계와 단일 머신의 한계는 다르다
date: '2026-09-13'
created: '2026-09-13T23:03:33+09:00'
source: https://eddie.codes/posts/pandas-should-go-extinct/
source_title: Pandas Should Go Extinct
author: jungseob
source_author: Eddie Atkinson
source_published: '2026-09-12'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: Pandas·Polars·DuckDB 비교 실험의 조건과 실행 계획, 메모리 초과 처리의 한계를 살핀다.
tags:
- data-engineering
- pandas
- polars
- duckdb
- performance
image:
  path: https://eddie.codes/og-image/pandas-should-go-extinct.png
  alt: Pandas Should Go Extinct 원문 대표 이미지
---

## TL;DR

- Pandas의 처리 지연만으로 분산 시스템이 필요하다고 결론 내릴 수는 없다.
- Polars의 지연 실행은 필터와 열 선택을 앞당겨 불필요한 작업을 줄인다.
- DuckDB의 디스크 유출 기능도 모든 중간 집계 상태의 메모리 초과를 해결하지는 못한다.

## 같은 집계에서 달라진 시간과 메모리

Eddie Atkinson은 Pandas에서 성능 문제가 생긴 뒤 Spark 같은 분산 도구로 넘어가는 경로를 비판한다. 그 사이에 Polars와 DuckDB로 처리할 수 있는 작업이 있다는 주장이다. 글의 약 100GB 경계는 보편적인 한계값이 아니다. Redshift 통계에서 용량을 추정한 대목도 행 크기와 처리량 가정에 의존한다.

원문의 10억 행 CSV 집계 실험은 Debian 12의 AWS m7a.8xlarge에서 실행했다. 32코어·128GB RAM 환경이며 출력 직렬화는 측정에서 제외했다. 준비 실행 두 번 뒤 30회 반복한 중앙값은 Pandas 4분 28초, Polars 5.04초, DuckDB 5.19초였다. 최대 USS 메모리의 중앙값은 각각 38.12GB, 18.02GB, 1.93GB였다. 저자의 특정 구현 비교이며 모든 분석 작업의 순위를 뜻하지 않는다.

노트북에서도 시간과 메모리 차이는 이어졌고 NYC 택시 데이터에서는 Pandas와 DuckDB를 혼합한 단계적 전환도 비교했다. Arrow는 이때 데이터를 주고받는 공통 형식이다. 다만 기존 생태계와의 결합이 깊으면 전환 비용이 남는다. 원문도 Pandas의 개선 가능성과 작업별 차이를 인정하며 분산 도구의 성급한 채택을 경계한다.

## 실행을 미루면 읽을 데이터부터 달라진다

Polars 공식 문서의 Lazy API 예제에서는 CSV를 읽고 조건을 적용하고 그룹별 평균을 계산한다. 즉시 실행 방식은 단계마다 중간 결과를 만든다. 반면 지연 실행은 계산 전체를 정의한 뒤 `collect()`에서 실행하므로, 계획을 세울 때 뒤에서 필요한 조건과 열을 미리 알 수 있다. 이 차이는 단순히 같은 코드를 빠르게 실행하는 것보다 앞선 단계에서 발생한다.

필터를 읽기 단계로 앞당기는 predicate pushdown은 이후 단계가 처리할 행을 줄인다. projection pushdown은 필요한 열만 선택해 불필요한 열의 로딩을 줄인다. 문서의 `explain()` 예제는 이 두 최적화를 실행 계획에서 보여 준다. 중간 결과를 직접 살피거나 최종 질의가 아직 정해지지 않은 탐색 작업에서는 즉시 실행도 선택지다. 따라서 라이브러리 이름뿐 아니라 데이터를 언제 읽고 어느 단계에서 줄이는지가 비교 대상이 된다. [Polars Lazy API](https://docs.pola.rs/user-guide/concepts/lazy-api/)

## 디스크로 넘길 수 있는 상태에도 경계가 있다

DuckDB 공식 문서는 메모리보다 큰 데이터와 중간 결과를 디스크로 유출해 처리하는 기능을 설명한다. 임시 저장 위치는 `temp_directory`로 지정할 수 있다. 그룹화·조인·정렬·윈도 연산처럼 많은 상태를 보관하는 연산도 메모리 초과 처리를 지원한다. 그러나 디스크를 사용한다는 사실만으로 모든 질의가 끝까지 실행된다고 보장되지는 않는다.

여러 blocking operator가 한 질의에 겹치면 상호작용 때문에 메모리 부족이 발생할 수 있다. `list()`와 `string_agg()` 같은 일부 집계 함수는 상태를 디스크로 넘기는 데 제한이 있고 `PIVOT`도 내부의 `list()` 사용으로 그 영향을 받는다. `EXPLAIN`은 실행하지 않고 계획을 확인하며 `EXPLAIN ANALYZE`는 실제 실행을 측정한다. 이때 병렬 단계의 시간을 합하면 전체 경과 시간보다 커질 수 있다. 단일 머신의 처리 가능성을 판단할 때도 입력 파일 크기만 볼 수 없는 이유가 여기에 있다. [DuckDB 성능 문서](https://duckdb.org/docs/current/guides/performance/how_to_tune_workloads)

## 참고 자료

- [Eddie Atkinson — Pandas Should Go Extinct](https://eddie.codes/posts/pandas-should-go-extinct/)
- [Polars — Lazy API](https://docs.pola.rs/user-guide/concepts/lazy-api/)
- [DuckDB — Tuning Workloads](https://duckdb.org/docs/current/guides/performance/how_to_tune_workloads)
