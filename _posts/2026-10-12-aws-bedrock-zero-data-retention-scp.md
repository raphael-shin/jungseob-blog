---
layout: post
title: "Amazon Bedrock에서 데이터 보존을 조직 차원에서 통제하는 법, Bedrock Projects와 SCP로 만드는 제로 데이터 보존"
date: "2026-10-12 12:54:17 +0900"
created: "2026-10-12T12:54:17+09:00"
source: "https://aws.amazon.com/ko/blogs/security/enforce-zero-data-retention-on-amazon-bedrock-with-bedrock-projects-and-service-control-policies/"
source_title: "Enforce zero data retention on Amazon Bedrock with Bedrock Projects and service control policies"
author: jungseob
source_author: "AWS Security Blog (작성자 표기를 페이지에서 찾지 못함)"
source_published: "2026-07-07"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "AWS Security Blog 글을 자세히 정리한다. Bedrock의 데이터 보존 모드가 허용 상한이라는 개념, 프로젝트 단위 격리, 조직 전체를 막는 SCP 구성, 교차 리전 추론과의 관계, 검증 절차를 다루고 블로그와 최신 공식 문서 사이의 용어 차이를 짚는다."
image:
  path: "https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2026/07/07/Enforce-zero-data-retention-on-Amazon-Bedrock-with.jpg"
  alt: "AWS Security Blog 대표 이미지 · Enforce zero data retention on Amazon Bedrock"
tags:
  - knowledge
  - blog
  - AWS
  - Bedrock
  - 보안
  - 거버넌스
  - web
---

## TL;DR

- 이 글은 Amazon Bedrock이 추론 요청의 프롬프트와 출력을 보존할지 여부를 계정·프로젝트 단위로 통제하는 방법을 설명한다. 핵심 개념은 보존 모드가 "허용하는 최대치"라는 것이다. 모드를 높게 잡아도 제로 보존을 지원하는 모델은 계속 제로 보존으로 동작하고, 모드를 `none`으로 두면 보존이 필요한 모델이 막힌다.
- 통제 수단은 세 겹이다. 계정 수준 모드, `bedrock-mantle` 엔드포인트에서만 쓰는 프로젝트 수준 모드, 그리고 AWS Organizations의 서비스 제어 정책(SCP)이다. SCP는 계정 관리자도 우회할 수 없어 가장 강한 강제 수단이다.
- 운영상 가장 위험한 함정은 새 계정이 `none`이 아니라 `inherit`가 기본값이라는 점이다. SCP는 값을 바꾸지 못하게 막을 뿐 설정해 주지는 않으므로, 연결하기 전에 각 계정을 먼저 `none`으로 세팅해야 한다.
- 이 글은 2026-07-07에 올라왔고 같은 해 8월 13일에 Batch API 언급이 빠지는 수정을 거쳤다. 링크된 최신 공식 문서에서는 `provider_data_share`가 legacy가 되고 `aws_review`가 현재 방식으로 바뀌었다. 블로그의 "제3자 모델 제공자와 데이터 공유"라는 서술과 문서의 "현재 모델 제공자와의 공유는 지원하지 않는다"는 서술이 다르므로, 실제 적용 때는 공식 문서를 기준으로 삼아야 한다.
- 이 노트는 블로그 본문 전체와 링크된 데이터 보존 공식 문서, re:Post 자동화 글의 핵심을 읽었다. 본문 이미지와 표는 텍스트로 가져오지 못했고 모든 설정은 실제 계정에서 실행해 보지 않았다.

## 이 글이 다루는 문제

글은 모델 제공자와 데이터를 공유해야 하는 모델이 나온 상황에서 시작한다. 예로 Claude Fable 5가 언급된다. 이런 모델이 생기면 조직은 데이터 보존 정책을 중앙에서 강제할 방법이 필요하다. Bedrock은 추론이 끝난 뒤 프롬프트와 출력을 보존할지 여부를 고객이 정하게 한다. 필자는 모든 계정에 같은 보존 설정을 강제하는 방법과, 선택한 모델이 허용하는 범위 안에서 프로젝트 단위로 세밀하게 통제하는 방법을 함께 안내한다. 글이 약속하는 학습 목표는 다섯 가지다. 보존 모드가 어떻게 동작하는지, 보존 요건이 다른 워크로드를 프로젝트로 나누는 방법, 조직의 누구도 데이터 공유를 켜지 못하게 하는 SCP를 쓰고 배포하는 방법, 교차 리전 추론 프로파일과의 상호작용, 설정이 제대로 동작하는지 확인하는 방법이다.

