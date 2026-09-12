---
layout: post
title: 개념 프레임워크와 동작하는 코드 사이의 간극 - AgentCore로 구현한 AI-DLC 구축 단계 두 사례
date: '2026-09-05'
last_modified_at: '2026-09-05T12:45:00+09:00'
author: jungseob
categories:
- 지식 노트
tags:
- AWS
- AgentCore
- AI-DLC
- 에이전트
- MCP
- 개발생산성
description: AI-DLC를 채택한 팀이 개념 프레임워크와 동작하는 코드 사이에서 겪는 간극을 두 개의 참조 구현으로 메운 글. SQL 스키마에서
  Mermaid ER 다이어그램을 만드는 에이전트와 다중 에이전트 코드 보안 분석 시스템을 아키텍처·코드·설계 결정 수준까지 담고, Kiro·Codex·Claude
  Code와의 결합 워크플로와 여덟 가지 권장 사항을 정리한다.
source: https://aws.amazon.com/ko/blogs/machine-learning/ai-driven-development-lifecycle-using-amazon-bedrock-agentcore/
source_title: AI-driven development lifecycle using Amazon Bedrock AgentCore
source_author: Arghya Banerjee · Ram Pathangi · Kunal Ghosh · Ananth Kommuri (AWS
  Sr. Solutions Architects)
source_published: ''
published: true
render_with_liquid: false
image:
  path: https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/31/ML-21366-featured-image.png
  alt: 원문 대표 이미지 · AI-driven development lifecycle using Amazon Bedrock AgentCore
---

# 개념 프레임워크와 동작하는 코드 사이의 간극

## TL;DR

- 문제 규정이 정확한데 **AI-DLC를 Amazon Bedrock AgentCore와 Kiro 같은 코딩 에이전트로 채택하는 엔지니어링 팀은 개념 프레임워크와 동작하는 코드 사이의 간극에서 자주 어려움을 겪는다**는 것이다. AI-DLC의 정의도 명시된다. **AI를 소프트웨어 개발 수명주기 전반의 중심 협력자로 배치해 일상적 실행을 처리하게 하면서 사람은 중요한 결정에 대한 감독을 유지한다**는 것이고, 이 글은 **동작하는 참조 구현으로 그 간극을 메운다.**
- 첫 번째 구현이 이벤트 기반 서버리스인데 **SQL 파일이 S3에 업로드되면 Lambda가 Cognito OAuth로 인증한 뒤 AgentCore 런타임 에이전트를 호출하고, 에이전트가 DDL을 파싱해 Mermaid erDiagram을 생성해 S3에 저장**한다. 경계도 분명하다. **스키마 메타데이터인 테이블과 제약, 외래키만 읽고 행 데이터는 절대 읽지 않아 스키마-다이어그램 자동화의 깔끔한 참조가 된다.**
- 두 번째 구현이 다중 에이전트 보안 분석인데 **GitLab 파이프라인에서 코드가 S3로 푸시되면 Strands 기반 에이전트가 Claude Sonnet으로 평가하고, CVE와 정책 검사용 MCP 도구를 Lambda에서 실행해 호출**한다. 산출물도 구체적으로 **1에서 10까지의 품질 점수와 권고안이 시맨틱 검색과 함께 AgentCore 메모리에 저장되고 실시간 세션 기반 웹 대시보드로 표면화된다.**
- 설계 결정의 핵심이 분리인데 **코드 분석 에이전트는 품질 평가에만 집중하고 정책 검사와 CVE 스캔은 AgentCore Gateway를 통해 호출되는 전용 Lambda에 위임해, 각 구성 요소를 단일 목적이며 독립적으로 갱신 가능하게 유지한다**는 것이다. Gateway의 이점도 명시된다. **외부 도구를 직접 호출이 아니라 MCP로 등록하면 에이전트를 도구 구현 세부에서 분리하고 에이전트 코드를 수정하지 않고 새 도구를 추가할 수 있다.**
- 권장 사항의 첫 항목이 원칙을 압축하는데 **각 에이전트를 단일하고 잘 정의된 책임으로 설계하라는 것이고 ER 다이어그램 에이전트는 ER 다이어그램만 생성하며, 조합 가능성은 개별 에이전트를 과부하시키는 데서가 아니라 오케스트레이션에서 나온다**는 것이다. 그리고 관측성은 미룰 수 없다고 못 박는다. **첫날부터 OpenTelemetry로 계측하라는 것인데 프롬프트 효과를 디버깅하고 성능 병목을 식별하는 데 필수적이기 때문이다.**

