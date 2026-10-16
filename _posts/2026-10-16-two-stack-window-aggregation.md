---
layout: post
title: "두 스택으로 이동 구간 집계하기"
date: "2026-10-16 22:57:29 +0900"
created: "2026-10-16T22:57:29+09:00"
source: "https://orlp.net/blog/two-stack-sliding-window-aggregation/"
source_title: "Two-Stack Sliding-Window Aggregation"
author: jungseob
source_author: "orlp"
source_published: "2026-10-02"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "역연산 없이 구간을 갱신하는 원리와 상각 비용의 한계."
tags: [knowledge, blog, web]
---

## TL;DR

- 두 스택의 집계를 결합하면 역연산 없이 구간을 갱신할 수 있다.
- 상각 O(1)은 개별 호출의 일정한 지연을 뜻하지 않는다.
- 부동소수점 오차와 구간 밖 값의 영향은 구분해야 한다.

## 삭제를 되돌리지 않고 집계한다

정수 합계는 새 값을 더하고 오래된 값을 빼면 이동 구간을 갱신할 수 있다. 최솟값처럼 역연산이 없는 집계에는 이 방식이 통하지 않는다. 두 스택 방식은 현재 구간을 앞부분과 뒷부분으로 나눠 관리한다. 각 부분의 집계 결과를 결합하므로 삭제한 원소의 기여를 역으로 계산할 필요가 없다.

새 원소는 입력 스택에 쌓으면서 집계를 갱신한다. 오래된 원소를 제거할 때 출력 스택이 비었다면 입력 원소를 역순으로 옮기며 누적 집계를 만든다. 이후에는 출력 스택의 꼭대기를 제거한다. 남은 출력 집계와 입력 집계를 결합하면 현재 구간 전체의 결과를 얻는다. 결합할 피연산자 순서는 원래 데이터 순서를 유지한다.

## 평균 비용과 수치 계산의 한계

결합 비용이 일정하면 원소마다 한 번 옮겨가는 작업은 상각 O(1)이다. 다만 한꺼번에 옮기는 순간에는 구간 크기만큼 작업한다. 따라서 개별 호출의 최악 지연도 일정하다는 뜻은 아니다. 최대 구간 크기를 w라 하면 저장공간은 O(w)이며, 구간은 고정 크기일 필요 없이 늘리거나 줄일 수 있다.

결합법칙이 성립해야 하지만 교환법칙은 필요하지 않다. 부동소수점 덧셈은 결합법칙을 엄밀히 만족하지 않아 계산 순서에 따른 오차가 남는다. 그래도 집계가 현재 구간의 원소에만 의존하므로 떠난 NaN이나 무한대가 이후 결과를 계속 오염시키지는 않는다. 이는 정확한 실수 연산을 보장하는 성질과는 구분해야 한다.

## 참고 자료

[Two-Stack Sliding-Window Aggregation](https://orlp.net/blog/two-stack-sliding-window-aggregation/)
