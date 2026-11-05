---
layout: post
title: "AI가 코드를 쓰는 시대, Amazon이 바꾼 개발자 기준"
date: "2026-11-05 09:25:47 +0900"
created: "2026-11-05T09:25:47+09:00"
source: "https://www.geekwire.com/2026/amazon-rewrites-its-software-engineering-playbook-for-an-era-when-ai-writes-the-code/"
source_title: "Amazon rewrites its software engineering playbook for an era when AI writes the code"
author: jungseob
source_author: "Todd Bishop (GeekWire)"
source_published: "2026-11-03"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "GeekWire가 Amazon의 바뀐 개발자 역할 기준을 보도했다. 이제 Amazon 개발자 대부분은 코드를 직접 쓰지 않고 AI 에이전트에게 맡긴다. 새 기준은 토큰 사용량이나 코드 줄 수가 아니라 고객에게 준 결과로 개발자를 평가하라고 한다. 일주일 만에 AI 모델을 공개한 35명 팀 Velocity Labs 이야기도 함께 나온다. 기사와 Amazon이 공개한 편지 원문, Strands Decider 발표 글을 대조해 쉽게 정리했다."
image:
  path: "https://cdn.geekwire.com/wp-content/uploads/2026/11/brooker-lead-3x2-1.jpg"
  alt: "GeekWire 기사의 Marc Brooker 사진"
tags:
  - knowledge
  - blog
  - AI
  - AWS
  - 개발문화
---
## TL;DR

- Amazon 개발자 대부분은 이제 코드를 손으로 쓰지 않는다. AWS의 Marc Brooker는 "구현 코드 거의 전부를 에이전트가 만든다"고 말했다. 2년 전만 해도 대부분 직접 썼다.
- Amazon은 개발자 역할 기준을 고쳤다. 핵심은 토큰을 얼마나 썼는지, 코드를 몇 줄 올렸는지가 아니라 고객에게 어떤 결과를 줬는지로 평가하라는 것이다.
- 기준과 함께 보낸 편지에는 이런 문장이 있다. "지금의 AI 도구가 내 일에 도움이 안 된다면, 그건 실패가 아니라 발견이다." 이유를 적고 공유하라고 한다.
- 다만 편지는 사용량 지표를 버리지 않았다. 사용량이 아직은 성과와 잘 맞아떨어진다며 "신중하게" 쓰라고 한다. 한편 직원들은 AI를 쓰라는 압박이 있다고 말해 왔다.
- AWS 안에는 35명짜리 Velocity Labs가 있다. 이 팀은 일주일도 안 돼 작은 AI 모델 Strands Decider 2B를 만들어 공개했다.

## 무슨 기사인가

GeekWire의 Todd Bishop이 2026년 11월 3일에 쓴 기사다. Amazon이 개발자(SDE) 역할 기준을 AI 시대에 맞게 고친 이야기다. 기사 본문을 끝까지 읽었다. 기사가 연결한 원문 세 개도 직접 열어 봤다. Amazon이 공개한 편지, Strands Decider 발표 글, Brooker의 블로그 글이다. 주요 인물은 두 명이다. Marc Brooker는 AWS 부사장이자 최고 등급 엔지니어(Distinguished Engineer)이고 새 팀 Velocity Labs를 이끈다. Terk Terkowitz는 Amazon 쇼핑 사업의 부사장 겸 최고 등급 엔지니어이고 편지에 이름을 올린 사람이다. Brooker도 편지를 함께 쓴 사람 중 하나다.

## 일하는 방식이 이렇게 바뀌었다

Brooker는 2년 전만 해도 Amazon 개발자 대부분이 코드를 직접 썼다고 말한다. 지금은 다르다. 그의 말로는 "개발자 대다수의 구현 코드는 거의 전부 에이전트가 만든다." 그는 이것을 "엄청난 변화"라고 부른다. 그 자신도 그렇다. 예전에는 코드 편집기와 명령줄에서 시간을 보냈다. 지금은 Kiro, Kiro Crew, Claude Code 같은 에이전트 도구를 주로 쓴다. 그는 "도구가 완전히 바뀌었다"고 말한다.

## 새 기준의 핵심: 결과로 평가한다

Amazon은 개발자 역할 기준을 공개한 적이 없다. 이번 개정판도 기사에 주지 않았다. 대신 기준과 함께 보낸 편지는 Amazon 공식 뉴스 사이트에 공개됐다. Brooker는 업계에 나쁜 습관이 보였다고 말한다. 토큰을 얼마나 쓰는지, 코드를 몇 줄 올리는지에 매달리는 것이다. 그런 숫자는 고객에게 주는 가치와 같지 않다. 그래서 새 기준은 투입량이 아니라 결과로 개발자와 팀을 보라고 한다. AI 사용이 인사 평가에 들어가느냐는 질문에 Brooker는 "숫자로 직접 들어가지는 않는다"고 답했다. 다만 AI를 써서 일을 더 잘하게 됐다면, 그만큼은 평가에 반영될 수 있다고 했다.

## 편지에 실제로 적힌 것

