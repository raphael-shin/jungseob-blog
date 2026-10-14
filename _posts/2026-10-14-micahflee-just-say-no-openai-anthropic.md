---
layout: post
title: "OpenAI와 Anthropic을 끊고 오픈 웨이트로 간다, Micah Lee가 Tinfoil과 GLM-5.3으로 옮긴 이유와 방법"
date: "2026-10-14 21:47:46 +0900"
created: "2026-10-14T21:47:46+09:00"
source: "https://micahflee.com/just-say-no-to-openai-and-anthropic/"
source_title: "Just say no to OpenAI and Anthropic"
author: jungseob
source_author: "Micah Lee"
source_published: "2026-10-11"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "소프트웨어·보안 엔지니어 Micah Lee가 ChatGPT와 Claude 대신 오픈 웨이트 모델을 쓰자고 주장한 글을 정리한다. 프라이버시, 사이버 가드레일, 격차 4개월이라는 판단, Tinfoil·Maple·OpenCode Go 활용법을 다루고 Z.ai 사고와 보존 정책을 원자료로 대조한다."
image:
  path: "https://images.unsplash.com/photo-1599595344070-c456bea6ee98?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMTc3M3wwfDF8c2VhcmNofDZ8fG9wZW58ZW58MHx8fHwxNzkxNzU0MTY2fDA&ixlib=rb-4.1.0&q=80&w=2000"
  alt: "열린 문을 찍은 Unsplash 사진, 글의 대표 이미지"
tags:
  - knowledge
  - blog
  - AI
  - 오픈소스
  - 개인정보
---

## TL;DR

- Micah Lee는 OpenAI와 Anthropic의 폐쇄형 모델이 대화를 제공사가 전부 볼 수 있고 사이버 분야에서 사용자를 감시하며 통제한다고 비판한다. 그는 그 대안으로 오픈 웨이트 모델을 권한다.
- 그가 보는 격차는 크지 않다. 오픈 웨이트가 폐쇄형 최신 모델에 약 4개월 뒤처졌고, GLM-5.3은 소프트웨어 엔지니어링에서 Claude Opus 5.5와 비슷하다는 것이 그의 체감이다.
- 실행 방법은 세 갈래다. 프라이버시가 중요하면 보안 엔클레이브 기반의 Tinfoil 또는 Maple, 공개 작업이면 월 10달러의 OpenCode Go, 중국 업체 계정 직접 가입은 피하라는 것이다.
- 링크 대조 결과 Z.ai ZCode의 저장소 무단 업로드 사고와 OpenCode Go의 보존 정책 표는 글과 맞는다. 다만 성능 비교는 체감이고 Tinfoil 가격은 확인하지 못했다.
- 글은 정치적 입장이 강한 의견글이다. 개인정보 문제와 사이버 가드레일 논점은 실질이 있지만, 필자의 모델 평가와 업체 성격 규정은 사실로 읽으면 안 된다.

## 글에 대하여

소프트웨어·보안 엔지니어 Micah Lee가 2026년 10월 11일에 쓴 글이다. 그는 Naomi Klein과 Astra Taylor의 『End Times Fascism and the Fight for the Living World』를 읽은 것이 계기라고 밝힌다. 이 책은 읽지 않았다. 그는 LLM이 매우 강력하다고 평가하는 소프트웨어·보안 엔지니어이면서 미국 프런티어 연구소의 경영진에 대해 극단적인 표현을 쓴다. 이런 표현은 필자의 주관적 평가이며 노트는 사실로 옮기지 않았다. 이 노트는 본문 전체를 읽었다.

## 폐쇄형 모델에 대한 두 가지 비판

첫째는 프라이버시다. ChatGPT와 Claude는 모델을 내려받을 수 없고 API나 채팅으로만 쓰므로 제공사가 사용자의 모든 활동을 볼 수 있다. 학습에 쓰지 말라는 옵션이 있어도 대화가 비공개가 되는 것은 아니다. 제공사가 열람하고 정부나 기업과 공유할 수 있다는 점에서 신뢰 문제가 남는다고 그는 말한다.