## Source

**AI-driven development lifecycle using Amazon Bedrock AgentCore** — Arghya Banerjee, Ram Pathangi, Kunal Ghosh, Ananth Kommuri, AWS Machine Learning Blog, 2026년 9월 3일

저자 네 명 모두 AWS의 Sr. Solutions Architect이며 대부분 샌프란시스코 베이 에어리어 소속이다.

<div align="center">

[aws.amazon.com/ko/blogs/machine-learning/ai-driven-development-lifecycle-using-amazon-bedrock-agentcore](https://aws.amazon.com/ko/blogs/machine-learning/ai-driven-development-lifecycle-using-amazon-bedrock-agentcore/)

</div>

## Knowledge

### 간극을 메운다는 문제 설정

글은 대상 독자의 어려움을 먼저 지목한다. AI-DLC를 Amazon Bedrock AgentCore와 Kiro 같은 코딩 에이전트로 채택하는 엔지니어링 팀들이, 개념 프레임워크와 동작하는 코드 사이의 간극에서 자주 어려움을 겪는다는 것이다. 그리고 두 축의 정의가 제시된다. Amazon Bedrock AgentCore는 어떤 프레임워크나 모델로도 규모에 맞게 에이전트를 구축하고 연결하고 최적화하기 위한 서비스라는 것이다. AI-DLC는 AI를 소프트웨어 개발 수명주기 전반의 중심 협력자로 배치해 일상적 실행을 처리하게 하면서 사람은 중요한 결정에 대한 감독을 유지하는 것이라고 규정된다. 그래서 이 글의 역할이 명확하다. 동작하는 참조 구현으로 그 간극을 메운다는 것이다.

다룰 범위도 구체적으로 밝힌다. 이 글은 Amazon Bedrock AgentCore와 Kiro, 그리고 로컬 에이전틱 코딩 도구를 사용해 AI-DLC 구축 단계 패턴을 보여주는 두 개의 참조 구현 뒤에 있는 아키텍처와 설계 결정, 핵심 코드 패턴을 훑는다는 것이다. 첫 번째는 AgentCore 런타임을 사용해 SQL 스키마에서 Mermaid 엔티티 관계 다이어그램을 생성한다는 것이다. 두 번째는 AgentCore Gateway와 AgentCore 메모리, 그리고 외부 도구 통합을 사용하는 다중 에이전트 아키텍처를 통해 자동화된 코드 보안 분석을 제공한다는 것이다. 그리고 두 구현의 공통 취지가 정리된다. 함께 놓고 보면 전달 속도를 높이면서도 휴먼 인 더 루프 거버넌스를 유지하는 AI 주도 워크플로를 어떻게 구조화하는지 보여준다는 것이며 두 구현 모두 각자의 GitHub 저장소에 있는 완전한 배포 지침으로 연결된다고 한다.

구축 단계의 성격도 규정된다. AI-DLC 구축 단계는 AI가 아키텍처를 제안하고 구현 계획을 생성하고 코드를 산출하고 배포 아티팩트를 만들도록 배치하며 팀원들은 기술적 결정에 대한 설명을 실시간으로 제공한다는 것이다. 그리고 두 구현이 이 패턴에 직접 대응한다고 밝힌다. 자동화된 아티팩트 생성은 에이전트가 구조화된 입력인 SQL 스키마 파일을 받아 상세한 계획을 만들고 산출물인 Mermaid ER 다이어그램을 생성해 사람의 검토를 위해 결과를 저장하는 것이다. 지속적인 코드 품질 강제는 다중 에이전트 시스템이 CI/CD 파이프라인을 통해 푸시된 코드를 분석해 보안 평가와 CVE 검사, 정책 준수 보고서를 산출해 사람의 의사결정에 정보를 제공하는 것이다. 그래서 공통 기반이 지목된다. 두 시스템 모두 AgentCore 위에 구축된 공통 아키텍처 기반을 공유하며 팀이 모듈화되고 관리 가능한 구성 요소로부터 AI 주도 워크플로를 조합할 수 있음을 보여준다는 것이다.

### 사례 1 — SQL 스키마에서 ER 다이어그램으로

첫 번째 프로젝트가 소개된다. 이 AWS Samples 프로젝트는 Amazon Bedrock AgentCore 위의 에이전틱 AI 워크플로를 사용해 SQL 스키마 파일에서 Mermaid ER 다이어그램을 자동 생성한다는 것이다. 흐름이 명시된다. 개발자가 SQL 코드를 체크인한 뒤 Amazon S3 트리거와 AWS Lambda 함수 기반 워크플로가 AgentCore 런타임을 호출하고 런타임이 데이터 정의 언어를 파싱해 .mmd 다이어그램을 산출해 S3로 다시 저장한다는 것이다. 그리고 경계가 강조된다. 스키마 메타데이터인 테이블과 제약, 외래키만 읽고 행 데이터는 절대 읽지 않으므로 스키마에서 다이어그램으로 가는 자동화의 깔끔한 참조가 된다는 것이다.

비즈니스 과제도 명확하다. 진화하는 SQL 스키마를 관리하는 데이터베이스 팀들은 현행 엔티티 관계 문서가 필요한데, ER 다이어그램의 수동 작성은 시간이 많이 들고 문서는 실제 스키마로부터 자주 표류한다는 것이다. 그래서 요구가 정리된다. 스키마 변경이 풀 리퀘스트를 통해 반영될 때, 팀은 개발 워크플로에 수동 문서화 단계를 추가하지 않으면서 갱신된 다이어그램을 필요로 한다는 것이다.

아키텍처가 서버리스 이벤트 기반으로 구성된다. S3 이벤트 트리거는 S3 버킷에 업로드된 SQL 파일이 분석 워크플로를 시작하는 Lambda 함수를 트리거하는 것이다. 인증은 Amazon Cognito가 OAuth2 머신 투 머신 인증을 제공하며 클라이언트 자격 증명은 AWS Systems Manager Parameter Store에 저장된다는 것이다. AgentCore 런타임에서는 Strands 프레임워크로 구축된 컨테이너화된 에이전트가 실행되며 에이전트는 Amazon Bedrock을 통해 Claude Sonnet 4를 사용해 SQL DDL 문을 파싱하고 Mermaid ER 다이어그램 구문을 생성한다는 것이다. AgentCore 메모리는 90일 만료의 지속적 세션 컨텍스트를 제공하며 이전 분석에 대한 시맨틱 검색과 점진적 스키마 이해를 지원한다는 것이다. 출력 저장은 생성된 .mmd 다이어그램 파일이 전용 프리픽스 아래 S3에 저장되며 원본 파일과 생성 타임스탬프를 추적하는 메타데이터가 함께 붙는다는 것이다.

워크플로가 다섯 단계로 진행된다. SQL 파일이 수동으로 또는 CI/CD 파이프라인을 통해 S3에 업로드된다. Lambda 트리거가 파일 내용을 읽고 Cognito OAuth를 통해 인증한다. 트리거가 SQL 내용을 페이로드로 하여 AgentCore 런타임 에이전트를 호출한다. 에이전트가 스키마를 분석해 테이블과 컬럼, 제약, 외래키 관계를 식별한 뒤 완전한 Mermaid erDiagram을 생성한다. 다이어그램이 S3에 저장되고 분석 세션이 AgentCore 메모리에 저장된다.

구현 세부에서 에이전트는 BedrockAgentCoreApp 런타임 래퍼와 @app.entrypoint 데코레이터를 사용해 핸들러를 등록한다고 밝힌다.

```python
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from bedrock_agentcore.memory import MemoryClient
from strands import Agent
from strands.models import BedrockModel

app = BedrockAgentCoreApp()
model = BedrockModel(model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0", region_name="us-west-2")
erdiagram_agent = Agent(model=model)
memory_client = MemoryClient(region_name="us-west-2")

@app.entrypoint
async def generate_er_diagram(payload: Dict[str, Any]) -> Dict[str, Any]:
    sql_content = payload.get("sql_content", "")
    file_name = payload.get("file_name", "unknown_file.sql")
    # Generate diagram, store in memory, save to S3
    ...
```

핵심 설계 결정이 셋으로 정리된다. 청크 처리는 큰 SQL 파일을 관리 가능한 세그먼트로 분할해 독립적으로 분석한 뒤 통합된 다이어그램으로 합치는 것이며 이를 통해 컨텍스트 한계를 초과하지 않으면서 수백 개 테이블을 가진 스키마를 처리한다는 것이다. 구조화된 프롬프팅은 에이전트가 다이어그램 구문을 생성하기 전에 테이블과 컬럼, 데이터 타입, 기본키, 외래키 관계를 추출하는 체계적인 분석 프롬프트를 사용하는 것이다. OpenTelemetry 트레이싱은 모든 단계가 스팬과 속성으로 계측되어 처리 시간과 청크 수, 오류 귀속에 대한 관측성을 제공하는 것이다.

그리고 저장소가 안내된다. OpenAI Codex 스킬과 MCP 서버 통합을 포함한 완전한 구현이 sample-to-create-mermaid-entity-diagrams-from-sql-using-agentic-ai-on-agentcore 저장소에서 이용 가능하다는 것이다.

### 사례 2 — 안전한 소프트웨어 인계

두 번째 구현이 소개된다. 이 서버리스 코드 보안 분석 솔루션은 Amazon Bedrock AgentCore를 사용해 Python 또는 Java 코드를 자동으로 스캔해 보안 취약점과 의존성의 CVE 위험, 정책 위반을 찾는다는 것이다. 트리거가 명시된다. 분석은 GitLab 파이프라인에서 코드가 S3로 푸시될 때 트리거된다는 것이다. 처리 경로도 구체적이다. 그다음 Strands 기반 에이전트가 Amazon Bedrock의 Anthropic Claude Sonnet 모델을 사용해 코드를 평가하고 CVE와 정책 검사를 위해 AWS Lambda에서 실행되는 Model Context Protocol 도구를 호출한다는 것이다. 산출물이 수치와 함께 제시된다. 1에서 10까지의 품질 점수와 권고안을 포함한 결과가 시맨틱 검색과 함께 AgentCore 메모리에 저장되고 실시간 세션 기반 웹 대시보드를 통해 표면화된다는 것이다. 그리고 부대 구성이 붙는다. Amazon Cognito가 인증을 제공하고 AgentCore Observability와 Amazon CloudWatch가 모니터링을 제공한다는 것이다.

비즈니스 과제가 진단된다. 보안 준수를 위한 코드 리뷰는 CVE 데이터베이스와 조직의 코딩 정책, 언어별 보안 패턴에 걸친 전문 지식을 요구한다는 것이다. 그래서 두 가지 문제가 지목된다. 수동 보안 리뷰는 전달 파이프라인에 병목을 만들고 팀 간 표준 적용의 비일관성은 가변적인 코드 품질로 이어진다는 것이다.

아키텍처가 개발 단계 간 안전한 소프트웨어 인계를 위한 다중 에이전트 구조로 제시된다. 코드 파일이 수동으로 또는 CI/CD 파이프라인을 통해 S3 버킷에 업로드되면, Lambda 트리거가 새 업로드를 감지해 OAuth2 인증과 함께 AgentCore 분석 워크플로를 시작한다는 것이다. MCP 도구를 가진 AgentCore Gateway가 외부 도구 통합 호출을 오케스트레이션하는데, 정책 검사 Lambda는 조직별 보안 정책에 대해 코드를 검증하고 CVE 데이터베이스 검사 Lambda는 알려진 취약점을 찾기 위해 의존성 파일을 스캔한다는 것이다. Strands 프레임워크의 AgentCore 런타임에서는 핵심 분석 에이전트가 구조 평가와 로직 품질 평가, 메모리 및 성능 분석, 보안 문제 탐지, 모범 사례 준수를 포함한 심층 코드 리뷰를 수행한다는 것이다. AgentCore 메모리는 시맨틱 검색 능력과 함께 분석 결과를 저장해 이력 비교와 추세 분석을 지원한다는 것이다. 대시보드 Lambda는 파일과 위반, 품질 지표에 걸쳐 검색과 다중 탭 내비게이션을 제공하는 세션 기반 결과 웹 UI를 서빙한다는 것이다.

핵심 기능 중 다차원 분석이 먼저 제시된다. 시스템은 구조적 품질과 알고리즘 효율성, 보안 태세, 표준 준수에 걸쳐 코드를 평가하며 구체적인 권고안과 함께 품질 점수를 산출한다는 것이다.

메모리 전략이 세 가지로 구분된다. 시맨틱 전략은 컨텍스트로 검색할 수 있도록 상세한 코드 분석 결과와 CVE 결과, 정책 위반을 저장한다는 것이다. 요약 전략은 대시보드 시각화를 위해 집계된 지표와 추세를 유지한다는 것이다. 사용자 선호 전략은 세션 간 대시보드 레이아웃과 필터 선호를 추적한다는 것이다.

Gateway를 통한 MCP 도구 통합의 이점도 명시된다. 이 기능은 에이전트가 분석 중 필요에 따라 정책 검사기와 CVE 스캐너 같은 외부 도구를 호출할 수 있게 하는데, 도구 호출이나 외부 API 로직을 에이전트 자체에 하드코딩하지 않고서 그렇게 한다는 것이다.

분석 에이전트는 사례 1과 동일한 AgentCore 런타임 패턴을 따르며 AgentCore Gateway를 통해 라우팅되는 MCP 도구 호출이 추가된다고 밝힌다.

```python
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from bedrock_agentcore.memory import AgentCoreMemory
from strands import Agent
from strands.models import BedrockModel

app = BedrockAgentCoreApp()
model = BedrockModel(model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0", region_name="us-west-2")
analysis_agent = Agent(model=model, tools=[analyze_code, check_quality])
memory = AgentCoreMemory(namespace="code-analysis")

@app.entrypoint
async def analyze_uploaded_code(payload: Dict[str, Any]) -> Dict[str, Any]:
    file_content = payload.get("file_content", "")
    file_name = payload.get("file_name", "unknown.py")
    session_id = payload.get("session_id", "")
    # Analyze code, store results in memory, return quality score
    ...
```

동작 순서가 정리된다. 에이전트가 Lambda 트리거로부터 코드 내용을 받아 파운데이션 모델을 사용해 다차원 분석을 수행한 뒤, 필요에 따라 AgentCore Gateway를 통해 정책 검사기와 CVE 스캐너 같은 외부 도구를 호출한다는 것이다. 결과는 대시보드 검색과 이력 비교를 위해 AgentCore 메모리에 영속화된다고 한다.

핵심 설계 결정이 셋으로 제시된다. 다중 에이전트 분리는 코드 분석 에이전트가 품질 평가에만 집중하고 정책 검사와 CVE 스캔은 AgentCore Gateway를 통해 호출되는 전용 Lambda 함수에 위임해, 각 구성 요소를 단일 목적이며 독립적으로 갱신 가능하게 유지하는 것이다. 세션 기반 결과 영속화는 각 분석 실행이 AgentCore 메모리에 고유한 세션을 생성하고 대시보드가 세션 ID로 결과를 검색해 개발자가 여러 코드 제출에 걸쳐 품질 점수를 비교할 수 있게 하는 것이다. Gateway 매개 도구 호출은 외부 도구를 직접 호출이 아니라 MCP를 사용해 AgentCore Gateway를 통해 등록하는 것이며 이것이 에이전트를 도구 구현 세부에서 분리하고 에이전트 코드를 수정하지 않고 새 도구를 추가할 수 있게 한다는 것이다.

완전한 구현은 sample-agentic-secure-software-handoffs 저장소에서 이용 가능하다고 안내된다.

### 로컬 에이전틱 도구 결합 — Kiro와 Codex, Claude Code

역할 구분이 먼저 제시된다. AgentCore가 배포된 이벤트 기반 에이전트 워크로드를 위한 클라우드 런타임을 제공하는 반면, 개발 워크플로 자체는 개발자의 워크스테이션에서 AI-DLC 패턴을 구현하는 로컬 에이전틱 도구의 이점을 본다는 것이다.

Kiro는 구조화된 명세와 커스텀 에이전트 스킬을 통해 AI-DLC의 착상 단계와 구축 단계를 지원한다고 한다. 스펙 주도 개발은 Kiro가 자연어 요구사항을 수용 기준을 가진 구조화된 명세로 변환한 뒤 그 명세로부터 구현 계획을 생성하는 것이며 이것이 AI가 계획을 만들고 실행 전에 사람의 검증을 구하는 AI-DLC 패턴에 직접 대응한다는 것이다. 커스텀 스킬은 팀이 조직 표준인 코딩 패턴과 보안 요구사항, 아키텍처 지침을 인코딩하는 재사용 가능한 Kiro 에이전트 스킬을 정의할 수 있게 해, AI가 생성한 코드가 일관되게 엔터프라이즈 품질 기준을 충족하게 하는 것이다. 에이전틱 태스크 실행은 Kiro의 에이전트 모드가 파일 생성과 터미널 명령, 검색 같은 자율적 도구 사용으로 다중 파일 구현 작업을 처리하면서 각 명세 체크포인트에서 휴먼 인 더 루프 검토를 유지하는 것이다.

OpenAI ChatGPT Codex 통합도 포함된다고 밝힌다. 저장소는 동일한 ER 다이어그램 생성 워크플로가 MCP와 커스텀 스킬을 통해 추가 코딩 에이전트로 확장되는 방식을 보여주는 Codex 통합을 포함한다는 것이다. 라이브 데이터베이스 스키마 접근을 위한 MCP 서버는 로컬 stdio 기반 MCP 서버가 INFORMATION_SCHEMA를 통해 Codex를 MySQL 또는 Amazon Aurora MySQL 데이터베이스에 연결하는 것이며 서버는 schema_summary와 generate_er_markdown, generate_mermaid라는 세 도구를 노출해 Codex가 테이블 행 데이터에 접근하지 않고 테이블 구조와 컬럼, 인덱스, 외래키 관계를 질의할 수 있게 한다는 것이다. 커스텀 Codex 스킬은 SKILL.md 파일이 ER 다이어그램 생성 워크플로를 재사용 가능한 Codex 스킬로 인코딩해 일관된 품질로 스키마 분석과 다이어그램 생성을 안내하는 것이다. 안전한 자격 증명 관리는 데이터베이스 자격 증명이 TLS 검증이 강제된 상태로 AWS Secrets Manager에서 검색되며 AgentCore 구현에서 사용된 것과 동일한 보안 패턴을 따른다는 것이다.

Claude Code는 AgentCore 배포를 보완하는 로컬 커맨드라인 에이전트로 동작한다고 규정된다. 빠른 프로토타이핑은 AgentCore 런타임에 배포하기 전에 개발자가 Claude Code를 사용해 에이전트 로직을 반복하고 프롬프트를 테스트하고 도구 통합 패턴을 로컬에서 검증하는 것이다. 코드형 인프라 생성은 Claude Code가 배포 스크립트와 Dockerfile, IAM 정책, CloudFormation 템플릿을 생성하는 것이며 이 아티팩트들은 AI-DLC 구축 단계에서 산출된 아키텍처 명세를 따른다는 것이다. 코드 리뷰와 리팩터링은 로컬 에이전트가 프로젝트 규칙과 커스텀 지침에 대해 1차 리뷰를 수행해, 코드가 CI/CD 파이프라인에 들어가기 전에 문제를 잡아내는 것이며 파이프라인에서는 안전한 소프트웨어 인계 시스템이 권위 있는 보안 분석을 제공한다는 것이다.

### 결합된 워크플로 — 볼트라는 단위

전체 흐름이 네 단계로 정리된다. 이 도구들을 사용하는 전형적인 AI-DLC 볼트가, 짧고 강도 높은 작업 주기라는 설명과 함께 다음 패턴을 따른다는 것이다.

착상 단계에서는 Kiro가 비즈니스 요구사항을 수용 기준을 가진 명세로 변환하며 팀은 몹 정교화 세션에서 AI가 생성한 명세를 검증한다는 것이다. 구축 단계에서는 Claude Code와 Kiro가 구현 코드와 배포 스크립트, 테스트 스위트를 생성하는데, 로컬 에이전트가 파일 생성과 반복적 개선을 처리하는 동안 Kiro가 태스크 오케스트레이션을 관리한다는 것이다. 검증 단계에서는 CI/CD를 통해 푸시된 코드가 자동화된 보안 분석을 트리거하고 다중 에이전트 시스템이 병합 전에 품질 평가를 제공한다는 것이다. 운영 단계에서는 ER 다이어그램 생성기 같은 프로덕션 에이전트가 AgentCore 런타임에서 지속적으로 실행되며 이벤트로 트리거되어 완전한 관측성과 함께 규모에 맞게 워크로드를 처리한다는 것이다.

### 여덟 가지 권장 사항

이 시스템들을 구현한 경험을 바탕으로 권장한다고 전제한 뒤 여덟 항목이 제시된다.

에이전트 관심사를 분리하라는 것이 첫째다. 각 에이전트를 단일하고 잘 정의된 책임으로 설계하라는 것이며 ER 다이어그램 에이전트는 ER 다이어그램만 생성한다는 것이다. 그리고 원칙이 못 박힌다. 조합 가능성은 개별 에이전트를 과부하시키는 데서가 아니라 오케스트레이션에서 나온다는 것이다.

컨텍스트 연속성을 위해 AgentCore 메모리를 쓰라는 것이 둘째다. 지속적 메모리는 에이전트가 이전 상호작용에서 배우고 현재 분석을 이력 기준선과 비교하며 재처리 없이 세션 간 상태를 유지할 수 있게 한다는 것이다.

첫날부터 OpenTelemetry로 계측하라는 것이 셋째다. 트레이싱은 에이전트 행동과 처리 시간, 실패 모드에 대한 가시성을 제공한다는 것이고 이유가 명시된다. 프롬프트 효과를 디버깅하고 성능 병목을 식별하는 데 필수적이라는 것이다.

Parameter Store에 설정을 저장하라는 것이 넷째다. 설정을 코드에서 분리하라는 것이며 Cognito 자격 증명과 메모리 ID, 모델 선택, 버킷 이름이 모두 런타임에 검색 가능해야 한다는 것이다.

큰 입력에 청크 처리를 구현하라는 것이 다섯째다. 모델 컨텍스트 윈도를 초과하는 입력을 분할하고 독립적으로 분석하고 결과를 통합해 처리하도록 에이전트를 설계하라는 것이다.

Cognito M2M 인증으로 보안을 확보하라는 것이 여섯째다. 서비스 간 통신에 OAuth2 클라이언트 자격 증명 흐름을 사용하고 하드코딩된 자격 증명이나 장기 유효 토큰을 피하라는 것이다.

수동 업로드가 아니라 CI/CD를 통해 통합하라는 것이 일곱째다. 프로덕션에서는 수동 파일 업로드를 요구하는 대신 에이전트를 병합 요청과 파이프라인 단계 같은 저장소 이벤트에 연결하라는 것이다. 그리고 이식성이 언급된다. 여기서 보여준 S3 트리거 패턴은 GitLab 웹훅이나 GitHub Actions 통합으로 직접 번역된다는 것이다.

프로덕션 에이전트 출력에 Amazon Bedrock Guardrails를 적용하라는 것이 여덟째다. 에이전트가 생성한 응답이 책임 있는 AI 표준을 충족하도록 콘텐츠 필터링 정책과 금지 주제 탐지, 그라운딩 검증을 구성하라는 것이다. 그리고 용도별 예시가 붙는다. 코드 분석 에이전트에 대해서는 가드레일이 안전하지 않은 코드 패턴이나 환각된 CVE 참조를 담은 출력을 차단할 수 있다는 것이다. 다이어그램 생성 에이전트에 대해서는 그라운딩 검사가 출력이 원본 스키마를 정확히 반영하는지 검증한다는 것이다. 마지막으로 결합이 권고된다. 에이전트 행동을 지속적으로 모니터링하고 기대 출력 품질로부터의 표류를 표시하기 위해 가드레일을 자동화된 평가 파이프라인과 결합하라는 것이다.

### 결론과 다음 단계

결론이 조건절로 정리된다. AI-DLC 방법론은 구체적인 구현 패턴으로 뒷받침될 때 실용적이 된다는 것이다. 그리고 역할 분담이 다시 요약된다. Amazon Bedrock AgentCore가 컨테이너화된 에이전트와 지속적 메모리, 안전한 게이트웨이, 외부 도구 통합이라는 런타임 인프라를 제공하는 동안, Kiro와 Claude Code 같은 로컬 도구가 개발 워크플로 자체를 가속한다는 것이다.

시작 경로도 순서대로 제시된다. 첫 AgentCore 에이전트를 배포하려면 SQL-to-ER-Diagram 샘플로 시작하라는 것이다. 배포 스크립트를 순서대로 따른 다음, 안전한 소프트웨어 인계 샘플을 사용해 다중 에이전트 조율과 MCP 도구 통합, CI/CD 주도 트리거로 패턴을 확장하라는 것이다. 더 깊이 들어가려면 에이전트를 프로덕션 규모로 가져가는 보완적 안내를 담은 문서를 보라고 권하며 전체 서비스 세부와 API 참조, 설정 지침은 Amazon Bedrock AgentCore 문서를 참조하라고 안내한다.

## 더 생각해보기

- 개념 프레임워크와 동작하는 코드 사이의 간극이 문제라면, 참조 구현 두 개로 그 간극이 실제로 메워지는가.
- 행 데이터를 절대 읽지 않는다는 경계는 스키마 문서화 자동화에서 어디까지 일반 원칙이 될 수 있는가.
- 1에서 10까지의 품질 점수는 어떤 근거로 산출되며, 병합 게이트로 쓸 만큼 신뢰할 수 있는가.
- 세 가지 메모리 전략을 나눈 설계는 어느 규모부터 관리 비용이 이득을 넘어서는가.
- Gateway 매개 도구 호출이 에이전트를 도구 세부에서 분리한다면, 그 대가로 생기는 지연과 실패 지점은 어떻게 다루는가.
- 조합 가능성이 오케스트레이션에서 나온다는 원칙은 에이전트 수가 늘어날 때 조율 비용을 어떻게 통제하는가.
- 첫날부터 OpenTelemetry로 계측하라는 권고는 프로토타입 단계에서도 정당한가.
- 청크 처리로 수백 개 테이블을 다룬다면, 청크 간 관계가 끊기는 문제는 통합 단계에서 어떻게 보장되는가.
- 환각된 CVE 참조를 가드레일로 차단한다는 접근은 오탐과 미탐 중 어느 쪽을 감수하는가.
- 로컬 도구가 1차 리뷰를 하고 파이프라인이 권위 있는 분석을 한다는 이층 구조는 중복 비용을 정당화하는가.
