---
layout: post
title: "작은 프로그래밍 요령이 시간을 아끼는 방식"
date: "2026-09-18"
created: "2026-09-18T10:44:18+09:00"
source: "https://will-keleher.com/posts/small-programming-tricks-matter/"
source_title: "Small Programming Tricks"
author: jungseob
source_author: "Will Keleher"
source_published: "2026-03-19"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "검색·관측·연결 재사용에 쓰이는 작은 프로그래밍 요령과, 사내 지식을 하루 하나씩 공유하는 방법을 정리한다."
tags:
  - knowledge
  - blog
  - programming
  - developer-productivity
  - web
---

## TL;DR

- 작은 요령은 배경지식을 많이 쌓기 전에도 당장의 작업을 줄인다. 명령 이력 검색이나 간단한 서버 실행이 그런 사례다. 다만 업무 분야와 이미 아는 내용에 따라 효용은 달라진다.
- 짧은 SQL 실험과 실행 계획은 추측을 실제 동작 확인으로 바꾼다. 로그 버킷은 값의 규모별 분포를 관측하는 데 쓰인다. 도구가 무엇을 실행하고 무엇을 뭉뚱그리는지 함께 알아야 한다.
- 연결 재사용과 코드 이력 검색은 적용 조건까지 알아야 쓸모가 있다. Node 내장 fetch와 node-fetch는 연결 설정 방식이 다르다. Git의 문자열 횟수 변화 검색과 diff 행 검색도 구별해야 한다.
- 팀에 필요한 작은 지식에는 담당자와 문서의 위치도 포함된다. Will Keleher는 이전 회사에서 Slack에 하루 하나씩 요령을 공유했다. 이미 아는 내용이 많아도 낯선 하나가 시간을 아끼고 대화를 열 수 있다.

## 배경지식이 적어도 바로 쓰는 도구

Will Keleher는 일상적인 엔지니어링 생산성의 상당 부분을 작은 지식의 축적으로 설명한다. 언어 기능 하나를 알거나 TCP 지연을 보고 Nagle 알고리즘을 떠올리는 식이다. 모든 지식이 작은 조각으로 이루어졌다는 당연한 사실보다, 많은 배경지식 없이도 바로 적용할 수 있는 요령에 초점을 둔다. `python3 -m http.server`로 현재 디렉터리에서 간단한 서버를 띄우는 데 Python 언어를 먼저 익힐 필요는 없다.

터미널 명령 이력은 이런 요령의 차이가 드러나는 작업이다. `ctrl + r`에 `fzf`를 연결하면 정확히 기억나지 않는 명령도 퍼지 검색으로 찾을 수 있고 `atuin`은 이력을 검색 가능한 SQLite 데이터베이스로 다룬다. `per-directory-history`는 현재 디렉터리에서 실행한 명령과 전체 이력을 오가며 찾게 해 준다. 저장할 이력의 양까지 설정하면, 검색 기능을 늘리는 일과 검색할 기록을 남기는 일을 함께 챙길 수 있다.

## 작은 실험과 관측으로 추측 줄이기

데이터베이스 함수의 동작이 헷갈릴 때는 테이블을 준비하지 않고 `FROM` 없는 `SELECT`로 확인할 수 있다. `SELECT TRUE <> NULL`은 NULL이 끼어 있는 비교를 직접 살펴보는 짧은 예제다. PostgreSQL과 MySQL의 `EXPLAIN ANALYZE`는 쿼리를 실제로 실행하면서 성능 정보를 보여준다. 단순히 실행 계획을 읽는 것과 실제 작업을 수행하는 것은 다르므로, 최적화에 유용하다는 이유만으로 실행 영향을 무시해서는 안 된다.

관측할 대상을 작게 좁히는 방법은 문자열과 지표에도 적용된다. 정규식의 `\b`는 단어 경계를 기준으로 시작이나 끝을 찾게 해 주므로, 경계를 직접 표현하는 수고를 줄인다. 원문의 지표 예제는 `Math.floor(Math.log10(userInGroupCount))`로 `bucket`을 구하고 `metrics.increment("my_metric", {bucket})`에 붙인다. 개별 값을 그대로 나열하는 대신 규모별로 묶어 분포를 살펴보는 방식이며 같은 버킷 안의 세밀한 차이는 드러나지 않는다.

## 연결 재사용은 실행 환경까지 확인하기

JavaScript에 `Array.flatMap`, `Object.entries`, `Promise.withResolvers`가 있다는 사실도 작은 지식에 속한다. 기능의 존재를 모르면 이미 제공되는 처리를 직접 구현하는 쪽으로 생각하기 쉽다. 이 제안의 범위는 언어 전체를 새로 배우는 일까지 넓어지지 않는다. 지금의 작업에 쓸 기능을 알아두는 일이 시간을 줄인다. 다만 기능 이름을 안다는 것과 사용 중인 실행 환경이 이를 지원한다는 것은 별도로 확인할 문제다.

