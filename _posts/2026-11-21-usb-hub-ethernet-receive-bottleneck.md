---
layout: post
title: 모니터 허브 뒤에서 느려진 유선 다운로드
date: 2026-11-21 22:59:58 +0900
created: '2026-11-21T22:59:58+09:00'
source: https://blog.tymscar.com/posts/studiodisplayethernet/
source_title: My Monitor Was Cutting My Download Speed by 75%
author: jungseob
source_author: Oscar Molnar
source_published: '2026-11-15'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 연결 경로별 손실을 비교한다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://blog.tymscar.com/studio-display-ethernet/og-card.png
  alt: 모니터와 이더넷 연결 실험
---

## TL;DR

- 허브 경유 시 손실이 증가했다.
- 교체 실험은 단일 변수를 통제하지 않았다.

## 연결 경로를 바꿔 손실 지점을 찾는다

Oscar Molnar의 유선 인터넷은 다운로드만 약 600Mbps에 머물고 업로드는 2.4Gbps가 나왔다. 이더넷 어댑터는 Studio Display XDR에 연결돼 있었다. 같은 어댑터를 Mac에 직접 꽂자 다운로드가 2.2Gbps로 회복됐고, 모니터를 거치면 다시 느려졌다. 운영체제 로그에는 프레임 손실이 없었지만 다운로드 중 다른 유선 기기로 보낸 핑은 일부 실패했다. 저자는 컴퓨터에 도달하기 전에 어댑터에서 손실이 생긴다고 의심했다.

흐름 제어를 끄고 Linux 기기에서 일정한 속도의 UDP 트래픽을 보내자 차이가 드러났다. 모니터 경유 시 어댑터가 Mac에 넘기는 프레임은 초당 약 16만 8천 개에서 더 늘지 않았다. 전송량을 높이면 어댑터 자체 카운터의 손실만 증가했다. 직접 연결에서는 손실이 거의 없었다. 흐름 제어를 켜면 다운로드가 약 2Gbps까지 개선됐지만, 저자는 다른 기기의 지연에 미칠 영향을 우려했다.

저자는 USB 전송 묶음 사이의 대기 시간으로 이를 설명했다. 기존 RTL8156B는 한 번에 4개 패킷을 보내는데, 허브를 거친 응답 지연이 수신 버퍼를 비우는 속도를 제한한다는 추정이다. RTL8157 어댑터로 바꾸자 최대 2.4Gbps의 시험에서 손실이 사라졌다. 다만 새 제품은 묶음 크기와 USB 링크 속도가 함께 달랐다. 따라서 이 비교만으로 개선 원인을 한 변수에 귀속하거나 모든 모니터에 일반화할 수는 없다.

## 참고 자료

[Oscar Molnar의 실험 기록](https://blog.tymscar.com/posts/studiodisplayethernet/)
