---
layout: post
title: 요청을 세지 않고 응답을 세면 우회당한다 - AWS가 공개한 Dogwood의 시간 조건
date: '2026-09-08'
last_modified_at: '2026-09-08T09:30:00+09:00'
author: jungseob
categories:
- 지식 노트
tags:
- AI에이전트
- 정책언어
- 런타임검증
- AWS
- 보안
description: 도구 호출이 에이전트 위험의 가장 큰 원천이라는 진단에서 출발해, 행동의 시퀀스에 관한 규칙을 표현하도록 설계되지 않은 Cedar에
  시간 조건을 더한 오픈소스 거버넌스 언어 Dogwood를 소개한 글. formerly와 count_within 같은 네 연산자, 속도 제한을 응답이
  아니라 요청으로 세야 하는 이유, 그리고 상태 추적 비용과 자동 추론 미지원이라는 대가까지 담았다.
source: https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/
source_title: 'Introducing Dogwood: runtime verification for AI agents'
source_author: Marc Brooker (AWS)
source_published: ''
published: true
render_with_liquid: false
---

# 요청을 세지 않고 응답을 세면 우회당한다

## TL;DR

- 위험의 위치가 도구 호출 경계로 특정되는데 **AI 에이전트를 유용하게 만드는 것의 일부가 도구를 실행해 외부 세계와 상호작용하는 능력인데 바로 그 도구 호출이 에이전트를 안전하게 쓰는 데서 가장 큰 위험의 원천이다.** 그래서 해법의 자리도 정해진다. **도구 호출 경계에 에이전트가 무엇을 할 수 있는지 규율하는 통제 층을 두는 것이 이 위험을 신뢰할 수 있고 확실하게 다루는 최선의 방법이다**
- Cedar의 한계도 정확히 규정되는데 **각 요청이 고립되어 평가되고 과거 행동에 의존하지 않는 시점 인증을 지원하므로 단일 행동 주위에 안전 봉투를 그릴 수는 있지만 행동들의 시퀀스에 관한 규칙을 표현하도록 설계되지 않았다.** 그래서 필요가 생긴다. **에이전트가 여러 행동을 더 긴 워크플로로 조합하면 그 시퀀스 자체가 팀들이 규율하고 싶어 하는 대상이 된다**
- Dogwood가 더하는 것은 시간 조건인데 **Cedar의 when 절이 현재 인증 요청만 보는 데 반해 Dogwood는 요청 이전에 온 것도 볼 수 있는 when temporal이라는 두 번째 절을 더한다.** 기반도 형식적이다. **런타임 검증에 뿌리를 둔 계량 1차 시간 논리 MFOTL에서 뽑아낸 핵심 연산자들로 정의되며, 행동 스키마는 에이전트가 이미 MCP로 노출하는 도구들에서 자동 생성된다**
- 가장 중요한 실무 교훈은 우회 사례로 나오는데 **속도 제한은 응답이 아니라 요청 사건으로 표현해야 하고 요청 사건은 인증이 검토되는 것까지 포함하지만 응답 사건은 완료된 이전만 포함한다.** 공격이 성립하는 방식이 구체적이다. **응답만 합산하면 에이전트는 어느 하나가 해소되기 전에 동시 요청을 많이 발행해 한도를 우회하며, 3번째 요청 시점에 6,000달러가 진행 중인데도 응답 기준 정책은 허용한다**
- 대가도 정직하게 밝히는데 **시간 정책의 표현력은 무료로 오지 않아서 평가에 사건의 상태 추적이 필요하고 평가의 시간 복잡도가 사건 로그의 길이에 의존할 수 있다.** 하나가 더 붙는다. **시간 조건은 현재 Cedar가 제공하는 강력한 자동 추론 분석 도구를 지원하지 않으며, 그것이 Cedar를 개조하는 대신 새 언어를 개발하기로 한 이유의 일부다**

## Source

**Introducing Dogwood: runtime verification for AI agents** — Marc Brooker, AWS Open Source Blog

<div align="center">

[aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents](https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/)

</div>

## Knowledge

### 도구 호출 경계라는 위치