## 보존 모드의 의미

Bedrock은 계정에 설정하는 모드 값으로 각 추론 요청이 끝난 뒤 프롬프트와 출력을 어떻게 처리할지 정한다. 필자는 모든 모델이 보존이나 공유를 요구하는 것은 아니며 요구하지 않는 모델은 계속 그대로 쓸 수 있다고 강조한다. 어떤 모델이 보존을 요구하는지는 공식 문서의 목록을 봐야 하고 컴플라이언스에 맞는 모델을 고르는 책임은 고객에게 있다.

한 가지 예외는 글머리에 별도 주의로 붙는다. 아동 성착취물(CSAM) 확산을 막기 위해 Bedrock은 입력과 출력에서 자동 탐지를 하며 플래그된 내용은 신고를 위해 저장하고 검토할 수 있다. 모드가 `none`이어도 마찬가지다. 즉 제로 보존에도 이 안전 목적의 예외는 남는다.

글이 가장 중요하다고 말하는 개념은 "상한이지 하한이 아니다"라는 것이다. 설정한 모드는 내가 받아들일 수 있는 보존의 최대치이지 모든 요청이 실제로 쓰는 값이 아니다. 계정을 `provider_data_share`로 설정해도 모든 요청이 갑자기 데이터를 보존하고 공유하기 시작하는 것은 아니다. 제로 보존을 지원하는 모델은 계정 설정과 무관하게 제로 보존으로 동작한다. 필자는 이를 권한 천장에 비유하며 Bedrock이 계정 모드가 허락한다는 이유만으로 필요 이상의 보존을 주지 않도록 설계되었다고 쓴다.

세 가지 보충 설명이 이어진다. 첫째, `provider_data_share`는 모델에서 상속되지 않는다. 계정이나 프로젝트에서 명시적으로 옵트인해야 한다. 계정이 `inherit`나 기본값이면 어떤 모델도 설정 없이 제공자 데이터 공유를 일으키지 못한다. 둘째, `inherit`는 위 범위의 값을 따른다. 프로젝트는 계정을, 계정은 서비스 기본값을 따르며 프로젝트가 `inherit`이고 계정이 `provider_data_share`이면 프로젝트도 그 값이 된다. 셋째, 일부 API는 모델 지원 여부와 상관없이 보존을 필요로 한다. 예로 `store=true`인 Responses API가 있다. 모드를 `none`으로 두면 이런 API는 막히고 이는 정상 동작이다. 보존이 없어야 한다는 상한을 정했으니 보존 없이는 동작하지 못하는 API는 쓸 수 없다는 논리다.

왜 이런 모드가 있느냐에 대해서는 이렇게 설명한다. 일부 파운데이션 모델은 `provider_data_share` 모드가 있어야 동작한다. 이런 모델은 `allowed_modes`가 `provider_data_share`뿐이어서 계정이 명시적으로 옵트인하지 않으면 사용 불가로 표시된다. AWS는 고객이 데이터 공유를 의식적으로 결정한 뒤에야 이 모델을 쓰도록 하겠다는 취지이며 최신 목록은 문서를 확인해야 한다.

## 통제 수단 세 가지

글은 통제를 세 겹으로 쌓아 각각 단독으로, 또는 심층 방어로 함께 쓰라고 한다.

첫째 수단은 Bedrock Projects다. 한 계정 안에서도 워크로드마다 보존 요건이 다르다. `bedrock-mantle` 엔드포인트(OpenAI 호환 API)를 쓴다면 프로젝트로 보존을 받아들일 수 있는 트래픽과 절대 보존하면 안 되는 트래픽을 같은 계정 안에서 나눌 수 있다. 글의 예는 최신 모델을 써 보려는 연구 프로젝트와 고객 데이터를 다루는 운영 프로젝트다. 연구 프로젝트에는 `provider_data_share`를 주고 운영 프로젝트는 `none`으로 잠근다. 프로젝트마다 자기 보존 상한을 독립적으로 강제한다.

