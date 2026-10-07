---
layout: post
title: "사서 쓰던 AI를 만들어 쓰는 쪽으로, Meta와 Microsoft가 사내 Claude 사용을 줄인다는 보도와 읽는 법"
date: "2026-10-07 22:10:16 +0900"
created: "2026-10-07T22:10:16+09:00"
source: "https://www.thestreet.com/technology/meta-microsoft-send-employees-memo-about-anthropic-claude"
source_title: "Meta and Microsoft just sent employees a memo about Anthropic"
author: jungseob
source_author: "Hillary Remy (TheStreet)"
source_published: "2026-10-06"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "TheStreet 분석 기사가 The Information 보도를 인용해 전한 Microsoft와 Meta의 사내 Claude 사용 축소를 PYMNTS와 TechRadar 보도로 대조하고, 보도된 사실과 기사의 해석을 나눠 정리한다."
image:
  path: "https://s.yimg.com/lo/mysterio/api/0dc7d9c4c5676d1b7cff6a31e3eda952fe9c79225dc4ba84a8c3e7ca6af11ac0/lightyear_networkapi/resizefill_w1200%3Bquality_80%3Bformat_webp/https%3A%2F%2Fmedia.zenfs.com%2Fen%2Fthestreet_881%2Fe637e7037667a7ca7052085f8469d497.jpg"
  alt: "기사 대표 이미지 · TheStreet 재게재본"
tags:
  - knowledge
  - blog
  - AI
  - 비즈니스
  - web
---

## TL;DR

- The Information은 Microsoft와 Meta가 직원들의 Anthropic Claude 사용을 줄이고 있다고 보도했다. TheStreet 기사는 이 보도를 받아 두 회사의 결정이 같은 논리라고 해설한다. 직접 만든 도구를 쓰면 돈과 데이터와 개선 고리가 안쪽에 남는다는 것이다.
- 보도된 숫자는 두 가지다. Microsoft는 올해 사내 Anthropic 지출이 최소 10억 달러가 될 것으로 보았으나 추정치를 3분의 1 넘게 낮췄다. Meta의 Claude Code 사용자는 올해 초 약 6만 명에서 약 3만 명으로 줄었다.
- 줄어든 이유는 보도마다 무게가 다르다. 기사는 Meta의 봄 감원이 일부를 설명하지만 주된 원인은 자체 도구 개발이라고 전한다. 비용 때문이라는 설명은 TechRadar의 추측에 가깝고 보도된 사실이 아니다.
- 기사는 이 축소가 Anthropic의 상업적 위치에 대한 판결은 아니라고 선을 긋는다. Microsoft 플랫폼을 통한 기업 고객 수요는 유지되고 있다고 전해진다. 다만 그 수요가 유지되고 있다는 근거도 The Information 보도의 인용이다.
- 이 노트는 TheStreet 본문을 Yahoo Finance 재게재본으로 읽었고, The Information 원문은 유료벽이라 읽지 못했다.

## 무슨 일이 보도되었나

출발점은 The Information의 10월 5일자 보도다. 공개된 도입부는 Meta와 Microsoft가 Anthropic의 가장 큰 기업 고객에 속하며 둘 다 직원들의 Claude 사용을 줄이려 한다고 적는다. 이 보도의 본문은 유료라서 읽지 못했다. PYMNTS가 같은 날 요약한 내용과 TheStreet, TechRadar가 그 요약을 받아 쓴 내용을 겹쳐 읽었다. 세 매체 모두 익명 취재원을 인용한 The Information의 보도를 다시 전하는 글이므로, 세 번 확인된 것이 아니라 한 보도가 세 곳에서 반복된 것이다.