AI 에이전트를 그토록 유용하게 만드는 것의 일부는 도구를 실행해 외부 세계와 상호작용하는 능력이다. 그리고 바로 그 도구 호출들이 에이전트를 안전하게 쓰는 데서 가장 큰 위험의 원천이다.

이 위험들을 신뢰할 수 있고 확실한 방식으로 다루는 최선의 방법은 도구 호출 경계에 통제 층을 두는 것이다. 그 층이 에이전트가 무엇을 하도록 허용되는지 규율한다. 에이전트가 도구를 어떻게 쓸 수 있는지에 대한 규칙을 강제함으로써, 에이전트가 외부 세계에 영향을 줄 수 있는 방식들에 대해 엄밀한 보장을 얻는다. 이것을 효과적으로 하려면 에이전트 행동에 관한 규칙을 정확히 명세하고 강제할 방법이 필요하다. 그래서 오늘 Dogwood를 공개한다. 에이전트와 그 도구들을 위해 설계된 오픈소스 거버넌스 언어다.

배경이 있다. 이전에 AgentCore Policy로 에이전트 도구 사용을 규율하는 논거를 제시했는데, 그것은 매 도구 호출마다 에이전트의 행동이 허용되는지 결정하는 Amazon Bedrock AgentCore의 층이다. AgentCore Policy는 그 정책들이 쓰이는 언어로 Cedar를 써서 출시됐다. Cedar는 빠르고 읽기 쉬우며 자동 추론을 통해 분석 가능하다. 그리고 감사와 강제가 의존하는 보장을 제공한다. 동일한 요청은 평가 순서나 시스템 상태와 무관하게 동일한 결정을 낸다.

### Cedar가 할 수 없는 것

Cedar는 효율적인 시점 인증 결정을 지원한다. 각 요청이 고립되어 평가되고 과거 행동에 의존하지 않는다. 그래서 어떤 단일 행동 주위에 안전 봉투를 그릴 수는 있지만 행동들의 시퀀스에 관한 규칙을 표현하도록 설계되지는 않았다.

시점 결정은 많은 형태의 접근 통제에 대해 타당하다. 문제는 에이전트가 여러 행동을 더 긴 워크플로로 조합할 때 생긴다. 그때부터 그 시퀀스 자체가 팀들이 규율하고 싶어 하는 대상이 된다.

Dogwood는 그 시퀀스에 대한 정책을 표현할 언어를 준다. 전제 조건과 속도 제한, 순서에 대한 제약을 포착하기 위한 것이다. 에이전트가 행동하기 전에 승인을 받도록 요구하고 싶을 수 있고 실행 중 한도 아래에 머물게 하고 싶을 수 있고 기밀 정보에 접근한 뒤에는 절대 외부 당사자와 접촉하지 않게 하고 싶을 수 있다. 이런 종류의 제한을 강제하려면 정책 층이 현재 요청을 넘어 되돌아볼 수 있어야 한다.

Dogwood에서 정책은 현재 요청만이 아니라 에이전트의 최근 사건들을 되돌아볼 수 있다. 기존 Cedar 정책을 평가하는 것도 지원하면서 새롭고 강력한 도구인 시간 조건을 더한다. 시간 조건은 이전 사건들의 이력을 참조한다. 그래서 에이전트가 도구를 올바른 순서로 쓰게 하고 어떤 도구들 뒤에는 다른 도구 사용을 멈추게 하고 어떤 도구들의 빈도를 제한하는 정책을 진술할 수 있다. Dogwood는 시간 논리라고 불리는 정확한 수학적 기초에 바탕을 두며 가장 결정적인 에이전틱 안전 문제를 푸는 데 필요한 강도를 준다.

AgentCore Policy 안에서 Dogwood 정책 지원도 함께 출시했다. Dogwood가 기존 Cedar 정책과 호환되므로 고객은 마이그레이션 없이 현재 정책을 계속 쓸 수 있다. 언어를 오픈소스로 공개했으니 고객은 자기가 좋아하는 IDE나 코딩 에이전트로 정책을 정의하고 Dogwood 파서와 검증기, 참조 인터프리터로 그 행동을 탐색할 수 있다. Dogwood 언어는 Apache 2.0 라이선스로 공개된다.

