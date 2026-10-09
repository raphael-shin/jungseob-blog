---
layout: post
title: "OSC 7501: 에이전트의 승인 대기와 완료를 터미널에 알리는 규약"
date: "2026-10-09 22:58:33 +0900"
created: "2026-10-09T22:58:33+09:00"
source: "https://mitchellh.com/writing/program-status-osc7501"
source_title: "A Terminal Protocol for Program Status (OSC 7501)"
author: jungseob
source_author: "Mitchell Hashimoto"
source_published: "2026-10-06"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "프로그램 상태의 직접 보고, 레코드 수명과 신뢰 경계를 살펴본다."
tags: [knowledge, blog, terminal, agents]
---

## TL;DR

- OSC 7501은 화면을 추측하는 대신 프로그램이 상태와 대기 이유를 직접 보고하게 한다.
- 레코드는 전체 교체하며 작업 중·대기와 완료·실패의 수명을 다르게 관리한다.
- 보고는 신뢰하지 않는 입력이고, 일부 도구 연동은 아직 개념 검증 단계다.

## 화면에서 추측하던 상태를 프로그램이 보고한다

Mitchell Hashimoto가 제안한 OSC 7501은 프로그램의 현재 상태를 터미널에 전달하는 규약이다. 작업 중인 에이전트와 승인을 기다리는 에이전트는 화면이 조용하다는 점만으로 구별하기 어렵다. 제목의 회전 기호를 읽는 방식도 UI가 바뀌면 탐지 규칙을 고쳐야 한다. 소개 글은 Claude Code의 기호 변경 때문에 상태 탐지 규칙을 유지보수한 Herdr 사례를 든다.

별도 소켓 API를 쓰면 프로그램이 상태를 직접 보고할 수 있지만 도구마다 연동해야 한다. SSH나 컨테이너에서는 추가 연결도 필요하다. OSC 7501은 이미 프로그램과 터미널을 잇는 의사 터미널(pty) 경로를 사용한다. 알림이나 받은 편지함을 강제하지 않고 상태만 전달하므로 같은 보고를 여러 UI로 표현할 수 있다.

## 승인 대기와 완료에는 서로 다른 수명이 있다

보고는 콜론으로 구분한 키와 값으로 구성되며 `state`가 필수다. `blocked`는 사용자 개입이 필요한 상태이며 `kind`로 승인·질문·인증을 구별한다. 자유 텍스트는 base64로 인코딩한다. 소개 글의 배포 예시처럼 루트는 작업 중이면서 특정 지역의 하위 작업만 승인 대기일 수도 있다.

상세 규격에서 같은 ID의 새 보고는 이전 레코드를 통째로 교체한다. 생략한 키가 남아 있는 부분 갱신이 아니다. 프로세스 종료나 다음 셸 프롬프트에서는 작업 중·대기 상태를 지우지만 완료·실패는 남긴다. 사용자가 돌아오기 전에 결과 표시가 사라지지 않게 하며, 상태 유지를 위한 주기적 재전송은 요구하지 않는다.

## 상태 보고는 신뢰 증명이 아니다

상세 규격은 메시지와 제목을 신뢰하지 않는 입력으로 취급한다. 디코딩한 제어 문자를 거부하고 마크업으로 해석하지 않아야 한다. 전체 시퀀스의 크기 제한을 넘으면 일부만 적용하지 않고 보고 전체를 버린다. 외부 알림에는 속도 제한을 권고하므로 프로그램의 반복 출력이 무제한 알림으로 이어지지 않게 한다.

지원 여부는 질의와 응답으로 확인하며 terminfo 항목이 없다는 이유만으로 미지원으로 판단해서는 안 된다. 구현 현황과 규격은 구별해야 한다. Hashimoto는 libghostty와 Rex 구현을 소개했지만 Terraform·Claude Code·Codex·Homebrew 연동은 플러그인이나 포크를 통한 개념 검증이었다. 모든 터미널과 도구에서 곧바로 지원되는 공통 기능으로 볼 수는 없다.

## 참고 자료

[A Terminal Protocol for Program Status (OSC 7501)](https://mitchellh.com/writing/program-status-osc7501)

[Program Status Protocol — 상세 규격](https://www.superlogical.com/rex/docs/build/program-status)
