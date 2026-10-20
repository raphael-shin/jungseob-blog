---
layout: post
title: "DeepInfer의 재현 가능한 추론과 공개 범위"
date: "2026-10-20 23:01:55 +0900"
created: "2026-10-20T23:01:55+09:00"
source: "https://github.com/deepseek-ai/DeepInfer"
source_title: "DeepInfer"
author: jungseob
source_author: "DeepSeek-AI"
source_published: "unknown"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "배치 불변 추론과 결정적 샘플링의 조건, 공개 엔진과 완성된 서비스의 경계."
tags: [knowledge, blog, web]
image:
  path: "https://opengraph.githubassets.com/ef909c78d50beb12fcd0cc09c107497b9e4167ad03051e1e31344511859eb75f/deepseek-ai/DeepInfer"
  alt: "DeepInfer 저장소 대표 이미지"
---

## TL;DR

- 배치 불변성과 결정적 샘플링은 설정 조건이 다르다.
- 공개본은 오프라인 추론이며 서비스 구성 요소는 별도로 필요하다.
- 재현성 기능의 NVIDIA 지원 조건을 확인해야 한다.

## 배치 불변성과 샘플링의 재현성

DeepInfer의 배치 불변 추론은 함께 처리하는 요청 구성이 달라져도 모델 결과를 같게 유지하는 기능이다. README는 NVIDIA 환경에서 `DEEPINFER_BATCH_INVARIANT=1`로 활성화하도록 안내한다. 요청마다 다른 배치에 섞일 수 있는 환경에서 결과를 비교할 때, 배치 구성에 따른 차이를 통제하는 설정이다.

결정적 샘플링에는 조건이 더 있다. 같은 입력 토큰과 샘플링 파라미터를 사용하면서 배치 불변성을 켜고, `DEEPINFER_ENABLE_MTP_VARLEN=0`으로 설정한 뒤 고정된 `seq_seed`를 전달해야 한다. 따라서 시드만 고정하는 절차와 구분해야 한다. 이 기능도 README의 지원 범위는 NVIDIA로 한정된다.

## 공개 엔진과 완성된 서비스의 경계

DeepInfer는 DeepSeek의 대규모 운영에 쓰이는 추론 프레임워크지만, 이번 공개본이 제공하는 것은 오프라인 추론이다. 지원 모델은 DeepSeek-V4.1-Flash이며 하드웨어는 NVIDIA SM100과 Huawei Ascend 950이다. 정규식·JSON 스키마·EBNF 문법으로 출력을 제한하는 기능과 CPU 배치 스케줄링을 장치 실행에 겹치는 비동기 스케줄링도 포함한다.

완성된 추론 서비스를 구성하려면 공개본에 없는 요소를 보충해야 한다. README는 KV 캐시 시스템과 VE·Prefill·Decode 분리, 데이터 병렬 복제본 사이의 부하 분산을 별도로 열거한다. 엔진 기능이 있다고 운영 서비스까지 완성된 것은 아니다. 위 설정은 문서의 보장 조건을 정리한 것으로, 이 노트에서 하드웨어 실행으로 재현성을 검증한 결과는 아니다.

## 참고 자료

[DeepInfer](https://github.com/deepseek-ai/DeepInfer)
