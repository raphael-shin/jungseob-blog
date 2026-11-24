---
layout: post
title: Rewind로 찾는 임계 경로와 필요한 대기 시간
date: 2026-11-24 23:08:00 +0900
created: '2026-11-24T23:08:00+09:00'
source: https://fzakaria.com/2026/11/12/worshipping-at-the-altar-of-brendan-gregg
source_title: Worshipping at the altar of Brendan Gregg
author: jungseob
source_author: Farid Zakaria
source_published: '2026-11-12'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: CPU 밖의 대기와 단축 가능한 시간을 구분한다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://fzakaria.com/assets/images/rewind-time-overview-crop.png
  alt: Rewind의 libuv 임계 경로 분석 화면
---

## TL;DR

- CPU가 쉬는 시간도 임계 경로를 늘린다.
- 발견한 대기가 테스트에 필요한지 확인해야 한다.

## CPU가 쉬는 동안에도 실행은 지연된다

Farid Zakaria의 Rewind 사례에서 libuv 빌드와 테스트는 가상 CPU 하나로 78초 걸렸다. 선행 작업을 기다리는 가장 긴 연쇄인 임계 경로는 47.4초였고, 그중 67%는 계산이 아닌 대기였다. 같은 의존 관계를 유지한다면 CPU를 늘려도 이 경로보다 빨리 끝낼 수 없다. CPU 프로파일만으로는 쉬는 스레드의 지연을 설명하기 어렵다.

`rewind time`은 재생용으로 기록한 문맥 전환에 깨우기 이벤트와 그 주체를 더해 대기 관계를 분석한다. 이 실행에서는 임계 경로 중 41.9초가 `make check`에 속했고, 테스트 실행기는 테스트 287개를 차례로 수행했다. 도구는 경로 위의 소요 시간과 특정 작업의 시간을 없앴을 때 전체 실행이 단축되는 시간을 따로 보여 준다. 두 시간은 같지 않을 수 있다.

기록을 재생해 `hrtime` 테스트의 대기 시작점으로 돌아가면 `uv_sleep(45)` 호출을 확인할 수 있다. 45밀리초 대기를 75번 반복해 약 3.38초가 쌓였다. 이 테스트는 잠든 동안 시계 값이 얼마나 변하는지 검사하므로 대기 자체가 검사 조건이다. 기다리는 위치를 찾았다는 사실만으로 그 대기를 제거해도 된다는 결론이 나오지는 않는다.

## 참고 자료

[Rewind의 임계 경로 분석 사례](https://fzakaria.com/2026/11/12/worshipping-at-the-altar-of-brendan-gregg)
