---
layout: post
title: "Sam Altman이 Stanford GSB에서 밝힌 인간이 통제하는 미래를 위한 속도 제한과 사이버 방어 전환과 수학자 반응의 닷새 주기, 학생 질문 답변을 외부 보도와 대조한 정리"
date: "2026-10-27 22:13:16 +0900"
created: "2026-10-27T22:13:16+09:00"
source: "https://youtu.be/anAmTGcewX8"
source_title: "Sam Altman, Co-Founder and CEO of OpenAI: Staying Human While Scaling Superintelligence"
author: jungseob
source_author: "Stanford Graduate School of Business (View From The Top, 진행 Claudia Chen)"
source_published: "2026-10-21"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Stanford GSB의 View From The Top에서 Sam Altman이 2026년 10월에 말한 48분 대담을 정리한다. 투자은행 인턴 대신 창업을 고른 일화, 딥러닝이 안 된다던 2005년의 교수, OpenAI가 은퇴 프로젝트로 시작해 제품 회사가 된 경로, 지능의 속도 제한이라는 가장 어려운 결정, 수학 추론에서는 이미 초지능이라는 주장, 사이버보안을 패치로 막을 수 없다는 경고, 수학자들의 반응 주기와 직업 종말론에 대한 반론, 오픈 웨이트 모델에 대한 입장, 학생 질문 답변을 다룬다. 수치와 주장의 대부분이 본인 서술이라는 점과 외부 자료로 확인되는 부분을 나눈다."
image:
  path: "https://i.ytimg.com/vi/anAmTGcewX8/maxresdefault.jpg"
  alt: "Stanford GSB View From The Top의 Sam Altman 대담 썸네일"
tags:
  - knowledge
  - blog
  - AI
  - OpenAI
  - 안전
---

## TL;DR

- Altman은 사람이 미래를 통제해야 하고 권력이 분산되어야 한다는 두 가지를 모두 믿으면, 지능을 얼마나 빠르게 얼마나 높이 올려도 되느냐는 속도 제한 문제가 가장 어려운 결정이라고 말한다. 지난 6개월의 진전이 자신의 신념 일부를 시험했고, 수학 추론이라는 좁은 영역에서는 이미 초지능이 있다고 본다.
- 사이버보안은 모델이 계속 똑똑해지므로 버그를 일일이 패치하는 방식으로는 막을 수 없고, 같은 기술로 새로운 방어 방패를 만들어야 한다는 것이 그의 경고다. 그는 이 문제가 받는 관심이 적다는 데 놀란다고 한다.
- 직업 종말론에는 반대한다. 수학자 공동체가 5일 만에 부정, 종말론, 분노, 재정의로 반응이 바뀐 사례를 들어, 일부 직업의 방식은 완전히 바뀌지만 사람이 하는 일의 가치는 남는다고 본다.
- 오픈 웨이트 모델은 일정 수준까지 사회에 중요하지만 현재 최고 내부 모델은 가까운 시일에 책임 있게 공개할 수 없다고 말한다. "세상이 나쁜 일을 받아들여야 한다"는 팟캐스트 발언은 모든 오픈소스 금지가 더 큰 비용이라는 취지였다고 해명한다.
- 이 노트는 영어 자막 전체를 읽고 일부 주장을 외부 자료로 대조했다. 모델 성능과 칩 수치는 OpenAI 자체 발표 기준이다.

## 대담에 대하여

