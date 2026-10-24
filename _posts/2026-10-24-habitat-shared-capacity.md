---
layout: post
title: "Habitat가 전용 컨테이너에서 공유 용량으로 돌아온 이유"
date: "2026-10-24 22:58:00 +0900"
created: "2026-10-24T22:58:00+09:00"
source: "https://openai.com/index/scaling-storage-one-billion-users-part-two/"
source_title: "Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II)"
author: jungseob
source_author: "Jon Lee, Hrachya Hakobyan, Chaomin Yu"
source_published: "2026-10-23"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "공유 자원 간섭을 격리로 해결한 뒤 다시 마주한 용량 계획의 부담."
tags: [knowledge, blog, web]
---

## TL;DR

- 논리 키를 나눠도 물리 파티션의 처리량은 공유된다.
- 전용 컨테이너는 격리와 함께 팀별 증설 책임을 만든다.
- 공유로 돌아가려면 요청 제어와 용량 확장 방식도 바뀌어야 했다.

## 저장량이 늘자 처리 여유가 줄었다

OpenAI의 Habitat 운영 회고에서 공유 컨테이너는 서로 다른 서비스의 부하를 한데 수용했다. 같은 물리 파티션에 놓인 키들은 처리량 한도를 공유하므로 한쪽의 과도한 요청이 다른 기능까지 방해했다. 논리 키를 나누는 것만으로는 로그인 같은 핵심 기능을 덜 중요한 기능의 부하에서 보호하기 어려웠다.

저장량 증가도 별도의 문제였다. 데이터를 담기 위해 물리 파티션이 분할돼도 컨테이너에 할당한 총처리량은 그대로였다. 이를 더 많은 파티션이 나눠 가지면서 파티션당 처리 여유가 줄었다. 요청량이 증가하지 않았는데도 저장량 증가만으로 기존 부하를 감당하기 어려워질 수 있었다.

## 격리 뒤에 남은 용량 계획

전용 컨테이너로 나누면 장애 범위를 기능별로 제한할 수 있었다. 대신 새 기능은 공유 풀의 여유를 이용하지 못하고 자체 용량을 준비해야 했다. 출시 전 작은 내부 테스트에서 실제 서비스로 넘어갈 때의 급증을 팀이 예측해야 했으며, 사전 증설을 놓치면 출시 당일 긴급 대응이 필요했다.

결국 공유를 기본으로 되돌리되 제어 방식을 바꿨다. 뜨거운 키를 먼저 제한하고 오프라인 요청의 우선순위를 낮춰 사용자 요청을 보호했다. Azure 팀과 개선한 서버리스 방식에는 저장량뿐 아니라 처리량 사용에 따른 분할도 추가됐다. 이는 일반 설정만 바꾼 사례가 아니라 공급자와 함께 용량 계획 부담을 줄인 운영 사례다.

## 참고 자료

[OpenAI의 Habitat 저장소 운영 회고 2부](https://openai.com/index/scaling-storage-one-billion-users-part-two/)