### 사건 추적과 행동 스키마

문법의 차이가 간단하다. `when { ... }` 절 안의 Cedar 정책 조건은 현재 인증 요청만 본다. Dogwood는 두 번째 종류의 절인 `when temporal { ... }`을 더하고 그 조건은 요청 이전에 온 것도 볼 수 있다.

시간 절은 사건들의 추적에 관한 속성을 표현한다. 각 사건은 도구 호출 요청 또는 그 결과에 대응하며 입력 인자와 요청 주체 같은 도구 호출과 연관된 데이터를 기록한다. 정책이 이야기할 수 있는 도구 호출들의 집합이 행동 스키마다. 에이전트에 대해 그 스키마는 이미 Model Context Protocol을 통해 노출하는 도구들로부터 생성된다.

`ApproveSale`과 `SellShares`, `Transfer`를 도구로 갖는 주식 거래 에이전트를 예시로 시간 정책 연산자들을 훑는다.

### 되돌아보기 — 팔기 전에 승인받아라

에이전트가 정확히 그 금액에 대한 승인을 이미 받은 경우에만 주식을 팔 수 있게 보장하고 싶다. `SellShares` 도구 호출이 앞선 사건에 의존하므로 시점 조건으로는 그것을 볼 수 없다.

```
// Permit a sale only if approval for the same amount of the same
// stock came back granted within the last hour.
permit ( principal, action == AgentCore::Action::"SellShares", resource )
when temporal {
  formerly within 1h AgentCore::Action::"ApproveSale"::response{
    input.stock: context.input.stock,
    input.shares: context.input.shares,
    output.approved: true
  }
};
```

`formerly` 연산자는 후방을 본다. 그것이 서술하는 조건이 지정된 시간 창 안에서 최소 한 번 일어났으면 성립한다. 여기서 창은 `within 1h`이므로 지난 한 시간을 되돌아보며 그 조건이 어느 시점에든 성립했는지 본다.

조건은 세 부분으로 나뉜다. 대응하는 `ApproveSale::response` 사건이 일어났어야 하는데, 그것은 어떤 앞선 `ApproveSale` 도구 호출의 결과를 나타낸다. 그 `ApproveSale`이 현재 요청의 `context.input.stock`과 `context.input.shares`에 일치하는 `input.stock`과 `input.shares` 필드를 가졌어야 한다. 그리고 그 호출의 `output.approved` 플래그가 참이었어야 하는데, 요청이 실제로 승인되었음을 나타낸다.

사건 추적의 표기법도 알아 두면 읽기 쉽다. 각 줄이 하나의 사건을 서술하고 사건 서술은 `@n` 형태의 타임스탬프로 시작하며 `n`은 사건이 일어난 시점을 초 단위로 나타낸다. Dogwood 정책에서 모든 시간 조건은 시간을 상대적으로 써서 요청과 앞선 사건들 사이의 시간 차이를 측정하므로, 이 타임스탬프의 절대값은 중요하지 않다. 타임스탬프 뒤에는 행동과 사건의 종류, 즉 도구 호출의 이름과 그것이 요청인지 응답인지가 오고 중괄호 안에 사건과 연관된 인자들이 온다. 사건이 요청일 때는 줄이 정책이 준 인증 판정으로 끝나며 DENY 또는 ALLOW다.

```
@0    SellShares::request  { stock: "AMZN", shares: 100 } -> DENY
@1700 ApproveSale::response { stock: "AMZN", shares: 100, approved: true }
@1800 SellShares::request  { stock: "AMZN", shares: 100 } -> ALLOW
@7200 SellShares::request  { stock: "AMZN", shares: 100 } -> DENY
```

첫 사건은 기록된 승인이 없어서 거부되는 요청이다. 두 번째 사건은 판매 승인 요청에 대한 응답인데, 요청이 아니므로 판정이 붙지 않지만 사건 이력에 기록되어 이후 요청에 영향을 준다. 세 번째 사건은 또 다른 요청인데 이번에는 시간 창 안에 승인이 있으므로 승인된다. 네 번째 요청은 승인이 창 밖이라서 다시 거부된다.