네트워크 요청에서는 외부 자원과의 연결을 유지하는 방법이 지연에 영향을 준다. 원문은 `https.Agent`를 만들고 `fetch(url, {method, agent})`에 전달하는 예제를 들지만 이 코드를 모든 Node 환경의 fetch에 그대로 적용할 수는 없다. 공식 문서로 보강하면 `node-fetch`는 `agent` 옵션을 지원하는 반면 Node 내장 `fetch`는 undici와 호환되는 `dispatcher`를 사용한다. 연결 재사용이라는 목적을 이해하되, 실제 설정은 사용하는 HTTP 클라이언트에 맞춰야 한다. 원문은 지연 개선 가능성을 강조할 뿐, 특정 환경의 측정값이나 보장된 개선 폭을 제공하지 않는다.

## 코드의 과거와 셸의 반복 작업 찾기

오래된 코드베이스에서 문자열이 언제 들어왔는지 찾을 때는 `git log -S pattern`이 유용하다. Git 문서상 이 검색은 파일 안에서 해당 문자열의 등장 횟수가 바뀐 커밋을 찾는다. `git log -G pattern`은 정규식에 맞는 추가·삭제 행이 diff에 있는지를 보므로, 등장 횟수가 같아도 관련 행이 바뀌면 검색할 수 있다. 원문이 언급한 행 이동 탐색도 이 차이로 이해해야 하며 모든 이동을 별도로 추적한다는 뜻은 아니다. `git checkout -`는 `cd -`와 비슷하게 이전 HEAD로 돌아가는 짧은 요령이다.

파일을 찾는 작업도 필요한 범위를 구분하면 짧아진다. 원문은 많은 `find` 명령을 `**/*.md` 같은 glob으로 대체할 수 있다고 설명하며 Bash에서는 `shopt -s globstar` 설정이 필요하다는 조건을 덧붙인다. 파일명 패턴으로 충분한 작업에 맞는 요령이지, `find`의 모든 기능을 대신한다는 주장은 아니다. 텍스트 검색에는 `grep`, `ack`, `ag`보다 `rg`인 ripgrep을 쓰는 방향을 권하지만 이 글 안에서 도구별 성능 비교를 입증하지는 않는다.

zsh 자동완성도 기능이 있다는 사실과 초기화 설정을 연결해야 쓸 수 있다. 원문의 설정은 Homebrew가 있으면 `$(brew --prefix)/share/zsh/site-functions`를 `FPATH` 앞에 더하고 이어서 `autoload -Uz compinit`과 `compinit`을 실행하는 흐름이다. 완성 함수의 위치를 알려 주는 단계와 완성 기능을 초기화하는 단계가 함께 들어 있다. 짧은 명령 하나를 외우는 경우뿐 아니라, 평소 놓치던 설정을 알아두는 경우도 작은 요령에 포함된다.

## 회사 안의 작은 지식은 하루 하나씩

같은 요령이 누구에게나 유용하지는 않다. 이미 모두 알고 있거나 전혀 다른 분야에서 일한다면 이 도구들은 당장의 문제를 줄이지 못할 수 있다. 회사 안에서는 특정 문제를 디버깅할 데이터 소스, 도움을 청할 담당자, 어려운 작업을 설명한 문서의 위치가 더 직접적인 지식이 된다. 수동 증설이 필요한 신호와 롤링 재시작 명령, 반복 작업을 스크립트로 만들 때 쓸 유틸리티도 업무 맥락을 알아야 연결할 수 있는 정보다.

Keleher는 이전 회사에서 기술 요령과 사내 정보를 Slack에 하루 하나씩 공유했고 동료들이 이를 유용하게 받아들인 경험을 적었다. 10개 중 9개를 이미 알아도 남은 하나의 문서나 기법이 시간을 아낄 수 있다는 예시다. 하루 하나라는 분량은 지식을 한꺼번에 쏟아내지 않으면서 때때로 대화가 시작될 여지를 남겼다. 이는 생산성 향상률을 측정한 실험 결과가 아니라 저자의 운영 경험이며 작은 지식을 쉽게 접근할 수 있게 쓰는 Julia Evans의 블로그가 글의 각주에 함께 등장한다.

## 참고 자료

[Small Programming Tricks — Will Keleher](https://will-keleher.com/posts/small-programming-tricks-matter/)

[Node.js 공식 문서 — fetch와 custom dispatcher](https://nodejs.org/api/globals.html#fetch)

[node-fetch — Custom Agent](https://github.com/node-fetch/node-fetch#custom-agent)

[Git 공식 문서 — git-log](https://git-scm.com/docs/git-log)
