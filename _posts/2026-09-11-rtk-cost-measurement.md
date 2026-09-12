---
layout: post
title: 줄어든 출력과 줄어든 청구서는 다르다 - RTK 비용 실험의 측정 단위
date: '2026-09-11'
last_modified_at: '2026-09-12T12:17:45+09:00'
author: jungseob
categories:
- 지식 노트
tags:
- ai-agents
- engineering
description: RTK 실험으로 출력 압축률과 성공 작업당 비용을 구분한다.
source: https://quesma.com/blog/does-rtk-make-ai-coding-cheaper/
source_title: RTK reports huge token savings, but our cost benchmarks disagree
source_author: Bartosz Kotrys, Jacek Migdal (Quesma)
source_published: '2026-09-11'
published: true
render_with_liquid: false
image:
  path: https://quesma.com/_astro/rtk-terminal-bench-verdict-wide.Cx7zyGD2.png
  alt: 원문 대표 이미지 · RTK reports huge token savings, but our cost benchmarks disagree
---

## TL;DR

- RTK의 출력 절감 카운터와 실제 청구 비용은 다른 지표다. 줄어든 출력만으로 후속 턴과 실패 비용을 설명할 수 없다.
- Quesma 실험의 성공당 비용은 Fable에서 3% 감소하고 DeepSeek에서 7% 증가했다. 작업별 평균에서는 Fable의 뚜렷한 절감이 없었다.
- 압축률·완료율·성공당 비용·작업별 분포를 함께 읽어야 한다. 실험에 사용한 버전과 이후 수정도 구분해야 한다.

## Source

[RTK reports huge token savings, but our cost benchmarks disagree](https://quesma.com/blog/does-rtk-make-ai-coding-cheaper/)

[RTK의 절감량 측정 설명](https://github.com/rtk-ai/rtk/blob/develop/docs/guide/resources/savings-explained.md)

## Knowledge

### 절감 카운터가 실제로 세는 것

RTK는 에이전트가 읽을 터미널 출력을 압축한다. Quesma는 `head -1` 요청을 전체 파일 크기와 비교해 절감량을 부풀린 사례를 발견했다. RTK의 설명 문서에 따르면 `rtk gain`은 출력 바이트 차이를 4로 나눈 추정치다. 실제 청구 토큰을 직접 집계한 결과로 읽을 수 없다.

이 차이를 이해하기 위한 가상 예를 들어보자. 원래 명령이 한 줄만 반환하는데 전체 파일과 한 줄의 차이를 절감으로 세면 사용하지 않을 출력까지 절약한 셈이 된다. 비교 기준은 도구를 끈 상태에서 같은 명령이 반환할 내용이어야 한다. 그렇지 않으면 카운터가 커졌다는 사실과 모델이 덜 읽었다는 사실이 연결되지 않는다. 기준선부터 확인해야 하는 이유다.

### 총액과 성공당 비용이 답하는 질문

실험은 Claude Code의 Fable 5.0과 OpenCode의 DeepSeek V4 Pro 0813을 비교했다. Fable은 거부가 발생한 보안 작업 4개를 제외한 85개, DeepSeek은 89개 작업에서 RTK 유무마다 다섯 번씩 실행해 총 1,740회였다. 전체 지출을 성공 횟수로 나눈 비용은 각각 3% 감소와 7% 증가였다. 작업별 평균에서는 Fable의 명확한 절감이 없고 DeepSeek은 17% 증가했다. Fable 총액의 이익은 특정 작업에 크게 의존했다.

집계 방식의 차이는 간단한 계산으로 확인할 수 있다. 가상의 두 작업 비용이 100원과 1원에서 90원과 2원으로 바뀌면 총액은 101원에서 92원으로 줄어든다. 그러나 작업별 변화율은 −10%와 +100%라 평균은 +45%다. 둘 중 하나가 계산 오류인 것은 아니다. 실제 지출을 묻는지 여러 작업에서 일관되게 효과가 나는지를 묻는지에 따라 필요한 지표가 달라진다.

### 짧아진 턴이 늘어나면 전체 비용이 오른다

DeepSeek은 턴당 입력이 평균 7% 줄었지만 턴 수는 18% 늘었다. 캐시로 할인된 입력을 줄이는 효과와 추가 출력·추론의 비용도 다르다. RTK 0.45.0에서 직접 `find`를 쓰라는 오류에 따라 재시도해도 플러그인이 다시 `rtk find`로 바꾸어 반복이 생겼다. 이 버그는 0.46.0에서 수정됐다. 따라서 이 결과를 모든 후속 버전의 성능으로 단정할 수는 없다.

도입 실험에서는 작업 시작부터 종료까지의 비용을 묶어 비교하는 편이 유용하다. 예를 들어 실패한 첫 실행을 제외하고 성공한 재시도만 세면 복구 비용이 숨는다. 반대로 실패를 전부 포함하더라도 완료율이 달라졌다면 비용만으로 어느 구성이 나은지 정할 수 없다. 같은 완료 기준과 작업 묶음을 사용하고 모델·도구 버전을 고정해야 해석이 가능하다. 이는 특정 제품에 대한 추가 실측이 아니라 비용 평가를 설계하는 방법이다.


## 더 생각해보기

- 현재 최적화 지표는 실제 청구 비용의 어느 부분을 측정하는가?
- 전체 절감액이 특정 작업 하나에 의존해도 도입할 이유가 있는가?
