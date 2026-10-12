---
layout: post
title: "Zig 템플릿의 타입 검사와 HTML 출력 안전성을 나누는 방법"
date: "2026-10-12 23:06:51 +0900"
created: "2026-10-12T23:06:51+09:00"
source: "https://lalinsky.com/2026/10/11/type-safe-html-templating-in-zig.html"
source_title: "Type-safe HTML templating in Zig"
author: jungseob
source_author: "Lukáš Lalinský"
source_published: "2026-10-11"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "zt의 컴파일 시점 검사와 HTML 출력 규칙, 명시적 예외를 살펴본다."
tags: [knowledge, blog, web]
---

## TL;DR

- zt는 템플릿을 Zig 코드로 바꿔 타입 오류를 빌드 중 잡는다.
- HTML 속성의 의미와 이스케이프 예외는 별도로 다뤄야 한다.
- 초기 프로젝트이며 실행 성능과 보안은 여기서 검증하지 않았다.

## 템플릿의 오류를 컴파일러로 옮긴다

Lukáš Lalinský의 zt는 HTML 템플릿을 빌드 중 Zig 소스로 변환한다. 템플릿에서 애플리케이션의 타입을 가져오고 호출 측에서도 같은 타입을 검사한다. 예컨대 사용자 필드 이름을 잘못 쓰거나 기대한 구조체 대신 문자열을 넘기면 컴파일에 실패한다. 오류 위치는 생성된 코드에 찍히며 주석으로 원래 템플릿의 위치를 연결한다.

생성된 코드는 중간 렌더링 상태 없이 `std.Io.Writer`로 출력한다. 호출자는 소켓에 직접 쓰거나 버퍼에 모을 수 있다. 저자가 설명하는 무할당 특성은 이 출력 경로에 관한 것이며 웹 애플리케이션 전체의 메모리 사용을 뜻하지 않는다. 원문에 별도 성능 측정은 없으므로 다른 엔진보다 빠르다는 비교 결론도 내릴 수 없다.

## HTML의 규칙을 기본 동작에 담는다

zt는 동적 텍스트와 속성 값을 기본적으로 HTML 이스케이프한다. URL 속성에서는 위험한 스킴도 검사한다. 원시 HTML 출력은 `{!value}`로 명시하며 태그는 올바르게 닫아야 한다. 이런 기본값은 흔한 XSS 원인을 줄이지만 모든 공격을 방어하는 보장은 아니다. 출력할 값의 타입 검사와 출력 문맥의 안전 처리는 서로 다른 역할을 맡는다.

저장소 README의 불리언 속성 예시는 HTML 의미를 더 구체적으로 다룬다. `checked="false"`도 체크 상태이므로 일반 동적 속성에 불리언을 넘기는 방식은 컴파일 오류가 된다. 조건부 속성 문법 `?=`를 쓰면 참일 때만 속성을 출력한다. 반면 `aria-expanded`처럼 문자열을 요구하는 속성은 참과 거짓에 대응하는 문자열을 직접 전달한다.

## 명시적인 예외와 아직 남은 문법 선택

README는 사용자 정의 출력에서도 안전성의 경계를 구분한다. `format` 메서드의 출력에는 이스케이프가 적용되지만 `formatHtml`은 가공하지 않은 HTML을 쓴다. 후자는 메서드 자체가 안전한 마크업을 만들어야 한다. 기본 이스케이프가 존재한다는 이유만으로 사용자 정의 출력까지 자동으로 안전하다고 볼 수 없는 지점이다.

원문 작성 시점에는 제어 흐름 문법도 확정되지 않았다. 줄 처음의 `if`를 코드로 해석하므로 같은 단어로 시작하는 일반 문장은 별도 처리해야 한다. 저자는 이를 구분하는 접두 문법을 검토하고 있다. 초기 프로젝트의 설계 소개로 읽어야 하며 이 노트에서는 예제 실행이나 보안 검증을 수행하지 않았다.

## 참고 자료

[Type-safe HTML templating in Zig](https://lalinsky.com/2026/10/11/type-safe-html-templating-in-zig.html)

[zt README](https://github.com/lalinsky/zt) — 불리언 속성과 사용자 정의 출력 규칙을 대조했다.