동시성에 대한 주의가 하나 필요하다. 이 추적에서 마지막 `SellShares::request`가 앞서 허용된 요청의 응답보다 먼저 일어난다. 에이전트가 병렬 도구 호출을 하고 도구들과 비동기적으로 상호작용할 수 있기 때문이다. 예시들은 단일 에이전트 정책에 초점을 맞추지만 이런 종류의 끼어들기는 다중 에이전트 환경에서도 생기므로, 정책을 쓸 때 이런 동시성을 염두에 두는 것이 중요하다.

### 시간 절과 비시간 절 섞기

이전 정책은 전적으로 시간적이었지만 대부분의 실제 규칙은 최근 과거에 관한 사실과 요청 자체에 관한 평범한 사실을 결합한다. 이를 지원하려고 Dogwood는 Cedar 표현식 안에 시간 절을 임베드하도록 허용한다. `temporal { ... }` 표식이 하나의 표현식이므로, 이미 쓰고 있는 Cedar와 나란히 평범한 `when` 절 안에 그대로 들어간다.

판매가 작으면서 최근에 승인되어야 한다는 규칙은 이렇게 쓴다.

```
permit ( principal, action == AgentCore::Action::"SellShares", resource )
when {
  context.input.shares <= 100
  && temporal {
    formerly within 1h AgentCore::Action::"ApproveSale"::response{
      input.stock: context.input.stock,
      input.shares: context.input.shares,
      output.approved: true
    }
  }
};
```

`context.input.shares <= 100`은 Dogwood 없이 쓸 Cedar 정책 그대로이며 현재 요청만 본다. 그 옆의 `temporal { ... }`은 최근 사건들을 되돌아본다. 요청이 인증되려면 둘 다 성립해야 한다.

```
@0   SellShares::request  { stock: "AMZN", shares: 50 } -> DENY
@60  ApproveSale::response { stock: "AMZN", shares: 50, approved: true }
@120 SellShares::request  { stock: "AMZN", shares: 50 } -> ALLOW
@180 ApproveSale::response { stock: "AMZN", shares: 500, approved: true }
@240 SellShares::request  { stock: "AMZN", shares: 500 } -> DENY
```

첫 요청은 주식 수가 Cedar 표현식이 정한 임계 아래인데도 거부되는데, 이력에 승인이 없어서 시간 쪽 절반이 실패하기 때문이다. 세 번째 줄의 요청은 주식 수가 작고 이력에 승인이 있으므로 허용된다. 마지막 요청은 이력에 승인이 있는데도 거부되는데, 주식 수가 Cedar 표현식의 임계를 초과하기 때문이다.

### 세기와 구별해서 세기와 합하기

또 다른 흔한 정책 부류는 과거에 무언가가 일어났다는 것만이 아니라 몇 번 일어났는지 아는 것을 요구한다. 가장 단순한 것은 어떤 창 안에서 사건이 일어난 모든 횟수의 평범한 셈이고 이것으로 속도 제한 정책을 쓸 수 있다. 각각이 아무리 작더라도 한 시간에 다섯 번을 넘는 이전은 안 된다는 규칙은 이렇다.

```
forbid ( principal, action == AgentCore::Action::"Transfer", resource )
when temporal {
  count_within(1h, AgentCore::Action::"Transfer"::request{ input.amount: _ }) > 5
};
```

이름이 시사하듯 `count_within`은 지난 한 시간 동안의 모든 `Transfer` 요청을 센다. `_`는 금액은 상관없고 그것이 일어났다는 것만 본다는 와일드카드다. 추적에서 다섯 번까지는 ALLOW이고 창 안의 여섯 번째가 한도를 초과해 DENY가 된다.

원하는 셈이 사건의 수가 아니라 사건들에 걸친 구별되는 값들의 수일 때도 있다. 이전이 몇 번이냐가 아니라 서로 다른 수령인이 몇 명이냐를 묻는 경우다. 에이전트가 한 시간에 최대 세 명의 구별되는 수령인에게 이전할 수 있다는 규칙은 이렇게 쓴다.

```
forbid ( principal, action == AgentCore::Action::"Transfer", resource )
when temporal {
  count_distinct_within(u, 1h, AgentCore::Action::"Transfer"::request{ input.user: u }) > 3
};
```