편지 원문을 읽어 보면 기사보다 조금 더 자세하다. 먼저 출발점이 흥미롭다. Amazon은 원래 역할 기준에 특정 기술을 적지 않았다. 클라우드나 서버리스가 유행할 때도 그랬다. 이번에도 그 원칙을 지켰다. 이유는 지금 "좋은 AI 개발 방법"을 정해 두면 내년이면 낡을 것이기 때문이다. 그래서 바뀌지 않는 것에 집중했다. 고객, 사업, 팀에 주는 영향이다. 편지는 Jeff Bezos의 말을 인용한다. "10년 동안 무엇이 바뀔지보다, 무엇이 바뀌지 않을지가 더 중요한 질문이다."

지표 이야기는 균형을 잡는다. 편지는 토큰 사용량이나 코드 변경 수 같은 지표에 "깊은 결함이 있다"고 인정한다. 이것을 목표로 삼으면 비용이 늘고 시스템이 복잡해진다. 편지는 이를 "토큰 맥싱"이라고 부른다. 그러면서도 이런 지표가 아직은 실제 성과와 잘 맞는다고 말한다. 그래서 "신중하게, 판단력을 갖고" 쓰라고 한다. 편지에는 기사에 없는 구체적인 권고도 있다. AI 사용이 하위 10%인 팀은 왜 잘 안 쓰는지 살펴보라고 한다. 상위 10%인 팀은 많이 쓰는 만큼 성과도 늘었는지 확인하라고 한다.

가장 많이 인용될 문장은 이것이다. "지금의 AI 도구가 내 일에 도움이 안 된다면, 그건 실패가 아니라 발견이다." 그 이유를 적고 동료와 관리자에게 공유하라고 한다. AI가 어디서 도움이 안 되는지 설명할 수 있는 엔지니어가 바로 회사가 원하는 판단력을 보여 준다는 것이다. 리더에게도 요구가 있다. 실제 업무에 AI 도구를 직접 써 봐야 한다. 그래서 도움이 된 일과 안 된 일을 하나씩 말할 수 있어야 한다. 남에게 들은 말로 판단하지 말라는 뜻이다. 편지는 또 회사가 커지면서 일부 개발자와 관리자가 고객과 멀어졌다고 인정한다. 이 흐름을 되돌리고 싶다고 쓴다.

## 그래도 압박은 있었다

기사는 반대쪽 이야기도 전한다. 2025년 New York Times 보도에서 Amazon 개발자 세 명은 관리자가 AI를 쓰라고 밀어붙인다고 말했다. 목표치는 오르고 마감은 더 빡빡해졌다. 어떤 개발자는 일이 "창고 일처럼" 느껴진다고 했다. Financial Times는 Amazon이 개발자 80% 이상이 매주 AI를 쓰게 하는 목표를 세웠다고 보도했다. KiroRank라는 사내 순위표도 있었다. AI 코딩 도구 Kiro를 얼마나 쓰는지로 직원 순위를 매겼다. 그런데 순위를 올리려고 도구를 과하게 쓰는 사람이 나왔다. Amazon은 2026년 5월에 이 순위표를 없앴다고 FT가 전했다. 이 일이 새 기준의 계기였냐는 질문에, Brooker는 순위표를 기억하지 못한다고 답했다.

사고도 있었다. 2026년 3월, Amazon은 쇼핑 사이트 장애 중 하나가 AI 에이전트의 틀린 조언을 따른 엔지니어와 관련 있다고 인정했다. 그보다 앞선 12월에는 AWS 서비스가 13시간 멈춘 일도 있었다. FT는 Kiro가 "환경을 지우고 다시 만들기로" 결정한 탓이라고 보도했다. Amazon은 이를 부인했다. 원인은 권한 설정을 잘못한 사람의 실수라고 했다. 이후 운영 환경 접근에 동료 검토를 의무로 붙였다고 한다.

## 35명 팀 Velocity Labs

Velocity Labs는 이번 기사로 처음 알려진 팀이다. 2026년 4월에 만들어졌고 약 35명이며 대부분 시애틀에 있다. 목표는 Amazon의 평소 제품 개발 방식에서 벗어나 아직 덜 탐구된 AI 분야에서 빠르게 시제품을 만드는 것이다. 채용 공고에는 이렇게 적혀 있다. "오픈소스 커뮤니티와 일부 경쟁사가 새 아이디어를 실험하고 빠르게 첫 제품을 내는 것을 봐 왔다." 팀 안에서는 과학자와 엔지니어가 서로의 일을 넘나든다. 엔지니어가 연구를 하고 과학자가 개발을 한다. AWS의 에이전트용 오픈소스 도구 Strands를 만든 개발자들도 이 팀에 있다.

이 팀이 10월 1일에 공개한 것이 Strands Decider 2B다. 이 모델은 글을 쓰지 않는다. 대신 정해진 보기 중 하나를 고른다. 예를 들면 "이 요청을 어느 도구로 보낼까?" 같은 질문이다. 발표 글에 따르면 크기는 20억 파라미터로 작다. 그래서 일반 컴퓨터에서도 돌아가고 수십 밀리초 안에 답한다. 답이 얼마나 확실한지 점수도 함께 준다. Alibaba의 공개 모델 Qwen3.5-2B를 바탕으로, 글을 만드는 부분을 떼어 내고 보기를 고르는 부분을 붙였다. 학습 데이터와 스크립트까지 모두 공개했다.