Microsoft 쪽은 이렇게 전해진다. 올해 초 경영진은 사내에서 Anthropic 도구에 최소 10억 달러를 쓸 것으로 보았고, 이 추정치가 3분의 1 넘게 줄었다고 TheStreet은 전한다. PYMNTS는 같은 내용을 올해 10억 달러를 쓸 궤도였다가 3분의 1을 낮췄다고 쓴다. 대상에는 Claude Code, Copilot 안의 Claude 모델, Claude Mythos가 포함된다고 PYMNTS는 적는다. 경영진은 직원들에게 Claude 사용을 제한하고 Microsoft 자체 AI 제품을 우선하라고 지시했다. Microsoft 대변인은 GitHub Copilot 쪽으로 유도하고 있지만 엔지니어가 다른 모델을 고를 수는 있다고 밝혔고, 이 발언은 PYMNTS만 전한다.

Meta 쪽은 Claude Code 사용 직원이 올해 초 약 6만 명에서 약 3만 명으로 줄었다는 것이다. 대체재로 사내 코딩 도구 MetaCode는 사용자가 3만 명을 넘었다. Meta 자체 모델로 구동되는 Muse Code는 8월에 외부 시험을 시작했고 보도 시점에 내부 사용자가 6천 명을 넘었다. 또 PYMNTS는 MetaCode를 사내 전용 도구로, Muse Code를 Claude Code의 경쟁 제품으로 구분한다. Meta는 The Information의 보도에 논평하지 않았다. PYMNTS는 Meta가 올해 AI 도구에 수십억 달러를 쓸 궤도였고 Claude Code가 가장 인기 있었다고 전한다.

## 기사의 해석, 만들면 남는 것이 다르다

TheStreet 기사는 사실 전달보다 해설이 중심이다. 핵심 논지는 AI 업계가 3년 동안 외부 모델을 가장 빨리 도입한 회사에 보상했지만 이제 두 번째 국면이 시작되고 있다는 것이다. 이 국면은 사서 쓰던 것을 직접 만든 것으로 바꾸는 회사에 유리하다. 사용 규모가 Microsoft와 Meta 수준이면 청구서가 빠르게 커지고 직접 만들면 초기 투자는 크지만 데이터가 자기 것으로 남고 도구를 직원의 실제 업무에 맞출 수 있다는 논리다.

기사가 드는 이유는 재무와 전략 두 가지다. 재무적으로는 9자리 숫자의 내부 AI 청구서를 마주하면 직접 만드는 쪽이 매력적으로 보이고 운영비도 시간이 갈수록 낮아진다. 전략적으로는 Microsoft가 자체 모델을 GitHub Copilot, Microsoft 365, Azure에 더 깊게 통합할 수 있고 Meta는 엔지니어의 작업 방식에 맞춘 도구를 학습시킬 수 있다. 자체 스택을 쓰는 회사는 사용 데이터를 통해 도구를 개선하지만 남의 모델을 빌리는 회사는 그 고리를 얻지 못한다. 기사는 최고의 모델을 갖는 것만으로는 더 이상 충분하지 않고 클라우드 연산과 개발자 도구와 기업용 소프트웨어 계층을 쥔 회사가 실제 우위를 굳힌다고 본다.

이 논리는 그럴듯하지만 기사가 제시한 근거는 보도된 두 회사의 결정이 전부다. 자체 도구가 Claude만큼 좋아서 바꾸는 것인지, 비용 때문인지, 전략적 통제 때문인지는 보도가 밝히지 않는다. 기사는 이유를 분석가의 논리로 채우고 있다.

## 축소가 Anthropic에 말해 주는 것과 말해 주지 않는 것

기사는 마지막 소제목에서 이번 보도가 Anthropic의 상업적 위치에 대한 판결이 아니라고 적는다. 근거는 세 가지다. Microsoft의 내부 지출 축소는 기업 고객에게 Claude를 파는 일과 별개이고, 그 고객 수요는 The Information에 따르면 유지되고 있다. 기업은 단일 공급자보다 여러 AI 제공자를 선호하는 경우가 많다. 자체 도구를 만들 역량이 없는 기업이 더 오래가는 수요일 수 있다. 기사는 이런 고객이 자체 대체재를 키우는 대기업보다 더 예측 가능한 매출을 줄 수도 있다고 쓴다. 기사의 결론은 Anthropic의 기회가 스스로 만들 수 있는 회사보다 그렇지 못한 기업 쪽에 있을 수 있다는 것이다.

