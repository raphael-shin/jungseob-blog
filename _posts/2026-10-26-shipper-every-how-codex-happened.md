---
layout: post
title: "Codex는 어떻게 OpenAI의 중심이 되었나, Dan Shipper가 Every에서 정리한 클라우드 실패와 로컬 전환과 코드 에디터 없는 데스크톱 앱 이야기를 날짜와 사용자 수치로 대조한 정리"
date: "2026-10-26 14:25:14 +0900"
created: "2026-10-26T14:25:14+09:00"
source: "https://every.to/p/how-codex-happened"
source_title: "How Codex Happened"
author: jungseob
source_author: "Dan Shipper (Every)"
source_published: "2026-10-15"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Every의 CEO Dan Shipper가 2026년 10월 15일에 쓴 장문의 취재 글을 정리한다. 2025년 5월 Codex Cloud의 제품 시장 적합성 실패, Thibault Sottiaux 주도의 로컬 전환과 Rust 에이전트 재작성, 코드 에디터를 뺀 데스크톱 앱 결정, 2026년 2월 앱 공개와 7월 ChatGPT 데스크톱 앱 통합까지의 경위를 다룬다. 날짜와 사용자 수치를 OpenAI 발표와 보도로 대조하고, 필자의 회사가 OpenAI의 사전 접근을 받은 이해관계와 인터뷰 중심 서술의 한계를 밝힌다."
image:
  path: "https://d24ovhgu8s7341.cloudfront.net/uploads/post/social_media_image/4521/full_page_cover_26537ee6e8f38c2c-Social_share.jpg"
  alt: "Every 글 How Codex Happened 대표 이미지"
tags:
  - knowledge
  - blog
  - AI
  - 코딩에이전트
  - OpenAI
---

## TL;DR

- Dan Shipper는 Codex가 OpenAI 반격의 중심이 된 과정을 내부 인터뷰로 재구성한다. 2025년 5월 출시한 클라우드 에이전트가 제품 시장 적합성을 찾지 못한 뒤, 팀은 로컬(터미널과 에디터) 방식으로 방향을 바꿨다.
- 전환의 핵심은 Thibault Sottiaux가 CLI를 기능 추가 대신 에이전트부터 Rust로 다시 쓴 일, 그리고 GPT-5가 실제 코드베이스에서 협업하도록 후속 훈련된 일이다. 이후 팀은 CLI와 에디터 확장이 잘 되는 상황에서 코드 에디터가 없는 데스크톱 앱에 투자했다.
- 앱은 2026년 2월 2일 macOS로 공개되었고 7월 9일 새 ChatGPT 데스크톱 앱이 되었다. Codex 주간 사용자는 3월 19일 200만 명, 6월 500만 명 이상이며 Every는 Codex와 ChatGPT for Work를 합쳐 4,000만 명이라고 쓴다.
- Shipper는 이를 Christensen의 혁신가의 딜레마가 10개월 안에 축소 재현된 사례로 읽는다. 병렬로 베팅하는 구조와 Codex로 Codex를 만드는 속도가 이유라는 해석이며 필자의 해석이다.
- 노트는 글 전체를 읽고 OpenAI 발표와 보도로 날짜와 수치를 대조했다. 필자의 회사는 OpenAI에게 GPT-5 사전 접근을 받았고, 서술의 상당 부분은 OpenAI 내부 관계자의 증언이다.

## 글에 대하여

