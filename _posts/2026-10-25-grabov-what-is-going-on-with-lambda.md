---
layout: post
title: "Lambda는 서버리스를 떠나고 있는가, Alexy Grabov가 Lambda의 세 가지 형태와 두 가지 확장을 AWS의 사업 동기로 읽은 글을 AWS 발표 자료와 대조한 정리"
date: "2026-10-25 16:45:44 +0900"
created: "2026-10-25T16:45:44+09:00"
source: "https://www.linkedin.com/pulse/what-going-lambda-alexy-grabov-plkne"
source_title: "What is going on with Lambda?"
author: jungseob
source_author: "Alexy Grabov"
source_published: "2026-10-24"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Alexy Grabov가 2026년 10월 24일에 LinkedIn에 쓴 글을 정리한다. Lambda가 Event Functions, Web Functions, MicroVMs의 세 형태에 Durable Functions와 Managed Instances라는 확장을 더하며 상태 없는 15분 함수라는 서버리스의 교리를 뒤집었다고 보고, 그 이유를 AI 에이전트 대응, 틈새 클라우드 견제, 서버리스 졸업 이탈 방지라는 세 가지 사업 동기로 읽는다. AWS 발표문과 문서로 기능 서술을 대조하고 필자의 추정과 과장된 대목을 밝힌다."
image:
  path: "https://media.licdn.com/dms/image/v2/D4E12AQEc8A9b8tqUtA/article-cover_image-shrink_720_1280/B4EaFu3pP5KEAQ-/0/1792861443369?e=2147483647&v=beta&t=F78e4g3v0klPSLHuj86rVECt809IqYj6S7NOfYTczKg"
  alt: "LinkedIn 글 What is going on with Lambda 대표 이미지"
tags:
  - knowledge
  - blog
  - AWS
  - Lambda
  - 서버리스
---

## TL;DR

- Alexy Grabov는 Lambda가 11년간 지킨 교리(상태 없음, 단발성, 단일 동시성, 최대 15분, 벽시계 과금)를 지난 1년간 모두 뒤집었다고 본다. 2026년 10월 기준 Lambda는 Event Functions, Web Functions, MicroVMs의 세 형태에 Durable Functions와 Managed Instances가 더해진 모음이다.
- AWS의 동기는 세 가지로 읽는다. 기존 Lambda가 LLM과 에이전트 작업에 맞지 않았고, Vercel·Temporal·E2B 같은 틈새 클라우드가 파고들었으며, 규모가 커진 고객이 컨테이너로 옮겨 가는 서버리스 졸업을 막아야 했다는 것이다.
- 기능 서술은 대체로 AWS 발표와 맞는다. Web Functions는 환경당 최대 128 동시 요청과 활성 CPU 과금이고, MicroVMs는 메모리와 디스크 상태를 최대 8시간 보존하며, Durable Functions의 한도는 10월 13일에 3,000에서 30,000 연산, 체크포인트 256KB에서 1MB가 됐다.
- 어긋나는 대목도 있다. Managed Instances의 90분 타임아웃은 비동기 호출과 이벤트 소스 매핑에만 해당하고, 오늘의 Lambda가 상태를 갖는다는 문장은 MicroVMs에만 맞는다. 사업 동기 세 가지는 근거 없는 필자의 추정이다.
- 이 노트는 글 본문 전체와 AWS 블로그, 문서, FAQ, What's New를 직접 읽고 대조했다. 글에 들어 있는 비교 표(기존 Lambda 대 새 Lambda)는 이미지라서 읽지 못했다.

## 글에 대하여

