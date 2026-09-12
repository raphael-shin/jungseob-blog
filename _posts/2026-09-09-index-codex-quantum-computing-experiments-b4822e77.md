---
layout: post
title: 실험을 맡기는 단위는 측정 절차였다 - 양자칩 보정에 연결한 에이전트
date: '2026-09-09'
last_modified_at: '2026-09-12T12:17:45+09:00'
author: jungseob
categories:
- 지식 노트
tags:
- agent-workflows
description: 양자칩 측정 사례에서 반복 업무의 위임 조건과 연구자 개입 지점을 살핀다.
source: https://openai.com/index/codex-quantum-computing-experiments/
source_title: How GPT-5.6 Sol helps run quantum computing experiments
source_author: OpenAI
source_published: '2026-09-08'
published: true
render_with_liquid: false
image:
  path: https://images.ctfassets.net/kftzwdyauwt9/53pCremlimLBTRxuMEnPyB/41f2eb372bada1bc3b0f7b721e671c9a/SEO-Card.png?w=1600&h=900&fit=fill
  alt: 원문 대표 이미지 · How GPT-5.6 Sol helps run quantum computing experiments
---

## TL;DR

- MIT 연구진은 Codex를 Jupyter MCP와 실험실 소프트웨어에 연결하고 측정별 실행·평가·실패 사례를 스킬로 제공했다.
- 앞선 측정의 결과가 다음 측정의 조건이 된다. 신호가 모호하면 연구자가 탐색 범위와 판단을 바로잡아야 했다.
- 기술 보고서의 12시간·200회 측정은 기존 오케스트레이터가 제어하는 루프를 에이전트가 감독한 사례다. 에이전트가 모든 측정을 독자적으로 설계했다는 뜻은 아니다.

## Source

[How GPT-5.6 Sol helps run quantum computing experiments](https://openai.com/index/codex-quantum-computing-experiments/)

[기술 보고서: Agentic Calibration of Superconducting Qubits](https://cdn.openai.com/pdf/case-study-agentic-calibration-of-superconducting-qubits.pdf)

## Knowledge

### 실험실 소프트웨어가 제공한 행동 범위

OpenAI가 소개한 Beatriz Yankelevich의 작업은 보정되지 않은 6큐비트 칩에서 시작한다. 냉각과 장착을 마친 초전도 칩은 소프트웨어로 제어할 수 있다. 에이전트는 그 소프트웨어를 통해 측정하고 결과를 분석한다. 공개 블로그가 강조하는 성과는 연구자가 매 단계를 지켜보는 부담을 줄였다는 점이며 숙련자보다 항상 빠르다는 비교 결과는 아니다.

연결된 기술 보고서에는 구현 조건이 더 구체적으로 나온다. Codex는 GPT-5.6 Sol의 Ultra 추론 수준으로 실행됐고 연구실의 Jupyter MCP를 통해 노트북을 사용했다. 측정 데이터와 그래프뿐 아니라 로그, 데이터베이스, 오케스트레이션 코드에도 접근했다. 여러 달의 반복을 거쳐 실험 장비 설명과 칩 설계, 측정별 스킬을 함께 제공하는 구성이 만들어졌다. 단순히 모델에 실험 목표만 전달한 사례와는 조건이 다르다.

### 스킬에는 성공과 실패를 구분할 근거가 필요하다

측정별 스킬에는 실행·분석 코드와 선행 보정, 매개변수 선택 요령이 포함됐다. 물리적 실패 원인과 성공·실패 그래프의 예시도 제공했다. 공진기 측정에서는 주파수와 출력 세기를 탐색하고 얻은 값을 다음 측정의 보정 설정으로 저장한다. 따라서 앞 단계의 잘못된 판정이 이후 실험 조건에도 영향을 미칠 수 있다.

잡음이 많은 가변 주파수 큐비트에서는 연구자의 개입이 필요했다. 에이전트가 측정을 괜찮다고 판단한 뒤에도 연구자는 신호가 탐색 범위 밖으로 벗어났을 가능성을 지적했다. 더 넓은 범위를 조사한 뒤에야 예측을 수정했다. 측정을 더 많이 수행하는 능력과 충분한 증거가 모였는지 판단하는 능력은 구분해서 평가해야 한다.

### 자율 실행의 시간과 연구자의 시간을 나눠 센다

보고서의 야간 작업에서는 오케스트레이터가 12시간 동안 200회 측정을 수행했고 에이전트가 이를 감독한 뒤 실패한 지점을 조사했다. 물리적 측정은 직렬로 시간을 소비하므로 에이전트를 많이 붙인다고 한 측정 경로가 즉시 빨라지지는 않는다. 새로운 다중 큐비트 실험은 표준 칩의 보정보다 복잡하다. 이 사례의 범위는 비교적 정형화된 측정 절차에 있다.

업무에 적용한다면 전체 경과 시간과 사람의 개입 시간을 따로 기록하는 것이 유용하다. 예를 들어 밤새 실행된 작업이 아침에 잘못된 결과를 남겼다면 무인 실행 시간이 길어도 도움이 작다. 반대로 조금 느리게 완료됐어도 사람이 다른 실험을 설계할 시간을 확보했다면 의미가 있다. 이는 실험 수치를 확장한 주장이 아니라 자동화 성과를 읽는 평가 관점이다. 완료 판정과 재검토 책임을 함께 정할 때 절약한 시간을 설명할 수 있다.


## 더 생각해보기

- 에이전트가 결과를 저장하고 다음 단계로 넘어가도 되는 기준은 무엇인가?
- 모호한 결과를 만났을 때 반복 실행과 사람의 개입을 어떻게 구분할 것인가?
