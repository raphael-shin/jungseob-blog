---
layout: post
title: "README를 읽는 대신 실행하게 했다: 첫 설치 경험의 사용자 검증"
date: "2026-10-11 23:02:05 +0900"
created: "2026-10-11T23:02:05+09:00"
source: "https://shkspr.mobi/blog/2026/10/i-paid-people-to-try-and-follow-my-readme/"
source_title: "I paid people to try and follow my README"
author: jungseob
source_author: "Terence Eden"
source_published: "2026-10-11"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "실제 설치 관찰과 반복 수정으로 README의 숨은 전제를 찾은 사례."
tags: [knowledge, blog, documentation]
image:
  path: "https://shkspr.mobi/blog/wp-content/uploads/2020/01/Storm-Trooper-Chocolate-Money.jpg"
  alt: "README 사용자 검증 사례의 원문 대표 이미지"
---

## TL;DR

- 화면 공유와 생각 말하기로 작성자가 놓친 설치 문서의 전제를 발견했다.
- 세션마다 수정한 README를 다음 참여자에게 다시 시험했다.
- 개선은 저자의 관찰이며 성공률의 정량 비교는 없다.

## 작성자가 아는 것을 독자는 모른다

Terence Eden은 ActivityBot의 첫 설치 경험을 실제 사용자와 검증했다. 작성자는 빠진 권한 설정이나 잘못 적힌 옵션을 무의식적으로 보완할 수 있다. 새 가상머신에서 스스로 문서를 따라 해도 이런 사전 지식까지 지우기는 어렵다.

참여자는 화면을 공유하면서 설치를 진행하고 생각을 소리 내어 설명했다. 무엇을 하는지와 어디서 혼란스럽거나 만족스러운지를 말하도록 요청했다. Eden은 손으로 메모하며 잘못된 전제를 수집했다. 보상은 한 시간에 25유로였고 전체 지출은 약 150유로였다.

## 한 번 고친 문서를 다음 사람에게 다시 시험한다

관찰된 문제에는 잘못된 데모 링크, 숨김 파일 이름 변경, 따옴표가 필요한 조건이 있었다. 일부 참여자는 README를 터미널에서 읽었다. 기술 용어와 섹션 순서뿐 아니라 소프트웨어가 무엇을 하는지에 대한 설명도 부족했다. 웹서버별 권한 차이까지 드러나 문서 검토가 문장 교정에 머물지 않았다.

Eden은 매 세션 뒤 어려웠던 부분을 수정하고 다음 참여자에게 다시 시험했다. 매번 새로운 참여자를 대상으로 수정한 지시를 실행할 수 있는지 확인했다. 다만 원문에는 설치 성공률이나 소요 시간의 전후 비교가 없다. 따라 하기 쉬워졌다는 저자의 관찰을 정량적 효과나 문서의 완전성으로 확대할 수는 없다.

## 참고 자료

[I paid people to try and follow my README](https://shkspr.mobi/blog/2026/10/i-paid-people-to-try-and-follow-my-readme/)
