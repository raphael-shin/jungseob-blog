---
layout: post
title: "Scion: 온라인 에이전트에 맞춘 소스 관리"
date: "2026-10-14 23:04:24 +0900"
created: "2026-10-14T23:04:24+09:00"
source: "https://www.anthropic.com/engineering/redesigning-source-control"
source_title: "Redesigning source control at Anthropic"
author: jungseob
source_author: "Nick G. and the source control team"
source_published: "2026-10-13"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Scion의 서버 중심 처리와 계층별 캐시 설계."
tags: [knowledge, blog, web]
---

## TL;DR

- Scion은 서버로 병합·이력 조회를 옮긴다.
- 불변 객체를 캐시하고 필요한 파일만 가져온다.
- 상시 연결과 대규모 저장소에 특화된 선택이다.

## 온라인 클라이언트를 전제로 바꾼 역할

Anthropic은 에이전트와 CI의 반복적인 체크아웃을 감당하려고 Scion을 만들었다. Git 미러와 저장소 스냅샷으로 버티던 방식은 변경량이 커질수록 운영하기 어려워졌다. Scion에서는 서버가 병합과 이력 조회를 맡는다. 클라이언트는 제한된 캐시와 작업파일을 관리하며, 필요한 데이터만 요청한다. 오프라인에서 완결되는 저장소라는 전제를 포기한 설계다.

변경사항은 changeset으로 기록한다. 첫 부모와 달라진 파일 목록과 콘텐츠 주소를 저장하고, 이력 조회에 필요한 자료는 별도로 계산한다. 이 파생자료는 필요에 따라 미리 만들거나 계산을 늦출 수 있다. 클라이언트에 내부구조를 노출하지 않으므로 서버의 자료구조도 독립적으로 개선한다. 일부 작업은 API만으로 처리해 체크아웃 자체를 없앤다.

## 캐시의 재사용과 설계의 경계

파일이 필요하면 노드의 데몬이 여러 작업에 객체를 재사용한다. 지역 캐시에 없는 객체만 상위 서버로 요청한다. 콘텐츠 주소로 식별한 객체는 바뀌지 않으므로 캐시간 조율 부담이 작다. 캐시 계층은 엄격히 분리해 지역 장애가 상위 서버 과부하로 번지지 않도록 한다. 필요한 디렉터리만 요청하는 방식은 희소 체크아웃에도 맞는다.

이는 Anthropic의 내부 사례이며 범용 Git 대체안은 아니다. 항상 연결된 클라이언트와 대규모 저장소라는 조건에 의존한다. 이전하려면 코드리뷰·검색·CI까지 바꿔야 한다. 개발 중에는 에이전트가 설계 제약을 어기거나 과도한 검증을 추가해 엔지니어의 판단도 필요했다. 코드작성 속도만으로 인프라 설계와 운영 책임이 사라지지는 않는다.

## 참고 자료

[Redesigning source control at Anthropic](https://www.anthropic.com/engineering/redesigning-source-control)
