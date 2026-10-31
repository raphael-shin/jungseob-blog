---
layout: post
title: "AI가 쓰고 누가 검증하나, Lean의 창시자 Leo de Moura가 Ben Lorica에게 말한 형식 검증이 코드 시대의 신뢰 병목을 푸는 방식을 Anthropic과 arXiv와 Lean 자료로 대조한 정리"
date: "2026-10-31 21:19:03 +0900"
created: "2026-10-31T21:19:03+09:00"
source: "https://youtu.be/r913hk9CYw0"
source_title: "AI Writes. Who Verifies?"
author: jungseob
source_author: "Gradient Flow (Ben Lorica, Leo de Moura)"
source_published: "2026-10-29"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Gradient Flow가 2026년 10월 29일에 올린 54분 대담을 정리한다. Lean의 창시자이자 AWS 자동 추론 그룹의 Leo de Moura가 Ben Lorica에게 테스트는 버그의 존재만 보이고 부재는 못 보인다는 점, AI가 모델링과 증명 비용을 낮춘 자동 형식화, 사양 중심으로 옮겨 가는 소프트웨어 공학, 증명 검사기를 여럿 두는 신뢰 구조, 검증된 소프트웨어 스택과 검증 주장을 의심하는 질문, 에이전트 샌드박스와 정책 검증, 수학과 물리와 금융과 법으로의 확산을 말한다. 대담의 사건과 수치를 Anthropic의 페르마 정리 형식화, arXiv의 Navier-Stokes 번역 불일치 논문, Boris Cherny의 게시물, lean-zip 저장소로 대조한다."
image:
  path: "https://i.ytimg.com/vi/r913hk9CYw0/maxresdefault.jpg"
  alt: "Gradient Flow의 Leo de Moura와 Ben Lorica 대담 썸네일"
tags:
  - knowledge
  - blog
  - AI
  - 형식검증
  - Lean
---

## TL;DR

- de Moura의 출발점은 테스트가 버그의 존재는 보이지만 부재는 보이지 못한다는 것이다. Lean에서는 코드가 만족해야 할 성질을 적고 AI가 구현과 증명을 함께 쓰며, 증명은 작은 커널이 기계로 검사하므로 사람과 AI 사이의 신뢰 병목을 푼다.
- 바뀐 것은 Lean이 아니라 AI다. 프런티어 모델이 어떤 언어의 코드든 Lean 모델로 옮기는 자동 형식화를 하게 되면서 진입 비용이 크게 줄었고, Anthropic의 Claude는 11일에 1,300만 줄의 Lean으로 페르마의 마지막 정리를 증명했다.
- 남는 위험은 모델이 코드와 같은지, 적은 성질이 원하는 것인지다. Navier-Stokes 증명에서 자연어 증명과 Lean 증명의 불일치(미분 4차 대 5차)가 실제로 지적되었고, 그는 이를 도구 문제로 보지만 독립 논문은 Lean 검증이 자연어 증명의 정확성을 보증하지 않는다고 주장한다.
- 소프트웨어 공학의 무게는 코드에서 사양으로 옮겨 가고, 사양서와 성질이 소스 관리의 핵심 자산이 된다. 그가 말하는 검증 주장을 의심하는 질문은 어떤 성질을, 어떤 사양에 대해, 어떤 검사기로, 얼마나 작은 신뢰 코드로 검증했느냐이다.
- 이는 Lean 창시자이자 AWS 임직원의 입장이다. 수치 일부(5,000만 줄, 검증된 검사기 두 개)와 Tao 프로젝트 일화는 확인하지 못했고 Boris의 게시물은 대담과 대상이 다르다.

## 대담에 대하여

