---
layout: post
title: "PHP2Shell, AI가 찾아낸 PHP의 낡은 버그"
date: "2026-11-05 15:39:03 +0900"
created: "2026-11-05T15:39:03+09:00"
source: "https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability"
source_title: "PHP2Shell and AI Put Half the Internet on Edge"
author: jungseob
source_author: "Dina Genkina (IEEE Spectrum)"
source_published: "2026-11-02"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "IEEE Spectrum이 PHP2Shell 취약점을 다뤘다. 2024년에 보고됐지만 단순한 프로그램 멈춤으로 여겨져 방치된 PHP 버그를, AI의 도움을 받은 보안 연구자가 2주 만에 서버를 장악하는 공격으로 바꿨다. 기사는 AI가 버그 찾기를 쉽게 만들었지만 고치기는 여전히 어렵다고 짚는다. 오픈소스 관리자에게 돈과 AI를 더 줘야 한다는 주장, AI가 만든 패치를 수학적으로 증명하는 기술에 대한 기대도 담았다."
image:
  path: "https://spectrum.ieee.org/media-library/image.jpg?id=68544156&width=1200&height=600&coordinates=0%2C312%2C0%2C313"
  alt: "IEEE Spectrum의 PHP2Shell 기사 이미지"
tags:
  - knowledge
  - blog
  - AI
  - 보안
  - 오픈소스
---
## TL;DR

- PHP2Shell은 10월 말 공개된 PHP의 심각한 취약점이다. WordPress나 Drupal로 만든 사이트를 포함해, NASA, Wikipedia, 백악관 사이트까지 위험에 놓였다.
- 원래 버그는 2024년에 보고됐지만 "프로그램이 멈출 뿐"이라 방치됐다. 보안 회사 Calif의 연구자가 AI의 도움을 받아 2주 만에 이를 서버 장악 공격으로 바꿨다.
- 컬럼비아대 Suman Jana 교수는 AI가 전문가를 대신하지는 못한다고 말한다. 대신 최상위 0.1% 전문가가 훨씬 많은 일을 하고, 그 바로 아래 사람도 그 수준에 닿게 해 준다고 본다.
- 버그를 찾기는 쉬워졌지만 고치기는 여전히 어렵다. PHP 패치에는 엔지니어 4명이 두 달을 썼다. 오픈소스 관리자에게 돈과 AI를 더 줘야 한다는 주장이 나온다.
- 기사는 패치 전에 악용된 일이 없다고 쓰지만, 미국 CISA는 10월 26일 이 취약점을 "실제로 악용된 취약점" 목록에 올렸다.

## 무슨 기사인가

IEEE Spectrum의 Dina Genkina가 2026년 11월 2일에 쓴 기사다. 제목은 「PHP2Shell and AI Put Half the Internet on Edge(PHP2Shell과 AI가 인터넷 절반을 긴장시키다)」다. 기사 본문을 끝까지 읽었다. PHP는 1994년에 나온 웹 프로그래밍 언어다. 원래 이름은 "personal home page"였다. 지금도 많은 웹사이트가 PHP로 돈다. WordPress와 Drupal 같은 유명한 사이트 제작 도구도 PHP를 쓴다.

## 무엇이 문제였나

PHP2Shell은 공격자가 서버의 민감한 데이터를 읽고 서버에서 마음대로 코드를 실행하게 해 주는 취약점이다. 다행히 보안 연구자들이 먼저 찾아 PHP 재단에 알렸다. 기사에 따르면 나쁜 사람들이 공격 방법을 손에 넣기 전에 패치가 나왔다. 보안 스타트업 Tolmo의 Matt Suiche는 이렇게 말한다. "지난 40년 동안 사람이 쓴 낡은 소프트웨어가 전부 드러나고 있다. 이제 기술 부채를 갚을 때다."

## 방치된 버그가 무기가 되기까지

