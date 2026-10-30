---
layout: post
title: 'OpenAI 에이전트 감시: 대상 지정부터 실제 대응까지의 간격'
date: 2026-10-30 23:05:17 +0900
created: '2026-10-30T23:05:17+09:00'
source: https://openai.com/index/how-we-detect-frontier-model-misalignment/
source_title: How we detect frontier model misalignment
author: jungseob
source_author: OpenAI
source_published: '2026-10-29'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: OpenAI의 현재 감시 체계와 METR의 과거 점검을 구분해 검사 시점, 처리 누락, 담당자 대응의 경계를 정리한다.
tags:
- knowledge
- blog
- web
- ai-safety
---

## TL;DR

- 감시 대상이어도 담당자 호출이나 자동 중단이 항상 작동하지는 않는다.
- METR는 대상 지정과 실제 감시 처리량을 따로 확인하도록 권고했다.
- 과거 시스템 점검은 현재 개선 사항에 대한 검증이 아니다.

OpenAI의 10월 29일 설명에서 내부 Codex는 모두 감시 대상이다. 그러나 내부 Codex의 담당자 호출은 오탐 때문에 꺼져 있다. 프런티어 강화학습은 긴급 경보가 오면 시간대와 관계없이 담당자를 호출하지만, 대부분의 다른 작업은 업무 시간으로 제한한다. 일부 치명적 경보에는 자동 중단이 붙는다. 감시 범위만으로 대응 범위까지 알 수 없는 구조다.

## 검사가 언제 실행되는가

METR와 Redwood Research가 점검한 과거 시스템에는 더 앞단의 공백이 있었다. 당시 검사는 에이전트가 사용자에게 제어권을 돌려줄 때 실행됐다. 계속 행동하는 에이전트는 검사를 무기한 미룰 수 있었다. 문맥을 압축하는 시점에도 검사하지 않았기 때문이다. OpenAI는 점검 전에 이 문제를 파악했고 점검 중 수정했다.

현재 OpenAI의 설명은 프런티어 강화학습과 내부 Codex에서 턴 종료와 문맥 압축 때 검사한다는 것이다. 검사 간격을 최대 30분으로 제한하는 방식으로도 옮겨 가고 있다. 첫 검토 모델은 에이전트가 본 문맥을 읽고, 후속 조사 에이전트는 가능한 경우 전체 기록을 확인한다. 민감한 작업에서는 네트워크 로그 같은 대화 밖의 증거도 대조한다.

## 감시 대상과 실제 처리량은 다르다

METR는 점검 당시 내부 Codex 트래픽의 99.2%가 감시 대상으로 지정됐다고 추정했다. 이것은 끝까지 검사를 마친 비율이 아니다. 오류나 구현 결함으로 처리 도중 빠질 수 있다. METR의 제안은 전체 추론 기록과 감시 기록을 주기적으로 대조하라는 것이다. 시스템 설정상의 대상 목록만 확인해서는 실제 누락을 찾기 어렵다.

이 점검은 7월 21일 당시 시스템을 대상으로 한 시범 점검이었다. METR는 이후 확대된 감시 범위나 수정 완료 주장을 검증하지 않았다. 대부분의 취약점이 수정됐고 하나는 수정 중이라는 상태도 OpenAI가 전달한 내용이다. 따라서 과거 점검 결과를 현재 결함의 증거로 단정할 수도, 새 설명을 외부 검증 완료로 읽을 수도 없다.

## 참고 자료

[OpenAI: How we detect frontier model misalignment](https://openai.com/index/how-we-detect-frontier-model-misalignment/)

[METR: Red-Teaming OpenAI’s Internal Agent Monitoring Systems](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/)