한 가지 맥락이 더 있다. 기사는 Meta와 Anthropic의 관계가 겹겹이라고 지적한다. Meta와 Anthropic은 Anthropic이 Meta 데이터센터 인프라 접근에 대가를 치르는 연산 계약을 논의해 왔다고 하며, 기사는 상업적 관계와 경쟁 관계가 한 업계에서 동시에 존재할 수 있다고 쓴다. TechRadar는 더 나아가 Anthropic이 미 국방부로부터 국가 안보 공급망 위험으로 지정된 일과, IPO 설명서가 중대한 매출 손실이나 사업 차질 가능성을 경고한 문구를 함께 언급한다. 두 대형 고객을 잃으면 수십억 달러 매출에 영향을 줄 수 있다는 것도 TechRadar의 평가다. 이는 TechRadar의 평가이고 The Information 보도의 내용은 아니다.

## 읽을 때 유의할 점

첫째, 모든 핵심 수치가 익명 취재원을 둔 한 보도에서 나온다. 10억 달러라는 추정치는 Microsoft가 경영진 차원에서 올해 초에 세운 전망이고 실제 집행액이 아니다. 줄었다는 3분의 1도 그 전망의 축소다. Meta의 6만에서 3만으로의 변화는 일부가 봄 감원으로 설명된다. TheStreet은 Bloomberg를 인용해 그 감원이 전체 인력의 약 10%였다고 쓰고, 주된 원인은 The Information에 따르면 자체 AI 도구 개발 추진이라고 적는다. 사용자가 절반이 된 것을 전부 정책 탓으로 돌릴 수는 없다.

둘째, 이 기사는 투자자용 해설이다. 글머리에 Microsoft(MSFT)와 Meta(META)의 티커가 붙어 있고 결론도 Anthropic의 수요 지속성을 투자 신호로 읽는 방식이다. 사실 보도와 분석가의 전망을 구분해 읽어야 한다. 셋째, 이 노트는 The Information 원문, Microsoft와 Meta의 공식 입장, Anthropic의 반응을 직접 확인하지 못했다. Microsoft 대변인 발언은 PYMNTS가 전한 내용이고 Meta는 논평하지 않았다.

그래도 실무에 가져갈 질문은 분명하다. 외부 모델을 쓰는 비용과 직접 만드는 비용을 서로 다른 시간축에서 비교하고 있는가. 사내 도구를 강제로 밀 때 개발자가 모델을 고를 수 있는 여지를 남기는가, 그리고 자체 도구가 충분히 좋아지기 전에 쓰던 도구의 사용자 수가 줄어들면 생산성이 어떻게 변하는지 재고 있는가.

## 참고 자료

[Hillary Remy — Meta and Microsoft just sent employees a memo about Anthropic (TheStreet)](https://www.thestreet.com/technology/meta-microsoft-send-employees-memo-about-anthropic-claude) — 원문 페이지는 봇 차단으로 열리지 않아, Yahoo Finance에 재게재된 전문을 읽고 정리했다. 재게재본은 원문 링크와 10월 6일 최초 게시를 명시한다.

[PYMNTS — Microsoft and Meta Steer Staff From Anthropic Claude to In-House AI](https://www.pymnts.com/news/artificial-intelligence/2026/microsoft-meta-steer-staff-from-anthropic-claude-in-house-ai/) — The Information 보도의 수치와 Microsoft 대변인 발언을 대조했다.

[TechRadar — Meta and Microsoft want to stop their employees using Claude](https://www.techradar.com/pro/meta-and-microsoft-want-to-stop-their-employees-using-claude) — 같은 보도의 수치와 TechRadar의 비용·국방부 지정 관련 평가를 대조했다.

[The Information — Microsoft Slashes Internal Claude Spending by a Third](https://www.theinformation.com/articles/meta-microsoft-work-wean-staff-anthropics-claude) — 유료벽이라 공개 요약(도입부)만 읽었다.
