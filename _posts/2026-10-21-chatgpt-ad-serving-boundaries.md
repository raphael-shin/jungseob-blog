---
layout: post
title: "ChatGPT 광고 시스템이 답변과 노출을 분리하는 방식"
date: "2026-10-21 22:58:42 +0900"
created: "2026-10-21T22:58:42+09:00"
source: "https://openai.com/index/building-chatgpt-ad-stack/"
source_title: "How we built ChatGPT’s novel ad stack for user trust and relevance"
author: jungseob
source_author: "Ritendra Datta and Karthik Gopalratnam"
source_published: "2026-10-21"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "광고 오케스트레이터의 결정 권한과 응답 지연·미노출을 처리하는 서비스 경계."
tags: [knowledge, blog, web]
---

## TL;DR

- 광고 선택은 일반 답변 생성과 별도 서비스에서 실행된다.
- 경매 통과와 실제 노출 사이에도 맥락·도착 시각 검사가 있다.
- 미노출 원인을 구분해야 개선할 단계를 찾을 수 있다.

## 답변과 광고를 분리하는 경계

OpenAI의 설계 설명에서 ChatGPT 답변 생성과 광고 선택은 모델·코드·서비스가 분리된 경로다. 광고 서비스는 대화 맥락을 받아 별도로 후보를 찾는다. 광고 쪽이 느리거나 사용할 수 없어도 일반 답변은 계속 생성되며, 광고를 기다리느라 사용자 응답을 늦추지 않는 구조다.

광고용 오케스트레이터는 대화가 진행되며 바뀌는 의도를 해석하고 검색·평가 도구를 반복 호출한다. 상품 이름을 언급했다는 이유만으로 구매 의도로 간주하지 않는다. 후보를 경매에 올릴 수는 있지만 최종 광고와 가격을 직접 결정하지는 않는다. 경매 도구가 품질을 반영한 순위와 가격, 최종 선택을 처리한다.

## 미노출도 구분해서 기록한다

경매를 통과해도 광고가 반드시 보이지는 않는다. 대화와 광고가 각각 정책을 통과했더라도 둘을 결합한 맥락이 부적절하면 차단한다. 서버가 광고를 보낸 뒤에도 답변 생성이 끝나기 전에 프런트엔드에 도착해야 표시된다. 따라서 후보 선정·서버 전송·사용자 노출은 같은 사건으로 취급할 수 없다.

운영 로그는 광고 대상이 아닌 턴, 검색을 요청하지 않은 세션, 후보가 없는 검색, 적격성 검사에서 탈락한 후보 등을 구분한다. 이 구분으로 기회 탐지와 검색 품질, 전달 신뢰성 중 어디를 개선할지 판단한다. 광고 없는 응답도 정상적인 결과다. 다만 이는 공급자의 아키텍처 설명이며, 답변의 중립성을 독립적으로 검증한 결과는 아니다.

## 참고 자료

[How we built ChatGPT’s novel ad stack for user trust and relevance](https://openai.com/index/building-chatgpt-ad-stack/)
