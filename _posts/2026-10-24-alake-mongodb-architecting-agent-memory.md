---
layout: post
title: "에이전트 메모리는 데이터베이스 설계 문제라는 주장, MongoDB의 Richmond Alake가 AI Engineer에서 제시한 메모리 유형과 관리 체계를 대조한 정리"
date: "2026-10-24 15:09:13 +0900"
created: "2026-10-24T15:09:13+09:00"
source: "https://www.youtube.com/watch?v=W2HVdB4Jbjs"
source_title: "Architecting Agent Memory: Principles, Patterns, and Best Practices — Richmond Alake, MongoDB"
author: jungseob
source_author: "AI Engineer (연사: Richmond Alake, MongoDB)"
source_published: "2025-06-27"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "AI Engineer에서 MongoDB의 Richmond Alake가 17분 동안 발표한 에이전트 메모리 강연을 정리한다. 에이전트의 정의에서 메모리가 핵심인 이유, 인간 기억에 빗댄 메모리 유형(페르소나·도구함·대화·워크플로·에피소드 등)과 메모리 관리 여섯 요소, 망각 메커니즘, 데이터베이스가 메모리 제공자라는 주장을 다루고 Voyage AI 인수, OpenAI 함수 수 권고, 라이브러리 라이선스, 신경과학 일화를 대조해 판매자 관점의 한계를 밝힌다."
image:
  path: "https://i.ytimg.com/vi/W2HVdB4Jbjs/maxresdefault.jpg"
  alt: "AI Engineer 영상 Architecting Agent Memory Richmond Alake MongoDB 썸네일"
tags:
  - knowledge
  - blog
  - AI
  - 에이전트
  - 메모리
  - MongoDB
---

## TL;DR

- Richmond Alake(MongoDB)는 에이전트를 환경을 인지하고 LLM으로 판단하며 도구로 행동하는 존재로 정의하고, 가장 중요한 요소로 단기 또는 장기 메모리를 꼽는다. 반성적이고 능동적이며 자율적인 에이전트라는 요구 대부분이 메모리로 풀린다는 주장이다.
- 메모리 관리는 컨텍스트 창에 넣을 정보를 체계적으로 조직하는 일이며 생성, 저장, 검색, 통합, 갱신, 삭제의 여섯 요소로 나뉜다. 큰 창은 데이터를 쑤셔 넣는 곳이 아니고 관련 기억만 끌어와 구조화하는 곳이라고 말한다.
- 메모리 유형은 페르소나, 도구함, 대화, 워크플로, 에피소드, 장기, 에이전트 등록부, 엔티티로 나뉜다. 도구 스키마를 DB에 넣어 검색해 쓰는 도구함 메모리와, 실패를 경험으로 저장하는 워크플로 메모리가 눈에 띈다.
- 기억은 삭제하지 말고 망각 메커니즘으로 다뤄야 한다는 주장이 일관되지만, 구현은 연사의 실험 라이브러리 수준(최근성·연관성 신호)에 머문다. 정량 결과는 없다.
- 이 발표는 데이터베이스 업체의 강연이라 MongoDB가 메모리 제공자라는 결론이 정해져 있다. 이 노트는 영어 자막 전체(17:36)와 MongoDB 발표문, OpenAI 문서, 라이브러리 저장소로 대조했다.

## 영상에 대하여

