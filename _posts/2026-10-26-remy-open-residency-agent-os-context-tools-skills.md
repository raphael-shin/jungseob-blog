---
layout: post
title: "채팅에서 에이전트로 넘어가는 법, Remy Gaskell이 Open Residency에서 설명한 컨텍스트와 도구와 스킬 세 축의 개인 AI 운영체제를 Anthropic 문서와 대조한 정리"
date: "2026-10-26 14:24:14 +0900"
created: "2026-10-26T14:24:14+09:00"
source: "https://youtu.be/5p-sq8v3OXw"
source_title: "AI Agents: The Most Valuable Skill You Can Learn in 2026 (Full Course)"
author: jungseob
source_author: "Open Residency (진행: Mark, 출연: Remy Gaskell)"
source_published: "2026-07-22"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Open Residency 팟캐스트(2026년 7월 22일 공개, 2시간 24분)에서 Remy Gaskell이 채팅과 에이전트의 차이, 관찰 생각 행동 루프, 컨텍스트 파일과 CLAUDE.md, 메모리, MCP와 도구, 스킬의 점진적 공개, OS 폴더 구조, 팀 단위 스킬 소유 문제를 설명한 내용을 정리한다. Anthropic 문서로 CLAUDE.md 로딩과 스킬 구조, 컨텍스트 명령을 대조하고 ChatGPT 메모리 서술과 생산성 수치는 확인 범위를 밝힌다. 출연자가 플러그인과 플레이북을 판매한다는 이해관계도 적는다."
image:
  path: "https://i.ytimg.com/vi/5p-sq8v3OXw/maxresdefault.jpg"
  alt: "Open Residency Remy Gaskell AI 에이전트 풀코스 영상 썸네일"
tags:
  - knowledge
  - blog
  - AI
  - 에이전트
  - 클로드코드
---

## TL;DR

- Remy Gaskell은 AI 활용을 채팅(질문에서 답)과 에이전트(목표에서 결과)로 나누고, 에이전트 사용자는 하루 생산성이 5~10배라고 말한다. 이 수치는 본인과 주변의 경험이며 측정 자료는 제시되지 않았다.
- 에이전트는 관찰, 생각, 행동을 반복하는 루프이고, 이 루프를 돌리는 앱이 하네스(Claude Code, Codex 등)다. 사용자가 조정할 수 있는 축은 관찰 단계의 컨텍스트와 스킬, 생각 단계의 모델, 행동 단계의 도구 네 가지다.
- 핵심 설계는 새 직원을 온보딩하듯 컨텍스트 파일(마크다운), 도구(MCP 커넥터), 스킬(AI용 SOP)을 폴더에 쌓는 것이다. CLAUDE.md는 세션마다 자동으로 읽히고 스킬은 이름과 설명만 먼저 읽히는 점진적 공개 구조다.
- 한 번 작동한 과정을 스킬로 저장하고 여러 번 고쳐 쓰는 방식을 권한다. 팀에서 스킬을 누가 소유하고 어떻게 공유할지는 아직 깔끔한 해법이 없다고 인정한다.
- 이 노트는 영어 자동자막 전체(2시간 24분)를 읽고 Anthropic 문서와 대조했다. 출연자는 AI Onboard 플러그인과 플레이북을 판매하며 방송에 후원 광고가 섞여 있다.

## 영상에 대하여

