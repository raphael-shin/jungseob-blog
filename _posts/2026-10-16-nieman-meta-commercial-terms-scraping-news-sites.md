---
layout: post
title: "Meta의 새 상업 약관이 뉴스 사이트 스크래핑을 허용한다, Nieman Lab이 법률 전문가 세 명에게 물은 10월 30일 시행 조항"
date: "2026-10-16 19:42:46 +0900"
created: "2026-10-16T19:42:46+09:00"
source: "https://www.niemanlab.org/2026/10/metas-new-commercial-terms-will-allow-the-scraping-of-news-sites-legal-experts-say/"
source_title: "Meta’s new commercial terms will allow the scraping of news sites, legal experts say"
author: jungseob
source_author: "Andrew Deck, Hanaa' Tameez (Nieman Lab)"
source_published: "2026-10-15"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Nieman Lab이 Meta 상업 약관의 새 크롤링 조항을 법률 전문가 세 명과 검토한 보도를 정리한다. 비즈니스 계정에 연결된 웹사이트를 스크래핑하고 Meta 제품 학습에 쓸 수 있다는 문구, 테스트 자격 증명, robots.txt와의 관계, 거부 불가라는 구조를 다루며 약관 원문과 대조한 결과와 확인하지 못한 점을 밝힌다."
tags:
  - knowledge
  - blog
  - AI
  - 저작권
  - Meta
---

## TL;DR

- 10월 30일부터 적용되는 Meta 상업 약관은 비즈니스 계정이 관리하는 제품·서비스와 연결된 웹사이트를 Meta가 스크래퍼와 "테스트 자격 증명"으로 수집하고 제품 개선과 학습에 쓸 수 있다고 정한다. 뉴스 매체 거의 전부가 비즈니스 계정을 갖고 있어 영향 범위가 넓다.
- 법률 전문가 세 명은 문구대로라면 Meta가 AI 학습에 뉴스 사이트의 콘텐츠를 쓰는 근거로 삼을 수 있다고 본다. 가입 자체가 동의라서 시행 전에 약관을 거부할 선택지는 없고, 동의하지 않으려면 비즈니스 용도 사용을 멈춰야 한다.
- Meta는 질문 목록에 답하지 않았다. 대변인은 크롤링 문구가 여러 약관에 흩어져 있던 것을 합친 것이며 Meta가 게시자를 크롤링하는 방식은 바뀌지 않고 robots.txt로 접근을 관리할 수 있다고 이메일로 밝혔다.
- 이 노트가 약관 원문과 대조한 결과, 기사가 인용한 문구는 Meta 약관 미리보기와 일치한다. 제3자 비교는 기존 약관에도 크롤링과 "연구·학습" 용도 문구가 있었고 새 약관이 "테스트 자격 증명"과 수집·검색 표현을 더했다고 정리한다.
- 법적 효력은 미정이다. 학습 목적 사용이 공정이용에 해당하는지는 소송 중인 쟁점이고, 전문가 인용은 모두 Nieman Lab이 고른 세 명이다.

## 기사에 대하여

Nieman Lab의 Andrew Deck과 Hanaa' Tameez가 2026년 10월 15일에 쓴 기사다. 한 독자의 제보로 시작했다. Meta Business Suite 대시보드에서 약관 변경 공지를 본 취미 매체 The Steampunk Explorer의 Stephen Beale가 연락했다. Nieman Lab 자신도 비즈니스 계정을 가진 이해당사자라고 기사가 밝힌다. 이 노트는 기사 본문을 전부 읽었고 Meta 약관 미리보기 페이지와 제3자 비교 글은 검색 결과 발췌로 확인했다. 기사는 직접 요청이 403이라 브라우저로 읽었다.

## 무엇이 바뀌는가

