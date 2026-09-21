---
layout: post
title: "Cloudflare가 TLS 재시도를 줄인 사전 측정과 단계적 전환"
date: "2026-09-21"
created: "2026-09-21T23:05:26+09:00"
source: "https://blog.cloudflare.com/automatic-key-exchange-for-origins/"
source_title: "Automatic Key Exchange: faster, post-quantum secure origin handshakes for 45 billion daily connections (and counting)"
author: jungseob
source_author: "Suleman Ahmad, Yawar Jamal, Alex Krivit"
source_published: "2026-09-08"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "원본 서버의 키 교환 지원을 사전 측정해 TLS 재시도를 줄인 과정과 적용 조건을 살핀다."
tags: [knowledge, blog, Cloudflare, networking, web]
image:
  path: "https://blog.cloudflare.com/_emdash/api/media/file/01M1PVVA86NJR4N0MTKCH06A9V.01M1PVVAXCHV18R9AZA18HS4AQ.png"
  alt: "Cloudflare Automatic Key Exchange 원문 대표 이미지"
---

## TL;DR

- Cloudflare는 원본 서버를 사전 측정해 첫 키 교환을 선택했다. 측정 대상 연결의 재시도율은 약 52%에서 3.7%로 줄었다.
- 선택 결과는 소량의 트래픽부터 적용하고 실패를 감시한다. 현재 설정은 zone 단위이며 기존 연결을 재사용하는 요청에는 효과가 없다.
- 자동 선택과 허용 알고리즘 제한은 별개다. 제한을 강화해도 원본 서버에 새 암호 기능이 생기지는 않는다.

## 첫 연결에서 잘못 고른 키 교환

Cloudflare가 원본 서버에 TLS 1.3 연결을 시작할 때는 서버의 답을 받기 전에 키 교환 재료를 보낸다. 기존에는 X25519를 먼저 선택했다. 서버가 다른 방식을 요구하면 HelloRetryRequest를 받아 다시 보내므로 네트워크 왕복이 추가된다. 지원 가능한 알고리즘을 목록에 넣는 것과 그 방식의 키 재료를 처음부터 보내는 것은 다르다. [TLS 1.3 협상 규칙](https://www.rfc-editor.org/rfc/rfc8446#section-4.1.1)

큰 키 재료가 여러 패킷으로 나뉘면 일부 구형 장비에서 연결이 실패할 수 있다. 그래서 Automatic Key Exchange는 실제 요청 경로 밖에서 알고리즘을 하나씩 시험한다. 이 방식은 기존 연결 기록만 보는 것으로는 드러나지 않던 지원도 찾아낸다. 서버가 양자내성 방식을 지원하면서 기존 방식도 그대로 받아들이면 수동적 관찰에는 그 능력이 나타나지 않는다.

## 측정한 결과를 실제 트래픽에 적용하기

설정은 zone 단위다. 여러 원본 서버가 있으면 트래픽 비중을 반영해 하나의 선호 값을 정하며 서버마다 설정을 달리하지는 않는다. 활성 원본은 약 24시간마다 다시 검사한다. 따라서 TLS 라이브러리를 업그레이드한 직후에도 다음 검사 전에는 기존 선택이 유지될 수 있다.

새 선택은 트래픽의 1%부터 시작한다. 연결 실패와 재시도율을 관찰하면서 적용 비중을 늘리고 문제가 생기면 이전 설정으로 돌아간다. 연결마다 허용된 다른 알고리즘도 함께 알리므로 서버가 다른 키를 요청할 여지는 남는다. 이 재시도는 왕복 시간을 늘리지만 공통으로 허용된 방식이 있으면 연결을 이어 갈 수 있다. [자동 선택의 동작](https://developers.cloudflare.com/ssl/origin-configuration/automatic-key-exchange/)

Cloudflare의 배포 중 측정에서는 대상 원본 연결의 재시도율이 약 52%에서 3.7%로 낮아졌고 핸드셰이크 지연의 p90은 150ms 넘게 줄었다. 전체 인터넷이나 모든 요청의 개선율은 아니다. 기존 keep-alive 연결에는 새 핸드셰이크가 없으므로 이 절감도 발생하지 않는다. 동적 요청이나 캐시 미스라도 새 연결을 여는 경우에 해당한다. [원문 측정 결과](https://blog.cloudflare.com/automatic-key-exchange-for-origins/)

## 자동 선택과 강제 제한의 차이

이 기능은 Full·Full (strict)·Strict 모드에서 원본과 TLS 1.3으로 연결할 때 적용된다. Cloudflare Tunnel은 별도 연결 구조를 쓰므로 대상에서 제외된다. 인증서 검증을 결정하는 SSL/TLS 암호화 모드와도 구분해야 한다. Automatic Key Exchange는 HTTPS 연결을 시작할 때 어떤 키 재료를 먼저 보낼지 결정하는 설정이다.

Compliance requirements는 선택할 수 있는 알고리즘의 범위를 제한한다. 자동 선택을 끄더라도 이 제한은 유지되며 제한 밖의 알고리즘을 대안으로 쓸 수는 없다. 양자내성 전용 제한을 걸었는데 원본이 이를 지원하지 않으면 공통 선택지가 사라진다. 운영 설정에서는 선호 순서를 바꾸는 일과 호환되는 대안을 제거하는 일을 구분해야 한다. [적용 범위와 설정](https://developers.cloudflare.com/ssl/origin-configuration/automatic-key-exchange/)

## 참고 자료

[Cloudflare 원문](https://blog.cloudflare.com/automatic-key-exchange-for-origins/)

[Automatic key exchange 공식 문서](https://developers.cloudflare.com/ssl/origin-configuration/automatic-key-exchange/)

[RFC 8446 — TLS 1.3 협상](https://www.rfc-editor.org/rfc/rfc8446#section-4.1.1)
