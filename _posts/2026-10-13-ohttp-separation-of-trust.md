---
layout: post
title: "OHTTP의 신뢰 분리: IP를 보는 곳과 요청을 읽는 곳"
date: "2026-10-13 23:09:22 +0900"
created: "2026-10-13T23:09:22+09:00"
source: "https://blog.cloudflare.com/announcing-cloudflare-ohttp-gateway/"
source_title: "Announcing Cloudflare OHTTP Gateway – expanding access to Cloudflare’s privacy-preserving infrastructure"
author: jungseob
source_author: "Lara Schull, Akshat Mahajan"
source_published: "2026-10-02"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "OHTTP의 운영자 분리와 요청 본문에 남는 식별 가능성을 설명한다."
tags: [knowledge, blog, web]
---

## TL;DR

- OHTTP는 사용자 IP와 요청 내용을 서로 다른 운영자가 보도록 분리한다.
- Cloudflare 게이트웨이는 Workers나 자사 프록시 호스트에서 온 요청의 복호화를 거부한다.
- 쿠키나 본문 식별자는 별도 문제이며 운영 독립성과 추가 비용도 고려해야 한다.

## 요청 내용과 접속자를 다른 곳에서 본다

OHTTP는 릴레이와 게이트웨이를 거쳐 HTTP 요청을 전달한다. 클라이언트는 게이트웨이가 풀 수 있도록 요청을 암호화하고 릴레이에 보낸다. 릴레이는 사용자 IP를 알지만 요청 내용은 읽지 못한다. 게이트웨이는 내용을 복호화해 애플리케이션에 전달하지만 접속 주소로는 릴레이를 본다. 신원과 내용을 한 운영자에게 모으지 않는 구조다.

Cloudflare의 새 게이트웨이는 이 분리를 배포 조건으로 만든다. Workers나 Cloudflare 프록시 호스트에서 도착한 요청은 복호화를 거부한다. 같은 회사가 릴레이와 복호화 지점을 모두 맡는 실수를 막기 위해서다. 게이트웨이를 사용하는 고객은 별도 릴레이를 마련해야 하며 두 운영자가 정보를 합치지 않는다는 신뢰도 필요하다.

## 관리형 서비스가 맡는 일과 남는 책임

Cloudflare의 발표에 따르면 게이트웨이는 고객의 zone에 연결되고 공개키 관리와 요청 복호화를 맡는다. 목적지를 해당 zone으로 제한해 다른 도메인을 공격하는 중계기로 쓰이는 것을 막는다. Cloudflare Access는 복호화 전에 릴레이 인증을 수행한다. 원문은 이 구성을 소개한 발표이며 이 노트에서 실제 서비스 동작을 시험하지는 않았다.

릴레이를 따로 실행하는 것만으로 운영 독립성이 완성되지는 않는다. 앱 운영자가 릴레이 로그까지 열람하면 접속자와 복호화된 내용을 다시 연결할 수 있다. 원문은 식별자 로그를 들여다보지 않는다는 약속을 검증 가능하게 만드는 일이 어렵다고 짚는다. 서버 위치뿐 아니라 누가 어느 기록을 볼 수 있는지도 분리의 일부다.

## IP를 숨겨도 본문은 익명이 되지 않는다

RFC 9458은 OHTTP의 적용 범위를 요청 사이의 상태와 함께 설명한다. 쿠키나 인증 정보가 들어가면 전송 계층의 연결을 끊어도 서버가 요청들을 연관 지을 수 있다. 요청 본문의 이메일 주소 역시 같은 문제를 만든다. 따라서 OHTTP를 켰다는 사실만으로 로그인된 서비스나 모든 API 호출이 익명화된다고 볼 수 없다.

이 표준은 일반 HTTP보다 추가 비용도 요구한다. 중계 요청과 암호화 메타데이터가 늘고 키 도출과 암복호화에 연산이 든다. DNS 질의나 사용 통계 전송처럼 요청의 사용자 연결을 줄일 가치가 있는 경우가 적용 예다. 네트워크 식별자 분리, 본문 설계, 운영자 간 신뢰 조건을 함께 충족해야 이 구조의 목적에 가까워진다.

## 참고 자료

[Cloudflare OHTTP Gateway 발표](https://blog.cloudflare.com/announcing-cloudflare-ohttp-gateway/)

[RFC 9458: Oblivious HTTP](https://www.rfc-editor.org/rfc/rfc9458.html) — 요청 흐름과 적용 범위, 클라이언트·릴레이 책임을 대조했다.