밑바탕의 버그는 이미 2024년에 PHP 재단에 보고됐다. 메모리 관련 오류였다. 어떤 데이터에 공간을 너무 작게 잡아 담지 못하는 문제다. 보통 이런 오류는 프로그램을 멈추게 할 뿐이다. 불편하지만 그 자체로 위험하지는 않다. 그래서 버그는 고쳐지지 않은 채 남았다. Suman Jana 교수는 이렇게 설명한다. "언제 보더라도 고쳐지길 기다리는 버그 보고가 잔뜩 있다. 그냥 멈추는 버그다. 대부분 그걸 심각하게 보지 않는다."

올해 보안 회사 Calif가 OpenAI의 후원으로 PHP를 독립 감사하겠다고 나섰다. 2주 만에 Calif의 연구자가 AI 도구의 도움을 받아 이 메모리 버그로 서버에서 아무 코드나 실행하는 방법을 찾았다. 그러면 악성 코드를 깔거나 중요한 데이터를 읽을 수 있다. 사소한 버그가 치명적인 취약점이 된 것이다. Calif 팀은 곧바로 PHP 재단에 알렸다. Jana 교수는 실제 공격이 어떤 일인지 설명한다. 서버에서 도는 특정 프로그램의 메모리 속 정확한 위치로 뛰어야 하고 어떤 비트를 어떤 순서로 덮어쓸지 정확히 계산해야 한다. "로켓 과학은 아니다. 다만 아주 구체적이고 고통스러운 추론이 많이 필요하다. 그런데 AI가 그걸 아주 잘 해냈다."

## AI가 전문가를 대신하지는 않는다

오해하면 안 되는 점이 있다. Calif의 연구자들, 그리고 취약점을 확인하고 넓힌 OpenAI와 보안 회사 Wiz는 보안과 PHP를 깊이 아는 사람들이었다. Jana 교수는 이렇게 말한다. "AI가 혼자 다 할 수 있다는 말은 아니다. 분명히 못 한다. 하지만 아주 빨리 좋아지고 있다. 그래서 최상위 0.1% 전문가는 훨씬 많은 일을 하고, 그 바로 아래 사람도 세부를 다 알지 못한 채 그 수준에 닿을 수 있다."

## 찾기는 쉽고 고치기는 어렵다

취약점이 알려진 뒤 PHP 재단의 엔지니어 4명이 두 달 동안 패치를 만들었다. Jana 교수는 이를 "근본적인 비대칭"이라 부른다. "버그를 고칠 때는 공격의 모든 경로가 막혔는지 확인해야 하고, 기존 기능을 망가뜨리지도 않아야 한다." 그 비대칭은 방어하는 쪽, 특히 오픈소스 관리자에게 큰 부담이다. PHP처럼 널리 쓰이지만 뚜렷한 수입이 없는 오픈소스를 유지하는 일은 AI 이전부터 어려웠다. AI 해킹 도구가 이 문제를 더 급하게 만들었다. 해법으로 그는 방어하는 쪽에 돈과 최신 보안 AI 모델을 더 주자고 말한다. "최전선 AI 연구소들이 토큰 예산 일부를 이런 버그 조사에 기부하고 있다. 아주 좋은 일이고, 더 많아져야 한다."

## AI가 만든 패치를 수학으로 증명하기

Jana 교수는 고치는 쪽도 자동화될 수 있다고 기대한다. "형식 검증"이라는 기술 덕분이다. 코드가 특정 버그에서 자유롭다는 것을 수학적으로 증명하는 방법이다. 그는 Anthropic이 10월 22일 발표한 연구를 예로 든다. "패치는 AI가 만들고, 그 패치가 맞다는 증명도 AI가 만든다. AI가 하지 않는 유일한 부분은 증명을 검사하는 프로그램이다. AI는 헛소리를 할 수 있으니, 누군가는 엄밀하게 확인해야 한다."

## 진짜 큰 사고가 나야 바뀐다