프로젝트 수준 규칙은 단순하다. 프로젝트는 자기 모드를 따로 가질 수 있다. `inherit`인 프로젝트는 계정 값을 따른다. `none`인 프로젝트는 계정 설정과 무관하게 제로 보존을 강제하고 그 프로젝트를 거치는 트래픽은 데이터 공유를 일으킬 수 없다. `provider_data_share`인 프로젝트는 데이터 공유가 필요한 모델을 허용하되 그 프로젝트 안의 요청에만 적용된다. 이렇게 하면 새 모델을 점진적으로 도입하면서 민감한 워크로드의 거버넌스는 엄격히 유지할 수 있다. 관리는 콘솔이나 `bedrock-mantle` API로 한다.

적용 범위에 관한 강한 단서가 두 번 반복된다. Projects는 `bedrock-mantle` 엔드포인트에서만 있다. 그 엔드포인트의 OpenAI 호환 API(Responses, Chat Completions)와 Anthropic Messages API에서 동작한다. 모든 모델이 이 엔드포인트에 있는 것은 아니므로 모델별 엔드포인트 지원 현황을 확인해야 한다.

둘째 수단은 `bedrock-runtime` 엔드포인트(Invoke, Converse API)에서의 계정 분리다. 이 엔드포인트에는 프로젝트가 없어 계정 수준 모드가 모든 요청에 적용된다. 워크로드 단위 격리가 필요하면 AWS 계정을 나눈다. 데이터 공유가 필요한 워크로드는 SCP가 없는 계정이나 OU에, 제로 보존이 필요한 워크로드는 SCP를 적용한 별도 계정이나 OU에 둔다. 글은 조직 루트 아래에 제로 보존 OU(SCP 연결, 두 운영 계정)와 연구 OU(SCP 없음, 실험 계정)를 두는 구조를 트리 그림으로 보인다. 프로젝트와 SCP를 함께 쓸 때의 규칙도 중요하다. 조직 수준에서 `none`을 SCP로 강제하면 `bedrock-mantle`의 모든 프로젝트 설정을 덮어쓴다. 프로젝트 단위 유연성을 원하는 계정에는 SCP를 걸지 않고 프로젝트 격리를 쓴다. 어떤 경우에도 데이터 공유가 없어야 하는 계정에는 SCP가 두 엔드포인트에 걸쳐 우회할 수 없는 보증을 준다.

셋째 수단은 조직 전체 강제를 위한 SCP다. 누가 관리자 권한을 가졌든 어느 엔드포인트를 쓰든 어떤 계정도 데이터 공유를 켤 수 없다는 절대적 보증이 필요할 때 가장 강한 수단이다. SCP는 Bedrock 컨트롤 플레인 동작(`bedrock:PutAccountDataRetention`)과 mantle 엔드포인트 동작(`bedrock-mantle:PutAccountDataRetention`, `CreateProject`, `UpdateProject`)에 모두 적용된다.

## SCP로 제로 보존을 강제하기

SCP는 조직 수준의 가드레일이다. 계정 관리자와 루트 사용자를 포함해 조직의 모든 주체를 덮어쓴다. 전체 관리자 권한이 있어도 SCP의 Deny는 IAM 정책으로 뒤집을 수 없다. 연결 위치는 루트, OU, 개별 계정의 세 단계다. 글은 모든 계정을 덮으려면 루트 OU에 연결해야 하며 하위 OU에 연결하면 그 밖의 계정은 보호받지 못한다고 강조한다. 조직 관리 계정은 SCP 통제를 받지 않는다는 점도 두 번 나온다.

사전 조건이 가장 중요하다. 새 계정의 기본값은 `none`이 아니라 `inherit`다. SCP는 모드를 바꾸는 것을 막을 뿐 `none`으로 만들어 주지 않는다. 따라서 SCP를 붙이기 전에 각 계정에서 `aws bedrock put-account-data-retention --region us-east-1 --mode none`을 실행해 명시적으로 `none`을 세팅해야 한다. 계정이 수백, 수천 개라면 자동화가 필요하며 글은 AWS re:Post의 「Automate Bedrock Zero Data Retention Across All Accounts in Your Organization」를 안내한다. 이 노트에서 그 글을 열어 보니 같은 전제(새 계정은 `inherit`, SCP는 값을 설정하지 않음)를 반복하고 제로 보존 OU는 전면 강제하고 연구 OU는 모니터링만 하는 조직 구조를 보여 준다.

