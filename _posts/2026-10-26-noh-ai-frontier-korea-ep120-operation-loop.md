---
layout: post
title: "가치는 새지 않는 희소성으로 간다, AI Frontier Korea의 노정석이 CoreWeave 신용 위기와 AI 시장 조정을 operation loop 가설로 해석한 대담을 보도와 대조한 정리"
date: "2026-10-26 07:55:58 +0900"
created: "2026-10-26T07:55:58+09:00"
source: "https://youtu.be/eO8brZguMpU"
source_title: "EP 120. 가치는 어디로 가는가: AI 시장 조정, CoreWeave 위기와 operation loop"
author: jungseob
source_author: "AI Frontier Korea (출연: 노정석, 박종현)"
source_published: "2026-10-25"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "AI Frontier Korea 120화(2026년 10월 25일 공개, 녹화 24일, 80분)를 정리한다. 노정석이 최근 2주의 AI 시장 조정을 수요 붕괴가 아니라 금융 환경의 충격으로 읽고, 가치는 새지 않는 희소성으로 간다는 렌즈로 Frontier Lab과 operation loop를 가진 사업으로 가치가 몰린다고 주장한다. CoreWeave의 채권과 CDS 수치, Anthropic 3분기 성장률, Kimi K3.1 출시, Meta·Oracle의 데이터센터 금융을 보도와 대조하고 발언자의 개인 확률과 해석을 구분한다. 투자 권유가 아니다."
image:
  path: "https://i.ytimg.com/vi/eO8brZguMpU/maxresdefault.jpg"
  alt: "AI Frontier Korea EP 120 가치는 어디로 가는가 썸네일"
tags:
  - knowledge
  - blog
  - AI
  - 투자
  - CoreWeave
---

## TL;DR

- 노정석은 최근 2주의 급락(한국 메모리 반도체 주가가 고점 대비 40% 넘게 하락)을 거품 붕괴가 아니라 재채기에 가깝다고 본다. 수요는 견실한데 금리와 공매도와 계약 기간 불일치 같은 금융 환경이 가장 약한 고리인 CoreWeave를 흔들었다는 설명이다.
- 그의 렌즈는 가치가 "새지 않는 희소성"으로 간다는 것이다. 연구 인력(talent)과 데이터는 이직과 데이터 판매로 새어 나가므로 Frontier Lab과 Near Frontier Lab의 격차는 줄고 모델은 범용재가 될 가능성이 크다. 새지 않는 것은 compute와, Lab이 신호를 가져가려면 큰 희생을 치러야 하는 operation loop(운영 신호가 닫힌 고리로 도는 사업)다.
- 그는 격차가 닫히고(X축) 매출이 감가상각과 이자를 넘는 전환점(Y축)이 아직 오지 않은 사분면 두 곳을 합쳐 약 80%로 본다. 이는 발언자가 매일 바꾸는 개인 확률이며 근거 계산은 제시되지 않았다.
- 보도와 맞는 사실은 CoreWeave의 2031년 만기 9.75% 채권 수익률 약 16%, CDS 1,000bp 돌파(10월 15일), Anthropic 3분기 매출 168억 달러(전 분기 대비 45%), Kimi K3.1 Pro 출시(10월 23일)다. 영상의 세부 수치(1,195bp 정점, 공매도 23.7% 등)는 이 노트가 찾지 못했다.
- 실행 결론은 Frontier Lab 주식을 보험으로 들고, 사업은 Lab이 하지 않는 곳, 곧 operation loop가 이미 있는 기업의 워크플로 재설계로 가라는 것이다. 투자 권유가 아니다.

## 영상에 대하여

