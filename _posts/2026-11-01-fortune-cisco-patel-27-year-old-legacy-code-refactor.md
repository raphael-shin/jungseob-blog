---
layout: post
title: "Cisco의 Jeetu Patel이 27세 전 창업자에게 무제한 AI 토큰을 주고 레거시 코드의 98% 리팩터링을 맡긴 Fortune 보도, 신입 채용 논리와 사실 확인 범위를 읽은 정리"
date: "2026-11-01 15:33:36 +0900"
created: "2026-11-01T15:33:36+09:00"
source: "https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/"
source_title: "Cisco chief found a 27-year-old ex-founder 'buried away in the organization doing something unstrategic'—now he's upgrading 98% of its code"
author: jungseob
source_author: "Orianna Rosa Royle (Fortune)"
source_published: "2026-10-30"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Fortune이 2026년 10월 30일 보도한 Cisco 사장 겸 최고제품책임자 Jeetu Patel의 이야기를 정리한다. EzDubs를 공동 창업했다가 Cisco에 인수된 27세 Padmanabhan Krishnamurthy에게 무제한 토큰을 주고 4주 안에 가능성을 증명한 뒤 24개월 안에 레거시 코드의 98%를 리팩터링하겠다는 계획, 신입이 경험자가 묻지 못하는 질문을 던진다는 채용 논리, 팀을 경험자와 시스템 사고자와 AI 네이티브 창업가 세 부류로 구성한다는 구상, Thrive Capital과 Tastewise와 Will.i.am의 비슷한 베팅을 다룬다. 인수 사실과 후속 보도를 확인하고, 보도가 기대는 말이 모두 한 임원의 진술이라는 한계와 98%의 정의가 기사마다 다른 점을 짚는다."
image:
  path: "https://fortune.com/img-assets/wp-content/uploads/2026/10/GettyImages-2270629609-e1793295597735.jpg?resize=1200,600"
  alt: "Fortune의 Cisco 27세 엔지니어 기사 대표 이미지"
tags:
  - knowledge
  - blog
  - AI
  - 채용
  - Cisco
---

## TL;DR

- Cisco의 Jeetu Patel 사장은 조직도에서 다섯 단계 아래에 있던 27세 전 창업자 Padmanabhan Krishnamurthy에게 "무제한 토큰"을 주고 레거시 코드 리팩터링을 맡겼다. 두 사람 팀이 4주 안에 가능성을 증명하기로 했고(기사의 문장은 Krishnamurthy가 스스로 4주를 정했다고 읽힌다), 최종 목표는 24개월 안에 레거시 코드의 98%를 리팩터링하는 것이다.
- 채용 논리는 경험이 없는 사람만 던질 수 있는 질문이 있다는 것이다. 신입을 뽑지 않으면 새 아이디어가 들어올 통로가 막힌다고 Patel은 말하며, 의도적으로 팀 안에 아이디어의 마찰을 만든다.
- 그가 그리는 팀은 세 부류다. 회사 엔진을 아는 숙련 운영자, 외부 시각의 시스템 사고자, AI 네이티브 창업가형 엔지니어가 각각 3분의 1이고 셋이 함께일 때 힘이 난다.
- Thrive Capital의 Josh Kushner, Tastewise의 Alon Chen, Will.i.am도 경력이 적은 젊은 인재에 베팅한다고 같은 기사가 전한다.
- 기사의 근거는 모두 Patel과 인터뷰이들의 진술이다. 98%의 정의가 기사마다 다르고 4주 시험의 기준과 결과는 공개되지 않았다.

## 기사에 대하여