수령인이 `u`에 묶이고 `count_distinct_within`은 창 안에서 본 `u`의 구별되는 값들을 센다. 같은 수령인에게 두 번 지불하면 한 번으로 세지만 새 수취인은 집계를 올린다. 추적에서 `bob`과 `carol`, `dave`는 각각 1, 2, 3번째 구별 수령인으로 ALLOW이고 `erin`은 네 번째 구별 수령인이 되므로 DENY다. 그 뒤의 `bob` 반복도 창이 이미 너무 많은 구별 수취인을 담고 있어 DENY로 남는다. 네 번째 구별 수령인은 그 단일 이전에 관한 모든 것이 괜찮은데도 거절되는 셈이다.

세기 외에 Dogwood는 사건들과 연관된 데이터를 합하는 방법도 제공한다. 돈을 이전하는 도구라면 이전 사건의 수만이 아니라 창 안에서 이전될 수 있는 총 달러를 제한하고 싶을 수 있다. 몇 건이 걸리든 지난 한 시간에 5,000달러를 넘게 이전하지 않는다는 규칙이다.

```
forbid ( principal, action == AgentCore::Action::"Transfer", resource )
when temporal {
  sum_within(a, 1h, AgentCore::Action::"Transfer"::request{ input.amount: a }) > 5000
};
```

`sum_within`은 `count_within`을 반영하지만 사건을 집계하는 대신 각 이전의 금액을 `a`에 묶어 그것들을 더한다.

### 요청을 세야 하는 이유

앞의 속도 제한 정책들에서 속도 제한을 `Transfer::response`가 아니라 `Transfer::request` 사건으로 표현했다. 동시적이고 비동기적인 도구 호출이 있는 상황에서 의도한 속도 제한을 안전하게 달성하려면 이 선택이 결정적이다.

차이는 명확하다. `Transfer::request` 사건은 인증이 검토되고 있는 것을 포함해 모든 요청을 포함하지만 `Transfer::response`는 완료된 이전만 포함한다. 다음은 잘못된 정책이다.

```
forbid ( principal, action == AgentCore::Action::"Transfer", resource )
when temporal {
  sum_within(a, 1h, AgentCore::Action::"Transfer"::response{ input.amount: a }) > 5000
};
```

앞의 정책에서 바뀐 것은 단 한 단어다. `Transfer::request` 사건 대신 `Transfer::response` 사건을 합한다. 이 정책은 응답과 연관된 금액만 합하므로, 에이전트는 어느 하나가 해소되기 전에 많은 동시 이전 요청을 발행해 의도된 한도를 우회할 수 있다.

```
                                        response  request
@0 Transfer::request  { amount: 2000 }   ALLOW     ALLOW
@1 Transfer::request  { amount: 2000 }   ALLOW     ALLOW
@2 Transfer::request  { amount: 2000 }   ALLOW     DENY
@3 Transfer::response { amount: 2000 }
@4 Transfer::response { amount: 2000 }
@5 Transfer::request  { amount: 2000 }   ALLOW     DENY
```

차이는 세 번째 `Transfer::request`에서 시작한다. 그 시점에 총 6,000달러가 요청되어 진행 중이므로 `Transfer::request` 사건의 금액을 합하는 정책은 거부한다. 그런데 그 시점에는 아직 `Transfer::response` 사건이 없었으므로, 합산에 `Transfer::response`를 쓰는 변종은 요청을 허용한다.

### 창의 총합에 이름을 붙이기

지금까지 모든 상한은 창의 총합을 고정된 수와 비교했다. 그런데 흥미로운 임계는 때때로 지금 검사되고 있는 요청 자체다.

하나의 이전이 이번 시간에 이미 결제된 모든 것을 초과해서는 안 된다는 것은 반스파이크 규칙이다. 에이전트가 확립해 온 규모에서 작동하게 허용하면서 나머지를 갑자기 압도하는 그 하나의 지불을 거절한다. 그러려면 창의 총합이 이름을 가져야 하고 그러면 현재 요청을 그것과 비교할 수 있다.