기사에 따르면 새 약관은 페이지와 그룹 관리, 광고 집행, 마케팅 메시지 발송, 비즈니스 계정 대시보드 사용을 폭넓게 포함한다. 핵심 조항은 이용자가 Meta(또는 Meta를 대행하는 주체)에게 자동화 소프트웨어(스크래퍼, 봇, 크롤러 등)를 쓰고 테스트 자격 증명을 만들어, 이용자의 제품·서비스와 연결되었거나 Meta 제품 사용을 통해 노출된 도메인·웹페이지·URL과 그 안의 콘텐츠를 접근, 색인, 캐시, 분석, 수집, 검색, 크롤링하도록 허락하고 주기적으로 갱신을 가져가게 한다는 내용이다. 이어서 Meta가 그 콘텐츠를 제품과 서비스를 제공하고 개발하고 개선하고 연구하고 학습하고 무결성을 유지하는 데 쓸 수 있다고 정한다. 다른 조항에서 Meta는 "AI at Meta"를 Meta 제품으로 정의한다고 기사가 설명한다.

시행은 10월 30일이고 그 전에 거부할 선택지는 없다. 약관은 동의하지 않으면 비즈니스·상업 목적으로 제품 접근과 사용을 멈추라고 안내한다. Meta는 10월 초 블로그와 Business Suite로 변경을 알렸다.

## 전문가 세 명의 해석

언론·지재권 변호사 Matt Topic(Loevy & Loevy)은 라이선스 시장에서 수백만 달러가 들 자료를 Meta가 얻게 하는 조항을 약관에 묻어 두었다고 비판한다. 법원이 집행할지는 불분명하지만 게시자는 집행된다고 가정해야 한다고 조언한다. 코넬 로스쿨의 James Grimmelmann은 뉴스 게시자에게는 사이트의 모든 콘텐츠로 AI를 학습시키고 일부는 게시자와 경쟁하는 용도로 배포할 허락이 된다고 말한다. 가장 넓은 해석으로는 모든 콘텐츠의 포괄 아카이브를 만들어 Meta가 원하는 대로 제공할 수 있게 된다. 게시자는 Meta가 문구 전부를 뜻하지 않으리라 믿거나 비즈니스 계정을 포기해야 한다는 것이 그의 요약이다.

위스콘신 대학의 Benjamin Sobel은 비즈니스 제품 사용을 스크래핑 허락과 묶는 방식이 반독점법의 끼워팔기(tying)를 떠올리게 한다고 말한다. 그는 AI Overviews와 AI Mode에 동의해야 검색 결과에 나오는 Google의 최근 정책에 비유한다.

## robots.txt와 테스트 자격 증명

Meta 대변인은 robots.txt로 콘텐츠 접근을 관리할 수 있다고 하고 Meta 개발자 페이지에는 크롤러 차단법이 안내되어 있다. 그러나 전문가들은 새 문구가 상업 약관이 다른 차단 지시보다 우선한다는 주장을 Meta에게 열어 준다고 본다. 테스트 자격 증명 문구는 Grimmelmann이 "가짜 사용자로 가입"해 게시자 사이트의 회원 가입 벽을 우회할 수 있다고 해석한다. 유료 콘텐츠를 우회할 수 있는지 묻는 질문에 Meta는 답하지 않았다.

## 맥락

기사는 학습이 공정이용인지가 아직 정리되지 않았고 게시자와 AI 업체 간 여러 소송이 연방 법원에서 진행 중이라고 쓴다. 5월에 대형 출판사 다섯 곳이 Meta가 Llama 학습에 수백만 권을 해적판으로 썼다며 낸 집단소송이 그 예다. 또 Meta가 최근 시작한 유료 구독 Meta One이 일부 계정의 외부 링크 게시 수를 제한한다는 점을 들어, Meta가 링크 게시에는 돈을 받으면서 같은 콘텐츠는 무료로 크롤링할 수 있게 되었다고 지적한다. 일부 언론사가 링크 제한에서 예외라는 Press Gazette 보도도 언급한다. Beale은 계정을 닫을 것을 진지하게 고려한다고 말한다.

## 약관 원문 대조