둘째는 게이트키핑이다. 사이버보안 작업을 하는 사람은 세션마다 대화 기록을 읽고 해킹 용도로 의심되면 세션을 멈추는 감시 에이전트를 만난다. 오탐이 자주 난다고 한다. 덜 제한된 모델은 OpenAI의 Trusted Access for Cyber와 Anthropic의 Cyber Verification Program 같은 심사를 통과한 곳만 쓴다. Anthropic은 10월 6일에 이 프로그램을 세 단계 접근 수준으로 확대했다고 발표했고 이는 확인했다. OpenAI 쪽 페이지는 접근이 막혀 읽지 못했다. 필자는 접근 권한을 정하는 힘이 두 CEO와 정부에 있는 것이 비민주적이라고 본다.

## 오픈 웨이트의 격차와 선택지

그가 제시하는 판단은 오픈 웨이트가 약 4개월 뒤처졌다는 것이다. 4개월은 별것 아니라는 말이 이어진다. 가장 인상적이라고 꼽는 모델은 Z.ai의 GLM-5.3이다. 벤치마크 대신 "느낌 기반" 평가로 Claude Opus 5.5와 비슷하다고 하고 더 작은 GLM-5.3-Flash는 Opus 4.8 정도로 보며 메모리 512GB의 Mac Studio 같은 장비가 있으면 개인도 돌릴 수 있다고 한다. 이 비교는 벤치마크가 없는 개인 체감이다.

Z.ai를 직접 쓰는 것은 권하지 않는다. 그 이유로 코딩 도구 ZCode가 동의 없이 로컬 저장소를 Alibaba Cloud로 올리다 적발된 사고를 든다. 링크된 Reuters 기사(9월 21일자)와 InfoWorld가 사고를 확인한다. 기본으로 켜진 "Codebase Indexing" 기능이 원인이었고 사용자 일부는 소스 코드와 데이터베이스 비밀번호까지 올라갔다고 주장했다. Z.ai는 기능을 끄고 클라우드 저장소를 삭제했으며 독립 평가 기관이 삭제를 확인했다고 밝혔고 코드를 공개했다. 필자는 이 사후 조치를 쓰지 않았다. 중국 업체가 데이터를 정부와 공유할 수 있다고 가정해야 한다는 것도 그의 판단이며 이 노트가 확인한 범위가 아니다.

