---
layout: post
title: "글자 깨짐을 언어가 아닌 문자 체계로 해결한 DatoCMS"
date: "2026-10-10 23:04:28 +0900"
created: "2026-10-10T23:04:28+09:00"
source: "https://www.datocms.com/blog/handling-less-common-scripts"
source_title: "When localization means more than just EN, DE, IT, ES, FR et al."
author: jungseob
source_author: "Roger Tuan, Ronak Ganatra, Silvano Stralla"
source_published: "2026-10-06"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "문자 체계별 대체 폰트와 unicode-range의 다운로드 조건을 살펴본다."
tags: [knowledge, blog, web, localization]
---

## TL;DR

- DatoCMS는 Myanmar 문자 조합 문제를 문자 체계별 Noto 폰트로 해결했다.
- `unicode-range`는 다운로드 필요 여부를 가르지만 폰트 파일 자체를 잘라주지는 않는다.
- CMS 내부 수정과 공개 웹사이트의 렌더링 검증은 별개다.

## 번역문이 있어도 화면에서 글자가 깨진다

DatoCMS의 고객은 S'gaw Karen 문장이 Firefox에서 점선 원과 함께 표시되는 문제를 겪었다. Chrome에서는 정상으로 보였다. 글꼴에 문자가 아예 없을 때의 빈 사각형과 달리, 이 사례는 글자와 결합 부호를 조합하는 단계에서 생겼다. 브라우저·운영체제·설치된 폰트에 따라 서로 다른 대체 폰트를 고르는 조건이 영향을 줬다.

팀은 언어 하나에 대한 예외보다 문자 체계 단위의 수정을 택했다. S'gaw Karen은 버마어·Mon·Shan과 Myanmar 문자를 공유한다. Noto의 문자 체계별 폰트를 쓰면 같은 규칙으로 여러 언어를 지원할 수 있다. 운영체제가 보편적으로 처리하는 문자를 제외하고 43개 문자 체계에 대체 폰트를 추가했다.

## 필요한 폰트만 내려받는 조건

구현은 UI 폰트와 일반 `sans-serif` 사이에 Noto를 배치하는 방식이다. 각 `@font-face`에 문자 범위를 지정했다. 기존 UI 글꼴을 유지하면서 부족한 문자를 대체하며, 사용하지 않는 문자 체계의 폰트는 불러오지 않는다. 팀이 밝힌 약 1KB는 압축된 CSS 크기이며 전체 폰트 용량이 아니다.

MDN의 `unicode-range` 설명에 따르면 범위 안의 문자가 페이지에 없으면 해당 폰트를 다운로드하지 않는다. 반대로 필요한 문자가 하나라도 있으면 해당 폰트 파일 전체를 받는다. 따라서 CSS에 좁은 범위를 적는 것과 폰트 파일 자체를 작게 분할하는 것은 다른 작업이다. 전송량을 줄이려면 어떤 범위에 어떤 파일을 연결했는지도 함께 봐야 한다.

## 적용 범위와 다운로드 범위를 구분한다

MDN은 단일 코드 포인트, 연속 범위, 와일드카드와 여러 범위의 조합을 지원한다고 설명한다. 같은 문장 안에서도 특정 문자만 다른 폰트로 표시할 수 있다. 이는 텍스트를 별도 요소로 감싸지 않고 글리프 선택 범위를 지정하는 방법이다. 다만 범위를 선언하는 것만으로 폰트에 없는 글리프나 조합 기능이 생기지는 않는다는 점은 구현 시 구분해야 한다.

DatoCMS의 변경은 편집기·입력 폼·미리보기 등 CMS 내부에 적용됐다. API 응답이나 고객 웹사이트는 바뀌지 않았다. 따라서 CMS에서 정상으로 보이는 것만으로 공개 사이트의 렌더링을 보장할 수 없다. 같은 콘텐츠라도 실제 서비스의 폰트 구성과 브라우저 조합에서 별도로 확인해야 한다.

## 참고 자료

[DatoCMS — When localization means more than just EN, DE, IT, ES, FR et al.](https://www.datocms.com/blog/handling-less-common-scripts)

[MDN — unicode-range](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/unicode-range)
