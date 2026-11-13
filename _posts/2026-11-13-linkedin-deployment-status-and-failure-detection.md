---
layout: post
title: LinkedIn이 배포 상태와 실패 판정을 묶은 방법
date: 2026-11-13 23:04:36 +0900
created: '2026-11-13T23:04:36+09:00'
source: https://www.linkedin.com/blog/engineering/infrastructure/how-we-scale-deployments-with-a-custom-gitops-engine
source_title: How we scale deployments with a custom GitOps engine
author: jungseob
source_author: Ramesh G. Iyer
source_published: '2026-11-02'
type: blog-knowledge-note
published: true
render_with_liquid: false
categories:
- 지식 노트
description: 배포별 상태를 추적한다. 실제 버전을 확인한다. 실패를 빨리 판정한다. 성과의 한계도 구분한다.
tags:
- knowledge
- blog
- web
- software-engineering
image:
  path: https://media.licdn.com/dms/image/v2/D4D08AQE2H6j9Tz9gUQ/croft-frontend-shrinkToFit1920/B4DaGcIQVNIMAM-/0/1793620772616?e=2147483647&v=beta&t=hLBwehcD8c9R7-my3wX_yw79VdbyLd-5lkMZvQ5ZszE
  alt: LinkedIn 자체 배포 엔진 소개 이미지
---

## TL;DR

- 정상 표시뿐 아니라 배포 식별자와 실제 버전을 확인한다.
- 배포별 실행 단위에서 검사부터 완료 판정까지 추적한다.

## 정상 상태가 이번 배포의 성공인지는 별개다

LinkedIn의 기존 배포 시스템에서는 Argo CD의 동기화·건강 상태만으로 이번 배포의 성공을 판정하기 어려웠다. 이전 배포의 상태를 새 배포의 결과로 오인할 수 있었다. 팀은 배포 식별자를 리소스에 붙여 상태와 연결했다. 정상 표시와 별개로 요청한 버전이 실제 적용된 버전과 같은지도 확인해야 했다. 오래된 저장소 캐시가 의도하지 않은 버전을 선택하는 경우가 있었기 때문이다.

자체 엔진에서는 배포별 임시 Pod가 사전 검사부터 적용, 완료 판정까지 맡는다. Pod는 쿠버네티스에서 프로그램을 실행하는 단위다. 서로 다른 배포가 컨트롤러 상태를 공유하지 않는다. 현재 객체와 이전 배포 명세, 새 명세를 비교해 예상 밖 변경을 찾는다. 해소되지 않은 변경이 있으면 실패 처리한다. 적용 이후에도 객체 상태가 목표에 도달하거나 제한 시간이 끝날 때까지 추적한다.

LinkedIn의 전년 동월 비교에서 실패한 배포의 시작부터 종료까지 걸린 시간 중앙값은 16.1분에서 2.45분으로 줄었다. 측정 시간에는 배포 중 일시 중지도 포함됐다. 성공한 배포의 중앙값은 비슷했다. 배포 조정 계층의 신뢰성과 오류 분류도 함께 개선됐으므로 전체 성과를 새 엔진에만 돌릴 수는 없다. Argo CD는 클러스터 부가 기능과 시스템 서비스 배포에 계속 사용한다.

## 참고 자료

[LinkedIn의 자체 배포 엔진 설계](https://www.linkedin.com/blog/engineering/infrastructure/how-we-scale-deployments-with-a-custom-gitops-engine)