모델 자체는 쓰되 업체에 데이터를 맡기지 말라는 구분이 핵심이다. DeepSeek, Qwen, Kimi 같은 중국계 오픈 웨이트 모델은 안전하게 쓸 수 있지만 그 업체에 대화를 맡기지 말라고 한다. 프랑스의 Mistral은 중국도 미국도 아닌 유일한 대형 업체로 데이터를 맡기기에 더 합리적이라고 평한다. 최근 공개된 Mistral Large 4는 이 블로그의 [Mistral Large 4 노트](https://raphael-shin.github.io/jungseob-blog/posts/mistral-large-4-open-weight-preview/)에서 다뤘다.

## 비공개 추론과 값싼 추론

로컬에서 못 돌릴 때의 대안은 보안 엔클레이브와 원격 증명을 쓰는 서비스다. 필자는 완벽하지는 않지만 제공사가 제한 없이 모든 것을 볼 수 있는 기본 상태와 큰 차이가 있다고 본다. Tinfoil은 이 분야에서 가장 많은 일을 하는 회사이고 Maple AI는 내부에서 Tinfoil 추론을 쓰는 소비자용 서비스다. 채팅과 웹 검색, 문서 읽기, 모바일 앱이 필요하면 Maple(무료 플랜과 월 20달러 Pro), 에이전트형 코딩이나 리버싱, 악성코드 분석, CTF 같은 작업이면 토큰당 과금하는 Tinfoil을 권한다. 그는 GLM-5.3의 Tinfoil 가격을 입력 100만 토큰당 1.80달러, 캐시 0.80달러, 출력 5.75달러로 소개하는데 이 노트는 가격 페이지를 확인하지 못했다.

프라이버시가 덜 중요하면 OpenCode Go가 있다. 월 10달러에 그 이상의 크레딧을 주는 추론 라우터라서 요청이 라우터와 실제 추론 제공자 모두에게 보인다. 필자는 보존 약속이 약속일 뿐 기술적 보장이 아니라고 짚는다. OpenCode 문서를 열어 보니 GLM-5.3, Kimi, Qwen, DeepSeek 계열은 학습에 쓰이지 않고 보존 0일(DeepSeek는 별표 주석)로 적혀 있었고 일부 모델은 30일 보존이나 학습 허용이었다. 필자의 서술과 맞는다.

## 실제 사용 방식

그는 OpenCode 하니스에 Tinfoil과 OpenCode Go를 연결해 쓴다. 주로 GLM-5.3을 낮은 추론 수준으로 돌리고 이미 오픈소스인 구현 같은 완전히 공개된 작업은 OpenCode Go로, 나머지는 모두 Tinfoil로 처리한다. 이렇게 일한 지 얼마 안 됐지만 ChatGPT와 Claude 사용을 비슷하거나 더 싼 가격으로 충분히 대체할 수 있어 보이고 프라이버시가 높고 가드레일이 훨씬 적다는 것이 결론이다. 오픈 웨이트 상황이 빠르게 변해 6개월 뒤에는 최선이 달라질 수 있다고 덧붙인다.

## 읽을 때 유의할 점

첫째, 이 글은 필자가 정치적 입장을 분명히 밝힌 의견글이다. 프런티어 연구소 경영진에 대한 인신 평가는 근거를 제시하지 않으며 이 노트는 그 부분을 논점에서 뺐다. 둘째, GLM-5.3이 Opus 5.5에 필적한다는 평가는 개인 체감이고 필자도 벤치마크가 따로 있다고 말한다. 4개월 격차도 근거 없는 판단이다. 셋째, 필자는 보안 분야에서 일하는 사람이라 사이버 가드레일 문제의 영향을 일반 사용자보다 크게 받는다. 일반적인 업무용 사용에서 같은 만족도가 나온다는 보장은 없다.

넷째, Tinfoil과 Maple의 비공개 추론은 엔클레이브 기술에 대한 신뢰에 기대며 필자 스스로 완벽하지 않다고 쓴다. 이 노트는 그 보안 모델을 검증하지 않았다. 다섯째, 오픈 웨이트 모델이라도 호스팅하는 쪽에 대화를 맡기면 같은 문제가 생긴다. 필자가 업체와 모델을 구분하는 이유다. 여섯째, 본인의 이해관계로 특정 서비스를 광고하는 글은 아니지만 Tinfoil, Maple, OpenCode Go를 구체적으로 추천하고 있으므로 제휴 여부는 글에 표시되지 않았다는 점을 밝혀 둔다.

그럼에도 이 글에서 가져갈 점검 질문은 선명하다. 지금 쓰는 모델 제공사에 어떤 데이터가 남는지 알고 있는가, 작업을 공개 가능한 것과 아닌 것으로 나눠 경로를 다르게 두었는가, 모델 하나에 묶이지 않고 바꿀 수 있는 하니스를 쓰는가, 업체와 모델을 구분해 신뢰를 따졌는가.

## 참고 자료

[Micah Lee — Just say no to OpenAI and Anthropic (2026-10-11)](https://micahflee.com/just-say-no-to-openai-and-anthropic/) — 본문 전체(약 9,000자)를 읽고 정리했다. 대표 이미지는 글의 Unsplash 사진이다.

[Reuters(Yahoo 재게재본) — China's Z.ai disables AI coding assistant features after security issue (2026-09-21)](https://tech.yahoo.com/cybersecurity/articles/chinas-z-ai-disables-ai-143912200.html) — ZCode 사고와 Z.ai의 조치를 확인했다. 원문 링크는 접근이 막혀 재게재본으로 읽었다.

[Anthropic — Expanding the Cyber Verification Program (2026-10-06)](https://www.anthropic.com/news/cyber-verification-program) — 세 단계로 확대된 접근 구조를 확인했다.

[OpenCode Go 문서](https://opencode.ai/docs/go/) — 월 10달러 요금과 모델별 학습 사용 및 데이터 보존 표를 확인했다.