존스홉킨스대 Matthew Green 교수는 덜 낙관적이다. "정말 나쁜 일이 일어나기 전까지 아무도 이 문제를 고치지 않을 것이다. PHP2Shell은 그만큼 나쁘지 않았다. 아마 2027년 초쯤 일반인이 화낼 만한 나쁜 일이 생기면, 그제서야 모든 걸 지원할 것이다." 그때까지 그의 조언은 단순하다. "휴대폰이 보안 업데이트를 설치하겠냐고 물으면 다음 주로 미루지 마라. 그냥 해라." Jana 교수의 마지막 말은 이렇다. "이게 마지막은 절대 아니다. 누가 먼저 찾느냐의 문제다. 이번처럼 착한 해커가 먼저 찾길 바랄 뿐이다."

## 확인해 본 것

PHP2Shell은 실제로 두 개의 CVE(CVE-2026-109618, CVE-2026-109619)로 공개됐다. Calif의 기술 설명 글, Wiz의 분석 글, OpenAI의 공동 공개 글이 모두 있다. OpenAI는 지난 두 달 동안 관리자와 연구자 연합을 이끌었다고 쓴다. 기사의 "두 달"과 맞다. Wiz는 이 취약점이 인터넷의 70%에 영향을 준다고 쓴다. 기사 제목의 "인터넷 절반"보다 큰 숫자다. Anthropic의 형식 검증 연구도 10월 22일에 발표됐고 Claude로 오픈소스 라이브러리 123개의 보안 성질을 증명했다고 전해진다.

기사와 어긋나는 점이 하나 있다. 기사는 패치 전에 나쁜 사람들이 공격 방법을 얻지 못했다고 쓴다. 그런데 미국 사이버보안 기관 CISA는 10월 21일 긴급 패치를 권고했고 10월 26일에는 두 CVE를 "실제로 악용이 확인된 취약점" 목록에 올렸다. 패치가 나온 뒤 실제 공격이 시작됐을 가능성이 크다. "재앙을 피했다"는 기사의 표현은 이 점을 감안해 읽어야 한다. 확인하지 못한 것은 버그가 2024년에 처음 보고됐다는 시점, Calif가 2주 만에 공격법을 찾았다는 기간, 패치에 엔지니어 4명이 참여했다는 인원이다. 기사의 설명을 따랐다.

## 읽을 때 생각할 점

이 사건은 OpenAI가 후원한 감사에서 나왔고 OpenAI가 공개를 이끌었다. AI 회사에는 "우리 AI가 인터넷을 지켰다"는 좋은 이야기이기도 하다. 이 점을 감안해 볼 만하다. 또 Green 교수의 "2027년 초"는 근거가 제시되지 않은 예측이다. 내 일에 가져올 질문은 이렇다. 우리 시스템에 "그냥 멈추는 버그"라고 방치된 것이 있는가? AI 덕에 버그 찾기가 쉬워졌다면, 고치는 속도는 따라가고 있는가? 우리가 기대는 오픈소스는 누가, 어떤 돈으로 지키는가?



## 참고 자료

[IEEE Spectrum: PHP2Shell and AI Put Half the Internet on Edge (2026-11-02)](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability): 기사 본문을 끝까지 읽고 정리했다.

[Calif: PHP2Shell](https://calif.io/php2shell/): CVE 번호와 발견 주체를 검색 발췌로 확인했다.

[Wiz: PHP2Shell, AI uncovers critical RCE vulnerabilities](https://www.wiz.io/blog/php2shell-php-rce): 영향 범위 주장을 검색 발췌로 확인했다.

[CISA: Critical Vulnerabilities in PHP Require Immediate Patching](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching): 악용 목록 등재를 검색 발췌로 확인했다.

[Anthropic: Formal verification](https://www.anthropic.com/research/formal-verification): 형식 검증 연구의 존재를 검색 발췌로 확인했다.