기본 정책의 구조는 이렇다. 한 개의 Deny 문장이 `bedrock:PutAccountDataRetention` 동작을 모든 리소스에 대해 막는다. 조건은 `StringNotEquals`로 `bedrock:DataRetentionMode`가 `none`이 아닐 때 거부가 발동하게 한다. 즉 `none` 외의 어떤 값으로도 바꿀 수 없다. 이 정책이 보장하는 결과는 네 가지다. 모델 제공자와의 데이터 공유를 아무도 켤 수 없고 계정 관리자도 접근 거부를 받는다. 공유가 필요한 모델(글은 Claude Fable 5와 Claude Mythos 5 등을 든다)은 조직 전체에서 영구히 쓸 수 없게 된다. `none`을 지원하는 모델은 영향이 없다. 어떤 IAM 정책도 SCP의 Deny를 넘을 수 없어 우회가 안 된다.

선택 사항으로 프로젝트 수준 우회 차단이 있다. `bedrock-mantle`은 프로젝트별 보존 설정을 지원하므로, 추가 조치가 없으면 누군가 프로젝트를 만들거나 수정하면서 `provider_data_share`를 넣어 계정 수준 제한을 우회할 수 있다. 이를 막으려면 같은 SCP의 동작 목록에 `bedrock-mantle:PutAccountDataRetention`, `bedrock-mantle:CreateProject`, `bedrock-mantle:UpdateProject`를 더한다. 글은 `bedrock-runtime`에는 이 차단이 필요 없는 이유도 밝힌다. 그 엔드포인트에는 프로젝트가 없어 보존을 바꾸는 유일한 방법이 계정 수준 동작인데, 기본 SCP가 이미 막고 있기 때문이다.

## 교차 리전 추론과 SCP의 전역성

교차 리전 추론 프로파일을 쓸 때 모드는 요청을 보낸 소스 리전에서 평가된다. 목적지 리전마다 모드를 설정할 필요는 없다. 다만 중요한 단서가 붙는다. 모드 검사는 소스 리전에서 일어나지만 데이터 자체는 추론이 처리되는 목적지 리전에 보존될 수 있다. 데이터가 지리적으로 어디에 있는지 추적해야 하는 조직에는 이 점이 중요하다.

실무적으로는 세 가지다. 소스 리전(예: us-east-1)이 `provider_data_share`이면 목적지 리전의 설정과 상관없이 교차 리전 요청이 허용된다. 소스 리전이 `none`이면 공유가 필요한 모델에 대한 요청은 목적지로 라우팅되기 전에 소스에서 차단된다. SCP는 계속 전역으로 적용되어, 루트 OU에 붙인 SCP 하나가 모든 리전에서 `provider_data_share`를 자동으로 막는다. 리전별 수동 설정에 의존하지 않는 것이 SCP를 쓰는 핵심 이점으로 꼽힌다.

참고로 최신 공식 문서는 보존 설정이 리전 단위이고 다른 리전으로 전파되지 않으며 설정하지 않은 리전은 `inherit`로 남아 각 모델의 기본값을 따른다고 쓴다. 블로그의 "SCP는 전역" 설명과 합치면, 모드 값 자체는 리전마다 따로 존재하고 그 값을 못 바꾸게 하는 SCP만 전역이라는 뜻이 된다. 또 문서는 교차 리전 추론이 켜진 경우 보존된 입출력이 요청이 처리되는 목적지 리전에 저장된다고 쓴다.

## 설정이 맞게 동작하는지 검증하기

글은 SDK, AWS CLI, 콘솔로 확인하라고 한다. 현재 모드를 보는 방법은 세 가지다. 콘솔에서는 Bedrock의 설정 아래 Data retention 메뉴를 쓴다. AWS CLI는 버전 2.35 이상이 필요하고 `aws bedrock get-account-data-retention --region us-east-1`로 조회하면 모드와 갱신 시각이 돌아온다. `bedrock-mantle` API는 Bedrock API 키를 헤더에 넣어 `/v1/data_retention` 경로를 조회하며 응답은 모드와 갱신 시각(Unix 시간)이다.

