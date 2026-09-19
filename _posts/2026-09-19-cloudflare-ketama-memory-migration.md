---
layout: post
title: "Cloudflare의 RAM 100TB 절감과 해시 링 전환"
date: "2026-09-19"
created: "2026-09-19T23:05:15+09:00"
source: "https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/"
source_title: "Saving another 100TB of RAM with math (and Rust)"
author: jungseob
source_author: "Kevin Guthrie, Mariia Iurchenko, Zaidoon Abd Al Hadi, Ivan Babrou"
source_published: "2026-09-18"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "해시 점의 개수와 저장 형식, 캐시를 보존하는 전환 절차를 함께 살펴본다."
tags: [knowledge, blog, performance, distributed-systems]
image:
  path: "https://blog.cloudflare.com/_emdash/api/media/file/01M2PFY1FZ7AH3P8JEQCDM9YWH.01M2PFY2XJ3KBV9JD78JMJK88K.png"
  alt: "Cloudflare 원문의 대표 이미지"
---

## TL;DR

- Cloudflare는 해시 점의 저장 공간과 개수를 줄여 PBR의 RAM 사용량을 전 세계에서 100TB 이상 줄였다.
- 해시 개수에 따른 분산 개선은 점차 작아지고, 연속 공간의 수식은 정수 해시 충돌까지 설명하지 못한다.
- 새 링은 요청 목적지를 바꾸므로 트래픽 비율과 데이터센터 범위를 나누어 전환했다.

Cloudflare의 Pingora Backend Router는 캐시 요청을 서버에 배분한다. 디스크 용량에 따른 가중치와 기능별 서버 조합을 지원하면서 해시 링이 늘어났고 일부 메모리 사용량은 6GB에 달했다. 이 글의 절감 수치는 회사가 보고한 운영 결과다.

## 해시를 늘릴수록 줄어드는 개선 폭

일관 해싱은 서버마다 담당할 해시 구간을 배정한다. 저자의 수학 보충 자료는 해시가 연속 공간에 균일하게 분포한다고 가정하고 구간 길이의 기대값과 표준편차를 구한다. 각 서버에 점을 하나씩 놓으면 담당 구간의 편차가 크다. 여러 점을 배정하면 각 구간을 더한 총길이의 편차가 줄어들지만 메모리에는 그 점들을 모두 저장해야 한다.

서버 N대에 각각 k개의 점을 놓을 때 변동계수는 `sqrt((N-1)/(N*k+1))`다. 이는 평균 대비 표준편차이며 최대 과부하나 실패 확률이 아니다. 같은 식에 N=100을 넣어 직접 계산하면 k=160에서는 약 7.87%, k=1,600에서는 약 2.49%다. 저장하는 점을 열 배 늘려도 상대적 편차는 약 3분의 1로 줄어든다. 모든 서버의 점 개수가 같다는 조건도 이 계산에 포함된다.

다만 연속 공간이라는 가정은 실제 정수 해시의 충돌을 반영하지 않는다. 보충 자료도 여러 점이 충돌하는 경우의 완성된 공식을 제공하지 않는다. Cloudflare의 32비트 시뮬레이션에서는 서버 2,048대에 점을 과도하게 늘리면 오히려 오차가 커졌다. 팀은 이러한 검토를 거쳐 서버별 해시 수를 90% 줄였다.

## 작은 정수로 바꿔도 구조체가 작아지지 않는 이유

Rust Reference에 따르면 타입의 크기는 정렬 요구사항의 배수이며 패딩을 포함한다. 따라서 필드 크기의 합만으로 실제 저장 공간을 계산할 수 없다. `u32`의 정렬이 4바이트인 환경에서 `u32`와 `u16`을 넣으면 값 자체는 6바이트여도 패딩 때문에 8바이트를 차지할 수 있다. 기본 Rust 표현에서는 필드 선언 순서도 일반적인 메모리 배치 계약이 아니다. 대상 환경의 크기와 정렬을 함께 확인해야 한다.

Cloudflare는 해시와 서버 인덱스를 6바이트 배열에 담고 접근 함수로 읽어 점당 공간을 25% 줄였다. Rust의 배열 규칙상 `[u8; 6]`은 6바이트이며 정렬은 `u8`과 같다. 배열 안의 바이트를 정수 값으로 복원하는 접근은 정렬이 맞지 않는 정수 참조를 만드는 접근과 다르다. 이 구현 선택은 저장 크기와 접근 방식을 함께 바꾼다.

Rustonomicon의 `repr(packed)` 설명은 패딩 제거의 비용을 짚는다. 정렬되지 않은 메모리 접근은 아키텍처에 따라 느려지거나 오류를 일으킬 수 있다. 특히 packed 필드의 참조는 정렬 조건을 어길 수 있으므로 단순히 크기가 줄었다고 안전한 구현은 아니다. 메모리 절감과 필드 접근의 유효성은 각각 확인할 문제다.

## 캐시를 유지하면서 새 링으로 옮기기

링이 바뀌면 요청의 목적지도 달라져 기존 캐시를 활용하지 못할 수 있다. 팀은 구형·신형 링을 동시에 유지하고 요청 해시에 따라 버전을 안정적으로 선택했다. 새 링의 트래픽 비율과 적용 데이터센터 범위를 따로 늘렸으며 재배포 없이 구형 링으로 돌아갈 경로도 남겼다.

전환 중에는 캐시 동작과 원본 서버 트래픽, 연결 오류, 메모리 등을 관찰했다. 전환이 끝난 뒤 구형 링을 제거하면서 절감 효과가 나타났다. 일시적으로 두 링을 보유한 비용과 최종 메모리 감소는 구분해야 한다.

## 참고 자료

[Saving another 100TB of RAM with math (and Rust)](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/)

[Consistent hashing math — 수식과 가정](https://ch.terabyteoff.com/)

[The Rust Reference — Type layout](https://doc.rust-lang.org/reference/type-layout.html)

[The Rustonomicon — Alternative representations](https://doc.rust-lang.org/nomicon/other-reprs.html)
