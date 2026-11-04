---
layout: post
title: JVM을 3초 만에 복원한 팀이 CPU 명령어를 제한한 이유
date: 2026-11-04 23:03:40 +0900
created: '2026-11-04T23:03:40+09:00'
source: https://medium.com/engineering-housing/we-stopped-our-jvm-from-ever-booting-cold-again-b5dbd492fe88
source_title: 'JVM Startup Time Story: From 330 Seconds to 3'
author: jungseob
source_author: Pulkit Garg
source_published: '2026-11-03'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: CRaC으로 JVM 워밍업을 재사용한 배포와 CPU 호환성 장애의 복구 과정.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://cdn-images-1.medium.com/max/1024/1*ZcxHV_gD_v0l1Kp2WVK7GA.png
  alt: JVM 시작 시간과 체크포인트 복원을 다룬 원문 그림
---

## TL;DR

- 워밍업을 마친 JVM을 복원해 새 파드의 준비 시간을 약 330초에서 2~3초로 줄였다.
- CPU가 다른 노드에서도 복원하려면 체크포인트에 담기는 기계어의 범위를 맞춰야 했다.

## 파드가 준비될 때까지 걸린 330초

Pulkit Garg의 팀에서 새 파드는 JVM을 띄운 뒤에도 바로 트래픽을 받을 수 없었다. JIT 컴파일러가 자주 실행하는 코드를 찾아 기계어로 바꾸는 데 시간이 걸렸다. 파드 하나가 요청을 받을 준비를 마치기까지 약 330초가 걸렸고, 부하가 몰려 파드를 늘려도 가장 바쁜 순간에는 새 파드가 일을 나눠 맡기 어려웠다.

팀은 실행기 한 곳에서 애플리케이션을 충분히 돌린 뒤 CRaC으로 프로세스 상태를 디스크에 저장했다. 새 파드는 그 이미지에서 이미 최적화를 마친 JVM을 복원했다. 팀이 측정한 파드 준비 시간은 2~3초로 줄었다. 여러 파드를 차례로 교체하는 전체 배포 시간도 약 20분에서 4분으로 짧아졌다.

## 같은 노드 그룹에서 복원이 실패한 이유

체크포인트에는 JIT가 만든 기계어도 들어 있다. 이미지를 만들 때 사용한 명령어를 복원 대상 CPU가 지원해야 그 코드를 실행할 수 있다. 운영 중 일부 파드는 시작 단계에서 CPU 기능 비트맵이 맞지 않는다는 오류를 내고 멈췄다. 팀은 먼저 체크포인트를 쓰지 않던 이전 이미지로 되돌려 서비스를 복구했다.

자동 확장기가 노드를 추가하는 환경에서는 같은 노드 그룹 안에서도 CPU가 제공하는 명령어가 달랐다. 팀은 체크포인트를 만드는 시작 스크립트에서 환경 변수로 기준 CPU 기능을 고정했다. 더 빠른 노드의 전용 명령어를 일부 포기하는 대신, 어느 노드에서든 저장한 코드를 다시 실행할 수 있도록 최적화 범위를 제한했다.

## 참고 자료

[Pulkit Garg의 JVM 체크포인트 운영 기록](https://medium.com/engineering-housing/we-stopped-our-jvm-from-ever-booting-cold-again-b5dbd492fe88)