Every의 CEO Dan Shipper가 2026년 10월 15일에 올린 글이다. 본문 약 5만 자를 전체 읽었다. 글은 필자가 2025년 여름 GPT-5 출시 전날 밤 OpenAI의 Mission Bay 사무실에서 Codex 팀의 Alexander Embiricos에게 "Claude Code에서는 그냥 내버려 둔다. GPT-5는 샌드박스에 갇혀 소심하다"고 말한 장면으로 시작해, 열 달 뒤 같은 사람과 다시 만나는 장면으로 끝난다. 인터뷰한 사람은 Embiricos, Sottiaux, Mia Glaese, Greg Brockman, Andrew Ambrosino, Ed Bayes, Sam Altman의 공개 발언 등이다. 글의 구성은 사고(thinking) 장면 사이에 "생각 중" 문구를 끼운 장치이며 본문 논리와는 무관하다. 이 블로그의 [Lauren Tan 신뢰 곡선 노트](https://raphael-shin.github.io/jungseob-blog/posts/tan-trust-curve-verification-agents/)와 [Kimflip pstack 노트](https://raphael-shin.github.io/jungseob-blog/posts/kimflip-pstack-dissection/)가 같은 코딩 에이전트 경쟁의 다른 면을 다룬다.

## 추론 모델이 열어 준 문

글은 Codex의 출발점을 추론 모델에서 찾는다. 초기 모델은 한 단어씩 즉흥으로 답했지만 2024년 9월 o1 미리보기부터 모델이 훈련으로 익힌 추론 흔적(scratch pad)에서 여러 각도로 문제를 풀고 막다른 길에서 되돌아 나온다. 프로그래밍은 편집, 실행, 확인이 몇 초 안에 닫히는 폐쇄 루프이므로 오래 생각할수록 이득이 큰 분야다. Codex라는 이름은 2021년 GPT-3 기반 모델에도 쓰였고 2024년 후반 OpenAI의 여러 팀이 서로 다른 방향에서 같은 꿈을 쫓았다. Embiricos는 터미널에 연결된 추론 모델을 처음 본 순간이 "feel the AGI" 순간이었다고 말한다. 화면을 읽는 모델은 느리고 서툴지만 터미널에서는 텍스트와 코드로 직접 일할 수 있기 때문이다. Sottiaux는 2024년 12월부터 연구자의 인프라 작업을 돕는 내부 코딩 에이전트를 OpenAI 모노레포에 훈련했고 이 모델이 다음 세대 모델을 만드는 데 쓰이는 부트스트랩 고리가 생겼다고 한다. 글은 이 에이전트 쪽과 Embiricos의 사람과 에이전트 협업 관점이 합쳐져 Codex 팀이 되었다고 쓴다.

## 클라우드의 실패

2025년 초 Codex 팀은 폼팩터가 터미널인지 에디터인지 클라우드인지 몰랐다. Altman이 말한 "OpenAI는 내부 스타트업 여러 개에 거는 베팅"이라는 구조는 낭비처럼 보일 수 있지만 모델이 계속 달라지는 시기에 필요하다고 필자는 본다. 2025년 2월 24일 Anthropic이 Claude Code를 연구 미리보기로 내놓았다. 내 컴퓨터의 파일에서 바로 일하고 중간에 끼어들 수 있으며 세션 간 학습을 쌓을 수 있다는 점이 Codex Cloud와 달랐다. Codex 팀은 약 7주 만에 클라우드 에이전트를 만들어 5월 16일에 출시했다. 사용자는 노트북의 설정과 권한을 클라우드에 재현해야 했고 몇 시간이 걸렸으며 작업 도중 끼어들 수 없고 후속 프롬프트도 새 클라우드 컴퓨터를 열었다. OpenAI 내부에서는 표준 환경 덕에 잘 됐지만 밖에서는 지속적으로 쓰이지 않았다. Embiricos는 모델이 아직 충분히 똑똑하지 않았다고 말한다. Sottiaux는 터미널 버전을 한 달 만에 폐기하고 클라우드를 택했다고 밝히며 "많은 설정 투자를 감수한다면 가장 이득을 볼 것에 최적화했다"고 설명한다. 공개된 Codex CLI는 4월 16일에 두 사람이 만든 부업이었고 기본 모델도 코딩용이 아니었다. 안전 문제로 로컬 에이전트 배포에 보수적이었다고 Embiricos는 말한다. 엔지니어링 매니저가 Cursor로 떠나고 Windsurf 인수도 7월에 무산되면서 팀은 "황무지"에 놓였다.

## 로컬 전환, 데스크톱 앱, 에디터 없는 선택

2025년 늦봄과 여름에 Sottiaux가 팀을 맡아 로컬로 전환했다. 그는 CLI에 기능을 얹는 대신 에이전트를 터미널에서 분리해 Rust로 다시 썼고 이 기계가 에디터, 데스크톱, 클라우드, ChatGPT 어디에나 들어가게 했다. 모델 쪽에서는 Michelle Pokrass 팀이 프로그래머를 관찰해 모델이 실패하는 지점을 훈련 과제로 만들었다. Brockman은 모델이 "지저분한 코드베이스나 프로그래머가 중간에 끼어드는 상황"을 본 적이 없었다고 설명한다. 그 결과 GPT-5는 단계별로 협업하고 허락을 구하는 쪽이었고 Every는 Claude Code보다 뒤처졌다고 평가했다. 그래도 8월 말 VS Code와 Cursor용 확장이 나오자 개발자들이 몰려 사용량이 10월까지 10배 이상 늘었다. 확장이 터미널을 넘어 가장 많이 쓰이는 면이 되었다.

팀의 다음 선택은 직관에 반했다. CLI는 유지하되 다음 큰 투자는 네이티브 데스크톱 앱이었다. 여러 에이전트와 이미지, 음성, 영상을 한꺼번에 다루려면 1970년대 텍스트 창으로는 부족하다는 판단이었다. 디자이너 Ambrosino는 4명 팀으로 앱을 만들면서 코드 에디터를 넣지 않기로 했다. 에디터를 넣으면 사용자가 되돌리기와 검색 같은 에디터의 모든 기능을 기대하기 때문이다. 에이전트로 충분히 좋게 코딩해 에디터가 필요 없게 만든다는 도박이었다. 2025년 11월 Google의 Antigravity가 에디터를 포함해 나오자 팀 내부도 흔들렸고 당시 Codex 전용 모델은 앱에 쓰기에 부족했다. 이후 11월 19일 GPT-5.1 Codex Max(수 시간 코딩), 12월 18일 GPT-5.2 Codex가 나오면서 분위기가 바뀌었다. 연말 휴가에 개발자들이 Opus 4.5와 GPT-5.2로 코드를 한 줄도 건드리지 않고 앱을 만든 일이 변곡점이라고 글은 쓴다. 1월에 팀 전원이, 2월에 OpenAI 엔지니어링과 연구 조직 대부분이 앱으로 옮겼다. Noam Brown은 "완전히 전환했다"고 했고 Brockman은 예전 워크플로로 돌아가는 것이 "과거로 가는 느낌"이라고 했으며 Altman은 "가장 사랑받은 내부 제품"이라고 했다고 글은 전한다.

앱은 2월 2일에 공개되었고 3일 뒤쯤 GPT-5.3 Codex가 나왔다. 이 모델은 프로그래밍 전용 훈련을 넘어 지식 노동 전반에 필요한 것을 묻기 시작한 첫 모델이었다고 Glaese는 말한다. Shipper는 Claude를 쓰던 일을 상당 부분 Codex로 옮겼고 GPT-5.4(3월 초)로 일상 도구가 되었다고 쓴다. 3월 19일 Codex는 주간 사용자 200만 명을 넘었고 4월에 인앱 브라우저와 다른 Mac 앱 조작이 추가되었으며 6월에는 500만 명 이상에 그중 약 다섯 명 중 한 명이 지식 노동자였다. 7월 9일 Codex 데스크톱 앱이 새 ChatGPT 데스크톱 앱이 되었다. 글 끝에서 Embiricos는 칠판에 클라우드, GPT-5 이후 CLI, 에디터 확장, 5.3과 데스크톱 앱 순으로 성장 곡선을 그리며 다음 곡선은 비동기 방식이라 클라우드로 다시 올라간다고 말한다. 직책은 Codex 에이전트 제품 책임자에서 엔터프라이즈 제품 책임자로 바뀌었고 Sottiaux는 ChatGPT와 Codex와 API를 포함한 핵심 제품 전체를 맡는다.

## 대조해서 확인한 점

핵심 날짜와 수치는 공개 자료와 맞는다. Codex 앱 공개(2월 2일)는 OpenAI의 소개 글이 확인하고 2026년 3월 기준 주간 사용자 200만 명은 Wikipedia 항목 요약이 전한다. OpenAI의 글은 "매주 500만 명 넘게 Codex를 쓴다"고 쓴다. 7월 9일 Codex 앱이 새 ChatGPT 데스크톱 앱으로 합쳐졌다는 점은 보도(Coursiv)로 확인했고 The New Stack은 2월 주간 활성 사용자가 100만 명 미만이었다가 6월 초 500만 명이 되었다고 쓴다. 이 숫자는 글의 서술(3월에 200만 명, 5배 성장)과 방향은 같다. 필자의 4,000만 명(Codex와 ChatGPT for Work 합산)은 한 매체가 "Every가 말하는" 합산이라 각 제품의 규모는 분리되지 않는다고 지적했다.

외부 사건도 대체로 맞는다. Claude Code의 2025년 2월 24일 연구 미리보기, Codex Cloud의 5월 16일 출시와 4월 16일 CLI, Windsurf 인수 무산(7월)과 Cursor의 당시 90억 달러 평가는 글의 서술이며 이 노트는 확인하지 못했다. 이 노트는 Codex 모델의 정확한 출시일(GPT-5.1 Codex Max 11월 19일, 5.2 Codex 12월 18일)을 원자료로 다시 확인하지는 못했고 글의 서술을 그대로 옮겼다. "OpenAI 내부에서 가장 사랑받은 제품" 같은 인용과 팀 내 Slack 메시지는 필자가 얻은 증언이며 독립 확인되지 않았다.

## 읽을 때 유의할 점

첫째, 필자의 회사 Every는 GPT-5를 출시 한 달 전에 사전 접근해 Vibe Check를 쓴 관계이고 글도 OpenAI 내부 사람들의 증언에 크게 기댄다. 둘째, 서사는 성공 이야기로 전개되며 다른 팀의 시각이나 경쟁 제품의 반론은 거의 없다. 셋째, "OpenAI의 복귀"라는 틀은 필자의 평가이고 같은 기간 Anthropic과 Cursor의 성장 수치는 비교하지 않는다. 넷째, 혁신가의 딜레마 해석은 은유이며 인과가 검증되지 않았다. 다섯째, 필자가 스스로 Claude에서 Codex로 옮겼다고 밝히는 것은 평가가 바뀐 증거이면서 동시에 이해관계 표시다. 여섯째, 코드 에디터를 뺀 선택이 성공 요인이었는지, 모델 개선이 요인이었는지 글도 분리하지 못한다.

그래도 가져갈 질문은 선명하다. 새 모델이 나올 때마다 제품의 폼팩터를 다시 정할 수 있는가, 내부 사용자의 환호를 외부 사용자의 사용으로 착각하고 있지는 않은가, 에디터 같은 익숙한 기능을 뺄 때 에이전트가 그 몫을 대신할 수 있다는 증거는 무엇인가, 병렬 팀에 베팅하는 구조에서 기존 제품의 성공이 다음 제품을 질식시키지 않게 하는 장치는 무엇인가.

## 참고 자료

[Every: How Codex Happened (Dan Shipper, 2026-10-15)](https://every.to/p/how-codex-happened): 본문 전체를 읽고 정리했다.

[OpenAI: Introducing the Codex app](https://openai.com/index/introducing-the-codex-app): 2월 2일 macOS 앱 공개를 검색 발췌로 확인했다.

[OpenAI: ChatGPT is now a partner for your most ambitious work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/): 주간 사용자 500만 명 이상 서술을 검색 발췌로 확인했다.

[Wikipedia: OpenAI Codex (AI agent)](https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)): 2026년 3월 주간 사용자 200만 명과 2월 데스크톱 앱을 검색 발췌로 확인했다.

[Coursiv: Codex merged with the ChatGPT app](https://coursiv.io/blog/codex-merged-with-chatgpt-app): 7월 9일 통합을 검색 발췌로 확인했다.

[The New Stack: GPT-5.6 Codex user surge](https://thenewstack.io/gpt-5-6-codex-user-surge/): 2월 100만 명 미만에서 6월 500만 명으로 늘었다는 서술을 검색 발췌로 확인했다.

[Superpower Daily: Every says Codex and ChatGPT for Work have 40 million weekly users combined](https://superpowerdaily.com/posts/every-says-codex-and-chatgpt-for-work-have-40-million-weekly-users-combined): 합산 수치와 한계 지적을 검색 발췌로 확인했다.