AI Engineer 채널이 2025년 6월 27일에 올린 17분 36초 영상이다. 영어 자동생성 자막만 있고 전체를 읽었다. 연사는 MongoDB 소속 Richmond Alake이고 설명란은 인간 기억(에피소드, 작업, 의미, 절차)에서 영감을 받은 메모리 구성 요소와 운영 방식, 벡터 DB와 하이브리드 검색을 이용한 영속화, 임베딩과 관련도 점수에 의한 증강, 다중 에이전트 환경에서의 규모 확장, 메모리 연쇄와 선택적 삭제를 다룬다고 소개한다. 설명란에는 현재 시점의 다음 AI Engineer 행사 공지도 붙어 있으나 발표 내용과는 무관하다. 같은 주제를 OpenAI 관점에서 다룬 [Build Hour 정리 노트](https://raphael-shin.github.io/jungseob-blog/posts/openai-build-hour-agent-memory-patterns/)와 함께 읽으면 데이터베이스 제공자의 시각과 모델 제공자의 시각이 대비된다.

## 에이전트의 정의와 메모리

연사는 약속으로 시작한다. 이 정보는 앞으로 6개월 동안 믿을 만하고 능력 있는 에이전트를 만드는 데 관련이 있을 것이다. 흐름은 챗봇(2022년 11월 ChatGPT 출시), RAG(도메인 지식으로 개인화), 규모를 키운 LLM의 추론·도구 사용, 에이전트 시스템 순이다. 에이전트가 무엇이냐는 논쟁에는 들어가지 않고 스펙트럼으로 본다. 웨이모의 자율주행 수준에 빗대어, LLM이 루프를 도는 최소 에이전트부터 도구에 접근하는 에이전트 무리인 레벨 4의 자율 에이전트까지 있다는 것이다. 정의는 환경을 인지하고 LLM으로 인지 능력을 갖추며 도구로 행동하는 계산 개체이고 가장 중요한 것은 단기든 장기든 어떤 형태의 메모리가 있다는 점이다.

인간 기억과의 유비는 이 발표의 논거다. AI의 목적이 인간 지능을 모방하거나 능가하는 것이고 가장 지능적인 사람을 가르는 것이 회상 능력이니 AI도 메모리가 필요하다는 논법이다. 인간은 단기, 장기, 작업, 의미, 에피소드, 절차 기억을 가지며 연사는 백플립 같은 기술은 소뇌에 저장된다고 90% 확신한다며 예로 든다. 이 대목은 청중 반응용 일화이며 이 노트가 신경과학적으로 확인한 내용이 아니다. 에이전트 메모리는 상태를 지속시키고 정보를 쌓아 데이터를 기억으로 바꾸며 그것이 다음 실행 단계에 영향을 주게 하는 메커니즘이다.

## 메모리 관리의 여섯 요소와 망각

메모리 엔지니어가 만들 핵심은 메모리 관리 시스템이다. 정의는 컨텍스트 창에 넣는 모든 정보를 체계적으로 조직하는 과정이며 큰 창은 데이터를 쑤셔 넣으라고 있는 것이 아니라 관련 기억을 끌어와 응답이 적절하도록 구조화하라고 있는 것이다. 구성 요소는 생성, 저장, 검색, 통합, 갱신, 삭제다. 연사는 마지막 항목이 거짓이라고 직접 말한다. 인간은 잊고 싶은 외상성 기억을 빼면 기억을 지우지 않으므로 삭제 대신 망각 메커니즘을 구현해야 하고 몇몇 연구가 에이전트에서의 망각을 탐구한다. 가장 중요한 요소는 검색이다. RAG는 단순하고 에이전트형 RAG는 검색 능력을 도구로 에이전트에게 주어 언제 정보를 부를지 에이전트가 정하게 한다. 벡터 검색만으로는 부족하고 다른 검색도 필요하다고 덧붙인다.

## 메모리 유형 여덟 가지

연사의 실험 라이브러리 Memoriz가 이 설계 패턴들을 담았다고 한다. 페르소나 메모리는 에이전트를 더 믿을 만하고 인간적으로 만들어 사용자와 관계를 맺게 한다. 연사는 OpenAI가 몇 달 전 ChatGPT에 성격을 부여했으나 잘 안 됐다고 말하는데, 이는 2025년 4월 GPT-4o 업데이트를 4월 29일 되돌린 일을 가리키는 것으로 보인다. 도구함 메모리는 OpenAI의 지침이 컨텍스트 창에 10~21개 도구의 스키마만 넣으라는 것이니, 도구의 JSON 스키마를 DB에 저장하고 LLM을 부르기 직전에 검색으로 관련 도구만 꺼내면 확장된다는 아이디어다. 대화 메모리는 타임스탬프, 대화 ID에 더해 최근성(recall recency)과 연관 대화 ID 같은 메모리 신호를 둔다. 연사는 이것이 망각 메커니즘을 구현하려는 자신의 시도라고 한다. 워크플로 메모리는 단계 실행이 실패하면 실패도 학습 경험이므로 저장해 다음 실행에서 같은 단계를 피하게 하는 것이다. 이어 에피소드 메모리, 장기 메모리, 에이전트 등록부(에이전트가 가진 도구와 페르소나 등), 엔티티 메모리가 있다.

MongoDB의 포지션도 분명하다. MemGPT, Mem0, Zep 같은 메모리 관리 도구는 훌륭하지만 메모리를 푸는 단일한 방법은 없으며 맞춤형 시스템을 위해서는 메모리 제공자가 필요하다는 것이다. 이것이 MongoDB의 역할이라는 결론으로 이어진다. 유연한 문서 모델과 그래프·벡터·텍스트·지리 공간 검색을 한 DB에서 제공한다고 주장한다. 2025년 초 Voyage AI를 인수했고 임베딩 모델과 재순위 모델을 몇 달 내 Atlas에 넣어 청킹 전략을 직접 쓸 필요가 없게 하겠다고 약속한다. 마지막 일화는 Hubel과 Wiesel의 고양이 시각 피질 연구가 합성곱 신경망에 영감을 주었다는 것이다. 연사는 자연이 최고의 지능 설계자이므로 안쪽을 들여다보자고 말하고 MongoDB 최고 AI 과학자이자 Voyage AI 창업자(자막의 Tenu는 Tengyu Ma로 읽었다)와 신경과학자들, MemGPT와 Letta의 창시자(자막의 Charles Parker는 Charles Packer로 알려진 인물이다)와 대화한 사실을 전한다.

## 인용된 근거와 대조 결과

Voyage AI 인수는 MongoDB가 2025년 2월 24일 발표했다. 연사가 약속한 통합은 2026년 8월 13일 MongoDB 발표문에서 Atlas의 자동 임베딩(Voyage AI 기반), 임베딩·재순위 API로 나왔다. 발표 후 약 14개월이 지난 시점이며 "몇 달 내"보다는 늦었다. 이 노트는 발표문의 요약만 확인했고 기능 범위를 직접 쓰지는 않았다. Hubel과 Wiesel의 노벨상은 1981년이며 연사가 말한 "90년대 후반"은 맞지 않는다. 고양이 시각 피질 실험은 1950~60년대로 연사의 서술과 맞는다.

도구 수 권고는 현행 OpenAI 문서와 다르다. 현행 함수 호출 문서는 한 턴 시작 시점에 쓸 수 있는 함수를 20개 미만으로 두라는 "소프트 제안"을 적고 자주 안 쓰는 도구는 tool search로 미루라고 한다. 연사의 "10~21개"는 정확한 인용이 아니라 대략적인 기억으로 보인다. 도구함 메모리의 취지는 이 tool search와 방향이 같다. Memoriz는 GitHub 저장소 README가 스스로 "교육용·실험용 소프트웨어"이며 프로덕션 보안 강화를 거치지 않았다고 밝히고 설치 문서는 PolyForm Noncommercial License 1.0.0을 쓴다고 안내한다. 상업 사용에는 제약이 있을 수 있다는 뜻이며 이 노트는 라이선스 전문을 읽지 않았다. 연사의 말대로 메모리 구현은 실험 단계다.

## 읽을 때 유의할 점

첫째, 이 강연은 데이터베이스 업체의 발표이고 "MongoDB가 메모리 제공자"라는 결론이 처음부터 있다. 대안과의 객관적 비교(성능, 비용, 운영 부담)는 없다. 둘째, 인간 기억 유비는 직관에는 좋지만 에이전트 메모리 설계의 정답을 보증하지 않는다. 소뇌 일화처럼 연사가 확신이 낮다고 말한 대목도 있다. 셋째, 정량 결과가 한 건도 없다. 메모리 신호나 망각 메커니즘이 정확도나 비용을 얼마나 바꾸는지 제시되지 않는다. 넷째, 메모리 오염, 개인정보, 삭제 요구 같은 위험은 다루지 않으며 "삭제하지 말고 잊게 하자"는 입장은 법적 삭제 요구와 충돌할 수 있다. 이는 이 노트의 지적이다. 다섯째, 17분이라 각 메모리 유형이 어떻게 쓰이는지 구체적인 시연은 없다.

그래도 가져갈 질문은 있다. 우리 에이전트의 메모리는 대화, 도구, 워크플로, 엔티티 중 어느 유형이 먼저 필요한가, 실패한 실행을 경험으로 남기고 다음 실행이 피하게 하려면 무엇을 저장해야 하는가, 삭제와 망각은 어떻게 다르게 설계할 것인가. 메모리가 검색 문제라는 관점은 [Jev의 메모리 파이프라인 노트](https://raphael-shin.github.io/jungseob-blog/posts/jev-memory-pipeline-ranking-chunking-and-context-loss/)와, 쓰기·검색·망각 규칙은 [rari의 메모리 스택 노트](https://raphael-shin.github.io/jungseob-blog/posts/whrrari-ai-memory-stack/)와 함께 보면 비교가 쉽다.

## 참고 자료

[AI Engineer — Architecting Agent Memory: Principles, Patterns, and Best Practices (YouTube, 2025-06-27)](https://www.youtube.com/watch?v=W2HVdB4Jbjs) — 영어 자동생성 자막 전체(17:36)와 설명란을 읽고 정리했다. 슬라이드 그림은 보지 못했다.

[MongoDB — MongoDB announces acquisition of Voyage AI (2025-02-24)](https://www.mongodb.com/company/newsroom/press-releases/mongodb-announces-acquisition-of-voyage-ai) — 인수 발표일을 검색 결과 발췌로 확인했다.

[MongoDB — Atlas Now Delivers Industry-Leading Context Retrieval (2026-08-13)](https://investors.mongodb.com/news-releases/news-release-details/mongodb-atlas-now-delivers-industry-leading-context-retrieval) — Voyage AI 기반 자동 임베딩과 임베딩·재순위 API 발표를 검색 결과 발췌로 확인했다.

[OpenAI — Function calling guide](https://developers.openai.com/api/docs/guides/function-calling) — 함수 20개 미만 권고(소프트 제안)와 tool search 안내를 읽었다.

[RichmondAlake — memorizz (GitHub)](https://github.com/RichmondAlake/memorizz) — README의 실험적 소프트웨어 고지와 라이선스 안내를 검색 결과 발췌로 확인했다.

[Nobel Prize — Hubel lecture](https://www.nobelprize.org/uploads/2018/06/hubel-lecture.pdf) — 고양이 시각 피질 연구와 1981년 수상을 검색 결과로 확인했다.