Fortune의 Orianna Rosa Royle가 2026년 10월 30일에 쓴 기사다. 본문 전체를 읽었고 같은 내용을 다룬 Tom's Hardware와 다른 후속 보도의 제목과 검색 발췌, EzDubs 인수 보도로 대조했다. Tom's Hardware의 본문은 읽지 못했다. Cisco 임원이 소규모 라운드테이블 저녁 자리에서 Fortune에 말한 내용이 기사의 중심이다. 이 블로그의 [정상혁 D2 노트](https://raphael-shin.github.io/jungseob-blog/posts/jung-naver-d2-ai-era-student-developers/)와 [Rieseberg 노트](https://raphael-shin.github.io/jungseob-blog/posts/rieseberg-hunger-beats-tenure-junior-engineers/)가 AI 시대 주니어의 자리를 다룬 다른 목소리다.

## 조직도 다섯 단계 아래에서 찾은 사람

기사는 신입 일자리가 사라지고 있다는 배경으로 시작한다. 경영자의 약 40%가 AI가 더 싸게 일하므로 졸업생을 덜 뽑겠다고 한다는 수치를 기사가 소개하지만 출처는 적지 않았다. Patel은 이 흐름에 동조하지 않고 자신 아래 다섯 단계에 있던 27세에게 회사의 가장 큰 일 가운데 하나를 맡겼다.

그 사람은 Padmanabhan Krishnamurthy, 애칭 Paddy다. 실시간 번역 스타트업 EzDubs를 2023년에 공동 창업했고 EzDubs가 2025년에 Cisco에 인수되면서 입사했다. Patel의 표현으로 그는 CEO 경험이 있는 전 창업자이지만 조직 안에서 "전략적이지 않은 일에 묻혀" 있었다. Patel이 샌프란시스코 사무실에 들러 이야기를 나누다가 Krishnamurthy가 두 사람 팀으로 Cisco의 레거시 코드를 다시 쓸 수 있다고 말했다. Patel은 자기 팀의 가장 AI 지향적인 사람들도 그렇게 생각하지 않았다고 말한다.

그래서 기사에 따르면 Krishnamurthy가 스스로 4주를 정해 가능성을 증명하기로 했다(문장의 주어가 모호해 Patel이 부과한 기한인지는 확인하지 못했다). 최종 목표는 24개월 안에 레거시 코드의 98%를 리팩터링하는 것이다. Patel은 "코드를 리팩터링할 것이므로 무제한 토큰을 줬고, 미친 듯이 해 보라고 했다"고 말한다. 그리고 비슷한 젊은 인재, 곧 체제와 현상에 도전하는 "에너자이저 버니" 같은 사람을 더 찾고 있다.

## 신입을 두는 이유

보통 이런 규모의 일은 수십 년 경력자에게 맡기지만 Patel은 그것이 문제라고 본다. 신입을 안 뽑고 기존 인력만 이어 가면 새 아이디어가 어디서 들어오고 현상에 어떻게 도전하느냐는 것이다. 숙련자도 새 아이디어를 낼 수 있지만 경험이 없는 사람만이 던질 수 있는 질문은 낼 수 없다는 주장이다.

그는 마찰이 의도라고 인정한다. 수십 년 근속자와 Z세대를 한 방에 두면 긴장이 생기지만 "긴장은 좋다"고 말한다. 다만 사람이나 성격이 아니라 아이디어 사이의 마찰이어야 하고 이를 위해 "비합리적인 목표를 스스로 세울 것"이라는 기대를 줄 만큼 신뢰를 먼저 쌓는다고 한다. 인턴은 모두 "역방향 멘토"로 대하고 대학 강연에서 "굶주린" 학생을 찾는다. 스탠퍼드 장학생 17~18세 학생 가운데 한 명인 Baya는 질문하는 줄에 끼지 않고 끝까지 듣다가 마지막에 말을 걸었다. Patel은 매달 AI에 대해 배운 것을 이메일로 보내라고 했고 그녀는 한 번도 거르지 않았으며 인턴십을 얻어 경험 있는 직원들이 풀지 못한 무언가를 재설계했다. 그는 데이터 입력을 시키려는 것이 아니라 사람들에게 완전히 다르게 생각하는 법을 가르치게 하려고 데려왔다고 말한다.

## 세 부류로 이루어진 팀

Patel은 추세가 AI 때문에 더 강해지리라고 말한다. 속도를 계속 올리려면 폭넓은 경험을 가진 사람들에 둘러싸여야 한다는 것이다. 그의 팀은 세 부류다. 약 3분의 1은 Cisco의 엔진이 어떻게 돌아가는지 아는 규모 경험이 있는 숙련 운영자다. 3분의 1은 시장에서 온 시스템 사고자로 외부 시각을 준다. 나머지 3분의 1은 AI 네이티브 창업가, CEO, 엔지니어로 창업자 모드로 일한다. 어느 한 그룹만으로는 세 그룹이 함께일 때만큼 강하지 않고 그것이 "마법"을 만든다고 한다.

기사는 다른 투자자와 창업자의 비슷한 베팅도 전한다. Thrive Capital 창업자 Josh Kushner는 업계 경력 4년 미만의 사람을 일부러 고용하며 26세에 회사를 세울 때 노련한 인력을 들이라는 압박을 받았지만 "재능 있는 경험자는 26세와 일하려 하지 않는다"고 보고 자기 나이대의 가장 똑똑한 사람을 뽑았다. 기사는 이 회사가 OpenAI를 포함해 수십억 달러 가치의 스타트업에 초기 투자했고 OpenAI가 최대 300억 달러를 1조 2,500억 달러 가치로 모금 중이라고 쓴다. Tastewise의 Alon Chen은 "경계와 한계 없이 세상을 생각한다"며 경력이 없는 신입을 뽑는다. Will.i.am은 MIT와 스탠퍼드의 젊은 혁신가가 AI에 "네이티브"이므로 다음 돌파구를 낼 것이라고 말하며 그것만 찾는다.

## 대조해서 확인한 점

EzDubs 인수는 TechCrunch가 2025년 11월 17일에 Cisco의 인수 발표를 보도했고 Webex 블로그가 11월 25일에 인수를 완료했다고 밝힌다. EzDubs는 Y Combinator 출신 실시간 음성 번역 스타트업이다. 이는 Fortune의 "2025년에 인수되어 입사했다"는 서술과 맞는다. 후속 보도는 제목과 발췌만 확인했고 Fortune을 인용한 보도로 보이며 독립적인 확인은 찾지 못했다.

중요한 차이는 98%의 정의다. Fortune의 제목은 "코드의 98%를 업그레이드한다"이고 본문은 "레거시 코드의 98% 리팩터링"이라고 쓴다. Tom's Hardware의 제목은 "98%를 다시 쓴다"고 하고 다른 보도는 "다룬다(address)"고 쓴다. 이 노트는 본문의 "레거시 코드의 98% 리팩터링, 24개월"을 따랐다. 어떤 코드베이스를 모수로 하는지, 무엇을 리팩터링 완료로 세는지, 4주 안에 무엇을 증명하면 통과인지는 기사에 없다. 토큰 "무제한"이 실제 상한이 없다는 뜻인지, 비용을 감수한다는 비유인지도 확인할 수 없다.

확인하지 못한 것은 "경영자의 약 40%가 졸업생을 덜 뽑겠다" 수치의 출처, Cisco의 시가총액 4,290억 달러, OpenAI의 모금 규모와 가치(기사가 전한 현재 진행형 수치)다. 이 노트가 본문까지 읽은 것은 Fortune 기사와 EzDubs 인수 보도뿐이다.

## 읽을 때 유의할 점

첫째, 모든 핵심 서술이 Patel의 구두 진술이며 Cisco의 공식 자료나 프로젝트 지표가 아니다. 4주 시험은 아직 결과가 없다. 둘째, 기사에 나온 "신입 채용"의 사례는 Krishnamurthy가 신입이 아니라 이미 창업 경험이 있는 27세라는 점에서 "Z세대 신입 일반"으로 일반화하기 어렵다. 셋째, 같은 기사에 나오는 투자자와 창업자들은 AI 인재 시장에서 이해관계가 있는 사람들이다. 넷째, 리팩터링을 에이전트에 맡기는 계획의 검증 문제(회귀, 보안, 동작 보존)는 기사가 다루지 않는다. 다섯째, 기사는 소규모 라운드테이블의 발언을 옮긴 것이어서 맥락이 줄었을 수 있다.

가져갈 질문은 선명하다. 우리 조직의 큰 리팩터링을 이 방식으로 시도한다면 4주 안에 무엇을 증명으로 삼을 것인가, 그 증명을 누가 어떤 기준으로 판정하는가, 경험자와 신입 사이의 마찰이 아이디어가 아니라 사람에게 향하지 않게 하려면 무엇이 필요한가.

## 참고 자료

[Fortune: Cisco chief found a 27-year-old ex-founder 'buried away in the organization' (2026-10-30)](https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/): 본문 전체를 읽고 정리했다.

[Tom's Hardware: Cisco gives 27-year-old engineer unlimited AI tokens to rewrite 98% of the company's legacy code](https://www.tomshardware.com/tech-industry/big-tech/cisco-gives-27-year-old-engineer-unlimited-ai-tokens-to-rewrite-98-percent-of-the-companys-legacy-code-in-24-months-president-plucks-former-startup-founder-telling-him-to-go-nuts): 후속 보도로 제목의 표현을 확인했고 본문은 Fortune을 따른다.

[TechCrunch: Cisco acquires translation startup EzDubs (2025-11-17)](https://techcrunch.com/2025/11/17/cisco-acquires-translation-startup-ezdubs): 인수 발표를 확인했다.

[Webex 블로그: Welcoming EzDubs to Cisco](https://blog.webex.com/collaboration/a-new-era-of-ai-powered-collaboration-welcoming-ezdubs-to-cisco): 2025년 11월 25일 인수 완료 갱신을 확인했다.