Gradient Flow가 2026년 10월 29일에 올린 54분 대담으로, The Data Exchange의 Ben Lorica가 사회를 보고 Lean의 창시자 Leo de Moura가 답한다. 진행자는 그를 AWS 자동 추론 그룹의 VP이자 Distinguished Scientist, 그리고 Lean FRO(집중 연구 조직)의 수석 아키텍트로 소개하며 에피소드 페이지도 같다. 반면 3월 미네소타 강연 슬라이드에는 직함이 Senior Principal Applied Scientist로 적혀 있어 이 노트는 직함을 진행자의 소개로 옮겼다. 영어 자동자막 전체를 읽었다. 화자 표시는 없지만 질문자와 답변자가 분명하다. 자막의 고유명사 오기가 많아 문맥으로 바로잡았다(예: IMES는 Aeneas, "vessel blueprint"는 Verso Blueprint, "fislib"는 Physlib, "entropic"은 Anthropic, "dog woods"는 Dogwood). 이 블로그의 [Dogwood 노트](https://raphael-shin.github.io/jungseob-blog/posts/opensource-introducing-dogwood-runtime-verification-for-ai-agents-22ab8488/), [Lauren Tan 신뢰 곡선 노트](https://raphael-shin.github.io/jungseob-blog/posts/tan-trust-curve-verification-agents/), [Kapur·Osmani 노트](https://raphael-shin.github.io/jungseob-blog/posts/kapur-osmani-who-verifies-the-software-factory/)가 같은 질문의 다른 답이다.

## 테스트와 증명, 무엇이 달라지나

Lorica는 생성이 쉬워진 시대의 병목이 검증이라는 전제로 시작해, 코드 리뷰와 QA와 테스트에 익숙한 청취자에게 형식 검증이 더하는 것을 묻는다. de Moura의 답은 Lean이 프로그래밍 언어이자 증명 보조기라는 데서 출발한다. 같은 언어로 코드를 쓰고 그 코드가 가져야 할 성질도 적으며 증명은 비형식적 서술이 아니라 Lean으로 쓰고 기계가 검사한다. 결과를 믿으려면 Lean 전체가 아니라 증명을 검사하는 커널만 믿으면 된다. 증명은 데이터이므로 내보내 다른 검사기로 다시 확인할 수 있다.

예전에는 소프트웨어를 구현하고 속성 기반 테스트 같은 틀을 붙였다. 테스트는 버그를 찾는 데는 좋지만 버그가 없음을 보이지는 못한다. 지금은 성질을 먼저 적고 AI에게 그것을 만족하는 코드와 Lean 증명을 쓰게 한 뒤 기계가 검사한다. 그는 Kim Morrison이 zlib 압축 라이브러리를 Lean으로 옮기고 "압축했다가 풀면 원본이 그대로 나온다"는 성질을 증명한 실험을 든다. 테스트를 AI로 많이 만들면 되지 않느냐는 반문에는 두 기술이 충돌하지 않고 보완한다고 답한다. 테스트는 이해와 확신을 쌓는 출발점이고 틀린 명제는 아무리 토큰을 태워도 증명할 수 없으니 먼저 테스트로 걸러야 한다. 증명은 시험한 입력만이 아니라 모든 입력에 성립함을 보인다. 진행자는 형식 검증이 ImageNet 순간을 맞았다고 말한다. de Moura가 드는 변화의 이유는 비용이다. 예전에는 사람이 손으로 증명하느라 너무 오래 걸려 인기가 없었는데 AI가 그 비용을 크게 낮췄다.

AI가 코드를 최적화할 때 증명이 가드레일이 된다는 점도 말한다. 이해하기 어려운 최적화라도 같은 것을 계산한다는 증명이 있으면 받아들일 수 있다.

## 자동 형식화와 규모

Rust로 쓴 코드는 어떻게 하느냐는 질문에 두 길이 나온다. 하나는 Rust를 Lean으로 옮겨 검증하는 도구 Aeneas이고 Microsoft의 암호 라이브러리 SymCrypt 팀이 쓴다. 다른 하나는 AI에게 어떤 언어의 코드든 읽고 Lean 모델을 만들게 하는 것이다. 수학에서 자동 형식화라 부르던 일이며 그는 1년 전이었다면 공상과학이라 했을 것이라고 한다. Lean 쪽이 한 일은 없고 프런티어 모델이 이를 할 수 있게 되었을 뿐이며 Lean 입장에서 달라진 것은 확장성이다.

수치로 그는 사람이 10년에 걸쳐 쓴 수학 라이브러리 Mathlib이 250만 줄이고 AI가 쓴 증명은 5,000만 줄에 이르며 Anthropic이 쓴 페르마 마지막 정리 증명이 1,300만 줄이라고 말한다. 마지막 수치는 확인된다. Anthropic은 Claude가 11일 동안 대체로 자율적으로 작업해 1,300만 줄의 Lean을 쓰고 중간 정리 2만 9,500개를 증명했으며 Mathlib의 5배를 넘는 크기라고 밝혔다. 5,000만 줄이라는 수치는 이 노트가 출처를 찾지 못했다.

주의할 점도 같이 말한다. AI가 만든 모델이 코드에 충실한가가 핵심 질문이다. 일부는 Lean 모델과 실제 프로그램에 같은 입력을 넣어 비교하는 차분 테스트를 쓰고 그렇게 버그가 발견된다. 그는 Claude Code 개발자 Boris가 Claude에게 Lean으로 버그를 찾으라고 시켜 모델을 만들고 성질을 증명하려다 못 해서 버그를 찾고 PR을 올렸으며 병합된 것이 진짜 버그였고 Boris가 Lean을 모른다고 했다는 일화를 소개한다. 버그 찾기에는 이것으로 충분하지만 버그가 없다고 말하려면 모델이 코드의 정확한 모델인지를 보고 동기를 유지해야 한다. 앞으로 몇 달에서 몇 년 사이 사람들이 코드보다 사양과 모델과 성질에 집중하리라는 것이 그의 예측이다.

## Navier-Stokes와 편집 가능한 증명

Lorica는 최근 Navier-Stokes 증명에서도 번역의 충실성 문제가 있었다고 묻는다. de Moura는 이 문제의 진술은 OpenAI가 모델을 돌리기 전부터 전문가가 다듬은 Lean 진술이 있었기에 진술 자체의 의심은 없었다고 말한다. 논란은 OpenAI가 자연어로 쓴 비형식 증명과 Lean의 형식 증명을 함께 냈는데 둘 사이에 불일치가 있다는 점이고 4차 미분을 가정하느냐 5차를 가정하느냐의 수준이라고 한다. 수학자에게는 중요하지만 차이가 그만큼 미묘하다는 설명이다. 그는 자연어와 Lean을 문서 하나에서 맞춰 보는 Verso Blueprint를 쓰면 이런 불일치가 생기지 않았을 것이라 자신하며 도구 개선의 문제라고 본다.

또 형식 증명이 정적인 객체라는 오해를 바로잡는다. 코드를 리팩터링하듯 증명도 단순화할 수 있다. 페르마 마지막 정리 증명을 절반으로 줄인 그룹이 이미 있고 기계 검사를 유지한 채 조작하고 탐색하고 질문할 수 있다고 한다.

## 사양 중심의 소프트웨어 공학

진행자가 정리한 두 틈은 요구 사항 틈(원하는 것과 적을 수 있는 것의 차이)과 모델 틈(시험 조건이 운영을 대표하는지), 그리고 Lean 커널에 대한 신뢰다. 커널은 사용자가 우리를 믿을 필요가 없다고 답한다. 서로 다른 구현의 검사기가 있고 증명을 여러 검사기로 확인할 수 있으며 검사기끼리 성능과 정확성을 겨루는 Lean Kernel Arena(arena.lean-lang.org)가 있다. 구현 언어도 Rust, Haskell 등 다양하고 Morrison이 TeX로 만든 것까지 있다고 한다. 검증된 검사기가 둘이고 셋째가 곧 나온다는 말은 이 노트가 확인하지 못했다. 아레나 페이지는 공식 구현과 외부 구현을 시험 모음으로 채점하는 구조를 보이며 일부 외부 검사기가 일관성 증명을 제공한다고 적는다.

사양서가 핵심 자산이 된다는 이야기가 이어진다. 지금은 설계 문서와 구현이 어긋나도 사람이 맞춰야 하지만 문서가 형식이면 도구가 구현과 설계의 일치를 검사한다. 고객이 원하는 X와 명세 X′의 차이는 계속 다듬는 과정이고 변경된 모델에 코드가 맞는지 도구가 알려 준다. 진행자는 매 버전을 AI가 처음부터 다시 쓰고 사람이 소유한 사양이 왕관의 보석이 된다고 요약하고 요구 문서(PRD)가 소스 관리의 대상이 된다는 데 두 사람이 동의한다. 컴퓨터과학 교육은 완전히 바뀌지 않고 적응한다고 그는 말한다. 형식 검증이 필수 과목이 아니던 대학이 많았고 이제 비중이 커지겠지만 저수준 언어를 아는 사람도 계속 필요하다. 형식 모델을 쓰는 일도 더 높은 수준의 코딩이라고 본다.

## 검증된 스택과 검증 주장을 의심하는 질문

그가 말하는 검증된 스택은 버그가 위기를 일으키는 핵심 소프트웨어, 곧 운영체제, 컴파일러, TCP/IP 같은 통신 계층이다. 비디오 게임은 버그가 짜증 나는 정도에 그친다. 이 부품들의 사양을 전문가가 쓰고 코드가 사양과 맞는지 검증해 가자는 방향이 투자할 만하다고 한다.

Fortune 500의 CTO에게 "우리 소프트웨어는 형식 검증됐다"고 파는 공급자를 어떻게 의심하느냐는 질문에, 그의 답은 사양을 보여 달라는 것이다. 어떤 성질을 검증했는가가 핵심이다. 아무 주장도 하지 않는 성질을 증명해도 "검증됨"이라 부를 수 있다. 어떤 증명 검사기를 썼는지, 신뢰해야 하는 코드(trusted code base)가 얼마나 작은지도 묻는다. 실제 환경과 비슷한 조건에서 돌려 봤는지도 근거를 더한다.

## 에이전트의 검증

장기 실행 에이전트에서의 검증은 믿을 만한 샌드박스에서 시작한다. 최근 몇 주 에이전트가 샌드박스를 탈출했다는 주장이 많았다며 검증된 스택의 일부로 샌드박스의 사양과 구현이 맞는다는 증명을 원한다. 에이전트 행동 정책을 쓰고 그 정책을 집행하는 코드를 형식 검증하는 것도 같은 맥락이다. 다른 에이전트가 검증하면 믿을 수 있느냐는 질문에는 에이전트가 커널이나 실행 환경의 결함을 이용할 가능성이 정당한 우려이고 그래서 여러 커널을 두며 증명이 독립 구현된 검증된 검사기 여러 개에 받아들여져야 한다고 답한다. 에이전트가 취약점을 찾는 데 극도로 능하기 때문에 심각한 문제라는 것이다. AWS의 AgentCore와 Dogwood 팀이 이미 Lean을 쓴다고 한다.

장기 실행 에이전트의 요구 사항은 어떻게 적느냐는 반문에는 AI가 첫 모델을 쓰고 사람이 반복해서 다듬는다고 한다. 에이전트 시스템은 부품과 통신 프로토콜이 얽힌 복잡계이므로 프로토콜의 정확성을 AI가 초안으로 형식화해 주는 것이 출발점이다. 학습 곡선이 높았던 것이 AI로 시작 비용이 낮아져 즉시 가치가 나온다는 점이 그의 낙관의 근거다. 이후 사람들이 Lean 모델을 직접 읽을 수 있게 배울 것이고 쓰지는 않더라도 에이전트가 만든 모델이 정확한지 에이전트와 논의하려 한다고 본다.

## 수학, 물리, 그리고 그 너머

수학은 가장 앞선 사례다. Mathlib은 정의가 정확한 수학자들이 만든 것이고 큰 규모로 일하는 데 Lean이 도움이 된다는 것이 수학 공동체에게 큰 성과였다. 그는 2024년 Terence Tao가 프로젝트를 작은 조각으로 나눠 건축가처럼 설계하고 만난 적 없는 많은 사람이 빈칸을 채웠다고 소개한다. Tao는 언젠가 AI 에이전트가 이 빈칸을 채울 것이라 했지만 이렇게 빨리 오리라고는 아무도 상상하지 못했다. 6개월 전만 해도 Lean 개발자와 Mathlib 유지보수자에게 말하면 믿지 않았을 것이다. Lean 개발자들도 이제 AI로 Lean을 구현한다.

물리는 Physlib(자막의 fislib)이라는 라이브러리가 형식화하고 있고 몇 달 전 한 중요한 물리 논문의 버그가 형식화 시도로 발견되었다. 물리는 현실의 모델이라 항상 부정확하다는 어려움이 있지만 이론 분야는 곧 흔들릴 수 있다고 한다. Navier-Stokes 이후 수학자 친구들의 반응은 흥분, 분노, 두려움이 섞여 있고 학생들은 자신의 미래를 걱정한다. 소프트웨어처럼 직업은 달라져도 사라지지는 않으리라는 것이 그의 희망이다.

진행자는 누가 필즈상을 받느냐가 "지능이 높은 사람"에서 "컴퓨트가 많은 사람"으로 바뀔지 묻는다. 그는 자신의 초능력이 고통을 견디는 힘이었는데 그 고통이 사라져 능력의 쓸모가 줄었다고 말한다. 대신 더 빨리 더 많이 이룰 수 있고 다른 기술 조합을 가진 사람이 기술을 더 잘 활용할 수 있다. 토큰 접근이 쟁점이 되겠지만 제임스 웹 망원경처럼 제안서를 써서 접근권을 얻는 방식이 되리라 본다.

금융은 알고리즘이 많아 관심이 있지만 비공개라 공개 라이브러리를 만들기 어렵고 화학과 생물 라이브러리도 시도되고 있다. 수학이 단연 앞서고 물리와 컴퓨터과학 라이브러리가 따라잡는 중이며 금융과 화학은 새 시도 단계다. 논문이 얼마나 엄밀한가가 형식 라이브러리를 만들기 얼마나 어려운지의 단서라고 한다. 회계(GAAP, 세법)와 법은 주관성이 있지만 민사 절차처럼 프로그램에 가까워 형식화할 부분이 있다는 이야기로 끝난다.

## 대조해서 확인한 점

Anthropic의 글은 Claude가 11일 동안 대체로 자율적으로 첫 완전 컴퓨터 검증 페르마 마지막 정리 증명을 썼고 1,300만 줄의 Lean과 2만 9,500개의 중간 정리가 있으며 Mathlib의 5배가 넘는다고 밝힌다. 이는 Mathlib이 약 250만 줄이라는 de Moura의 서술과 앞뒤가 맞는다. Kevin Buzzard가 이 작업을 "extraordinary"하다고 평했다고도 적혀 있다.

Navier-Stokes는 2026년 10월 6일 arXiv에 올라온 Bastounis, Circelli, Hansen의 논문 「Navier-Stokes lost in translation」이 대담의 불일치를 상세히 다룬다. 이 논문은 자연어 논문의 식 (8.19)가 m+4 미분을 요구하는데 OpenAI의 Lean 코드는 m+5 미분을 요구해 더 약한 추정이 되며 비슷한 불일치가 Lean 코드 곳곳에서 반복된다고 보인다. 이 논문의 결론은 de Moura보다 강하다. Lean 검증이 자연어 논증의 정확성을 보증하지 않으며 충실한 번역은 원리상 어렵다는 것이다. 그는 이를 도구 문제로 보지만 이 논문은 번역 문제 자체의 한계로 본다. 논문은 아직 심사를 거치지 않은 프리프린트이므로 두 입장 어느 쪽도 확정된 것이 아니다. 이 블로그의 [Altman Cheeky Pint 노트](https://raphael-shin.github.io/jungseob-blog/posts/altman-cheeky-pint-against-single-superintelligence/)가 같은 증명을 OpenAI 쪽에서 다뤘다.

Boris Cherny의 일화는 대상이 다르다. 그의 9월 22일 게시물은 Opus 5.5로 Claude Agent SDK를 Lean으로 형식 검증했고 짧은 프롬프트 몇 개로 버그와 경쟁 상태를 고치는 PR 16개가 나왔다고 쓴다. TLA+도 잘 되고 둘 다 잘 모르지만 Claude가 둘에 능하다고 덧붙인다. de Moura가 말한 "Claude Code"가 아니라 Agent SDK이고 이 노트는 어느 쪽이 맞는지 판단하지 않고 게시물을 따랐다. lean-zip 저장소는 순수 Lean DEFLATE 인코더와 디코더를 담고 "압축은 어떤 입력에서도 데이터를 손상시키지 않는다"는 정리를 커널이 인증한다고 쓴다. de Moura의 3월 강연 슬라이드도 일반 목적 AI가 zlib를 Lean으로 바꾸고 테스트를 통과한 뒤 코드가 맞음을 증명했다고 소개한다. Aeneas는 Microsoft 연구 블로그가 SymCrypt를 Rust, Aeneas, Lean으로 검증한다고 설명해 확인된다. Physlib에서 Lean이 2006년 문헌의 오류를 찾아낸 사례는 New Scientist와 arXiv 논문(2603.08139)에서 확인된다.

확인하지 못한 것은 AI가 쓴 증명이 5,000만 줄에 이른다는 수치, 검증된 검사기가 둘이고 셋째가 곧 나온다는 말, Tao의 2024년 프로젝트 일화, Navier-Stokes의 Lean 진술이 이전부터 전문가가 다듬은 것이라는 서술, 금융 분야 시도들이다. Verso Blueprint는 Lean FRO가 개발하는 도구로 확인되지만 "이것을 썼다면 불일치가 없었다"는 주장은 de Moura의 자신일 뿐 검증되지 않았다.

## 읽을 때 유의할 점

첫째, 화자는 Lean의 창시자이자 AWS 임직원이다. 형식 검증이 중요하다는 결론이 자신이 만든 도구와 소속 회사의 방향과 맞닿아 있다. 둘째, "모델이 충실한가"와 "사양이 원하는 것인가"라는 두 틈은 Lean이 메우지 못한다. 그는 이를 인정하면서도 도구와 반복으로 줄어든다고 낙관하고 독립 논문은 더 비관적이다. 셋째, 대담은 54분의 대화라서 비용과 시간, 실패 사례, 적용 한계(상태가 크고 환경과 얽힌 시스템)에 대한 수치가 거의 없다. 넷째, 자막 오기를 문맥으로 고쳤고 읽지 못한 부분이 있을 수 있다. 다섯째, Navier-Stokes 논쟁은 진행 중이므로 이 노트는 어느 쪽도 옳다고 판단하지 않는다.

가져갈 질문은 선명하다. 우리가 "검증됐다"고 부르는 것에서 어떤 성질이 어떤 사양에 대해 증명되었는가, AI가 만든 모델이 코드와 같다는 점을 무엇으로 확인하는가, 사양서와 성질을 소스 관리의 일급 자산으로 다루는가, 핵심 스택에서 사양을 가장 먼저 형식화할 부분은 어디인가.

## 참고 자료

[Gradient Flow: AI Writes. Who Verifies? (YouTube, 2026-10-29)](https://youtu.be/r913hk9CYw0): 영어 자동자막 전체(54분)를 읽고 정리했다.

[The Data Exchange: Leo de Moura on Formal Proofs, AI Agents, and the End of "Trust Me" Code](https://thedataexchange.media/leo-de-moura-lean-aws): 에피소드 설명과 인물 소개를 읽었다.

[Anthropic: Formalizing Fermat's Last Theorem](https://anthropic.com/research/formalizing-fermats-last-theorem): 11일, 1,300만 줄, 중간 정리 2만 9,500개, Mathlib의 5배 이상을 읽었다.

[Bastounis, Circelli, Hansen: Navier-Stokes lost in translation (arXiv:2610.08144, 2026-10-06)](https://arxiv.org/abs/2610.08144): m+4 대 m+5 미분 불일치와 결론을 읽었다.

[Boris Cherny의 X 게시물 (2026-09-22)](https://x.com/bcherny/status/2102543349102338309): Claude Agent SDK를 Lean으로 검증해 PR 16개를 얻었다는 내용을 읽었다.

[kim-em/lean-zip (GitHub)](https://github.com/kim-em/lean-zip): 검증된 DEFLATE 구현과 왕복 정리를 읽었다.

[Leo de Moura: Lean, Machine-Checked Mathematics and Verified Programming (2026-03-30)](https://leodemoura.github.io/static/minnesota2026/): zlib 변환 일화와 당시 직함을 읽었다.

[Lean Kernel Arena](https://arena.lean-lang.org/): 증명 검사기를 시험 모음으로 채점하는 구조를 읽었다.

[Microsoft Research: Verifying Rust cryptography in SymCrypt](https://www.microsoft.com/en-us/research/blog/verifying-rust-cryptography-in-symcrypt-from-standards-to-code/): Aeneas와 Lean의 사용을 검색 발췌로 확인했다.

[New Scientist: Computer finds flaw in major physics paper for first time](https://newscientist.com/article/2520546-computer-finds-flaw-in-major-physics-paper-for-first-time): Lean이 물리 논문의 오류를 찾은 사례를 검색 발췌로 확인했다.

[leanprover/verso-blueprint (GitHub)](https://github.com/leanprover/verso-blueprint): 자연어 설명과 Lean 코드를 잇는 Blueprint 문서 도구의 존재를 확인했다.
