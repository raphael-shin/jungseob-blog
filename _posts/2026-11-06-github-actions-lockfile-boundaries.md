---
layout: post
title: GitHub Actions 잠금 파일이 고정하는 것과 적용 범위
date: 2026-11-06 23:01:00 +0900
created: '2026-11-06T23:01:00+09:00'
source: https://docs.github.com/en/actions/concepts/security/workflow-dependency-lockfiles
source_title: Workflow dependency lockfiles
author: jungseob
source_author: GitHub
source_published: unknown
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 액션의 실행 커밋을 고정한다. 내부 의존성도 기록한다. 저장소의 숫자 ID를 확인한다. 재사용 워크플로는 따로 지정한다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://docs.github.com/assets/cb-345/images/social-cards/actions.png
  alt: GitHub Actions 공식 문서 대표 이미지
---

## TL;DR

- 잠금 파일은 액션과 내부 액션의 실행 커밋을 고정한다.
- 재사용 워크플로 호출과 실행 환경에는 별도 관리가 필요하다.

## 태그 이름과 실제 실행 코드를 함께 기록한다

GitHub Actions에서 태그로 지정한 액션은 실행 시점에 그 태그가 가리키는 코드를 가져온다. 관리자가 태그를 옮기면 같은 워크플로 파일로 다른 코드가 실행될 수 있다. 잠금 파일은 실행할 커밋을 따로 기록한다. 커밋은 코드의 특정 변경 상태를 식별하는 값이다. 워크플로에는 읽기 쉬운 태그를 남기면서 실행 대상을 고정할 수 있다.

잠금 파일은 액션이 내부에서 사용하는 다른 액션까지 기록한다. 원본 저장소와 소유자의 숫자 ID도 저장해 이름 뒤의 저장소가 바뀌었는지 확인한다. 실행할 커밋은 기록된 태그나 브랜치에서 도달할 수 있어야 한다. 다른 포크에만 있는 커밋이나 해당 참조에서 더는 찾을 수 없는 커밋은 실행 때 거부된다.

재사용 워크플로를 호출하는 부분은 별도로 전체 커밋 SHA를 지정해야 한다. 그 워크플로 안의 액션은 호출된 저장소의 잠금 파일이 관리한다. 또한 입력값, 비밀값, 실행기 이미지는 액션 잠금의 범위에 들어가지 않는다. 잠금 파일은 GitHub CLI의 확장 도구인 gh actions-lock으로 생성하며, 공식 문서는 수동 편집을 금지한다.

## 참고 자료

[GitHub의 워크플로 의존성 잠금 파일 문서](https://docs.github.com/en/actions/concepts/security/workflow-dependency-lockfiles)
