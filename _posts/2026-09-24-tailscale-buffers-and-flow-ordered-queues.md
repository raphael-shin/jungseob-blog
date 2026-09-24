---
layout: post
title: "Tailscale의 버퍼 복사 절감과 순서를 지키는 병렬 처리"
date: "2026-09-24"
created: "2026-09-24T23:04:20+09:00"
source: "https://tailscale.com/blog/making-tailscale-faster"
source_title: "We’re making Tailscale faster"
author: jungseob
source_author: "Kabir Sikand, Kevin Purdy"
source_published: "2026-09-22"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Tailscale의 버퍼 공유와 멀티큐 설계를 Linux 네트워크 인터페이스와 함께 살펴본다."
tags: [knowledge, blog, networking, performance]
image:
  path: "https://cdn.sanity.io/images/w77i7m8x/production/a61f95892ebd9647722faaff16ac3a9f6787490a-2304x1188.png"
  alt: "Tailscale 성능 개선 원문 대표 이미지"
---

## TL;DR

- Tailscale은 작은 패킷마다 큰 버퍼를 할당하던 복사를 줄이고, 흐름별 순서를 유지하는 멀티큐 처리를 준비했다.
- 패킷을 묶는 GRO와 처리 큐의 병렬화는 서로 다른 기능이다. Linux 문서에서도 각각의 인터페이스와 역할을 구분한다.
- netmap 캐시는 최초 접속을 대신하지 않는다. 출시 계획과 제한된 조건의 성능 결과를 전체 환경의 보장으로 해석하면 안 된다.

## 큰 수신 버퍼를 패킷마다 복제하지 않기

Tailscale의 기존 처리는 1 KiB 패킷도 별도 64 KiB 버퍼로 복사했다. 개선안은 큰 수신 버퍼 안에서 패킷 경계를 구분해 할당을 공유한다. Linux·Android 대상 변경으로 여러 네트워크 구성에서 약 5% 개선을 관찰했으며 사용량이 적었던 대기열 깊이도 줄였다. 이는 업체의 측정 결과로 모든 연결의 향상률을 뜻하지 않는다. [Tailscale 원문](https://tailscale.com/blog/making-tailscale-faster)

[Linux의 오프로딩 문서](https://docs.kernel.org/networking/segmentation-offloads.html)에서 GRO는 수신 프레임을 합치고 GSO는 이를 다시 나누는 상보적인 기능이다. 이상적인 경우 합친 결과를 분할하면 원래 프레임의 순서와 내용으로 돌아온다. GSO는 장치가 해당 오프로딩을 수행하지 못할 때 소프트웨어로 분할을 처리하는 역할도 한다. 패킷을 크게 묶어 전달하는 방식과 개별 패킷을 별도 메모리로 복사하는 방식은 구분해야 한다.

## 흐름 안의 순서를 유지하며 큐를 나누기

기존 파이프라인에서는 독립적인 연결들이 하나의 처리 경로를 공유했다. 새 멀티큐 설계는 같은 흐름을 같은 큐에 배정해 순서를 유지하고 큐 사이를 병렬로 처리한다. 큐 수는 피어 수가 아닌 머신 자원에 맞춘다.

[Linux TUN/TAP 문서](https://docs.kernel.org/networking/tuntap.html)의 가상 장치는 사용자 공간과 커널 사이에서 패킷을 주고받는 인터페이스다. TUN은 IP 패킷을, TAP은 이더넷 프레임을 전달한다. Linux는 3.8부터 여러 파일 디스크립터를 큐로 사용하는 멀티큐 인터페이스를 지원한다. 같은 장치 이름에 `IFF_MULTI_QUEUE`를 지정해 `TUNSETIFF`를 반복 호출하면 각 큐에 접근할 디스크립터를 얻는다. 이 설명은 커널 인터페이스의 배경이며 Tailscale의 정확한 호출 순서를 확인한 결과는 아니다.

여러 큐를 만들었다고 애플리케이션의 흐름 배정까지 자동으로 설명되지는 않는다. 커널 문서는 큐를 열고 붙이거나 떼는 인터페이스를 정의한다. `TUNSETQUEUE`와 `IFF_ATTACH_QUEUE`, `IFF_DETACH_QUEUE`로 큐의 활성 상태를 바꿀 수 있다. 따라서 커널의 병렬 입출력 지원과 애플리케이션의 패킷 순서 보존을 나누어 읽을 필요가 있다.

## 연결 시작을 돕는 캐시와 출시 범위

netmap 캐시는 이전에 받은 네트워크 지도를 디스크에 저장해 제어 서버 응답 전에 연결을 시작한다. 최초 접속 이력과 영구 저장 공간이 필요하다. 큰 네트워크의 쓰기량이나 SD 카드 수명도 제약이다. 원문 시점에 버퍼 변경과 캐시 기본 활성화는 v1.104 예정이며 멀티큐·모바일 캐시는 후속 출시 계획이다. 성능 진단 도구 역시 탐색 단계다.

## 참고 자료

[Tailscale — We’re making Tailscale faster](https://tailscale.com/blog/making-tailscale-faster)

[Linux Kernel — Segmentation Offloads](https://docs.kernel.org/networking/segmentation-offloads.html)

[Linux Kernel — Universal TUN/TAP device driver](https://docs.kernel.org/networking/tuntap.html)