AI Frontier Korea 120화로 2026년 10월 25일 공개된 1시간 20분 26초 영상이다. 녹화는 10월 24일 토요일 아침이다. 한국어 자막 전체(80분)를 읽었다. 진행은 노정석과 박종현이고 설명란에 편집자가 적혀 있다. 설명란의 목차는 반도체 급락, 대항해시대 비유, 희소성과 마진 구조, CoreWeave의 금융 구조, operation loop로의 가치 이동, 네 가지 시나리오, 시장 타이밍 일곱 지표다. 노정석은 직접 쓴 에세이와 도표를 공개하겠다고 말하고 자료 조사에 Claude와 ChatGPT와 봇을 수없이 돌렸다고 밝힌다. 이 블로그의 [SpaceX 3분기 실적 해설 노트](https://raphael-shin.github.io/jungseob-blog/posts/spacex-q3-call-compute-payback/)와 [Pichai 컴퓨트 희소성 해설 노트](https://raphael-shin.github.io/jungseob-blog/posts/sixsigma-pichai-compute-scarcity-bubble-question/)가 같은 컴퓨트 수익성 논쟁의 다른 쪽을 다룬다.

## 조정을 읽는 법: 수요가 아니라 금융

노정석은 지금이 인프라 구축(build-out) 국면의 끝자락이라고 보면서도, 철도 때처럼 과투자 뒤의 조정이 폭망이 아니라 소유자 교체라고 말한다. 투자자와 채권자가 손해를 보는 것은 국룰이고 그 위에 응용을 세운 사업자가 더 크게 가져가거나 편익이 사회 전체로 퍼진다. 시장이 놀란 이유로는 Anthropic의 성장 둔화를 꼽는다. 코더는 약 3천만 명이 이미 들어왔는데(a16z 수치로 소개) 코더가 아닌 지식 노동자 15억 명은 아직 들어오지 않아 시차가 있다는 설명이다. 그래서 4분기 성장률이 중요하고 한 번은 평지 구간이 있을 수 있다고 한다. 박종현은 3분기가 전 분기 대비 45% 성장인데도 기대가 꺾였다는 점이 기대가 얼마나 컸는지를 보여 준다고 덧붙인다. 비관이 너무 빨리 왔고 한 번은 조정된 뒤에도 상승 여지가 남아 있다는 것이 노정석의 개인적 시각이다. 수요 쪽 근거로는 비디오 모달리티가 아직 오지 않았다는 점을 든다. 인터넷 초기에 남는 대역폭으로 Netflix와 YouTube가 생겼듯 모델도 그럴 개연성이 있다는 것이다.

CoreWeave 구조는 이렇게 설명한다. 데이터센터 15년 임대, 고객 계약 3년, 5년 만기 채권을 하나의 박스(특수목적회사)에 넣고 hyperscaler가 구매를 보증해 금리를 낮추며 이익과 위험이 본체에 쌓인다. 본체가 낸 무담보 채권은 올해 초 9.75%로 발행한 2031년 만기물이고 최근 만기 수익률이 15.78%까지 올랐으며 100원짜리 채권을 약 80원에 살 수 있는 수준이다. CDS는 1,100bp대로 매년 100원에 11원을 보험료로 내는 셈이다. 그는 이 둘이 수요 때문이 아니라 금융 환경, 곧 금리 상승과 다음 채권 발행이 막히는 위험 때문이라고 본다. 박종현이 정리한 대로 GPU가 안 팔리면 망하는 구조라 시장이 파산 가능성을 가격에 반영한 것이다. 노정석은 10년물 국채가 6%를 넘으면 구조가 무너진다는 시장의 이야기를 전하면서 자신은 엑셀로 계산해 판단하지 않았다고 선을 긋는다. 고객 계약 3년, 임대 15년, 채권 5년의 만기 불일치가 다음 조달 실패의 이유로 의심된다는 설명은 Fable이라 부르는 모델이 찾아온 것이라고 말한다. 공매도 쪽은 CoreWeave와 Nebius의 공매도 잔고가 크고 공매도 계좌의 평가이익이 약 60억 달러이며 더 이상 들어올 자본이 없는 시점에 비관론이 겹쳤다고 설명한다. Citadel의 Ken Griffin은 거품이라고 Goldman Sachs는 공격적 매수라고 본다는 월가의 엇갈린 시각도 전한다.

데이터센터 위험 지도도 그린다. 가장 안전한 쪽은 자기 영업현금으로 짓던 Google, Amazon, Microsoft인데 올해 Google이 처음 채권을 발행했다. 그다음이 Meta로, Hyperion 데이터센터를 자기 지분 20%와 Blue Owl 계열 80%로 짓고 임대 보장과 지급 보증을 붙여 장부상 부채를 줄였지만 잠재 의무가 주석에 남는다. 더 위험한 쪽이 Oracle로, 은행 대출을 신디케이트로 쪼개 파는데 잘 안 팔린다고 들었다고 한다. 가장 위험한 곳은 CoreWeave와 Nebius 같은 정크 등급이고 xAI는 고금리로 많이 빌렸지만 Musk의 상장과 가치 상승으로 부채가 지분으로 바뀌는 방식이 가능하다고 본다. 이자율이 오르면 오른쪽에서부터 위험해지고 왼쪽까지 전염되지는 않으리라는 것이 그의 판단이다. 거품이 터지는지 두 주 동안 물었으며 아니라는 것이 결론이라고 한다.

## 가치는 새지 않는 희소성으로 간다

핵심 렌즈는 공급망에서 마진은 희소한 곳이 가져간다는 것이다. 희소성이 오래 가려면 새지 않아야 하고 이는 해자가 있다는 말과 같다고 그는 설명한다. 이 렌즈로 보면 Frontier Lab이 가격을 올리지 못하는 이유가 드러난다. 미국에는 Muse, Grok, Google, 잠재적 Microsoft와 Amazon이 있고 중국에는 수십 개의 Lab이 있어 모델이 희소하지 않다. 노정석은 그날 아침 나온 Kimi K3.1의 Terminal-Bench 성적이 Opus 5.5에 근접했다고 전하고 이 때문에 Frontier와 Near Frontier의 격차(time gap)가 확 줄었다고 본다. 박종현은 Canva와 HeyGen 같은 서비스가 자체 영상 모델을 내놓고 NeoLab도 뛰어든다고 관찰한다. 노정석은 이를 모델이 자기 사업에 존재 위협이 되므로 Lab에게서 자기 영역(vertical)을 지키려는 노력으로 읽는다. 여기서 domain gap은 Lab이 도메인을 모델의 기능으로 하나씩 박아 넣으며 좁혀진다. 데이터 판매 업체가 같은 RL 데이터셋을 여러 Lab에 파는 식이다.

Frontier Lab을 보는 기준은 compute, data, talent 세 가지다. 그중 data와 talent는 새는 자원이다. 연구자는 샌프란시스코에서 밥 한 끼로 방향성이 퍼지고 데이터는 판매 회사가 이쪽에 판 것을 저쪽에 판다. 그래서 Lab 간 격차를 만드는 것은 천재 한 명이 아니라 compute이며 Ilya Sutskever의 베팅은 잘못됐다는 것이 그의 평가다. 이 경쟁은 누군가 완전히 쓰러질 때까지 멈추지 않으므로 compute는 남아돌지 않는다. 1GW는 Blackwell 기준 GPU 40만~50만 개, 금액으로 500억~800억 달러이고 메모리 값이 2~3년 전보다 10배 올랐다고 말한다. 지금의 성능 향상은 RSI(재귀적 자기개선)가 아니라 compute를 더 투입한 결과이며 compute를 10배 투입하면 체감 성능이 두 배쯤 가는 수준이라고 본다. 수요 측면에서는 대항해시대 비유를 쓴다. 모두가 배를 띄우고 어떤 이는 북극에 닿고 어떤 이는 황금의 땅에 닿으며 한 명의 스타(이효리)에게 기댓값이 몰리니 수만 명의 연습생이 같은 연습량을 쏟는 연예기획사 구조와 같다. 따라서 수요는 대체가 아니라 창조되고 있다는 것이다.

Lab의 공격 경로는 세 가지로 나눈다. 살 수 있는 데이터(buyable)를 사서 장착하는 방식, 신약처럼 기댓값이 큰 곳에 reward signal을 얻는 wet lab을 직접 세우는 방식, 영상 생성 같은 도메인을 직접 가져오는 방식이다. 순서는 시장 크기를 데이터 구매 난이도로 나눈 "Lab의 attention"이 큰 곳부터이고 회계사·변호사·의사처럼 "사" 자 직업들이 전문가를 시간당 고용해 문제와 정답을 만드는 방식으로 검증 가능한 데이터셋이 되면 끝난다. Lab이 건드리기 어려운 곳은 규제가 있거나 시장이 작거나 특허로 보호되는 곳이다. 규제가 해자인 곳으로는 공공 조달 중심의 sovereign 모델 회사를 든다.

## 네 사분면과 operation loop

X축은 Frontier gap이 닫히는지 열리는지, Y축은 매출이 감가상각과 이자를 넘는 전환점이 왔는지다. 지금은 투입이 훨씬 크므로 아래쪽이다. OpenAI와 Anthropic이 원하는 사분면(S3)은 격차가 유지되며 지능의 독점 인프라가 되는 경우다. 노정석은 격차가 닫힐 확률이 높다고 보며 S1(격차가 닫히고 수익 전환이 온 경우)과 S2(격차가 닫히고 투자만 크고 수익 전환이 아직인 경우)의 합을 거의 80%로 둔다. S2는 닷컴 버블에 해당해 인프라가 망한 뒤 시체가 best practice를 이룬 곳으로 흡수되어 S1로 올라간다는 시나리오다. S1과 S2는 동전의 양면이고 시장이 아직 결정하지 않았으며 timing이 가장 중요한 변수라고 한다. Frontier 모델이 유틸리티가 되면 가치는 위아래로 흐른다. 아래는 전력·냉각·Nvidia이고(칩은 희소성에서 벗어나 마진 이전이 있을 수 있다), 위는 operation loop를 가진 곳이다. 그 loop조차 Lab이 가져가 경쟁이 되면 편익은 소비자에게 가고 초지능이 0원이 되는 시대도 가능하다고 말한다.

operation loop는 이렇게 정의한다. 사업에서 매일 생기는 신호(매출이 이렇게 빠지면 이곳이 문제여서 이렇게 고친다)가 질문과 답으로 쌓이다 몇 개의 규칙, 곧 지혜의 압축체로 줄어든다. 모델에 심을 만큼 큰 데이터셋은 아니지만 그 사업만의 규칙이다. 그 사업에 반드시 자체 모델이 필요하지는 않고 near-frontier 오픈웨이트 모델에 compute를 꽂으면 해결되는 경우가 많으며 그래서 그의 문장은 "weight의 소유는 감가, signal의 소유는 복리"다(이 문구는 모델이 쓴 것이라고 밝힌다). 모델 작업 밖의 후보는 셋이다. B2B에서 기업 운영 안에 loop를 짓는 쪽(Palantir, 각 Lab의 FDE 조직이 이미 한다), B2C에서 소비자 눈앞을 잡는 비서 싸움(Muse Spark, Gemini Spark, Grok Bot, 국내 대형 업체도 만들 것이며 승부는 일의 범위와 깊이의 곱), Tesla처럼 수직계열화로 자체 신호 loop를 돌리는 쪽이다. 투자 결론은 Frontier Lab 주식을 인플레이션까지 막는 보험으로 들고 사업은 Lab이 하지 않는 곳으로 가라는 것이며 그 자신도 B2B 기업용 AI 회사를 차릴 생각이라고 말한다.

타이밍 지표 일곱 가지는 정량이 아닌 추적 항목이다. spot과 contract 가격 격차, GPU 회수 기간(payback period)과 감가 연한(3년 대 8년), 오픈웨이트와 Frontier의 격차(4개월에서 2개월 안쪽으로 줄어드는 것으로 느낌), 코딩 밖의 도메인 에이전트 확산, 대형 도메인의 진입, FDE 프로젝트에서 토큰 비용 대비 컨설팅 마진의 비율, RSI의 첫 관측이다. 박종현은 퇴역한 A100에서도 매출이 나온다고 덧붙인다.

## 대조해서 확인한 점

보도와 맞는 서술이 많다. CoreWeave는 4월에 17.5억 달러의 9.75% 무담보 채권(2031년 10월 만기)을 액면가로 발행했고 5년물 CDS가 10월 15일 1,000bp를 넘어 사상 최고 수준에 이르렀으며 2031년 만기 채권 수익률은 16%에 가까웠다. 부채와 의무 잔액은 510억 달러를 넘는다고 한 보도가 전한다. 공매도 세력의 평가이익 60억 달러는 Reuters(10월 22일)가 이달 들어 네오클라우드와 데이터센터 업체에 베팅한 투자자들의 평가이익으로 전한 수치와 일치한다. Anthropic은 투자자들에게 3분기 매출이 전 분기 대비 45% 늘어 168억 달러이며 조정 이익 기준으로 흑자였다고 밝혔고 최대 2조 달러 기업 가치로 상장을 노리다가 성장 둔화로 투자자들이 기대 가치를 낮췄다고 Reuters와 조선일보가 전한다. Kimi K3.1 Pro는 10월 23일 출시되었고 Artificial Analysis는 GDPval-AA에서 Claude Opus 5.5 바로 아래라고 평가했다. Moonshot은 코딩 시험에서 Opus 5.5에 근접한다고 주장하고 가중치를 11월 4일까지 공개하겠다고 했으며 이 평가는 회사 주장이다. Meta의 Hyperion은 Blue Owl 계열이 80%, Meta가 20%를 보유하는 합작이며 임대 갱신 보증이 붙는다는 점이 맞다. Oracle 관련 은행 대출 380억 달러는 6개월 넘게 인수자를 찾았다는 보도가 있다. 코스피가 고점 대비 40% 넘게 빠졌다는 보도도 있어, 영상의 "메모리 반도체 주가 40% 하락"과 방향은 같지만 지수와 개별 종목 수치를 따로 확인하지는 못했다. a16z의 "약 3천만 명의 개발자"는 a16z 글에 있다.

이 노트가 찾지 못한 것은 다음이다. 채권 수익률 15.78%와 CDS 정점 1,195bp, 현재 1,115bp의 정확한 값, CoreWeave 공매도 23.7%, 코더 아닌 지식 노동자 15억 명과 컴퓨트의 90%를 1%의 회사가 쓴다는 a16z 수치, Anthropic의 2026년 1분기 매출이 2025년 전체보다 컸다는 주장, Ken Griffin과 Goldman의 입장, SpaceX의 3GW 규모와 spot 판매, 1GW의 GPU 수와 금액, 메모리 값 10배, Chinchilla의 하한 1.68과 "10배 compute에 reducible loss 30% 감소"라는 정량이다. 그의 확률 80%와 사분면 모델은 개인 판단이며 영상도 숫자를 모든 포인트마다 설명하지 않는다고 밝힌다.

## 읽을 때 유의할 점

첫째, 발언자의 이해관계다. 노정석은 이 자리에서 Frontier Lab 주식을 보험으로 들고 B2B AI 회사를 차릴 생각이라고 말하며 결론이 자신의 계획과 맞닿아 있다. 둘째, 가치가 새지 않는 희소성으로 간다는 렌즈는 설명 틀이지 검증된 예측 모델이 아니다. 격차가 닫힌다는 전제는 Kimi 같은 한 사례와 느낌의 지표(4개월에서 2개월)에 기대고 있다. 셋째, 사분면 확률 80%는 계산이 공개되지 않았고 영상에서 매일 바꾼다고 말한다. 넷째, CoreWeave를 두고 "수요는 견실하고 금융 환경이 문제"라는 진단과 "10년물 6%에서 무너진다"는 시장의 말을 함께 전하면서 본인이 재무 계산을 하지 않았다고 밝히는데, 이는 기사 수준의 정리와 다른 층위다. 다섯째, operation loop의 신호가 사업마다 어떻게 규칙으로 압축되는지, 얼마나 지속적인 해자인지는 사례로 증명되지 않았다. 그는 몇 개 회사로 이미 증명하고 있다고 말하지만 이름은 밝히지 않았다. 여섯째, 자동화된 조사(여러 모델이 찾아온 자료)를 근거로 썼다는 점을 스스로 밝히므로 개별 수치는 원자료로 다시 확인해야 한다. 이 노트는 투자 권유가 아니다.

그래도 가져갈 질문은 선명하다. 우리 사업의 매출 중 사용자의 체류에서 오는 부분과 기반 서비스에서 오는 부분은 각각 얼마인가, Lab이 데이터를 사거나 직접 연구소를 세워도 신호를 가져갈 수 없는 고리가 우리에게 있는가, 모델 가격이 범용재로 내려갈 때 우리의 마진은 위와 아래 중 어디에서 오는가, 매출이 감가상각과 이자를 넘는 전환점을 우리는 어떤 지표로 볼 것인가.

## 참고 자료

[AI Frontier Korea — EP 120. 가치는 어디로 가는가: AI 시장 조정, CoreWeave 위기와 operation loop (YouTube, 2026-10-25)](https://youtu.be/eO8brZguMpU) — 한국어 자막 전체(80분)를 읽고 정리했다. 화면의 도표는 보지 못했다.

[Sotkn — CoreWeave CDS 1,000 bp after Gartner neocloud forecast](https://sotkn.com/wire/coreweave-cds-1000-bp-gartner-neocloud-shakeout-wire) — 10월 15일 CDS 1,000bp 돌파를 검색 발췌로 확인했다.

[Universeblend — CoreWeave AI infrastructure debt](https://universeblend.blog/coreweave-ai-infrastructure-debt) — 4월 17.5억 달러 9.75% 2031년 10월 만기 무담보 채권을 검색 발췌로 확인했다.

[Pivotnews — CoreWeave credit risk hits record](https://pivotnews.ai/five/coreweave-credit-risk-hits-record-as-swaps-price-60) — 10월 15일 사상 최고 CDS와 2031년물 수익률 16% 근처를 검색 발췌로 확인했다.

[Reuters via Investing.com — Short sellers pocket 6 billion in profits as neoclouds slide (2026-10-22)](https://www.investing.com/news/stock-market-news/short-sellers-pocket-6-billion-in-profits-as-neoclouds-slide-on-ai-debt-fears-4966395) — 공매도 평가이익 60억 달러를 검색 발췌로 확인했다.

[Reuters via The Hindu BusinessLine — Investors temper Anthropic IPO valuation expectations (2026-10-17)](https://www.thehindubusinessline.com/info-tech/investors-temper-anthropic-ipo-valuation-expectations-over-revenue-growth-slowdown-sources-say/article71590936.ece) — 3분기 매출 168억 달러, 전 분기 대비 45%를 검색 발췌로 확인했다.

[Artificial Analysis — Kimi K3.1 Pro launch benchmarks](https://artificialanalysis.ai/articles/kimi-k3-1-pro-launch-benchmarks) — GDPval-AA 3위, Opus 5.5 바로 아래라는 평가를 검색 발췌로 확인했다.

[The Next Web — Moonshot Kimi K3.1 Pro (2026-10-23)](https://thenextweb.com/news/moonshot-kimi-k3-1-pro-open-weight-cyber) — 출시일과 11월 4일 가중치 공개 계획, 회사의 근접 주장을 검색 발췌로 확인했다.

[Meta — Meta and Blue Owl Capital develop Hyperion data center (2025-10-21)](https://about.fb.com/news/2025/10/meta-blue-owl-capital-develop-hyperion-data-center) — Blue Owl 80%, Meta 20% 합작 구조를 검색 발췌로 확인했다.

[Brookings — The 10 trillion question: financing the AI buildout](https://www.brookings.edu/articles/the-10-trillion-question-financing-the-ai-buildout/) — Hyperion의 임대 갱신 보증 구조 설명을 검색 발췌로 확인했다.

[Yahoo Finance — Banks arranged 38 billion in AI debt, finding buyers took months](https://finance.yahoo.com/technology/ai/articles/banks-arranged-38-billion-ai-152113770.html) — Oracle 관련 은행 대출의 인수자 탐색 지연을 검색 발췌로 확인했다.

[a16z — The trillion dollar AI software development stack](https://a16z.com/the-trillion-dollar-ai-software-development-stack/) — 3천만 명의 개발자 수치를 검색 발췌로 확인했다.