특정 모델에 실제로 적용되는 모드와 허용 모드는 `bedrock-mantle` API의 `/v1/models/{모델 ID}`로 본다. 글의 예시 응답에서 Claude Fable 5는 상태가 available이고 유효 모드가 계정에서 온 `provider_data_share`이며 `allowed_modes`가 `provider_data_share` 하나다. 모델이 unavailable이면 `status_reason` 필드가 보존 모드 충돌 이유를 설명한다.

SCP가 실제로 막는지 확인하는 방법은 일부러 `provider_data_share`로 바꿔 보는 것이다. CLI든 mantle API든 SCP가 동작하면 `AccessDeniedException`이 나오고 메시지에 "service control policy의 명시적 거부"가 들어간다. 반대로 요청이 성공하면 SCP가 동작하지 않는 것이므로 즉시 `none`으로 되돌려야 한다. 그다음 점검 항목은 세 가지다. SCP가 하위 OU가 아니라 루트 OU에 붙었는지, 정책 구문과 조건 키가 맞는지, 조직 관리 계정은 SCP 면제이므로 그 계정에는 IAM 정책으로 따로 강제해야 한다는 점이다.

공유가 필요한 모델을 쓰려는 계정(SCP를 적용하지 않은 계정)에서는 CLI의 `put-account-data-retention --mode provider_data_share`, mantle의 `PUT /v1/data_retention` 요청 본문에 모드를 담는 방식, 또는 콘솔로 설정한다. 되돌릴 때는 같은 명령에 `--mode none`을 쓴다.

프로젝트 수준 설정은 mantle API로만 한다. 프로젝트 ID 경로에 POST하고 본문에 `data_retention.mode`를 담아 `provider_data_share`나 `none`을 지정하며 같은 경로의 조회로 현재 설정을 본다. 실효 모드의 결정 규칙은 프로젝트, 계정, 모델 기본값의 순서에서 `inherit`가 아닌 첫 값을 택하는 것이다. 프로젝트가 `none`이면 계정 설정과 무관하게 제로 보존이고 `inherit`이면 계정 값을 따른다. 프로젝트 수준 보존에는 CLI 명령이 없다. 앞의 CLI 명령들은 컨트롤 플레인의 계정 수준 설정만 관리한다.

## 블로그와 최신 공식 문서의 차이

이 부분은 글에 없는 노트의 대조 결과다. 링크된 데이터 보존 공식 문서를 열어 보니 블로그 본문과 용어와 의미가 상당히 다르다.

첫째, 모드 구성이 다르다. 문서는 `none`, `default`, `aws_review`, `provider_data_share (legacy)`, `inherit` 다섯 가지를 정의한다. `aws_review`는 입출력이 AWS 내부에서 사람 검토를 위해 보존될 수 있게 하는 현재 방식이다. 모델 제공자는 내용을 보지 못하고 공유도 되지 않는다. `provider_data_share`는 legacy이며 문서는 Bedrock이 현재 모델 제공자와 내용을 공유하지 않으므로 이 모드를 설정해도 공유가 일어나지 않고 새 설정에는 `aws_review`를 쓰라고 한다. 이미 `provider_data_share`인 경우 모드 순서상 `aws_review`보다 위여서 그대로 두어도 `aws_review`를 요구하는 모델을 계속 쓸 수 있다.

둘째, 대상 모델이 다르다. 문서는 사람 검토를 요구하는 모델로 Claude Fable 5와 Claude Fable 5.1을 들고 그 `allowed_modes`가 `aws_review`와 `provider_data_share`라고 쓴다. 블로그가 함께 든 Claude Mythos 5는 문서에서 찾지 못했다. 반대로 Claude Opus 4.8처럼 `none`을 허용하는 모델은 어떤 모드를 설정해도 보존되지 않는다는 예가 문서에 있다.

셋째, 보존 기간과 위치다. 문서는 `aws_review`가 필요한 모델의 프롬프트와 완료문이 AWS 경계 안에서 최대 30일 보존되고 AWS가 검토할 수 있다고 쓴다. 블로그에는 기간이 없다. 넷째, 콘솔이다. 블로그는 콘솔 Settings의 Data retention에서 바꿀 수 있다고 쓰지만 문서는 출시 시점에 콘솔 UI가 없고 API나 SDK를 써야 한다고 쓴다. 어느 쪽이 더 최신인지, 그 사이에 콘솔이 추가되었는지는 확인하지 못했다.

