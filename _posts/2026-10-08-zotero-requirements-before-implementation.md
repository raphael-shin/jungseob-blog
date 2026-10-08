---
layout: post
title: "Zotero는 구현 전에 무엇을 만들지 배웠다"
date: "2026-10-08 23:07:02 +0900"
created: "2026-10-08T23:07:02+09:00"
source: "https://newsletter.dancohen.org/archive/the-slow-formation-of-durable-software/"
source_title: "The Slow Formation of Durable Software"
author: jungseob
source_author: "Dan Cohen"
source_published: "2026-10-06"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "웹 수집과 서지 관리의 한계에서 Zotero의 요구가 형성된 과정."
tags: [knowledge, blog, software-engineering]
---

## TL;DR

- 별개였던 웹 수집과 서지 관리의 한계가 Zotero의 요구를 구체화했다.
- Firefox 확장은 브라우저 안에서 수집·정리를 연결할 구현 경로였다.

## 수집 도구와 서지 관리 도구가 따로 있던 시기

Zotero 개발자 Dan Cohen의 회고는 선행 도구들의 한계에서 시작한다. Web Scrapbook은 브라우저의 이미지와 링크를 모았지만 학술 메타데이터 처리가 약했다. FileMaker로 만든 Scribe는 인용·주석·검색을 지원했지만 로컬 프로그램이었다. 연구가 웹으로 이동하면서 자료를 발견하는 곳과 정리하는 곳을 연결해야 했다.

2003년의 요구 목록에는 온라인 서지 데이터베이스 연결, 인용 형식 확장, 공동 편집과 다국어 지원이 들어갔다. 로컬 작업의 온라인 공개도 포함했다. 목표는 웹페이지 저장을 넘어 연구 자료의 구조를 알아보는 도구였다. 다만 이때는 브라우저와 독립 프로그램의 기능을 어떻게 합칠지 정하지 못했다.

## 브라우저 확장이 구현 경로를 열다

2004년 Firefox와 XUL은 브라우저 자체를 확장할 방법을 제공했다. 책 정보 API로 서지 항목을 자동 입력하고 공개 데이터베이스에 저장하는 구상이 가능해졌다. 당시 AWS는 Amazon의 도서 정보 API였다. 이후 Firefox의 mozStorage와 SQLite도 구현 기반이 됐다.

2005년 초안은 메타데이터·메모·폴더를 나눠 보여줬고, 개발진이 합류하면서 화면과 기능이 통합됐다. 2006년 출시 이후에는 추가 지원금으로 협업 동기화를 확장하고 Firefox 밖으로 옮겨갔다. Cohen의 핵심은 구현 속도보다 요구를 함께 발견한 시간에 있다. 다만 개인 회고이며 느린 개발의 우월성을 검증한 실험은 아니다.

## 참고 자료

[The Slow Formation of Durable Software](https://newsletter.dancohen.org/archive/the-slow-formation-of-durable-software/)
