---
layout: post
title: "엔지니어TV가 정리한 Colossus 2, 연말 Blackwell 120만 개와 다섯 개 건물 구성과 122일 건설 속도와 20GW 시나리오를 Epoch AI 자료와 머스크 게시물에 맞춰 본 정리"
date: "2026-11-03 20:37:08 +0900"
created: "2026-11-03T20:37:08+09:00"
source: "https://youtu.be/Ui_5-NrPaRw"
source_title: "머스크가 세계 1위 AI 데이터센터를 장악했다! GPU 120만 개에서 20GW까지, 구글도 뛰어든 초대형 AI 인프라 전쟁"
author: jungseob
source_author: "EngineerTV (엔지니어뷰)"
source_published: "2026-11-03"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "EngineerTV가 2026년 11월 3일에 올린 11분 3초 해설 영상을 정리한다. Epoch AI의 연산 성능 순위에서 1위인 SpaceX Colossus 2가 H100 환산 약 111만 대이고, 머스크가 X에 밝힌 건물별 계획(Macrohard 33만, Macroharder 22만, Minihard 22만, Gun Range 22만, Spam 약 20만)이 연말 약 120만 개로 이어진다는 설명, 첫 Colossus를 122일에 지은 속도, Brian Wang의 2027년 말 19.64GW 시나리오, Epoch가 추정한 구글 Goodnight 시설을 다룬다. Epoch AI 데이터베이스와 머스크의 게시물 보도, xAI 공식 페이지로 대조하고, 영상의 순위 서술이 현재 Epoch 목록과 다른 점과 출처가 불분명한 매출 수치를 밝힌다."
image:
  path: "https://i.ytimg.com/vi/Ui_5-NrPaRw/maxresdefault.jpg"
  alt: "EngineerTV의 Colossus 2 해설 영상 썸네일"
tags:
  - knowledge
  - blog
  - AI
  - 데이터센터
  - SpaceX
---

## TL;DR

- 영상의 요지는 세계에서 가장 강력한 AI 데이터센터가 SpaceX의 Colossus 2이고, 머스크가 연말까지 Blackwell GPU를 약 120만 개로 늘린다는 것이다. Epoch AI는 이 시설의 연산을 H100 환산 약 111만 대로 추정하며, 영상은 다섯 개 건물(Macrohard, Macroharder, Minihard, Gun Range, Spam)을 합쳐 약 119만 개가 된다고 계산한다.
- 경쟁력은 건설 속도다. 첫 Colossus를 122일에 지었고 첫 서버 랙부터 학습 시작까지 19일이 걸렸으며 92일 뒤 20만 GPU로 두 배가 되었다는 서술이 xAI 공식 페이지와 NVIDIA 발표로 맞는다.
- 2027년 말 19.64GW는 머스크의 확정 계획이 아니라 Brian Wang이 개인 가정으로 세운 시나리오다. 구글의 Goodnight는 Epoch가 2027년 4분기 H100 환산 약 228만 대, 약 1GW로 추정하지만 소유와 사용 여부는 확정되지 않았다.
- 순위는 영상과 현재 Epoch 목록이 다르다. Epoch 목록에서 2위는 OpenAI Stargate Abilene(약 102만)이고, 영상이 2위로 든 Anthropic-Amazon New Carlisle(약 82만)은 3위다.
- 시설당 월 14억~20억 달러 매출과 2027년 1분기 500억 달러는 출처를 밝히지 않은 수치라 확인하지 못했다.

## 영상에 대하여