다섯째, IAM 강제 방식이다. 문서는 mantle 쪽 쓰기 동작에 `bedrock-mantle:DataRetentionMode` 조건 키가 있다고 쓰고 사람 검토만 막는 예시 SCP와 `none`만 허용하는 예시 SCP를 제시한다. 블로그의 확장 SCP는 mantle 동작에도 `bedrock:DataRetentionMode` 키를 쓴다. 이 키가 mantle 동작에서 평가되는지 이 노트는 확인하지 못했다. 실제로 적용하기 전에 두 키의 동작을 테스트 계정에서 확인해야 한다. 여섯째, 문서는 모드를 `none`으로 두면 Responses API의 `store=true`가 거부되고 백그라운드 모드를 쓸 수 없으며 `default`에서도 `store=false`가 제로 보존을 보장하지 않는다고 쓴다. 보장이 필요하면 모드 자체를 `none`으로 두어야 한다.

일곱째, 제로 보존이 필요한데 보존 요구 모델이 필요한 경우다. 문서는 AWS 계정 담당자를 통해 계정별·모델별 ZDR 접근 자격을 논의할 수 있다고 쓴다. 승인된 계정은 해당 모델의 `allowed_modes`에 `none`이 들어가 보이고 Claude 모델의 ZDR 자격은 Anthropic이 관리한다.

## 읽을 때 유의할 점

첫째, 이 글은 AWS 공식 보안 블로그의 안내이며 구현 지침이다. 효과를 측정한 자료는 없고 설정 동작은 AWS의 서술에 의존한다. 이 노트는 어떤 설정도 실제 계정에서 실행해 보지 않았다. 둘째, 위 차이점 때문에 블로그만 보고 설계하면 낡은 용어와 모델 목록을 따를 수 있다. 글은 7월 7일에 게시되고 8월 13일에 수정되었으며 최신 문서는 그 이후의 변화를 반영하는 것으로 보인다. 셋째, 본문의 모드 표, 조직 구조 그림, 일부 도표는 텍스트로 가져오지 못했다. 모드 표의 정확한 내용은 문서로 대조했다. 넷째, 필자의 이름이 페이지에서 확인되지 않아 작성자를 AWS Security Blog로만 적었다. 다섯째, 글에는 실행 예시용 API 키와 계정 ID가 마스킹된 형태로 나오며 이 노트는 예시 값을 옮기지 않았다.

그럼에도 이 글에서 가져갈 점검 질문은 선명하다. 모든 계정이 `none`으로 명시 설정되어 있는가, SCP가 루트 OU에 붙었고 조직 관리 계정은 별도 IAM 정책으로 막았는가, mantle의 프로젝트 우회 동작까지 SCP에 포함했는가, 교차 리전 추론으로 데이터가 어느 리전에 남는지 추적하고 있는가, 사용 중인 모델의 `allowed_modes`를 정기적으로 확인하는가, 그리고 블로그와 공식 문서의 용어 차이를 어느 쪽 기준으로 운영할지 정했는가.

## 참고 자료

[AWS Security Blog — Enforce zero data retention on Amazon Bedrock with Bedrock Projects and service control policies](https://aws.amazon.com/ko/blogs/security/enforce-zero-data-retention-on-amazon-bedrock-with-bedrock-projects-and-service-control-policies/) — 본문 전체를 읽고 정리했다. 요청한 한국어 주소(`/ko/`)가 영문 본문을 돌려주어 영문 본문으로 읽었다. 게시일은 페이지 메타데이터의 2026-07-07이고 8월 13일 수정 안내가 붙어 있다. 대표 이미지는 글 표지다.

[Amazon Bedrock User Guide — Data retention](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html) — 모드 정의, 모드 순서, 실효 모드 결정 규칙, 보존 기간, 예시 SCP, IAM 동작 목록을 대조했다. 위 "차이" 절의 근거다. [AWS re:Post — Automate Bedrock Zero Data Retention Across All Accounts in Your Organization](https://repost.aws/articles/ARujqzEisKTLqNMFrw-dv1RA) — 새 계정 기본값과 조직 구조 부분만 확인했다. 블로그가 링크한 Anthropic의 발표와 데이터 처리 부속서(DPA), 교차 리전 추론, abuse detection 문서는 읽지 않았다.
