---
layout: post
title: 외부 샌드박스의 도구별 격리 경계
date: 2026-11-18 23:00:08 +0900
created: '2026-11-18T23:00:08+09:00'
source: https://blog.primeradiant.com/external-sandboxes-for-coding-agents/
source_title: External sandboxes for coding agents
author: jungseob
source_author: Simon Willison
source_published: '2026-11-17'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 명령 실행과 도구별 격리 범위를 구분한다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://storage.ghost.io/c/c2/33/c2337b7d-2a3a-4cb4-8e28-7d30596f7cd7/content/images/2026/11/converted_image-2.png
  alt: 외부 샌드박스
---

## TL;DR

- 도구 연결 방식에 따라 격리 범위가 달라진다.
- 쓰기 폴더와 허용 서버의 위험은 남는다.

## 에이전트와 명령 실행 환경을 분리한다

Prime Radiant의 외부 샌드박스에서는 에이전트가 호스트에서 실행되고 명령은 별도 Linux 환경으로 전달된다. 외부라는 말은 다른 컴퓨터가 필요하다는 뜻이 아니다. 에이전트가 자신의 실행 환경을 수정하는 일을 피하고 격리 경계를 살피기 쉽게 하려는 선택이다. 샌드박스에는 지정한 폴더만 연결하며, 외부 네트워크는 기본적으로 차단한다.

같은 샌드박스라도 에이전트와 연결하는 방식에 따라 보호 범위가 달라진다. 이 구현에서 Claude Code는 Bash 명령만 보내므로 기본 파일 읽기와 편집은 호스트에 남는다. Codex는 프로세스와 파일 작업을 전달한다. Pi는 기본 도구를 끄고 대체 도구를 사용한다. 이 설정에서는 연결이 실패해도 호스트 도구로 돌아가지 않고 오류를 낸다. 명령 하나가 Linux에서 실행됐다는 사실만으로 모든 도구가 격리됐다고 볼 수는 없다.

네트워크를 허용할 때는 프록시에서 접속 대상과 HTTP 메서드를 제한한다. 인증 정보도 프록시가 대체하므로 샌드박스에는 실제 키 대신 임시 값을 넣을 수 있다. 다만 허용한 서버가 응답으로 키를 되돌려줄 가능성은 남는다. 쓰기 가능한 폴더 안의 파일도 손상될 수 있다. 저자들은 세 구현을 실험적 시제품으로 규정하며, 민감한 작업을 맡길 수준으로 감사를 거치지는 않았다고 명시했다.

## 참고 자료

[Prime Radiant의 외부 샌드박스 설계](https://blog.primeradiant.com/external-sandboxes-for-coding-agents/)
