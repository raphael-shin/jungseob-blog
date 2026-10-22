---
layout: post
title: "PHP 보안 수정이 멈춘 이유 — 발견 이후의 의사결정과 검증"
date: "2026-10-22 23:05:08 +0900"
created: "2026-10-22T23:05:08+09:00"
source: "https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/"
source_title: "Today's PHP Security Release, and How We're Strengthening PHP Security"
author: jungseob
source_author: "The PHP Foundation"
source_published: "2026-10-21"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "PHP 재단이 인정한 수정 지연의 구조적 원인과 보안팀의 재현·분류 절차."
tags: [knowledge, blog, web]
image:
  path: "https://thephp.foundation/assets/share/2026-10-21-todays-php-security-release-and-how-were-strengthening-php-security.png"
  alt: "PHP 재단의 보안 릴리스와 대응 개선 회고 표지"
---

## TL;DR

- 수정안의 호환성 비용과 합의 절차, 전문 인력 부족이 대응을 지연시켰다.
- 공개 일정에는 사용자가 실제로 업데이트할 수 있는 준비 상태도 반영됐다.
- AI가 보고를 분류해도 재현·심각도 판단·패치 검토는 사람의 책임이다.

## 수정안을 고르지 못한 시간

PHP 재단의 보안 회고에서 메모리 부족 문제의 징후는 2024년 외부 감사 후속 작업까지 거슬러 올라간다. 당시에는 구체적인 원격 코드 실행 경로가 확인되지 않았다. 수정 후보는 있었지만 기존 코드와의 호환성을 깨거나 서비스 거부 가능성을 만들고, 수많은 외부 확장 모듈의 변경을 요구하는 등 각각 비용이 컸다.

합의로 결정하던 보안팀은 잘못된 선택의 파장을 우려했다. 엔진을 깊이 이해하는 소수 개발자는 다른 책임도 맡고 있었고 수정 작업은 수개월 동안 멈췄다 다시 시작되기를 반복했다. 재단은 이를 의사결정 방식과 자원 부족에서 생긴 구조적 실패로 인정했다. 이후 다수결로 결정을 내리고 절충안을 허용하는 방향으로 절차를 바꾸기 시작했다.

## 발견 이후에도 배포를 조정해야 한다

2026년 8월에는 같은 근본 원인으로 원격 코드 실행이 가능하다는 보고가 들어왔고 수정이 최우선 과제가 됐다. 전담 인력의 작업과 관계자 조율에는 재단의 지원이 필요했다. 회고의 개선 방향에는 복잡한 절충 때문에 막힌 취약점을 지도부가 더 일찍 다룰 수 있도록 하는 절차도 포함된다.

공개를 앞두고 정보가 유출되자 출시일을 하루 앞당겼지만 즉시 배포하지는 않았다. 배포판 업체들이 아직 패키지를 준비 중이어서 곧바로 공개하면 손쉽게 업데이트할 수 없는 사용자가 생겼기 때문이다. 이는 재단이 설명한 일정 조정의 이유다. 이 글은 재단의 대응 회고이며 외부 감사자의 독립적인 사후 평가는 아니다.

## 보고서 검증도 엔지니어링 작업이다

재단이 연결한 앞선 보안팀 운영 글에서 AI의 역할은 보고서 검증과 분류다. 같은 근본 원인을 건드리는 보고를 묶고 주장한 영향이 실제로 성립하는지 살핀다. 재현 환경은 CI와 맞추며 메모리·정의되지 않은 동작을 검사하는 도구를 사용한다. 특정 맞춤 빌드의 충돌만으로 일반 배포 환경의 취약점을 단정하지 않는다.

최종 판정과 심각도 결정, 패치 작성이나 검토는 사람이 맡는다. 보고가 취약점으로 분류되지 않아도 실제 버그라면 견고성을 높이는 작업으로 넘길 수 있다. 제출자에게 필요한 것도 긴 설명보다 최소 재현 코드와 실행 환경, 공격자가 통제하는 입력과 얻을 수 있는 영향이다. 모델의 출력을 그대로 보내는 일은 이 검증 비용을 없애지 못한다.

## 참고 자료

[Today's PHP Security Release, and How We're Strengthening PHP Security](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)

[How the PHP Security Team Handles Your Reports — Alexandre Daubois, 2026-10-14](https://thephp.foundation/blog/2026/10/14/how-the-php-security-team-handles-your-reports/)
