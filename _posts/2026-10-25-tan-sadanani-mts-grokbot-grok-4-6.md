---
layout: post
title: "Grok 4.6 발표 당일 MTS 인터뷰에서 Lauren Tan과 Roshan Sadanani가 라이브로 보인 Grok Bot 에이전트 팀과 비용 대비 성능 주장을 공개 벤치마크와 대조한 정리"
date: "2026-10-25 17:32:31 +0900"
created: "2026-10-25T17:32:31+09:00"
source: "https://www.youtube.com/watch?v=A63sedG-p5Q"
source_title: "Are Agents About to Replace Software Engineering? Lauren Tan and Roshan Sadanani"
author: jungseob
source_author: "MTS (진행) · Lauren Tan, Roshan Sadanani (Cursor)"
source_published: "2026-08-13"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "MTS 방송이 2026년 8월 13일에 올린 29분 인터뷰를 정리한다. Grok 4.6 발표 당일 Cursor의 Lauren Tan과 Roshan Sadanani가 Grok Bot의 내부 PMF, 이름 붙인 봇 팀과 조율 봇의 라이브 시연, 클라우드 에이전트 연결, 엔지니어의 역할 변화, 비용 대비 성능 주장을 이야기한다. 벤치마크 수치(70.8% 대 70.5%, 과업당 2.81달러 대 17.32달러)를 x.ai와 제3자 자료로 대조하고 자사 벤치마크라는 한계를 밝힌다."
image:
  path: "https://i.ytimg.com/vi/A63sedG-p5Q/maxresdefault.jpg"
  alt: "MTS 영상 Are Agents About to Replace Software Engineering Lauren Tan and Roshan Sadanani 썸네일"
tags:
  - knowledge
  - blog
  - AI
  - 에이전트
  - Grok
---

## TL;DR

- Lauren Tan과 Roshan Sadanani(Cursor)는 Grok Bot이 내부에서 개발자, 영업(go-to-market), 운영, 제품 팀 모두에게 번져 PMF를 얻었다고 설명한다. 인터뷰 중 라이브 시연에서는 조율 봇(chief of staff)이 쇼핑 봇과 마케팅 봇에게 일을 시키고, 마케팅 봇이 자기 컴퓨터로 LinkedIn에 게시글을 올린다.
- 제품 설계 지침은 단순함이다. 에이전트를 도구 호출을 일일이 지시할 대상이 아니라 동료로 대하게 하고, iMessage 같은 화면에서 이름과 정체성이 있는 봇과 대화하며 봇이 자기 컴퓨터에서 하는 일을 볼 수 있게 한다.
- Tan에게 엔지니어의 역할은 봇 팀을 관리하는 총주방장 쪽으로 옮겨 간다. 봇이 사용자 피드백을 받아 클라우드 에이전트로 버그를 고쳐 PR을 올리고, 그녀는 PR을 검토하며, 코드베이스를 린트와 CI로 조여 PM과 디자이너도 좋은 코드를 낼 수 있게 하는 것이 엔지니어의 책임이라고 말한다.
- 비용 주장은 방송 진행자가 읽었다. Grok 4.6 Extra High가 CursorBench 3.2에서 70.8%, 과업당 2.81달러이고 Fable 5 Max는 70.5%에 17.32달러라는 것이다. 제3자 자료와 일치하지만 벤치마크가 Cursor 자체 것이며 x.ai 표의 Grok 4.6 High는 69.9%다.
- 이 노트는 영어 자막 전체(28분 41초, 광고 낭독 제외)를 읽고 x.ai 발표와 보도로 수치를 대조했다.

## 영상에 대하여

