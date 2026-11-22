---
layout: post
title: Muru의 지연 import가 첫 요청에 남기는 비용
date: 2026-11-22 23:03:36 +0900
created: '2026-11-22T23:03:36+09:00'
source: https://grahamdumpleton.me/posts/2026/11/muru-when-lazy-imports-help/
source_title: 'Muru: when lazy imports help'
author: jungseob
source_author: Graham Dumpleton
source_published: '2026-11-22'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 시작 시간과 요청 지연의 교환을 살펴본다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://grahamdumpleton.me/assets/images/graham-blog-banner.png
  alt: Graham Dumpleton 블로그
---

## TL;DR

- 지연 import는 비용을 첫 요청으로 옮긴다.
- 실제 트래픽에 따라 미리 불러올 모듈이 달라진다.

## 시작 비용이 첫 요청으로 옮겨 간다

Muru는 호스트 프로세스에서 애플리케이션을 읽어 들인 뒤 작업 프로세스를 복제한다. 미리 불러온 모듈의 메모리는 변경 전까지 공유된다. 모듈을 처음 사용할 때 불러오는 지연 import는 이 비용을 각 작업 프로세스의 첫 요청으로 옮긴다. 데몬 배포에서는 새 릴리스가 준비돼야 트래픽을 넘기므로, 시작을 단축해도 기존 방문자의 대기 시간을 줄이지는 않는다.

Graham Dumpleton은 Python 3.14의 Flask 예제를 작업 프로세스 두 개로 실행했다. import 기록 기능을 끄고 각 조건에서 다섯 번 시작한 결과, openpyxl 로딩을 미루자 시작 시간 중앙값이 83ms에서 35ms로 줄었다. 그러나 첫 스프레드시트 요청은 모듈 로딩 비용을 부담했다. pandas를 처음 불러오는 보고서 요청에서는 같은 프로세스의 다른 스레드도 import 잠금에 막혔다. 직접 로딩한 요청과 잠금을 기다린 요청 모두 약 140ms가 걸렸다.

모든 작업 프로세스가 쓰는 모듈은 복제 전에 불러오는 편이 나았다. 보고서 모듈을 미리 읽자 각 프로세스의 첫 보고서 요청은 4.5~9ms로 줄었다. 처음에는 일부 프로세스만 쓰던 openpyxl도 다운로드가 늘자 모두가 로딩했다. 따라서 개발 중 적은 요청으로 내린 판단은 달라질 수 있다.

## 참고 자료

[Graham Dumpleton의 Muru 실험](https://grahamdumpleton.me/posts/2026/11/muru-when-lazy-imports-help/)