LinkedIn에 2026년 10월 24일 올라온 Alexy Grabov의 글이다. 필자는 자신의 이전 글 「AWS who? Meet AAS」와 같은 기조로, 코드나 CDK 설정이 아니라 AWS가 무엇을 만들고 어떻게 값을 매기며 누구와 갑자기 경쟁하는지를 통해 방향을 읽는 사업·경제·전략 글이라고 소개한다. 검색으로 확인한 LinkedIn 프로필 발췌에 따르면 필자는 Palo Alto Networks의 시니어 스태프 엔지니어이자 AWS Community Builder이며 AWS 직원은 아니다. 본문 전체를 읽었다. 첫머리가 논지를 말한다. 11년 동안 "Lambda"는 한 가지를 뜻했고 지금은 그렇지 않다는 것이다. 이 블로그의 [Garman 대담 노트](https://raphael-shin.github.io/jungseob-blog/posts/garman-cloud-for-ai-agents/)와 [Jassy 대담 노트](https://raphael-shin.github.io/jungseob-blog/posts/jassy-a16z-220b-capex-demand-left-on-table/)가 다룬 AWS의 에이전트 중심 재편과 겹치는 이야기다.

## 세 형태와 두 확장

필자가 먼저 세우는 구도는 이렇다. 예전 Lambda는 상태가 없고 단발성이고 이벤트로 움직이고 한 번에 요청 하나를 처리하고 최대 15분을 살고 벽시계 시간으로 과금했다. 상태나 장시간 프로세스, 포트를 듣는 웹 서버, 전용 EC2가 필요하면 ECS, EKS, EC2로 안내했다. 2026년 10월 기준으로 AWS는 Lambda를 세 계산 원형으로 나눴고 모두 Firecracker 마이크로VM 위에서 돈다고 필자는 쓴다.

첫째는 Event Functions다. 기존에 Lambda 함수라고 부르던 것의 새 이름이다. 코드와 배포는 그대로이고 S3, SQS, EventBridge 이벤트 하나를 격리된 환경 하나가 처리하며 시작부터 끝까지의 시간에 값을 낸다. 필자는 이름을 바꾼 이유가 서비스가 모든 것을 하게 되면 원조에도 이름표가 필요해서이고 이벤트 기반 접착 코드가 이제 Lambda 정체성의 3분의 1일 뿐이라는 신호라고 읽는다. 둘째는 Web Functions다. 코드가 포트를 듣는 표준 HTTP 서버(Express, Hono, Fastify, Next.js)이고 어댑터 없이 명령 한 줄(`aws lambda-web deploy`)로 배포하며 한 환경이 최대 128개 요청을 동시에 처리하고 활성 CPU 시간에 값을 낸다. Bedrock이 토큰을 돌려주기까지 15초를 기다리는 시간은 CPU를 거의 쓰지 않으므로 값이 거의 들지 않는다는 예가 붙는다. 필자가 지적하는 기존 방식의 비용은 API Gateway 앞단, 요청마다 새 환경을 띄우는 콜드 스타트, 유휴 대기 시간까지 내는 벽시계 과금이다.

셋째는 MicroVMs다. 2026년 중반에 도입되었고 Firecracker로 격리된 전용 가상 머신이며 Amazon Linux 2023 또는 자기 Dockerfile을 쓰고 HTTP/2, gRPC, WebSocket을 받는 전용 HTTPS 엔드포인트를 갖는다. 핵심은 수명주기를 고객이 정한다는 점이다. 사용자 세션마다 MicroVM을 띄워 AI 에이전트가 패키지를 설치하고 파일을 쓰고 신뢰할 수 없는 코드를 돌리게 하다가, 사용자가 쉬면 메모리와 디스크 상태를 보존한 채 최대 8시간 동안 일시 정지하고 다음 프롬프트에 거의 즉시 재개한다. 필자는 이것을 "서버리스 애완 VM"이라고 부른다.

두 확장은 별도 원형이 아니라 위에 얹힌 것으로 다뤄진다. Durable Functions는 체크포인트와 재생 엔진을 Lambda 코드에 넣은 것으로(필자가 "Step-Lambdas"라 부른 것), `context.step()`과 `context.wait_for_callback()` 같은 호출로 실행을 멈추고 기반 컨테이너를 내린 채 기다리다가 최대 1년 뒤에도 이어 간다. 필자는 2026년에 연산 한도가 3,000에서 30,000으로, 체크포인트 크기가 4배인 1MB로 늘어난 것이 LLM 에이전트 대화 이력을 단계 사이에 저장할 만큼이라며 우연이 아니라고 쓴다. Managed Instances(LMI)는 자기 계정과 VPC 안의 전용 EC2에서 Lambda 함수를 돌린다. 운영체제 패치, 라우팅, 확장은 AWS가 맡고 환경당 다중 동시성, Graviton4, 사용자 지정 CPU 대 메모리 비율, 콜드 스타트 없는 웜 플릿, EC2 Savings Plans와 예약 인스턴스로 비용을 낮추는 길이 열린다. 덧붙인 보너스는 테넌트 격리 모드로, 테넌트 ID를 넘기면 A용으로 데워진 환경이 B에 재사용되지 않음을 컴퓨트 층에서 보장한다.

## 왜 하는가: 세 가지 동기

필자는 이를 단위 경제와 시장 방어의 이야기로 읽는다. 첫 번째 동기는 기존 Lambda가 AI와 에이전트에 맞지 않았다는 것이다. 추론 모델이 25초 동안 토큰을 디코딩하는 동안 CPU 사용률이 0.1%여도 25초 치 컴퓨트를 냈고 사람 승인을 세 시간 기다리며 500번 반복하는 에이전트는 15분에 끊겼으며 30분짜리 디버깅 세션에서 코드를 쓰고 실행하는 코딩 에이전트에게는 너무 잠겨 있고 상태가 없었다. 각 문제에 Web Functions, Durable Functions, MicroVMs가 하나씩 대응한다. 두 번째 동기는 틈새 클라우드 견제다. Vercel과 Cloudflare(프런트엔드와 풀스택), Temporal·Inngest·Cloudflare Workflows(내구성 오케스트레이션), E2B·Modal·Fly.io(AI 코드 샌드박스)가 파고든 영역에 AWS가 각각 Web Functions, Durable Functions, MicroVMs로 답했고 새 서비스 다섯 개를 만들지 않고 개발자가 이미 아는 Lambda 이름 아래 묶었다는 것이다.

세 번째 동기는 "서버리스 졸업 이탈"을 막는 일이다. 스타트업이 Lambda로 시작해 규모가 커지면 청구서가 인건비보다 커지고 6개월을 들여 EKS나 EC2 컨테이너로 다시 쓰는데, 그 재설계 순간에 Google Cloud, Azure, 베어메탈이 파고든다고 필자는 쓴다. Managed Instances와 Web Functions는 코드를 바꾸지 않고 Lambda를 Managed Instances로 돌려 Savings Plan을 붙이게 하여 졸업할 이유를 없앤다. 결론에서 필자는 서버리스를 2014년의 교리(상태 없음, 단일 동시성, 15분 핸들러)로 정의하면 Lambda는 서버리스를 떠났지만 개발자가 원한 것은 함수의 순수성이 아니라 추상화(비즈니스 로직만 쓰고 워크로드에 맞는 과금을 받는 것)라고 말한다. Lambda는 더 이상 FaaS 제품이 아니라 AWS의 범용 컴퓨트 추상화 계층이 되었고 어떤 워크로드든 진입점이 Lambda이길 AWS가 원한다는 것이다.

## 대조해서 확인한 점

세 원형 구도는 AWS 자료와 맞는다. 2026년 10월 12일 AWS 뉴스 블로그의 Web Functions 발표는 Lambda가 Event Functions, Web Functions, MicroVMs의 세 형태를 갖고 모두 Firecracker 격리 위에 있다고 쓰고 Event Functions라는 이름은 기존 Lambda 함수에 붙인 것이라고 밝힌다. 문서도 Lambda 함수를 "Event Functions(구 Lambda 함수)"로 부른다. 필자의 "이름만 바뀌었다"는 서술과 맞는다.

Web Functions의 세부도 맞는다. 발표문은 환경당 최대 128 동시 요청, CPU 시간 계량(DB나 API를 기다리는 시간은 CPU를 거의 안 씀), 메모리는 환경이 존재하는 동안 계량이라고 쓴다. 명령 `aws lambda-web deploy`는 발표문의 예 그대로이고 다중 리전은 `--regions` 옵션을 쓰는 선택 기능이다. 필자가 "기본으로 따라온다"고 쓴 다중 리전 복제와 지연 기반 라우팅은 FAQ가 엔드포인트 수준에서 켜는 옵트인 기능이라고 설명하므로 표현이 다소 후하다. 발표문의 예는 Node.js 프레임워크이며 다른 런타임 지원은 이 노트가 확인하지 못했다.

MicroVMs는 AWS가 2026년 6월에 발표했고 7월 10일 컴퓨트 블로그가 자세히 다뤘으며 이후 리전이 8월(5곳), 10월 22일(4곳) 확대되었다. 필자의 "중반 도입"과 맞는다. 메모리와 디스크 상태를 최대 8시간 보존하고 유휴 시 자동 일시 정지하며 재개한다는 서술이 제품 페이지와 같다. 엔드포인트가 HTTP/2, WebSocket, gRPC를 지원한다는 점, Dockerfile로 이미지를 만든다는 점도 AWS 블로그가 쓴다. Durable Functions의 한도는 2026년 10월 AWS의 What's New가 "연산 3,000에서 30,000, 체크포인트 페이로드 256KB에서 1MB"라고 밝힌다. 필자의 "4배"도 맞고 최대 1년 실행도 FAQ와 같다. 다만 "대화 이력을 저장하기에 딱 맞는 크기"는 필자의 추정이다.

어긋나는 곳이 둘 있다. 첫째, Managed Instances의 "최대 90분 타임아웃"은 조건이 빠졌다. 문서는 15분이 기본이고 90분은 Managed Instances 함수를 비동기 호출하거나 이벤트 소스 매핑(Amazon MQ와 DocumentDB 제외)으로 호출할 때만이며 동기 호출은 그대로 15분이라고 쓴다. 둘째, 서두의 "오늘의 Lambda는 상태를 갖는다"는 MicroVMs에만 해당한다. Event Functions는 여전히 호출 간 상태를 전제하지 않는다. 또 LMI가 EC2 Nitro에서 컨테이너 격리를 쓴다는 설명은 확인하지 못했고 현재 인스턴스에서 Graviton4를 쓸 수 있다는 부분은 문서가 맞다. Lambda Managed Instances 자체는 2025년 11월 30일 re:Invent 2025에서 발표되었다. 테넌트 격리 모드는 2025년 말 출시 뒤 이벤트 소스 매핑과의 통합이 AWS 컴퓨트 블로그에 올라 있다.

사업 동기 세 가지는 AWS가 밝힌 것이 아니다. 발표문은 Web Functions를 웹 앱의 성능과 일관성, 개발자의 표준 프레임워크 사용이라는 고객 문제로 설명하고 경쟁사나 이탈 방지를 이유로 들지 않는다. 필자가 말한 틈새 업체와 기능의 짝짓기(Vercel·Cloudflare 대 Web Functions 등)와 서버리스 졸업 비용 서술은 필자의 해석이며 이 노트는 근거를 찾지 못했다. 글이 기대는 Amazon Agentic Services(AAS)라는 틀은 필자의 이전 글이 붙인 이름이고 이 노트의 검색에서는 AWS가 공식 브랜드로 쓴 사례를 확인하지 못했다. 글의 비교 표(기존 대 새 Lambda)는 이미지로 들어 있어 읽지 못했고 어떤 칸의 수치가 어긋나는지는 판정하지 못했다.

## 읽을 때 유의할 점

첫째, 필자는 사업·전략 해석을 AWS의 의도처럼 확정적으로 쓴다("three motives become crystal clear"). 확인된 것은 기능과 출시 시점이고 동기는 추정이다. 둘째, "서버리스는 죽었다"는 제목식 선언은 정의 문제다. 필자 스스로 2014년의 엄격한 정의를 쓸 때만 맞고 추상화 관점에서는 이어진다고 쓴다. 셋째, 기능이 늘어난 사실이 곧 선택하기 쉬워졌다는 뜻은 아니다. 다섯 가지 형태와 확장 사이를 고르는 기준(요금, 지연, 운영 부담)은 글에 구체적으로 없다. 넷째, 비용 서술(Web Functions가 I/O 대기에 거의 값을 안 낸다, LMI가 Savings Plan으로 비용을 줄인다)은 워크로드에 따라 다르고 글에 계산 사례가 없다. AWS 발표문도 I/O 중심 워크로드에서 "줄일 수 있다"고만 쓴다. 다섯째, 이 노트는 요금표와 한도 전체를 대조하지 않았다.

그래도 가져갈 질문은 선명하다. 우리 Lambda 중 요청 시간 대부분이 외부 호출 대기인 것은 무엇인가(Web Functions 후보), 15분을 넘겨 쪼개 놓은 워크플로는 무엇인가(Durable Functions 후보), 규모가 커져 컨테이너 이전을 검토하던 함수는 Managed Instances로 코드 변경 없이 해결되는가, 에이전트가 코드를 실행하는 기능이 있다면 세션별 격리 샌드박스를 MicroVMs로 둘 수 있는가.

## 참고 자료

[Alexy Grabov: What is going on with Lambda? (LinkedIn, 2026-10-24)](https://www.linkedin.com/pulse/what-going-lambda-alexy-grabov-plkne): 본문 전체를 읽고 정리했다. 비교 표 이미지는 읽지 못했다.

[AWS 뉴스 블로그: Announcing AWS Lambda Web Functions (2026-10-12)](https://aws.amazon.com/blogs/aws/announcing-aws-lambda-web-functions-for-fast-consistent-web-app-performance-anywhere/): 세 형태, 128 동시 요청, CPU 계량, 배포 명령을 읽었다.

[AWS 컴퓨트 블로그: Announcing Lambda MicroVMs (2026-07-10)](https://aws.amazon.com/blogs/compute/announcing-lambda-microvms-serverless-compute-environments-with-vm-level-isolation-and-near-instant-startup/): 수명주기 제어, 이미지 빌드, HTTPS 엔드포인트를 읽었다.

[AWS What's New: Lambda MicroVMs](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lambda-microvms/): 최대 8시간 보존과 일시 정지·재개를 검색 발췌로 확인했다.

[AWS What's New: Lambda durable functions 한도 상향 (2026-10)](https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-gen-limit-increase/): 3,000에서 30,000 연산, 256KB에서 1MB 체크포인트를 검색 발췌로 확인했다.

[AWS Lambda FAQ](https://aws.amazon.com/lambda/faqs): 세 형태, 다중 리전의 옵트인 성격, 15분과 90분 타임아웃 조건, 1년 내구 실행을 읽었다.

[AWS 문서: Lambda Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html): EC2 현세대 인스턴스(Graviton4 포함)와 90분 조건을 검색 발췌로 확인했다.

[AWS 뉴스 블로그: Introducing AWS Lambda Managed Instances (2025-11-30)](https://aws.amazon.com/blogs/aws/introducing-aws-lambda-managed-instances-serverless-simplicity-with-ec2-flexibility/): 발표일을 검색 발췌로 확인했다.
