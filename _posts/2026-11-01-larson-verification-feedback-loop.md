---
layout: post
title: PR 검증 기록을 다음 날의 도구 개선으로 연결하기
date: 2026-11-01 22:57:48 +0900
created: '2026-11-01T22:57:48+09:00'
source: https://lethain.com/adopting-verification-pattern/
source_title: Self-reinforcing quality / adopting verification pattern
author: jungseob
source_author: Will Larson
source_published: '2026-10-30'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: Imprint의 PR 검증 기록과 도구 개선 과정.
tags:
- knowledge
- blog
- web
- ai-agents
image:
  path: https://lethain.com/static/author.png
  alt: 원문 저자 Will Larson
---

## TL;DR

- PR 준비 조건은 검증 기록이다.
- 미검증 항목은 도구 개선에 쓴다.
- 실행 환경 실패는 feedback 도구로 수집한다.

## 검증하지 못한 부분도 PR에 남긴다

Imprint는 PR마다 하네스가 수행한 검증과 수행하지 못한 검증을 파일로 남기게 했다. 이 파일이 없으면 초안 상태를 검토 준비 상태로 바꿀 수 없다. Will Larson은 로컬에서 돌릴 수 있는 린트조차 실패한 채 CI에 도달하는 PR을 반복해서 보았다.

매일 검증 파일을 살펴 반복해서 확인하지 못한 부분을 이슈로 만들고 검토한다. 기능 지도와 검증 도구를 갱신하는 변경도 PR로 올린다. 자동 코드 리뷰의 의견을 받아들였는지 거부했는지도 검토한다. 낮은 품질의 의견을 거부할 때 이유를 남겨 이후 리뷰 지침을 다듬는 재료로 쓴다.

## 기록을 만들기 전에 실패하는 경우

검증 파일만으로는 실행 환경의 실패를 모두 볼 수 없다. 컨테이너 실행기가 중간에 죽으면 파일 자체가 생성되지 않을 수 있다. Imprint는 이런 문제를 별도의 feedback 도구로 보고한다. 개별 변경의 검증 공백과 검증 절차를 실행하지 못하게 하는 환경 문제를 함께 수집하는 구조다.

이 과정은 저장소별 중앙 운영으로 이루어진다. 영역마다 하나의 지침 묶음을 계속 개선하고 중복되거나 충돌하는 안내를 줄인다. 다만 중앙화는 팀별 탐색을 좁힐 수 있다. Larson도 이 긴장을 인정한다. 초기 경험을 소개한 글로 생산성 효과를 입증한 비교 실험은 없다.

## 참고 자료

[Will Larson: 검증 패턴 도입기](https://lethain.com/adopting-verification-pattern/)