기사가 "전문"이라며 실은 크롤링 문단을 Meta 약관 미리보기 페이지(facebook.com/legal/commercial_terms_preview)의 문단과 대조했다. 두 문구는 일치한다. 검색 결과에 보인 Steampunk Explorer의 두 글도 같은 문단을 같은 출처로 싣고 Meta의 공지에서 Product Catalog Terms와 Ad Creative Generative AI Terms를 각각 Commercial Terms와 Self-Serve Ad Terms에 편입한다는 설명을 인용한다.

Meta 대변인의 "기존 문구를 합친 것"이라는 설명은 부분적으로 뒷받침된다. 광고 약관을 비교한 제3자 글(AdTestBench)에 따르면 기존 약관에도 URL을 "접근, 색인, 캐시, 분석, 크롤링"할 수 있고 용도에 "연구와 학습"이 포함되었다. 새 약관은 여기에 "테스트 자격 증명 생성"과 "수집, 검색"을 더하고 용도를 "연구, 학습"으로 적는다. 이 노트가 기존 약관 전문을 직접 읽지는 못했다. 또 동의하지 않을 때의 문구를 기사는 "please stop"으로, 그 글은 "you may stop"으로 인용해 한쪽이 다른 판본일 수 있다. 어느 쪽이 최종인지 확인하지 못했다.

## 읽을 때 유의할 점

첫째, 이 기사의 해석은 Nieman Lab이 약관 검토를 요청한 법률 전문가 세 명의 것이며 법원이 같은 결론에 이른다는 뜻이 아니다. Topic도 집행 여부는 불분명하다고 말한다. 둘째, "허용한다"는 제목은 가능한 해석이며 Meta가 실제 학습에 쓴다고 확인한 것은 없다. 기사도 Meta가 그 점을 확인하지 않았다고 밝힌다. 셋째, 약관이 어떤 웹사이트까지 포함하는지("연결된" 범위)는 문구가 넓어 해석이 갈릴 수 있다. 넷째, 필자들이 속한 Nieman Lab이 영향을 받는 당사자다. 다섯째, 이 노트는 법률 자문이 아니다.

그럼에도 가져갈 점검 질문은 선명하다. 우리 조직의 어떤 사이트와 도메인이 Meta 비즈니스 계정과 연결되어 있는가, 약관 동의가 robots.txt 정책을 덮어쓴다는 주장에 대비해 어떤 기술·계약 조치를 준비했는가, 회원 전용·유료 콘텐츠에 테스트 자격 증명이 접근할 가능성을 검토했는가, 비즈니스 계정을 유지할 때 얻는 도달과 잃을 수 있는 콘텐츠 권리를 어떻게 저울질하는가. 같은 날 Meta가 공개한 오픈웨이트 모델을 정리한 [Muse Spark Open 노트](https://raphael-shin.github.io/jungseob-blog/posts/meta-muse-spark-open-weights-release/)에서, 모델 카드가 학습 데이터에 인터넷에서 크롤링한 자료가 포함된다고 적은 것은 같은 맥락이지만 두 사안의 직접적 연결은 확인된 바 없다.

## 참고 자료

[Andrew Deck, Hanaa' Tameez — Meta’s new commercial terms will allow the scraping of news sites, legal experts say (Nieman Lab, 2026-10-15)](https://www.niemanlab.org/2026/10/metas-new-commercial-terms-will-allow-the-scraping-of-news-sites-legal-experts-say/) — 본문 전체를 읽고 정리했다. 직접 요청이 403이라 브라우저로 읽었다.

[Meta Commercial Terms (미리보기, 2026-10-30 시행)](https://facebook.com/legal/commercial_terms_preview) — 크롤링 문단이 기사 인용과 일치함을 검색 결과 발췌로 확인했다. 약관 전문은 읽지 못했다.

[AdTestBench — Meta's generative AI ad terms, 30 October 2026](https://adtestbench.com/guides/meta-generative-ai-ad-terms) — 기존 약관과 새 약관의 크롤링 문구 비교를 읽었다. 제3자의 정리이며 이 노트가 Meta 원문과 모두 대조한 것은 아니다.
