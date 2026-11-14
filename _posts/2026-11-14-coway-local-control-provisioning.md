---
layout: post
title: 코웨이 공기청정기를 클라우드 없이 연결한 과정
date: 2026-11-14 23:02:03 +0900
created: '2026-11-14T23:02:03+09:00'
source: https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/
source_title: Reverse Engineering My Coway Air Purifier to Ditch the Cloud
author: jungseob
source_author: Scott J. Goldman
source_published: '2026-11-11'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 서버 의존성을 줄인다. 통신을 분석한다. 초기 설정도 바꾼다. 로컬에서 제어한다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/coway-airmega-icons-cover.jpg
  alt: Coway Airmega IconS 공기청정기
---

## TL;DR

- 명령 전달뿐 아니라 블루투스 초기 설정까지 대체했다.
- AI의 분석 결과를 기록과 대조하고 중간 출력을 검토했다.

## 제어 서버뿐 아니라 초기 설정도 바꾼다

Scott J. Goldman의 공기청정기는 Home Assistant에 연결돼 있어도 코웨이 서버를 거쳐 명령을 받았다. Home Assistant는 가정의 기기를 연결하는 자동화 소프트웨어다. 서버 장애나 앱 변경, 계정 차단이 생기면 집 안의 팬도 원격으로 제어할 수 없었다. 저자는 자신의 Airmega IconS가 통신하는 방식을 분석해 제조사 서버 대신 로컬 서버를 쓰도록 바꿨다.

통신 분석으로 명령을 중계하는 MQTT 서버를 대체해도 초기 설정에는 코웨이 앱이 남았다. MQTT는 기기 사이에 메시지를 전달하는 통신 방식이다. 다음 단계는 블루투스 설정 절차였다. AI가 휴대전화의 블루투스 기록과 앱 코드를 대조했고, 저자는 중간 산출물에서 인증서와 접속 설정을 가져올 서버 주소를 발견했다. 그 주소를 초기 설정에 직접 넣을 수 있어 최종 구성에는 통신 가로채기가 필요하지 않았다.

완성된 통합에서는 노트북을 기기 근처로 가져가 브라우저의 블루투스 기능으로 설정한다. 이후 공기청정기는 와이파이로 Home Assistant와 직접 통신하고 Apple Home에도 연결된다. AI가 재구현한 설정은 캡처한 기록으로 검증할 수 있었다. 서버 주소의 의미를 알아본 것은 중간 출력을 지켜보던 저자였다. 이 사례는 해당 기기의 구현 경험이며, 모든 코웨이 모델에서 같은 방식이 작동한다고 확인한 결과는 아니다.

## 참고 자료

[Scott J. Goldman의 공기청정기 역공학 기록](https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/)