Stanford GSB의 View From The Top 시리즈로, 2026년 10월 21일에 올라온 48분 48초 영상이다. 진행은 MBA 27학번 Claudia Chen이고 뒤 절반은 학생 질문이다. 녹화일은 영상에 적혀 있지 않지만 대담 속에서 Altman이 9월 UN 연설과 10월 초 Decoded 팟캐스트 발언을 최근 일로 말하므로 10월 초 이후로 보인다. 영어 사람 자막 전체를 읽었다. 이 블로그의 [Altman 통제와 안전 노트](https://raphael-shin.github.io/jungseob-blog/posts/sam-altman-ai-control-and-safety/)와 [권력 집중 노트](https://raphael-shin.github.io/jungseob-blog/posts/sam-altman-ai-control-power-concentration/)가 같은 인물의 9월 발언을 다룬다.

## 창업과 OpenAI의 경로

Altman은 Stanford에서 모두가 투자은행을 가려 해서 또래 압력으로 인턴을 구했다가 점점 두려움이 커졌고 Y Combinator가 여름 생활비를 대 주겠다고 해 그것을 우주의 신호로 받아들였다고 말한다. 창업은 평생 가장 학습률이 높은 환경이었고 "MBA 전체를 한 달에 배운다"는 말을 Paul Graham쯤에게 들었다는 일화도 전한다. 준비하기보다 해 보며 배우라는 것, 곧 가설을 세우고 반성하는 의도적 연습이 핵심이라는 조언이다.

OpenAI에 대해서는 2005년 Stanford CS 교수가 "딥러닝은 안 된다는 것이 확실한 한 가지"라고 했던 일화를 들고 2012년 AlexNet과 2014년의 스케일링 관찰이 방향을 바꾸었다고 말한다. 아름답게 스케일링하는 지수 곡선을 보면 계속 밀어야 한다는 것이 자기 경력의 중심 통찰이다. OpenAI는 은퇴 프로젝트로 보던 연구소였고 초지능을 개발하면 사람들이 혜택을 받으리라는 물음표가 가득한 계획이었으나 기술이 예상과 다른 경로로 가면서 제품 회사가 되어야 했고 2020년 말과 2021년 초에 큰 회사가 될 것임이 분명해졌다고 한다. 그는 이 경로가 전기나 트랜지스터 같은 정상적인 경제적 힘에 가까워 더 좋은 방향이라고 본다. 진행자는 ChatGPT를 주간 10억 명 넘게 쓴다고 소개한다.

## 속도 제한과 안전

가장 어려운 결정으로 그는 속도 제한(pacing)을 꼽는다. 사람이 항상 미래를 통제해야 하고 권력이 분산되어야 한다는 두 믿음을 함께 지키면, 인간 최고 지능보다 AI를 얼마나 빨리 얼마나 높게 올려도 되는지, 사람의 이해 능력을 얼마나 키워야 하는지를 물을 수밖에 없다는 것이다. 모든 규제가 나쁘다는 입장도, 모든 진전을 지금 멈추자는 입장도 틀렸다고 보고 양쪽 사이의 실용적 중도는 어려운 자리라고 말한다.

지난 6개월에 대한 평가는 이렇다. 반복 배포, 사회가 기술과 함께 부딪혀야 한다는 믿음, 사람은 기계의 일에 크게 관심이 없다는 믿음은 유지한다. 그러나 진전 속도가 신념을 시험했고 한두 해 같은 속도라면 현재 구조를 바꾸지 않고는 안 된다고 본다. 그의 관찰로는 조직 안의 논쟁도 모델이 얼마나 좋아질까에서 무엇을 해야 하나로 옮겨 갔다. 정부와의 관계는 최근 몇 달 사이 진지해졌다고 평가한다. 정렬에 대해서는 학생 질문에 이렇게 답한다. 2020년에는 정렬 문제가 더 어려울 것이라 보았는데 모델이 크게 초인적이 되었는데도 지금까지는 예상보다 쉬웠다. 그러나 n+1에서도 쉬우리라는 보장은 없고 오히려 훨씬 어려워질 것 같으며 틀렸을 때의 비용은 크게 올랐다. 샌드박스와 모니터링은 한동안 통하겠지만 결국 이해하고 확신할 수 있는 정렬뿐이라고 하며 세계 일부 AI 노력이 정렬이 쉬웠다는 이유로 지나치게 앞서간다고 우려한다.

이 구간은 Altman 개인의 서술이다. 수학 추론의 "초지능"은 좁은 영역에 한정한 주장이고 기준이나 평가는 제시되지 않는다. 그가 말한 UN 연설은 OpenAI 사이트에 안전보장이사회 연설문이 있고(9월), 같은 날 Dario Amodei도 별도 브리핑을 했다고 Guardian이 보도한다. 이 블로그의 [Amodei 인터뷰 노트](https://raphael-shin.github.io/jungseob-blog/posts/amodei-isaacson-builders-anthropic-trust-red-lines/)는 같은 주제를 경쟁사 쪽에서 본다.

## 사이버보안은 패치로 안 된다

개인과 조직이 위험에 대비하려면 무엇을 해야 하느냐는 질문에 그는 사이버보안 한 가지만 꼽는다. 올해 초 Mythos 소동 때는 일부 버그가 패치되며 나아졌지만 그의 진단으로는 사람들이 지수 곡선을 직관하지 못했다. 모델이 찾은 취약점이 존재하는 전부라고 생각했지만 모델은 계속 똑똑해져, 하드웨어 수준의 위협 모델 밖 버그까지 찾을 수 있다. 조직 리더 대부분은 이미 넘어갔다. 그는 더는 모든 버그를 패치할 수 있다고 보지 않으며 같은 기술로 새로운 방어 방패를 만들도록 방어 모델 전체를 바꿔야 한다고 주장한다. 그는 이것이 거대한 안전과 보안 문제인데 관심이 놀랄 만큼 적다고 말한다. Mythos가 공개를 보류한 Anthropic 모델이라는 배경은 Gizmodo와 CNBC 보도로 확인된다.

## 일자리, 수학자, 의미

학생들에게 그는 변화가 사람들이 생각하는 것만큼 빨리 다르지 않다고 말한다. 많은 업무가 AI로 더 낫고 싸고 빠르게 바뀌고 일부 직업은 지금의 방식이 완전히 AI로 넘어가지만 직업 종말은 아니라는 것이다. 예로 지난 10일간 수학자 공동체의 반응을 든다. 0일에는 가짜라는 반응, 1일에는 우리 분야는 끝났다, 3일에는 OpenAI가 이래선 안 된다, 5일쯤에는 한 종류의 수학 직업은 끝났지만 대부분의 일은 밀레니엄 문제를 푸는 것이 아니라 지식을 이해하고 전달하는 것이었다는 쪽으로 바뀌었다고 한다. 코더, 컨설턴트에게도 비슷한 주기가 있었고 프로그래머는 오히려 더 높은 임금을 받는 방향이라는 설명이다. 그는 변화가 가장 큰 시기에 커리어를 시작하는 것이 유리하고 MBA 학생은 늘 5년 전에 멋졌던 일을 하려 한다는 만성적 실망이 있다고 말한다. 그는 지금이 OpenAI의 복제본을 만들 때가 아니라고 선을 긋고 OpenAI가 내놓은 기술 위에 더 큰 회사가 서길 바란다.

무엇을 직접 배워야 하느냐는 질문에는 필기체 이야기로 답한다. 쓸모를 믿지 못했던 필기체와 달리, 글쓰기는 생각하는 법을 배우는 도구라는 두 번째 교사의 말이 옳았다. 생각을 돕는 기술은 계속 가치가 있고 기계의 영역이 분명한 기술은 그렇지 않다. 그의 논리로는 사람이 하기 때문에 가치와 일에 의미가 있으며 통제 상실 사고만 없다면 둘은 계속 중요하다. 그는 AI의 에너지가 산업혁명 쪽, 곧 모든 것을 자동화하고 사람을 톱니로 만드는 쪽으로 쏠렸다고 보고 창의와 탐구의 르네상스 쪽을 희망한다. 사회와 경제 압력이 냉혹한 효율로 기울어 있어 이에 맞서는 힘이 회사나 정부나 사람들에게서 나와야 한다는 단서를 붙인다.

## 학생 질문: 인프라, 오픈 웨이트, 해자

인프라 질문에 그는 로봇을 첫째로 꼽는다. 로봇이 로봇을 짓고 데이터센터가 데이터센터를 짓는 루프가 AI 연구의 재귀적 개선 루프만큼 큰 일인데 이야기가 적다는 것이다. 둘째는 자체 칩 Jalapeño와 후속 칩으로 와트당 지능에서 시장의 어떤 것보다 큰 이득이라고 하고 셋째는 팹과 전력과 장비의 공급망 투자다. 소프트웨어 해자에 대해서는 역사적으로 소프트웨어 자체가 강한 해자였던 적이 많지 않고 네트워크 효과, 규모 효과, 데이터 해자가 전통적 해자이며 소프트웨어는 그것을 쌓기 위한 임시 우위일 뿐이라고 답한다.

오픈 웨이트 질문(OpenAI Foundation 비서실장 학생)에는 일정 높은 수준까지는 사회에 중요하다고 답한다. 얼마나 큰 피해를 사회가 받아들일지는 앞으로 몇 년 격렬히 논쟁될 이동 표적이며 사회가 회복력을 쌓을수록 달라진다. 그러나 현재 최고 내부 모델은 가까운 시일에 책임 있게 오픈소스로 공개할 수 없다는 것이 그의 입장이다. 사이버 방어 모델이 바뀌어야 하고 생물 방어층이 필요하며 그밖의 긴 목록이 있다는 것이다. 다만 그 수준의 모델을 오픈소스로 낼 곳이 얼마나 뒤처져 있느냐는 확신이 없다고 하며 폐쇄 가중치의 이 앞선 우위가 세계가 방어를 쌓을 시간이라고 본다. 팟캐스트 발언에 대해서는 이렇게 해명한다. 오픈소스 모델이 혐오 발언, 해킹, 사기를 낳고 새 세대의 전화 사기가 나올 것이므로 오픈소스를 전부 금지하자는 사람들이 있는데, 자신은 전부 금지하는 것이 혁신과 자유에 너무 큰 비용이라고 말하려 했고 그 부분이 잘렸다. 인터넷을 마비시키거나 사람에게 물리적 해를 입히거나 새 생물 테러를 만드는 것을 허용할 수 없는 선이 분명하며 이 선을 어디에 그을지가 핵심이라는 것이다. 이 발언 논란은 The Verge와 Guardian이 10월 초에 보도했다.

조직 설계에 대해서는 군대에서 베낀 위계가 기본이지만 1만 개 에이전트가 함께 일한 Navier-Stokes 풀이에서는 리더도, 공로 다툼도, 다툼도 없이 하나의 목표로 정렬되어 있었다고 말한다. 사람은 다른 방식으로 일하겠지만 배울 점이 있고 새 조직 설계가 덜 탐구된 분야라는 것이 마지막 제안이다.

## 대조해서 확인한 점

외부 자료로 확인되는 것은 다음과 같다. OpenAI는 9월에 Navier-Stokes 풀이를 발표했고 약 1만 개 에이전트 집단이 관여했다고 쓴다(OpenAI 글, CNBC 9월 9일). Altman이 UN 안전보장이사회에서 연설한 것은 9월 23일 보도로 확인된다. Decoded 팟캐스트 발언은 Guardian 10월 5일, The Verge가 보도했고 Snopes가 문구를 점검했다. Jalapeño는 OpenAI와 Broadcom의 추론 칩이며 OpenAI는 비교 시스템 대비 와트당 처리량 1.5~1.9배, 종단 지연 1.7~3.6배 낮음을 보고한다. 이는 OpenAI 자사 비교 결과이며 Altman의 시장 최고 수준이라는 표현은 이 비교 범위를 넘는다. Mythos 소동은 Anthropic 공개 보류 모델을 두고 일어난 일이다.

주의할 점도 있다. Navier-Stokes 풀이의 수학적 타당성은 이 블로그의 Schmidt 노트에서 다룬 대로 외부 논쟁 중이고 VentureBeat는 OpenAI가 한 연구자의 비공개 Codex 데이터에서 이득을 봤을 가능성을 배제하지 못한다고 보도했다. Altman이 말한 수학자 반응의 닷새 주기는 그의 요약이고 어느 공동체 설문이나 자료로 확인한 것이 아니다. 대담 앞뒤의 "지난 10일간"이 어느 사건을 가리키는지는 대화에서 이름이 나오지 않는다. 같은 블로그의 [Thompson 노트](https://raphael-shin.github.io/jungseob-blog/posts/thompson-why-the-mathematicians-weep/)가 수학자 쪽 반응을 다룬다. "초지능을 이미 가졌다"는 수학 추론 주장은 기준 없이 한 말이다. OpenAI Foundation이 세계 최대 재단이라는 말은 확인하지 못했다.

## 읽을 때 유의할 점

첫째, 학생 청중 앞의 호의적 행사이고 후속 질문이나 반박이 거의 없다. 둘째, 그는 OpenAI의 CEO로서 속도 제한을 말하면서 같은 회사의 제품과 칩과 모델을 앞세운다. 속도 제한 주장과 실제 배포 계획 사이의 관계는 대담에서 설명되지 않는다. 셋째, 정렬이 지금까지 쉬웠다는 평가는 본인의 서술이며 근거 자료를 제시하지 않았다. 넷째, 오픈 웨이트에 대한 입장은 경쟁사와 중국 오픈 모델 논쟁에서 다른 이해관계를 가진다. 이 블로그의 Cohere·Qwen 노트가 그 한 단면이다. 다섯째, 직업 종말론에 대한 반론은 낙관적 서사이며 고용 통계를 인용하지 않는다.

그래도 가져갈 질문은 선명하다. 지능을 얼마나 빨리 올릴지 결정하는 주체와 기준은 누구인가, 사이버 방어를 패치에서 에이전트 방어로 바꿀 준비가 되어 있는가, 오픈 웨이트의 선은 어떤 능력 수준에 그을 것인가, 내 일에서 사람이라서 의미 있는 부분은 무엇인가.

## 참고 자료

[Stanford GSB: Sam Altman, Staying Human While Scaling Superintelligence (YouTube, 2026-10-21)](https://youtu.be/anAmTGcewX8): 영어 자막 전체(48분)를 읽고 정리했다. 마지막 타임스탬프가 영상 길이와 맞다.

[OpenAI: Navier-Stokes solution](https://openai.com/index/navier-stokes-solution): 약 1만 개 동시 에이전트 서술을 검색 발췌로 확인했다.

[CNBC: OpenAI Navier-Stokes math problem solved (2026-09-09)](https://www.cnbc.com/2026/09/09/openai-navier-stokes-math-problem-solved.html): 발표 사실을 검색 발췌로 확인했다.

[VentureBeat: OpenAI solves longstanding math problem with 10,000-agent swarm](https://venturebeat.com/technology/openai-solves-longstanding-math-problem-with-10-000-agent-swarm-but-cant-rule-out-benefitting-from-a-researchers-private-codex-data): 비공개 Codex 데이터 가능성 단서를 제목과 발췌로 확인했다.

[OpenAI: Sam Altman UN Security Council remarks](https://openai.com/index/sam-altman-un-security-council-remarks): UN 연설 사실을 검색 발췌로 확인했다.

[The Guardian: UNGA Sam Altman Dario Amodei (2026-09-23)](https://theguardian.com/world/2026/sep/23/unga-sam-altman-dario-amodei): 두 CEO의 별도 브리핑을 검색 발췌로 확인했다.

[The Guardian: Sam Altman says the world should accept bad things (2026-10-05)](https://www.theguardian.com/technology/2026/oct/05/sam-altman-open-ai-chatgpt-benefits-risks): Decoded 팟캐스트 발언 보도를 검색 발췌로 확인했다.

[OpenAI: Jalapeño first results](https://openai.com/index/jalapeno-first-results/): 와트당 처리량 1.5~1.9배 보고를 검색 발췌로 확인했다.

[Gizmodo: Sam Altman, I no longer think we are going to be able to just patch all the bugs](https://gizmodo.com/sam-altman-i-no-longer-think-were-gonna-be-able-to-just-patch-all-the-bugs-2000829947): 같은 발언 보도와 Mythos 배경을 검색 발췌로 확인했다.
