---
layout: post
title: Socratic Tutor가 학습 수준을 확인하는 평가 규칙
date: 2026-11-12 23:03:48 +0900
created: '2026-11-12T23:03:48+09:00'
source: https://github.com/janestreet/agent_skills/blob/master/socratic-tutor/SKILL.md
source_title: Socratic Tutor
author: jungseob
source_author: Jane Street
source_published: unknown
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 수준을 진단한다. 질문하며 가르친다. 회상을 확인한다. 종합 평가로 마친다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://opengraph.githubassets.com/f65af2ca122493481364ec29d284f5db9812d0376e3b02ee6139d64c9163b436/janestreet/agent_skills
  alt: Jane Street agent_skills 저장소
---

## TL;DR

- 승급에는 독립적인 확인 두 번과 자발적 회상이 필요하다.
- 이전 내용의 재평가와 최종 통합 문제로 이해를 확인한다.

## 질문과 회상으로 이해를 확인한다

Jane Street의 Socratic Tutor는 질문으로 사고를 유도하는 학습용 에이전트 지침이다. 단발성 설명 요청에는 수업을 시작하지 않는다. 학습을 요청하면 주제를 세부 능력으로 나누고, 먼저 3~5개 질문으로 출발 수준을 진단한다. 진단이 끝나기 전에는 가르치지 않는다. 설명으로 방금 알게 된 내용을 기존 실력으로 착각하지 않도록 순서를 분리한 설계다.

수업에서는 한 번에 질문 하나만 던지고 답을 기다린다. 틀린 답에는 곧바로 정답을 주지 않고 모순이 드러나는 더 좁은 질문을 한다. 2~3번 실패한 뒤 직접 설명하더라도 다른 각도에서 다시 확인한다. 도구를 쓸 수 있는 실습에서는 학습자의 설명 대신 실제 출력물을 검사한다. 사용자가 답을 바로 요청하면 해당 질문에 한해 문답 방식을 해제할 수 있다.

숙련도는 설명을 따라가는 수준과 혼자 수행하는 수준을 구분한다. 승급에는 두 번 이상의 독립적인 확인이 필요하다. 그중 하나는 답을 알려 준 직후가 아닌 자발적 회상이어야 한다. 이전 내용을 예고 없이 다시 묻고 실패하면 수준을 낮춘다. 모든 세부 능력이 목표에 도달해도 전체를 섞은 최종 평가와 통합 문제를 거친다. 공개 문서는 이 운영 규칙을 제시하며, 실제 학습 효과를 측정한 실험 결과는 포함하지 않는다.

## 참고 자료

[Jane Street의 Socratic Tutor 지침](https://github.com/janestreet/agent_skills/blob/master/socratic-tutor/SKILL.md)
