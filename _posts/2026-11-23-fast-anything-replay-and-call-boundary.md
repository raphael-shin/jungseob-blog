---
layout: post
title: fast-anything의 호출 재생과 Rust 교체 조건
date: 2026-11-23 23:02:35 +0900
created: '2026-11-23T23:02:35+09:00'
source: https://github.com/EL4CTEO/fast-anything
source_title: fast-anything README
author: jungseob
source_author: EL4CTEO
source_published: unknown
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 함수 이식의 동작과 비용을 검증한다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://opengraph.githubassets.com/c64ec5d3fe964c38a30747d28069ac901a482ab7181fa93f863e642f28e68c3d/EL4CTEO/fast-anything
  alt: fast-anything 저장소
---

## TL;DR

- 기록한 호출과 추가 입력으로 이식 결과를 비교한다.
- 호출 경계의 비용까지 측정해야 한다.

## 함수 교체 전에 동작과 호출 비용을 확인한다

fast-anything은 실행 시간을 많이 쓰면서 이식하기 쉬운 함수를 골라 Rust로 옮기는 도구다. 프로젝트 README의 절차는 측정, 호출 기록, 이식, 검증, 교체로 나뉜다. 코딩 에이전트가 받은 작업에는 함수별 Rust 프로젝트와 지시 파일이 포함된다. 검증에서는 기록한 실제 호출을 재생해 원래 함수와 결과를 비교한다. 대상은 단순 데이터를 받아 같은 입력에 같은 결과를 내는 함수다.

실제 호출은 최대 500건까지 기록하며, 여기서 빈 입력이나 비ASCII 문자열 같은 추가 사례도 만든다. 원래 구현을 비교 기준으로 삼아 값뿐 아니라 오류 발생 여부도 확인한다. README에는 문자를 바이트로 잘못 비교한 이식 코드가 호출 재생에서 발견된 사례가 나온다. 다만 이런 검사는 기록·생성한 입력에서의 일치를 확인한다. 모든 가능한 입력의 동작이 같다는 수학적 증명으로 해석해서는 안 된다.

결과가 맞아도 함수 호출이 더 느려지면 교체하지 않는다. Rust로 넘어가는 비용이 줄인 계산량보다 클 수 있기 때문이다. 도구는 작은 내부 함수를 반복 호출하기보다 가능한 바깥 반복문을 옮겨 언어 간 왕복을 줄인다. 전체 애플리케이션도 원래 구현과 교체 구현을 번갈아 실행해 측정한다. README의 배속은 예제별 자체 측정값이며, 다른 앱에 같은 향상을 보장하지 않는다. 교체는 함수별로 되돌릴 수 있다.

## 참고 자료

[fast-anything의 설계와 검증 절차](https://github.com/EL4CTEO/fast-anything)