```
forbid ( principal, action == AgentCore::Action::"Transfer", resource )
when temporal {
  bind(prior,
    sum_within(a, 1h, AgentCore::Action::"Transfer"::response{ input.amount: a }),
    context.input.amount > prior)
};
```

`bind`는 집계에 이름을 연관시키게 해 준다. 여기서 결제된 총합이 `prior`가 되고 그것에 관한 평범한 조건을 쓸 수 있다. `context.input.amount`는 결정되고 있는 이전의 금액이므로, `context.input.amount > prior`는 결제된 모든 것을 합한 것을 초과하는 바로 그 이전을 금지한다. 추적에서 1,000달러가 결제된 상태라면 500달러와 800달러는 ALLOW이고 2,000달러만 DENY다. 그 2,000달러가 에이전트 자신의 최근 결제된 행동에 비해 균형에서 벗어났기 때문이다.

### 시간 논리와 매크로

흔한 시나리오는 네 가지 질문으로 정리된다. 이것이 일어났는가는 `formerly`, 몇 번인가는 `count_within`, 몇 가지가 다른가는 `count_distinct_within`, 총 얼마인가는 `sum_within`이다.

구조를 밝히면 이렇다. 마지막 세 연산과 `bind`는 Dogwood의 원시 연산이 아니라 Dogwood 표준 라이브러리의 매크로로 정의된다. 이 매크로들은 계량 1차 시간 논리 MFOTL이라는 논리에서 뽑아낸 시간 연산자들의 핵심 부분집합으로 정의된다. 많은 사용자가 이 상위 수준 매크로 연산으로 정책을 표현할 수 있을 것으로 예상하지만 더 고급 정책은 MFOTL의 하부 연산으로 직접 쓸 수 있다.

MFOTL은 형식 방법의 한 분야인 런타임 검증에 뿌리를 둔다. 실행 중인 시스템을 그것이 어떻게 행동해야 하는지에 대한 형식 명세에 대고 검사하는 학문이다. 그러니 Dogwood는 MFOTL의 강력한 기능들을 Cedar의 시점 인증 지원과 결합한 것이다.

### Cedar 위에 세울 수 있었던 이유

런타임 검증이 인증을 대체하는 것이 아니라 일반화하기 때문에, Dogwood는 Cedar에서 떠나는 대신 Cedar 위에 직접 세울 수 있었다.

구문적으로 유효한 어떤 Cedar 정책도 구문적으로 유효한 Dogwood 정책이다. 기존 Cedar 정책 집합을 그대로 재사용할 수 있고 재작성도 마이그레이션도 없다. 평범한 Cedar로 충분한 곳에서는 계속 평범한 Cedar를 쓸 수 있다.

Cedar의 인증 의미론도 온전히 유지된다. 기본 거부 행동이고 `forbid`가 `permit`을 무시한다. 감사와 강제가 이미 의존하는 보장들이 변하지 않고 이어진다.

### 대가

반면 시간 정책의 표현력은 무료로 오지 않는다. 평가에 사건들의 상태 추적이 필요하고 평가의 시간 복잡도가 사건 로그의 길이에 의존할 수 있다. 게다가 시간 조건은 현재 Cedar가 제공하는 강력한 자동 추론 분석 도구들을 지원하지 않는다.

그 절충이 에이전틱 행동을 규율하는 정책에는 적절하다고 믿는다. 다만 Cedar 같은 정책 언어가 쓰여 온 다른 모든 방식에는 옳지 않을 수 있다. 그것이 Cedar를 개조하는 대신 새 언어를 개발하기로 한 이유의 일부다.

### 설정과 다음 단계

위의 예시들은 Dogwood를 배포된 그대로 썼지만 필요할 때 거의 모든 조각이 설정 가능하다. 반복되는 패턴에 이름을 붙이는 자기 매크로를 정의해 표준 라이브러리를 넘는 공유 라이브러리를 만들 수 있다. 도구 호출의 요청과 응답 사건을 넘어 추가 종류의 사건을 포함하는 더 풍부한 사건 모델을 선언해, 에이전트 환경의 다른 사건들을 참조하는 속성도 표현할 수 있다. 새 정보 제공자를 정의하는 것도 지원하는데, 정책이 인라인으로 읽을 수 있는 사실을 계산하는 작은 샌드박스 함수들이다. 패턴 일치나 거부 목록 검사, 분류기의 판정 같은 것이 여기 든다. 시작을 돕는 기능도 있다. 에이전트의 MCP 도구 매니페스트에서 곧바로 행동 스키마를 생성하는 방법을 포함해, 도구당 하나의 행동으로 에이전트가 인증하는 신원들을 이미 모델링한 준비된 템플릿 위에 올려 준다.