Open Residency가 2026년 7월 22일에 올린 2시간 24분 11초 영상이다. 영어 자동생성 자막 전체를 읽었다. 출연자 Remy Gaskell은 스스로 비기술자라고 소개하는 광고 에이전시 출신 운영자이며 설명란은 그가 한 전자상거래 브랜드의 AI 에이전트 팀을 운영한다고 적는다. 진행자 Mark의 이름은 자막에서 확인했고 성은 확인하지 못했다. 설명란의 챕터는 채팅에서 에이전트로의 전환, 에이전트의 정의, 관찰 생각 행동 루프, 실시간 시연, 컨텍스트 파일과 CLAUDE.md, 자기 개선 메모리, MCP 커넥터, 보안과 권한, 도구 모음, 스킬, 에이전트 OS 폴더 구조, 팀의 미래, 속답으로 이어진다. 후원 낭독(WhisperFlow, Ketone-IQ, Momentous)은 제외했다. 출연자가 만든 Claude Code 플러그인 AI Onboard(출시 시 50% 할인)와 무료 PDF 플레이북 홍보 문구가 방송 안에 여러 번 나오며 이 노트는 그 판매 문구를 근거로 쓰지 않았다. 이 블로그의 [Katz 하네스 노트](https://raphael-shin.github.io/jungseob-blog/posts/katz-is-the-agent-harness-dead/)와 [Lauren Tan 신뢰 곡선 노트](https://raphael-shin.github.io/jungseob-blog/posts/tan-trust-curve-verification-agents/)가 같은 하네스와 스킬 논의를 개발자 쪽에서 다룬다.

## 채팅과 에이전트, 그리고 루프

Gaskell은 채팅이 질문에서 답으로 가는 일이고 에이전트는 목표에서 결과로 가는 일이라고 구분한다. 채팅은 뛰어난 컨설턴트에게 조언을 받는 것이고 에이전트는 그 사람을 사내에 고용해 일을 시키는 것이라는 비유다. 마케팅 예로, 이전에는 노션의 캠페인 브리프를 복사해 챗봇에 붙이고 결과를 이메일 도구와 광고 관리자에 손으로 옮겼지만 새 방식에서는 에이전트가 노션과 쇼피파이에서 정보를 가져와 광고 100개를 만들고 승인된 것만 Klaviyo와 광고 관리자에 입력한다. 사용자가 좋아하는 이메일 5개와 광고 10개만 고르면 된다는 설명이다.

에이전트 안에서는 관찰, 생각, 행동 세 단계가 목표가 달성될 때까지 반복된다. 인스타그램 상위 영상 분석 시연에서 에이전트는 컴퓨터에서 관련 파일을 찾고 60개 릴 데이터를 발견했으며 빠진 첫 3~5초 발언 정보를 얻으려고 하위 에이전트(자기 복제본)를 띄운 뒤 HTML 보고서를 냈다. 그는 이 일에 20~30번의 루프와 20분이 걸렸다고 추정한다. 루프를 돌리는 프로그램이 하네스이며 Claude Code, Codex, Manus, Perplexity Computer가 모두 하네스라고 설명한다. "에이전트를 만들었다"는 말은 대부분 새 하네스를 만든 것이 아니라 기존 하네스를 조정(tuning)한 것이다. 조정할 수 있는 축은 컨텍스트와 스킬(관찰), 모델(생각), 도구(행동)다. 그는 하네스를 자동차에 비유하며 운전의 기본(조향, 브레이크, 가속)을 알면 어느 차든 5분 안에 몰 수 있다고 말한다. 모델 이름은 몇 달이면 바뀌므로 원리에 집중하겠다고 한다.

## 컨텍스트: 마크다운 파일과 CLAUDE.md

온보딩 비유에서 에이전트는 능력은 크지만 사용자와 사업을 모르는 낯선 사람이다. 그래서 자기 소개, 사업 정보, 상품 목록, 이상적인 고객 프로필, 브랜드 목소리 같은 문서를 마크다운으로 준다. 마크다운은 제목, 굵게, 목록 정도의 서식을 가진 일반 텍스트이고 PDF보다 에이전트가 읽기 쉽고 토큰 비용도 적다. 문서는 챗봇에게 인터뷰를 시켜 음성 입력으로 3시간 답하는 방식으로 만들었다고 한다. 생성된 문서는 줄마다 읽어 확인해야 한다고 강조한다. 예를 들어 이상적인 고객 프로필에 잘못된 문제 지점이 들어가면 모든 마케팅 문구가 그 방향으로 쏠린다.

세션이 시작되면 폴더의 CLAUDE.md(다른 하네스에서는 AGENTS.md)가 자동으로 읽히므로 이 파일이 북극성이다. 다른 컨텍스트 파일은 CLAUDE.md가 가리킬 때 읽는다. 시연에서 빈 폴더의 Claude는 사용자가 누구인지 몰랐지만 CLAUDE.md를 넣자 즉시 알았다. 컨텍스트 창이 가득 차면 앞부분이 밀리고 환각이 늘어나는 현상을 그는 컨텍스트 썩음(context rot)이라 부른다. Claude Code의 `/context` 명령으로 창 사용량을 볼 수 있고 시연에서는 짧은 메시지 하나로 6%가 이미 쓰였다. 파일이 100개면 시작부터 20%가 찰 수 있으므로 간결하고 밀도 높게 유지하라고 한다. 파일에는 `@` 기호로 직접 태그하면 별도 탐색 없이 바로 읽힌다.

메모리는 별도의 `memory.md`로 둔다. 사용자가 교정하면(예: "웹사이트는 항상 다크 모드로") 에이전트가 이 파일에 규칙을 추가하고 이후 모든 작업 전에 읽는다. 하네스 자체 메모리가 최근 추가되었지만 사용자가 통제하지 못하는 블랙박스라는 이유로 파일 방식을 유지한다. 규칙이 쌓여 충돌하면 한 번씩 정리하면 된다는 입장이다. 그는 ChatGPT의 메모리도 보이지 않는 `memory.md`와 비슷하게 작동한다고 설명한다.

## 도구: MCP와 여섯 가지 추천

도구는 에이전트가 쓰는 계정과 컴퓨터다. MCP(Model Context Protocol)는 Claude가 Gmail, Slack, 노션 같은 외부 서비스와 대화하게 하는 번역기이며 Claude 데스크톱의 커스터마이즈 화면에서 한 번 로그인으로 커넥터를 붙일 수 있다. 기본 권한은 승인 필요이고 신뢰가 쌓이면 항상 허용으로 바꾼다. 그는 SaaS를 고를 때 MCP가 없으면 후보에서 뺀다고 하며 이제 앱 프런트엔드를 열지 않고 하루를 Claude 안에서 보낸다고 말한다. 보안은 위험과 생산성 이득을 저울질하는 개인 판단이고 불안하면 읽기 전용 권한으로 시작하라고 한다. 그의 가장 큰 걱정은 도구 오작동이 아니라 기업 고객이 민감한 데이터를 모델에 보내기 꺼리는 점이라고 덧붙인다.

추천하는 여섯 도구는 Apify(수천 개의 스크레이퍼 마켓), Firecrawl(웹페이지를 실제로 읽는 크롤러), Composio(수천 개 앱을 한 번에 잇는 연결자), Chrome DevTools(에이전트가 자기 작업을 확인하는 새 브라우저), Playwright(로그인된 기존 브라우저 제어), Higgsfield(이미지와 영상 생성 모델 모음)다. Composio를 찾은 계기는 Claude 서버가 한 시간 다운되었을 때 Codex로 갈아탔는데 Claude에 붙인 도구 50개가 따라오지 않았기 때문이라고 한다. Composio에서는 같은 Gmail 계정 세 개도 따로 연결한다고 말한다. 1Password 연결은 위험하다는 진행자의 지적에, 지문 인증이 뜬다고 답한다.

## 스킬: AI를 위한 SOP

스킬은 사람 직원에게 주는 SOP 문서와 같은 마크다운 파일이다. 제안서를 쓰며 15~20분 동안 취향을 설명하고 완성했다면, 그 과정을 스킬로 저장해 다음 세션에서 반복하지 않게 한다. 각 스킬은 폴더 안의 `SKILL.md`이고 이름, 설명, 내용 세 부분이다. 에이전트는 책장 책등에 적힌 이름과 설명만 세션 시작에 읽고 작업이 맞는 스킬을 찾으면 전체 내용을 불러온다. 그는 이를 점진적 공개라 부른다. 유튜브 제목 스킬의 예에서 단계는 주제 파악, Apify로 경쟁 채널 상위 영상 수집, 제목 구조 분석, 호기심 격차 같은 유형별 제목 생성이다.

만드는 방법은 목표 우선과 과정 우선이 있고 그의 스킬 90%는 과정 우선이다. 먼저 에이전트와 한 번 작업을 끝까지 하고 만족하면 "이 과정을 스킬로 만들어 달라"고 요청한다. Claude에 기본 내장된 skill-creator 스킬이 이를 만든다. 첫 판은 거의 완벽하지 않으며 그의 스킬 대부분은 5~10번째 판이라고 한다. 시연한 경쟁사 광고 분석 스킬은 광고 라이브러리 링크 하나로 54개 활성 광고(영상 37, 이미지 14)와 랜딩 페이지를 정리했고 Beehiiv MCP와 노션을 이용한 뉴스레터 제목 스킬은 시연 중 새로 만들었다. 한 스킬이 다른 스킬을 순서대로 부르는 오케스트레이터 스킬(유튜브 게시 워크플로)도 있다.

## 폴더 구조와 팀 문제

모든 작업은 하나의 OS 폴더에서 한다. 처음에는 마케팅, 광고 같은 좁은 폴더마다 에이전트를 열었지만 모델이 충분히 똑똑해져 OS 폴더 하나로 합쳤다고 한다. 하위에 사업별 폴더(교육, 컨설팅)와 일회성 프로젝트용 active 폴더가 있고 작업할 때 `@marketing`처럼 폴더를 태그한다. 전역 CLAUDE.md는 지주회사 수준의 원칙이고 프로젝트 폴더의 CLAUDE.md는 그 아래 개별 회사 수준이다. 건강 데이터 같은 개인 영역도 폴더 하나와 CLAUDE.md로 시작하라고 한다. 사람 이름을 붙인 마케팅 에이전트들은 결국 "폴더와 스킬과 예약 작업"이라고 정리한다. 예약 작업의 예는 매일 밤 Facebook 광고 보고서를 이메일로 받는 것이다.

두 번째 층으로 개인 OS가 확장이라면, 고객 지원 같은 기업 인프라 에이전트는 Hermes나 OpenClaw 같은 별도 프레임워크를 집의 Mac mini에 올려 돌린다고 설명한다. 원리는 같다. 팀 차원의 문제는 스킬의 소유와 공유다. 직원이 만든 스킬이 회사 자산인지, 퇴사하면 어떻게 되는지, 복사본이 어긋나지 않게 동기화하는 깔끔한 방법이 없다고 인정한다. AI 네이티브 기업을 만드는 길로는 외부 전문가가 부서를 인터뷰해 위에서 만드는 방식보다, 직원이 AI를 익혀 자기 일을 자동화하는 방식을 권한다. 진행자는 둘을 섞자고 한다. 비용은 월 약 1,000달러이고 구독 일부는 잊고 있었다고 말한다. 속답에서 처음 만들 스킬은 이메일 받은편지함 분류, 가장 과대평가된 도구는 앱 빌더(Lovable, Bolt), 가장 바뀐 스킬은 여러 페르소나가 토론하고 익명 동료 평가를 거쳐 의장이 판정하는 Claude Council이다.

## 대조해서 확인한 점

설정 서술은 Anthropic 문서와 맞는다. Claude Code 문서는 CLAUDE.md가 세션 시작마다 읽히고 저장소가 AGENTS.md를 쓰면 별도 절을 보라고 하며 파일이 로드되었는지 `/context`로 확인하라고 안내한다. Agent Skills 문서와 Anthropic 가이드는 YAML 머리말(이름과 설명)이 시스템 프롬프트에 항상 로드되고 본문은 필요할 때 읽는 3단계 점진적 공개를 설명한다. Composio 문서도 같은 도구의 여러 계정을 별칭으로 연결하는 다중 계정 모드를 지원한다.

틀리거나 확인하지 못한 서술도 있다. ChatGPT 메모리를 볼 수도 통제할 수도 없는 파일처럼 설명한 부분은 OpenAI 도움말과 어긋난다. 설정의 메모리 관리에서 저장된 기억을 보고 삭제할 수 있으며 메모리가 내부에서 마크다운 파일로 구현되었다는 설명도 확인하지 못했다. 생산성 5~10배(그는 7배를 중간값으로 쓴다), 구독 300달러 플랜에서 약 6,000달러어치 토큰 사용, "주요 AI 회사는 모두 적자", Anthropic의 사용량 한도가 줄고 있다는 서술은 근거가 제시되지 않았다. 적자 서술은 Reuters가 전한 Anthropic 3분기 조정 이익 흑자 보도와 어긋나는 점이 있다. 이 보도는 회사가 투자자에게 한 설명이고 영상은 그 직전 시점의 녹화다.

## 읽을 때 유의할 점

첫째, 출연자는 플러그인과 플레이북을 팔고 진행자는 방송에서 후원 광고를 낭독한다. 둘째, 시연은 정제된 사례이며 20분짜리 작업의 품질 평가나 실패 사례가 없다. 셋째, 읽기 전용에서 시작하라는 조언은 타당하지만 본인은 모든 도구에 전체 권한을 주고 8개월간 문제가 없었다고 말하는데, 이는 한 사람의 경험이다. 넷째, 문서와 스킬이 회사 자산이라는 점을 인정하면서도 접근 권한과 비밀 관리, 외부 데이터 유출 같은 위험은 다루지 않는다. 다섯째, 에이전트 권한과 책임의 문제가 큰 기업 환경에서 개인 OS 방식이 어디까지 확장되는지는 검증되지 않았다.

그래도 가져갈 질문은 선명하다. 내가 반복하는 일 가운데 한 번 끝까지 해 보고 스킬로 저장할 만한 것은 무엇인가, 컨텍스트 파일 중 비서가 매번 읽어야 하는 것과 필요할 때만 읽으면 되는 것은 어떻게 나뉘는가, 에이전트에 읽기 전용 권한으로 시작해 어떤 증거가 쌓이면 쓰기 권한을 줄 것인가, 팀이 스킬을 만들 때 소유와 버전 관리를 어디서 할 것인가.

## 참고 자료

[Open Residency: AI Agents, The Most Valuable Skill You Can Learn in 2026 (YouTube, 2026-07-22)](https://youtu.be/5p-sq8v3OXw): 영어 자동생성 자막 전체(2시간 24분)를 읽고 정리했다. 광고 낭독은 제외했다.

[Claude Code 문서: Memory](https://code.claude.com/docs/en/memory): CLAUDE.md가 세션마다 읽히고 `/context`로 확인한다는 서술을 검색 발췌로 확인했다.

[Claude Code 문서: Context window](https://code.claude.com/docs/en/context-window): `/context`가 실제 사용량을 보여 준다는 서술을 검색 발췌로 확인했다.

[Anthropic: Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): 스킬이 SKILL.md를 가진 디렉터리라는 구조를 검색 발췌로 확인했다.

[Anthropic: The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf): 3단계 점진적 공개를 검색 발췌로 확인했다.

[OpenAI Help: Memory in ChatGPT](https://help.openai.com/en/articles/8590148-memory-in-chatgpt): 저장된 기억을 설정에서 보고 삭제할 수 있다는 서술을 검색 발췌로 확인했다.

[Composio Docs: Managing multiple connected accounts](https://docs.composio.dev/docs/managing-multiple-connected-accounts): 같은 도구의 다중 계정 연결을 검색 발췌로 확인했다.

[Open Residency: Remy Gaskell](https://openresidency.com/remy-gaskell): 출연자 소개와 AI Onboard 플러그인을 검색 발췌로 확인했다.

[Reuters via The Hindu BusinessLine: Investors temper Anthropic IPO valuation expectations (2026-10-17)](https://www.thehindubusinessline.com/info-tech/investors-temper-anthropic-ipo-valuation-expectations-over-revenue-growth-slowdown-sources-say/article71590936.ece): Anthropic 3분기 조정 이익 흑자 설명을 검색 발췌로 확인했다.