MTS(기술·비즈니스·정치·문화를 다루는 생방송 인터뷰 쇼)가 2026년 8월 13일에 올린 28분 41초 영상이다. 영어 자동생성 자막 전체를 읽었다. 출연자는 Cursor의 Lauren Tan(X 계정 poteto, 엔지니어)과 Roshan Sadanani(자막에는 Sadhnani, 설명란 표기를 따랐고 직함은 방송에서 밝히지 않았다)이다. 방송은 "오늘 아침 Cursor와 SpaceX가 Grok 4.6을 공동 발표했다"는 말로 시작하며 Tan이 Grok Bot이 어제 나왔다고 말하는 것이 8월 11일 출시와 맞는다. 14분께와 27분 이후의 광고 낭독(ElevenLabs, Neon, Kong, Blitzy, AdQuick, Arena, VCX)은 내용에서 제외했다. 같은 인물의 긴 강연은 이 블로그의 [신뢰 곡선 노트](https://raphael-shin.github.io/jungseob-blog/posts/tan-trust-curve-verification-agents/)에, Grok Bot 설계 대담은 [Grok Bot 팀 노트](https://raphael-shin.github.io/jungseob-blog/posts/grokbot-team-bots-yang-interview/)에 정리했다.

## Grok Bot의 내부 PMF

Sadanani는 Grok Bot이 매우 작은 팀이 프로토타입으로 만들던 것에서 시작해 점차 사내로 번졌다고 설명한다. 영업, 운영, 엔지니어링, 제품 팀이 모두 붙잡았고 각자 일에 맞는 재미있는 쓰임을 찾았다. Tan은 자신이 이 제품으로 오디세이 IMAX 티켓을 예매했다는 일화를 든다. 이 제품에는 봇이 자기 컴퓨터를 가지고 있어 사용자가 컴퓨터 앞에 없어도 돈다는 점이 핵심이다. Cursor가 제품을 사내에 먼저 내보내 취향이 높은 동료들의 피드백으로 PMF를 가늠한 뒤 외부로 내보낸다는 절차도 설명한다. 배경에는 Cursor 안에서 사람들이 직접 에이전트를 짜 맞추고 Slack 봇을 만들던 일이 있었다. 맥락이 많이 필요한 이 일을 제품으로 포장할 수 있겠느냐는 발상이었다.

## 시연: 봇 팀

Tan의 화면에는 봇 팀이 있다. 조율 에이전트(chief of staff)는 캘린더를 알고 다른 에이전트에게 메시지를 보낼 수 있다. 시연에서 조율 봇이 쇼핑 봇(Shoppie)에게 물어 최근 구매를 확인한다. 마케팅 봇은 그녀의 LinkedIn에 로그인된 자기 화면을 가지고 있어 게시글을 가져오고 요청을 받아 "Grok Bot을 라이브로 이야기 중"이라는 게시글을 MTS 계정을 태그해 올린다. 방송 진행자는 올바른 MTS 계정이 태그됐다고 확인한다. 또 조율 봇에게 사내 채널 "Grok Bot wins"의 피드백을 모아 Figma 슬라이드로 만들게 한다. Tan은 이를 지루한 일(drudgery)을 자동화하는 예로 든다. 설계 영감은 지능적인 동료와 채팅하는 느낌이다. 차례를 기다리거나 생각이 끝나기를 기다릴 필요 없이 대화하고 봇이 자기 컴퓨터에서 하는 일을 볼 수 있다는 점이다.

두 번째 시연은 엔지니어링 쪽이다. 조율 봇이 오늘 흥미로운 버그가 있었는지 찾아 몇 건을 보여 주고 Tan이 지시하자 기능별 봇 팀(각 봇이 한 기능 담당)에게 과업을 나눠 보낸다. 끝에는 PR, 영상, 스크린샷이 돌아온다. 한 봇은 클라우드 에이전트를 직접 시작하는데, Cursor에서 클라우드 에이전트를 설정해 두면 Grok Bot의 봇이 이를 켤 수 있다는 눈에 안 띄는 기능이다. 이미 진행 중인 작업이 여럿 있어 검토할 PR이 쌓인다고 한다. 봇 아바타는 고양이 사진이다. Tan은 여러 번 자신의 봇 Benny가 사용자 피드백을 받아 밤새 버그를 고치는 것이 출발이었다고 말한다. 지금은 피드백이 들어올 때마다 봇이 알아서 고치러 가고 그녀는 코드를 검토한다. 그녀는 자신이 디지털 동료들의 관리자 같다고 표현한다.

## 설계 의도와 엔지니어의 역할

방송 진행자는 openclaw와 텔레그램으로 쇼핑 에이전트를 직접 구성해 봤는데 자주 고장 났다며 이 UI와 구조가 마음에 든다고 말한다. Sadanani는 설계 지침이 단순함이었고 많은 AI 애플리케이션이 힘과 복잡함의 균형 때문에 통제 옵션을 많이 준다고 말한다. Tan은 Cursor가 파워 개발자용으로 손잡이가 많고 코딩에 맞춰져 있다고 비교하며 Grok Bot에서는 에이전트가 동료라면 어떤 모습일지를 새로 생각했다고 한다. 동료에게 어떤 도구 호출을 쓰고 있느냐고 묻지는 않는다는 것이다. 타깃 사용자는 모두라고 한다. 반응에 대해서는 Tan이 사람들이 정체성, 애니메이션, 로고를 좋아하고 직관적이며 어머니에게 공유해 온보딩하는 사례도 봤다고 말한다. 아직 버그가 있다고도 인정한다.

엔지니어의 역할에 대한 대목이 가장 길다. Tan은 에이전트 세계의 엔지니어는 에이전트의 엔지니어링 매니저와 비슷하다고 보고 코드베이스를 PM과 디자이너도 품질 높은 코드를 낼 수 있는 상태로 유지하는 것이 책임이라고 말한다. 리팩터링과 재작성에 투자하고 규칙과 스타일 가이드를 린트 규칙이나 CI 실패 같은 경질 제약으로 옮겨, 영리하지 않은 에이전트도 잘하게 한다. 대규모 리팩터링과 마이그레이션을 거의 혼자서 한 사람과 에이전트 팀으로 했고 원래 팀 단위로 몇 달에서 몇 해가 걸릴 일이라고 말한다. 비유는 미슐랭 주방이다. 직접 요리하지는 않지만 스킬과 리팩터링으로 훈련한 에이전트 팀을 두고 접시를 조립하고 품질을 책임지는 총주방장이다. Sadanani는 효율을 한 단어로 꼽는다. 아이디어와 존재 사이의 병목을 줄이고 싶고 에이전트 무리가 자신의 취향에 맞는 품질로 결과를 내는 것이 꿈이라고 한다. 이런 논의가 있는데도 엔지니어 수요가 오히려 늘고 있다는 진행자의 관찰에는 두 사람이 동의하며 취향의 역할을 든다. 앞으로의 방향으로 Tan은 iMessage로 봇에게 문자를 보내는 기능(초기에 직접 해킹해 붙였다)을 언급하지만 Grok Bot에 넣을지는 미정이고 두 사람은 에이전트에게 휴가(PTO)를 주자는 농담을 나눈다.

## 비용 대비 성능

진행자가 Cursor의 벤치마크 CursorBench 3.2 결과를 읽는다. Grok 4.6 Extra High가 70.8%에 과업당 평균 2.81달러이고 Fable 5 Max는 70.5%에 17.32달러라는 것이다. Tan은 자신은 토큰이 무제한이라 아끼지 않지만 많은 고객은 비용에 민감하다고 말하고 다른 대형 모델만큼 좋으면서 비용이 일부인 효율적 모델에 가장 흥분한다고 한다. Sadanani는 월 20달러 같은 예산에서 과업당 비용이 내려가면 더 많은 일을 할 수 있다고 말한다. 같은 대화에서 Tan은 앞서 Grok 4.5를 말하다 4.6을 가리키는 말실수를 하는데 같은 토큰 비용에 더 높은 지능이라는 취지다. 진행자는 이것이 스타트업과 인디 개발자의 경기장을 평평하게 한다고 정리한다.

## 대조해서 확인한 점

벤치마크 수치는 외부 자료와 일치한다. 제3자 분석 글(aireiter)은 Grok 4.6 Extra High가 CursorBench에서 70.8%에 과업당 2.81달러, Fable 5 Max가 같은 에이전트 하네스에서 70.5%에 17.32달러이고 단계 수는 46 대 72라고 쓴다. x.ai의 Grok 4.6 발표 표는 등급을 달리해 Grok 4.6 High 69.9%, Grok 4.5 High 66.7%, GPT-5.6 Sol Max 67.2%, Fable 5 Max 70.5%를 싣는다. 따라서 70.8%는 Extra High 등급의 수치이고 표의 High와 구분해야 한다. 가격은 입력 100만 토큰당 2달러, 출력 6달러로 Tan의 "토큰 비용이 4.5와 같다"는 서술과 맞는다. 다만 이 비교는 Cursor가 만든 벤치마크에서 Cursor 직원이 낸 결과이고 같은 발표에서 다른 벤치마크(DeepSWE v1.1)는 Grok 4.6이 65.9%로 GPT-5.6 Sol 73%, Fable 5 70%보다 낮다. 비용 우위가 모든 과업에 적용되지는 않는다.

Grok Bot의 출시 시점과 기능(이름 붙은 봇, 자기 컴퓨터)은 앞서 정리한 Grok Bot 자료와 맞는다. LinkedIn 게시나 슬라이드 생성 시연이 일상 업무에서 얼마나 안정적인지는 라이브 시연 한 번으로는 알 수 없다. 사내 "PMF"와 반응에 대한 서술에는 수치가 없다.

## 읽을 때 유의할 점

첫째, 출연자 둘 다 Cursor 직원이며 제품 출시일에 나온 홍보성 인터뷰다. 진행자의 질문도 우호적이다. 둘째, 라이브 시연은 성공한 장면이며 실패율이나 오작동은 보이지 않는다. 셋째, 봇이 로그인된 계정으로 외부에 글을 올릴 수 있다는 점은 권한과 책임 문제를 낳는다. 이 블로그의 [Seemann 노트](https://raphael-shin.github.io/jungseob-blog/posts/seemann-releasing-ai-generated-software/)가 다룬 것처럼 에이전트가 한 일의 책임은 사람에게 남는다. 방송에서는 이 문제가 논의되지 않았다. 넷째, 벤치마크 수치는 자사 지표이며 독립 재현은 확인하지 못했다. 다섯째, "엔지니어 수요가 늘고 있다"는 진행자의 관찰은 근거가 제시되지 않았다.

그래도 가져갈 질문은 선명하다. 에이전트에게 자기 컴퓨터와 로그인 권한을 줄 때 어떤 행동까지 사전 승인 없이 허용할 것인가, 조율 에이전트가 하위 에이전트에 일을 나누는 구조에서 책임은 누구에게 돌아가는가, 비용 대비 성능 비교를 우리 과업으로 다시 재 본 적이 있는가.

## 참고 자료

[MTS — Are Agents About to Replace Software Engineering? Lauren Tan and Roshan Sadanani (YouTube, 2026-08-13)](https://www.youtube.com/watch?v=A63sedG-p5Q) — 영어 자동생성 자막 전체(28:41)를 읽고 정리했다. 광고 낭독은 제외했고 화면 시연은 말로만 파악했다.

[x.ai — Grok 4.6](https://x.ai/news/grok-4-6) — 벤치마크 표(CursorBench v3.2 등)와 가격을 검색 결과 발췌로 확인했다.

[aireiter — Grok 4.6 vs Fable 5](https://aireiter.com/blog/grok-4-6-vs-fable-5) — Extra High 70.8%, 과업당 2.81달러 대 17.32달러를 검색 결과 발췌로 확인했다.

[Analytics India Magazine — SpaceXAI launches Grok 4.6](https://analyticsindiamag.com/ai-news/spacexai-launches-grok-46-to-take-on-gpt-56-and-fable-5) — DeepSWE v1.1 수치와 가격을 검색 결과 발췌로 확인했다.