앞으로의 방향은 셋이다. 첫째는 절대 시간을 포함한 더 풍부한 연산자다. 오늘 모든 창은 상대적이며 한 시간 안이란 지난 60분을 뜻하는 슬라이딩 창이다. 그런데 많은 실제 규칙은 비슬라이딩 창에 고정되어 있다. 자정에 리셋되는 일일 할당량이나 영업 종료 전 같은 것이다. 그런 규칙은 지금부터 거꾸로 측정되는 것이 아니라 벽시계 경계에 고정된 창, 즉 절대 시간 연산자를 필요로 한다.

둘째는 안전성을 넘어선 활성이다. 안전성은 무엇이 일어나서는 안 되는지를 말하고 그 대응물인 활성은 무엇이 일어나야 하는지를 말한다. 승인은 결국 이행되어야 하고 시작된 작업은 종료 상태에 도달해야 하고 열린 자원은 해제되어야 한다. 활성 검증에는 과거뿐 아니라 미래에 대해 추론하는 연산자가 필요한데, MFOTL이 이미 이 개념들을 모델링하므로 Dogwood를 확장해 지원하는 것이 자연스러운 다음 단계다.

셋째는 다중 에이전트 시스템을 위한 오케스트레이션이다. 작업이 여러 협력 에이전트에 퍼지면 검사할 만한 속성이 한 에이전트에 관한 것이기를 멈추고 앙상블에 관한 것이 된다. 누가 누구에게 인계할 수 있는지, 어느 에이전트가 잠금을 갖고 있는지, 그룹 전체가 진전을 이루고 있는지가 그런 속성이다. 그 환경으로 런타임 검증을 가져오는 것이 궁극적으로 Dogwood를 데려가고 싶은 곳이다. 이 계획들의 목표는 정책의 표현력을 높이는 것이고 에이전트의 커지는 범위와 자율성을 반영한다.

Dogwood는 Apache 2.0 오픈소스다. 참조 코드 외에 전체 언어를 실용 예시로 훑는 언어 가이드도 함께 있다. 아직 직접 기여는 받지 않지만 언어 설계와 향후 방향에 대한 커뮤니티 피드백은 환영한다. 이미 Cedar 커뮤니티 구성원들과 Dogwood를 공유하고 그들의 초기 입력을 반영했다. 개방성은 반복적으로 키울 계획이다. 먼저 반응과 피드백을 모으고 언어가 안정되면 기여를 열고 그 주위에 형성되는 커뮤니티와 함께 거버넌스를 만든다.

## 더 생각해보기

- 시퀀스에 대한 규칙이 필요하다는 진단은 어느 규모의 에이전트에서부터 유효한가.
- 요청을 세는 정책은 요청이 실패로 끝났을 때 한도를 어떻게 회복하는가.
- 상태 추적 비용이 로그 길이에 의존한다면 실제 운영에서 창 크기는 무엇으로 정하는가.
- 자동 추론 분석을 포기한 대가는 정책 오류를 어떤 방식으로 늦게 발견하게 만드는가.
- MCP 매니페스트에서 행동 스키마를 자동 생성하면 도구가 바뀔 때 정책은 어떻게 되는가.
- 반스파이크 규칙이 결제된 총합을 기준으로 삼는다면 첫 거래는 어떻게 처리되는가.
- 다중 에이전트 환경에서 사건 이력은 누구를 기준으로 모아야 하는가.
- 활성 조건을 검증하려면 위반 판정을 언제 내려야 하는가.
- 절대 시간 창이 없는 지금 자정 리셋 할당량은 어떻게 우회 없이 구현되는가.
- 직접 기여를 받지 않는 오픈소스 공개는 어떤 종류의 피드백을 얻는 데 유리한가.