시작은 Brooker의 개인 실험이었다. 9월 15일 스타트업 TypeSafe AI가 비슷한 모델 Jev를 내놓자, 그는 집에 있는 GPU로 직접 모델을 만들어 봤다. 그의 블로그에 따르면 그 모델 이름은 Hobson이었다. 그는 이렇게 썼다. "코드는 한 줄도 빠짐없이 에이전트가 썼다. 하지만 핵심 아이디어는 내 것이거나, 최소한 내가 이해한 것이 되게 하려 했다." 아이디어에서 공개까지 일주일이 안 걸렸다. Brooker는 팀이 작고 서로 믿기 때문이라고 말한다. 각자 일의 한 부분을 맡고 필요할 때 도움을 청한다. 그는 이런 팀이 더 생기겠지만 회사 전체가 이렇게 되지는 않을 것이라고 봤다.

## 일자리는 어떻게 되나

Amazon은 2025년 말부터 사무직 약 3만 명을 줄였다. CEO Andy Jassy는 AI 때문에 사무직 인력이 점점 줄 것이라고 말해 왔다. 한편 AWS CEO Matt Garman은 2026년 4월에 "개발자는 예전만큼 뽑고 있다"고 말했다. Amazon은 올해 인턴과 신입 개발자 1만 1천 명 이상이 들어온다고 밝혔다. AI 때문에 개발자 수가 줄어드냐는 질문에 Brooker는 "개발자 수를 바꾸지는 않는다고 본다"고 답했다. 회사가 원하는 사람은 주인의식이 있고 호기심이 많고 자기 분야 밖도 빨리 배우는 사람이다. 마지막으로 그는 이렇게 말했다. "맞는 도구가 최신 모델을 쓰는 AI 에이전트라면 아주 좋다. 하지만 파이썬 세 줄이라면 그것도 좋다."

## 확인해 본 것

편지 원문은 Amazon 공식 뉴스 사이트에서 읽었다. 결과 중심 평가, "실패가 아니라 발견", 지표를 신중하게 쓰라는 말, 고객과 멀어졌다는 인정 모두 기사 인용과 같다. 하위·상위 10% 팀을 살피라는 권고는 기사에 없고 편지에만 있다. Strands Decider 발표 글의 날짜는 2026년 10월 1일이다. 20억 파라미터, Qwen3.5-2B 기반, 학습 데이터 공개도 기사와 같다. Brooker의 블로그에서 집 GPU로 만든 모델 Hobson과 "코드는 한 줄도 빠짐없이 에이전트가 썼다"는 문장을 확인했다.

확인하지 못한 것도 있다. FT, New York Times, Business Insider 기사는 유료라 원문을 열지 않았다. "일주일도 안 걸렸다"는 기간, 35명이라는 인원, 개발자 대다수의 코드를 에이전트가 쓴다는 말은 Brooker의 설명이다. 개정된 역할 기준 문서 자체는 공개되지 않았다.

## 읽을 때 생각할 점

이 기사의 중심은 Amazon 경영진의 말과 회사가 공개한 편지다. 바깥에서 검증한 수치가 아니다. "결과로 평가한다"는 원칙이 실제 평가에서 어떻게 쓰이는지도 아직 알 수 없다. 편지는 사용량 지표도 "신중하게" 쓰라고 하므로, 현장에서 느끼는 압박이 금방 사라진다고 보기는 어렵다. 내 일에 가져올 질문은 이렇다. 우리 팀은 AI를 얼마나 썼는지 재는가, 아니면 그 결과 고객에게 무엇이 좋아졌는지 재는가? AI가 도움이 안 된 일을 숨기는가, 아니면 기록하고 공유하는가? 이 문제에 꼭 에이전트가 필요한가, 아니면 파이썬 세 줄이면 되는가?



## 참고 자료

[GeekWire: Amazon rewrites its software engineering playbook for an era when AI writes the code (2026-11-03)](https://www.geekwire.com/2026/amazon-rewrites-its-software-engineering-playbook-for-an-era-when-ai-writes-the-code/): 기사 본문을 끝까지 읽고 정리했다.

[About Amazon: An update from Amazon engineering leadership on the role of the developer in the age of AI](https://www.aboutamazon.com/news/company-news/amazon-software-engineer-role-guideline-ai): Terk Terkowitz 명의의 편지 원문을 읽었다.

[Strands Agents: Introducing Strands Decider 2B](https://strandsagents.com/blog/introducing-strands-decider/): 모델 구조와 공개 범위를 확인했다.

[Marc Brooker: Small Decisions, Engineering a Leading Model](https://brooker.co.za/blog/2026/09/28/engineering-system-one.html): 집 GPU 실험과 에이전트 코딩 관련 문장을 확인했다.