EngineerTV(엔지니어뷰)가 2026년 11월 3일에 올린 11분 3초 영상이다. 한국어 사람 자막 전체를 읽었고 마지막 타임스탬프가 영상 길이와 맞는다. 제목 뒤의 해시태그는 제외했다. 진행자 이름은 영상에 나오지 않고 설명란은 멤버십 안내와 문의처뿐이라 원자료 링크가 없다. 그래서 순위와 건물 구성은 영상이 인용한 출처(Epoch AI, 머스크의 X 게시물, Brian Wang)를 직접 찾아 확인했다. 이 블로그의 [SpaceX Q3 콜 노트](https://raphael-shin.github.io/jungseob-blog/posts/musk-spacex-q3-call-arbty-excerpt/)와 [Ghori 인터뷰 노트](https://raphael-shin.github.io/jungseob-blog/posts/ghori-relentless-inside-xai/)가 같은 회사의 다른 면을 다룬다.

## 순위: 누가 가장 강력한가

영상은 Epoch AI가 발표한 연산 성능 순위를 소개한다. H100 환산 기준이고 1위가 SpaceX의 Colossus 2(약 111만 대), 2위가 Anthropic-Amazon의 New Carlisle로 1위가 35% 높으며 3위 마이크로소프트, 4위 OpenAI Stargate, 5위 구글 Pryor North가 모두 미국에 있다는 서술이다. 그다음 말레이시아의 DayOne 두 곳이 세계 10위 안에 들어 있고 DayOne의 최대 고객이 ByteDance라고 한다. 진행자는 AI 강국이 되는 길이 GPU를 직접 만드는 것만이 아니라 AI 컴퓨팅이 모이고 연결되는 중심지가 되는 것도 전략이라고 해석한다.

## Colossus 2의 건물별 구성

머스크가 X에 올린 계획을 풀어 설명하는 대목이 핵심이다. Colossus 2는 건물 하나가 아니라 여러 대형 데이터센터로 이루어진 단지이고 건물에는 독특한 이름이 붙어 있다. 진행자는 Macrohard가 Microsoft의 패러디이고 Macroharder와 Minihard는 말장난이라고 해석하는데, 이는 진행자의 설명이다.

Macrohard에는 GB200 11만 개와 GB300 22만 개를 합쳐 33만 개가 있고 Macroharder와 Minihard에는 각각 GB300 22만 개가 학습용으로 들어 있으며 800기가비트급 네트워크로 구성되었다. Gun Range에도 같은 규모가 들어가 11월 말 가동이 목표이고 Spam에는 약 20만 개가 추론용으로 들어가 12월 가동이 목표다. 다섯 건물을 합치면 약 119만 개다. 영상의 설명에서 중요한 점은 추론용 시설의 네트워크가 학습용보다 단순해 광케이블이 절반도 안 필요하다는 것이다. 학습과 추론의 통신 방식이 다르기 때문이며 머스크가 최근 현장을 둘러봤다고 한다.

## 건설 속도의 비밀

영상은 경쟁력의 중심이 속도라고 말한다. 기존 업체가 제시한 공사 기간이 최대 24개월이었는데 xAI는 GPU 10만 대 규모의 첫 Colossus를 122일에 지었고 첫 서버 랙이 들어온 뒤 AI 학습이 시작되기까지 19일이 걸렸으며 92일을 더 들여 20만 개로 늘렸다고 설명한다. 진행자는 전력 확보와 냉각과 네트워크 연결이 건물 짓기와 다른 문제이고 테슬라의 Megapack 같은 에너지 저장 장치와 제조 노하우가 이 압축을 가능하게 한 것으로 보인다고 추정한다. 이 속도를 다음 시설에서도 반복 적용한다는 것이 요지다.

## 왜 이렇게 짓는가

진행자는 데이터센터 건설이 먼저 막대한 자금을 투입하고 하루라도 빨리 가동해 회수하는 구조라고 본다. 시설이 하나 가동될 때마다 월 14억~20억 달러의 추가 매출이 가능하고 네 곳이면 80억 달러, 2027년 1분기 매출이 500억 달러에 이를 수 있다고 말한다. 대표적인 사례로 Anthropic과 SpaceX의 계약을 들지만 계약 내용은 영상에서 설명하지 않는다. 머스크의 구상은 컴퓨팅을 다른 AI 기업에 공급해 번 돈으로 자체 AI 개발과 데이터센터 확장에 재투자하고 테슬라의 자율주행과 Optimus 같은 기계가 늘수록 더 많은 컴퓨팅이 필요해진다는 선순환이라는 해석이다. 진행자는 구글과 Amazon과 Microsoft와 Meta도 에이전트와 로봇을 개발하므로 같은 미래를 준비한다고 본다.

## 20GW 시나리오와 구글

미국 매체 Next Big Future의 Brian Wang은 머스크와 직접 이야기한 데이터를 분석해 SpaceX가 2026년 말 약 3.4GW, 2027년 말 19.64GW까지 갈 수 있다는 시나리오를 제시했다. 영상은 이를 Wang 개인의 분석이라고 먼저 밝히며 2027년 1분기에는 매월 한 개, 2분기와 3분기에는 두 개, 4분기에는 세 개의 Rubin 기반 데이터센터를 완공한다는 가정이라 한 해 24개가 추가되고 Colossus 2의 약 20배 전력이라고 설명한다.

구글도 세계 최대급 시설을 짓고 있다는 대목에서는 Epoch AI의 Goodnight 프로젝트를 소개한다. 텍사스에 건설 중이고 2027년 4분기 H100 환산 227만 대, 전력 약 1,000MW, 투자 약 381억 달러로 전망되며 현재 Colossus 2의 2배가 넘는다. Epoch는 소유가 구글일 가능성과 DeepMind가 사용할 가능성을 말하지만 확정은 아니라고 한다. 영상은 이 자료에 머스크가 "그렇게 크지 않다"고 댓글을 달았고 이는 더 큰 시설을 짓고 있다는 의미일 것이라고 해석한다.

## 대조해서 확인한 점

**연산 순위.** Epoch AI의 데이터센터 목록(2026년 11월 3일 확인)은 Colossus 2를 H100 환산 약 111.2만 대로 1위에 둔다. 영상의 약 111만 대와 맞다. 그러나 2위는 OpenAI Stargate Abilene(약 101.9만 대)이고 Anthropic-Amazon New Carlisle(약 81.8만 대)은 3위, Microsoft Fairwater Atlanta(약 76.9만 대) 4위, Google Pryor North(약 63.7만 대) 5위다. 영상의 "2위 New Carlisle보다 35% 높다"는 New Carlisle과의 비교에서만 맞고(111.2만을 81.8만으로 나눈 값), 현재 목록의 2위와는 약 9% 차이다. 영상의 순위 차트가 어느 시점의 것인지 영상만으로는 알 수 없다. DayOne 두 곳(Nusajaya 약 58.4만 대, Kempas 약 48.1만 대)은 6위와 8위로 10위 안에 든다.

**전력 순위.** Epoch가 2026년 10~11월 기준으로 추정한 현재 IT 전력은 New Carlisle이 약 1,037MW로 가장 크고 Colossus 2가 약 946MW, Stargate Abilene이 약 824MW다. 연산에서 1위라는 사실과 전력에서 1위라는 사실이 다르다. Colossus 2의 종료 시점 계획 용량은 약 1,531MW로 추정된다.

**머스크의 게시물.** 머스크는 10월 31일(미국 시간) X에 Macroharder와 Minihard가 각각 GB300 22만 개이며 800기가 NIC로 학습용으로 구성되었고 Gun Range도 같은 규모이며 Spam은 약 20만 개 GB300을 추론용으로 갖고 광섬유가 절반 미만이라고 썼다. 현장을 두 번 걸어봤고 Gun Range는 11월 말, Spam은 12월 가동이 목표라고 썼으며 이어서 연말까지 Colossus 2에 Blackwell이 총 약 120만 개 있을 것이라고 썼다(보도 인용). 영상의 "11월 1일 게시"는 한국 시간 기준이다. 건물별 수치와 목표 시점은 영상과 맞는다. Macrohard가 33만 개라는 수치는 머스크가 이후 정정했다고 Next Big Future가 쓴다. 이는 영상의 "9월에 공개한 GPU 55만 개"와 구별해야 한다. 이 노트는 55만 개라는 9월 수치의 출처를 찾지 못했다.

**건설 속도.** xAI 공식 페이지는 Colossus를 122일에 지었고 92일 만에 두 배로 늘려 20만 GPU가 되었다고 쓴다. NVIDIA의 발표는 첫 랙에서 학습 시작까지 19일이 걸렸다고 보도되었다. 영상의 서술과 맞는다.

**20GW 시나리오.** Next Big Future는 머스크가 10GW는 확신하고 2027년에 20GW 추가를 목표로 하며 20GW가 더는 확률 0%가 아니라고 말했다고 쓴다. 또한 GB300 Minihard 하나가 약 400~450MW, Rubin 판이 600~700MW라서 20GW에는 건물 24~28개가 필요하다고 계산한다. 영상의 19.64GW와 한 해 24개 건설 가정은 Wang의 산식이며 머스크의 확정 계획이 아니다. 영상도 이를 구분한다.

**Goodnight.** Epoch의 Goodnight 페이지는 2027년 4분기 H100 환산 약 228만 대, 약 1,006MW, 투자 381억 달러라는 영상의 수치와 같다. 이 추정은 위성사진과 규제 서류에 근거하며 소유자가 구글일 가능성과 DeepMind 사용 가능성을 밝힌다. 첫 건물의 서류상 완공일은 2026년 9월 12일이지만 Epoch는 현재 상태로 보아 지켜지기 어렵다고 본다. 머스크의 "그렇게 크지 않다" 댓글은 확인하지 못했다.

확인하지 못한 것은 DayOne의 최대 고객이 ByteDance라는 서술, 시설당 월 14억~20억 달러 매출과 2027년 1분기 500억 달러(출처 불명이며 Next Big Future에는 4분기 매출 250억~270억 달러 시나리오가 있다), Anthropic과 SpaceX의 계약 내용, Macrohard 등 이름의 어원 해석, 머스크의 Goodnight 댓글이다.

## 읽을 때 유의할 점

첫째, 한국어 시장 해설 영상이고 원자료 링크가 없어 수치의 출처가 흐리다. 영상 끝의 투자 아이디어는 멤버십 유도다. 둘째, 연산 순위는 현재 가동 규모이고 계획 용량은 다르다. 연말 120만 개는 계획이며 11~12월 가동분은 아직 설치되지 않았다. 셋째, 20GW 시나리오는 한 매체 필자의 가정이고 이 필자는 SpaceX와 Tesla 보유를 밝힌다. 넷째, Epoch의 추정치는 위성사진 기반이며 소유 관계는 불확실하다. 다섯째, 매출 수치는 근거가 없으므로 투자 판단에 쓰면 안 된다.

가져갈 질문은 선명하다. 연산 규모와 전력 규모 중 어느 쪽이 경쟁의 병목인가, 학습용과 추론용 시설을 따로 지으면 네트워크 비용이 어떻게 달라지는가, 계획이 현실이 되는 속도를 가늠할 독립 지표는 무엇인가.

## 참고 자료

[EngineerTV: 머스크가 세계 1위 AI 데이터센터를 장악했다 (YouTube, 2026-11-03)](https://youtu.be/Ui_5-NrPaRw): 한국어 자막 전체(11분)를 읽고 정리했다.

[Epoch AI: AI data centers directory](https://epoch.ai/data/ai-data-centers/directory): 연산 순위를 확인했다.

[Epoch AI: Largest AI data centers by power capacity](https://epoch.ai/graphs/largest-ai-data-centers-by-power-capacity): 전력 순위를 확인했다.

[Epoch AI: Goodnight](https://epoch.ai/data/ai-data-centers/directory/goodnight): 구글 시설의 전망 수치를 읽었다.

[FourWeekMBA: Musk says Colossus 2 will hold 1.2M Blackwells by year-end](https://fourweekmba.com/ai-musk-says-colossus-2-will-hold-1-2m-blackwells-by-year-end/): 머스크의 10월 31일 게시물 인용을 읽었다.

[Converge Digest: SpaceX Colossus 2 Gun Range and Spam GPU roadmap](https://convergedigest.com/spacex-colossus-2-gun-range-spam-gpu-roadmap/): 건물별 구성과 합계를 읽었다.

[Next Big Future: Elon Musk replied to me and gave critical SpaceXSI information (2026-11)](https://www.nextbigfuture.com/2026/11/elon-musk-replied-to-me-and-gave-critical-spacexsi-information.html): 20GW 산식과 건물 정보를 읽었다.

[xAI: Colossus](https://x.ai/colossus): 122일 건설과 92일 증설 주장을 확인했다.
