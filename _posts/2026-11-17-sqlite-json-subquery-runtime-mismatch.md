---
layout: post
title: SQLite의 JSON 수정이 LLM 로그를 깨뜨린 이유
date: 2026-11-17 22:57:57 +0900
created: '2026-11-17T22:57:57+09:00'
source: https://simonwillison.net/2026/Nov/16/llm/
source_title: 'Release: llm 0.37.3'
author: jungseob
source_author: Simon Willison
source_published: '2026-11-16'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 서브쿼리의 JSON 처리와 CI의 SQLite 버전 차이가 로그 오류로 이어졌다.
tags:
- knowledge
- blog
- web
- software-engineering
---

## TL;DR

- 서브쿼리 결과를 JSON으로 명시해 문자열 삽입을 피했다.
- 기존 테스트도 SQLite 버전이 다른 CI에서는 문제를 발견하지 못했다.

## 배열이 문자열로 바뀐 경계

Simon Willison의 LLM 도구는 SQLite 3.54.1을 사용하는 환경에서 일부 과거 로그를 표시하지 못했다. 첨부 파일이 있는 도구 실행 결과가 대상이었다. 조회문은 서브쿼리에서 첨부 목록을 만든 뒤 JSON 객체에 넣었다. 그런데 목록이 배열 대신 문자열로 들어가면서 표시 코드가 그 문자열의 글자를 하나씩 순회했다. 객체에 쓰는 메서드를 문자열에 호출해 오류가 발생했다.

SQLite에서 JSON처럼 생긴 텍스트가 항상 JSON 값으로 삽입되는 것은 아니다. 공식 문서는 객체 생성 함수의 값 인자를 보통 문자열로 해석한다. 다른 JSON 함수가 직접 반환한 값은 JSON으로 받아들이지만, 스칼라 서브쿼리를 통과한 결과는 SQL 텍스트다. Willison의 최소 예제는 3.54.0에서 배열을 넣었지만 3.54.1에서는 같은 배열 모양의 문자열을 넣었다. SQLite 개발자 Richard Hipp은 새 동작이 문서에 맞는 버그 수정이라고 확인했다.

해결 방법은 서브쿼리 결과를 바깥 JSON 객체에 넘기기 전에 `json()`으로 감싸는 것이다. JSON으로 해석해야 할 지점을 명시하면 배열을 문자열로 삽입하는 일을 피할 수 있다. 다만 이 함수는 임의의 텍스트를 원하는 자료구조로 고치는 도구가 아니다. 입력이 JSON이라는 전제와 구조가 맞는지는 별도로 확인해야 한다.

이 문제는 기존 테스트로도 재현됐지만 CI에서는 나타나지 않았다. 신고 당시 CI의 Python은 더 오래된 SQLite에 연결돼 있었고, 문제가 난 macOS의 Homebrew Python은 3.54.1을 사용했다. 저장소에는 SQLite를 빌드하고 해당 버전으로 테스트하는 변경이 추가됐다. 쿼리 수정과 함께 테스트 환경도 바뀐 사례다. 오류 원인은 모델 응답이 아니라 로그를 읽는 데이터 경로에 있었다.

## 참고 자료

[Simon Willison의 LLM 0.37.3 기록](https://simonwillison.net/2026/Nov/16/llm/)

[LLM 로그 오류 신고와 CI 변경](https://github.com/simonw/llm/issues/1879)

[SQLite 개발자의 동작 설명](https://sqlite.org/forum/forumpost/dff1a343157e422f)

[SQLite JSON 값 인자 문서](https://sqlite.org/json1.html#value_arguments)
