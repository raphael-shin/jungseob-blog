---
layout: post
title: GitHub 리뷰 화면의 스크롤 보정
date: 2026-11-16 23:01:52 +0900
created: '2026-11-16T23:01:52+09:00'
source: https://github.blog/engineering/user-experience/rendering-huge-pull-requests-in-the-github-copilot-app/
source_title: Rendering huge pull requests in the GitHub Copilot app
author: jungseob
source_author: Alberto Gimeno
source_published: '2026-09-23'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 댓글 높이와 스크롤을 관리한다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://github.blog/wp-content/uploads/2026/06/MSFTBuild_Blog_Header_01.jpg
  alt: GitHub Copilot
---

## TL;DR

- 코드와 댓글의 높이를 따로 계산한다.
- 스크롤의 발생 주체를 구별한다.

## 댓글 높이가 바뀌어도 읽던 위치를 유지한다

GitHub Copilot 앱의 코드 비교 화면에서는 코드보다 댓글의 높이를 계산하기 어려웠다. 코드는 글꼴 크기로 행 높이를 미리 계산할 수 있지만, 댓글은 줄바꿈과 이미지 로딩에 따라 달라진다. GitHub는 두 종류의 높이를 별도로 관리했다. 댓글이 늘어나도 코드 전체의 위치 계산을 다시 하지 않는다. 댓글은 현재 픽셀 위치 대신 파일과 줄을 기준으로 식별해 화면 배치가 바뀌어도 추적한다.

처음에는 크기 변경 감지기가 높이를 측정해 즉시 화면 배치에 반영했다. 그 변경이 다시 감지기를 자극하는 반복이 문제였다. 최종 방식은 스크롤이 멈춘 뒤 화면 주변의 댓글 높이를 한꺼번에 읽는다. 기본적으로 감지기는 재측정이 필요하다는 표시만 남긴다. 다만 화면에 보이는 댓글을 펼칠 때는 아래 코드도 함께 움직이도록 같은 프레임에서 보정한다. 이 즉시 반영은 프레임당 한 번으로 제한하며 스크롤 중에는 미룬다.

높이 보정 전에는 읽던 행과 그 안의 상대 위치를 저장한다. 보정 후 같은 행을 찾아 화면 위치를 유지한다. 그런데 사이드바를 열어 너비가 바뀌면 앱 자체가 일으킨 스크롤까지 사용자 동작으로 오인해 필요한 보정을 건너뛰었다. 해결책은 사용자 스크롤과 앱이 만든 스크롤을 구별하는 것이었다. 화면 위치 유지 기능이 자기 동작 때문에 중단되지 않도록 수정했다.

## 참고 자료

[GitHub의 대규모 코드 비교 화면 설계](https://github.blog/engineering/user-experience/rendering-huge-pull-requests-in-the-github-copilot-app/)
