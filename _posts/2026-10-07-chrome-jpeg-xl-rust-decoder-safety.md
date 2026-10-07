---
layout: post
title: "Chrome의 JPEG XL 디코더, Rust와 SIMD로 나눈 안전성 책임"
date: "2026-10-07 23:06:29 +0900"
created: "2026-10-07T23:06:29+09:00"
source: "https://developer.chrome.com/blog/jpeg-xl-in-chrome"
source_title: "Shipping JPEG XL in Chrome"
author: jungseob
source_author: "Luca Versari, Moritz Firsching, Philip Jägenstedt"
source_published: "2026-10-06"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "JPEG XL 디코더의 Rust 전환과 SIMD 최적화를 Chromium의 안전성 원칙에 연결한다."
tags:
  - knowledge
  - blog
  - Rust
  - web
image:
  path: "https://developer.chrome.com/static/blog/jpeg-xl-in-chrome/images/cover.png"
  alt: "Chrome의 JPEG XL 지원 원문 대표 이미지"
---

## TL;DR

- Chrome은 Rust 디코더로 JPEG XL을 지원하고 SIMD 최적화를 함께 적용한다.
- Chromium의 안전성 원칙은 권한 축소와 메모리 안전성을 별개로 다루며 `unsafe` 검토 조건을 둔다.
- 버그 미발견은 무결함 보장이 아니며 포맷 선택도 실제 이미지로 비교해야 한다.

## 디코더를 Rust로 옮기면서 지킨 성능 조건

Chrome 팀은 155부터 JPEG XL 디코딩을 지원한다. 통합한 디코더는 Rust로 다시 구현한 `jxl-rs`다. 이미지 디코더는 네트워크에서 온 복잡한 바이너리를 렌더러에서 처리한다. 샌드박스로 피해 범위를 줄이면서 구현 언어로 메모리 오류의 원인을 줄이는 접근이다.

성능에는 SIMD 추상화 계층 `jxl_simd`가 쓰인다. Rust의 `target_feature_11` 안정화를 바탕으로 SIMD 사용을 지원하고, `unsafe`는 검토한 소수 지점에 제한한다. `libjxl`의 최적화를 이어받아 영역 경계를 넘는 처리 파이프라인과 데이터 복사 절감도 적용했다.

## 샌드박스와 메모리 안전성이 맡는 역할

Chromium의 Rule of 2는 신뢰할 수 없는 입력, 메모리 안전하지 않은 구현 언어, 높은 권한을 한곳에 모두 모으지 않는 원칙이다. 권한을 낮추면 취약점이 생겼을 때 가능한 피해를 줄인다. 메모리 안전한 언어는 메모리 손상이라는 오류 종류를 줄이는 데 쓰인다. 두 방법은 서로 다른 지점에 작용하므로 샌드박스를 쓴다는 이유만으로 언어 선택이 무의미해지지 않는다.

Rust 안의 `unsafe`도 별도로 검토해야 한다. 이 원칙은 해당 코드를 최소화하고 안전한 API 뒤에 감싸며, 전제 조건과 충족 근거를 문서화하도록 요구한다. 검토자는 작은 범위의 코드만으로 그 안전성을 판단할 수 있어야 한다. 메모리 안전한 언어로 감싼 API라도 내부 구현이 안전하지 않다면 이름만으로 안전한 구현이 되지는 않는다.

## 검증 결과와 포맷 선택의 범위

Chrome 팀은 퍼징과 AI 코드 검토를 수행했고 구현 과정에서 메모리 안전성 버그를 찾지 못했다고 밝혔다. 이는 팀의 관찰이며 버그 부재의 증명은 아니다. 브라우저 간 호환성은 Interop의 JPEG XL 조사와 기능별 테스트로 확인한다.

Chrome 팀이 밝힌 JPEG 대비 압축 개선 폭은 30~50%다. 다만 AVIF와 JPEG XL을 모두 시험하도록 권하며 모든 이미지에서 같은 결과를 보장하지 않는다. 고품질 사진·무손실 압축·세밀한 점진 디코딩을 주요 활용처로 꼽는다. HDR·JPEG 무손실 변환도 지원한다.

## 참고 자료

[Shipping JPEG XL in Chrome](https://developer.chrome.com/blog/jpeg-xl-in-chrome)

[Chromium — The Rule Of 2](https://chromium.googlesource.com/chromium/src/+/main/docs/security/rule-of-2.md)
