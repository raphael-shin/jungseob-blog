---
layout: post
title: "Cohere Rerank 5가 구절 단위 Context Focus와 보정된 점수로 내건 토큰 절감, 자사 벤치마크와 자체 개발 지표로 낸 수치를 읽는 법"
date: "2026-10-25 17:06:33 +0900"
created: "2026-10-25T17:06:33+09:00"
source: "https://cohere.com/blog/rerank-5"
source_title: "Introducing Rerank 5: precise, efficient enterprise document retrieval"
author: jungseob
source_author: "Cohere Team (Clifton Poth, Nils Reimers 외 기여자 10명)"
source_published: "2026-10-21"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Cohere가 2026년 10월 21일에 낸 Rerank 5 발표를 정리한다. Pro와 Fast 두 등급, 문서 안에서 관련 구절만 돌려주는 Context Focus, 확률로 읽히는 보정 점수, 다국어와 파싱된 PDF 성능, 가격을 다루고 평가 지표(RCP-nDCG@10)가 Cohere 자체 개발이라는 점, 에이전트 실험이 내부 실험이라는 점, 경쟁사 Voyage의 반박 수치를 대조해 읽을 때의 한계를 밝힌다."
image:
  path: "https://cdn.sanity.io/images/rjtqmwfu/web3-prod/001e212cb8f99611514f36805a3c3ef32a51f7d9-3840x2160.png?rect=0,72,3840,2016&w=1200&h=630&q=80&fit=crop&auto=format"
  alt: "Cohere Rerank 5 발표 글 대표 이미지"
tags:
  - knowledge
  - blog
  - AI
  - RAG
  - 검색
---

## TL;DR

- Cohere는 10월 21일 Rerank 5를 Pro와 Fast 두 등급으로 내놓았다. 핵심 신기능은 문서 안에서 질문과 관련된 구절만 점수와 함께 돌려주는 Context Focus이고, 검색 결과를 LLM에 넘기기 전에 줄여 토큰 비용을 낮춘다는 것이 판매 논리다.
- 자사 실험에서 Context Focus로 문맥의 절반을 덜어도 답변 품질은 96% 유지되고 4분의 3을 덜어도 87%가 유지된다. BM25에 Rerank 5 Pro와 Context Focus를 얹은 검색 에이전트는 토큰을 35% 덜 쓰고 정확도가 46%에서 58%로 올랐다.
- 두 번째 기능은 보정된 점수다. 0.7이 70% 확률로 쓸모 있다는 뜻이 되도록 만들어 모델과 도메인이 바뀌어도 임계값 하나를 쓰게 하고, 임계값 아래이면 에이전트가 쿼리를 다시 쓰거나 모른다고 답하게 하는 용도를 제안한다.
- 읽을 때의 핵심 단서는 평가의 주체다. 헤드라인 벤치마크의 지표 RCP-nDCG@10도 에이전트 실험도 Cohere가 만들고 돌린 것이며, 경쟁사 Voyage는 9월 말 자사 rerank-3가 Cohere Rerank 4 Pro를 긴 문서 검색에서 13.84% 앞선다고 발표했다.
- 이 노트는 발표 글 전체와 Cohere 변경 기록, 지표 글, 제3자 보도와 Voyage 글의 요약을 읽었다. 벤치마크는 재현하지 않았다.

## 글에 대하여

Cohere가 2026년 10월 21일에 공개한 제품 발표 글이다. 변경 기록과 제3자 보도(MarkTechPost 10월 22일 등)가 같은 날짜를 확인한다. Rerank 5는 Embed 5, Parse 5와 함께 최신 세대 검색 모델이며 Cohere API, Model Vault, Microsoft Foundry, Amazon SageMaker, 고객 VPC나 온프레미스, 자사 North 사용자에게 제공된다. API 가격은 Pro가 100만 토큰당 0.05달러, Fast가 0.02달러다. 모델은 Pro(rerank-v5.0-pro)와 Fast(rerank-v5.0-fast)이며 제3자 보도는 문맥 창이 32K 토큰이고 파라미터 수와 오픈 웨이트는 공개되지 않았다고 전한다. 이 블로그의 [OpenAI Build Hour 노트](https://raphael-shin.github.io/jungseob-blog/posts/openai-build-hour-agent-memory-patterns/)와 [Jev 메모리 파이프라인 노트](https://raphael-shin.github.io/jungseob-blog/posts/jev-memory-pipeline-ranking-chunking-and-context-loss/)가 다룬 컨텍스트 선택 문제의 검색 쪽 해법이다.

## 성능 주장

Cohere는 Rerank 5 Pro가 ViDoRe V3, nanoMTEB, BRIGHT, BEIR 같은 공개 벤치마크에서 시험한 모든 경쟁 모델을 앞선다고 쓴다. 평가한 복합(composite) 데이터셋 46개 중 39개에서 1위, 43개에서 2위 이상이다. 추론 중심 검색 BRIGHT에서 82.2점으로 Voyage AI Rerank 3보다 5.8점, 자사 Rerank 4 Pro보다 12.4점 높고 이는 네 대표 벤치마크 중 세대 간 가장 큰 향상이다. 가장 강한 외부 경쟁자보다 ViDoRe V3에서 1.6점, BEIR에서 1.8점, nanoMTEB에서 3.4점 앞선다. 금융·경제에서 격차가 가장 커서 Voyage Rerank 3보다 9.6점 높고 의료, 과학, 에너지 영역도 비슷한 결과라고 한다. 다국어에서는 Pro가 평가한 모든 언어에서 Rerank 4 Pro보다 낫고 스페인어, 프랑스어, 독일어, 아랍어, 한국어에서 2점 이상 높으며 내부 평가 19개 비영어 언어 중 14개에서 1위다. 파싱된 PDF 검색은 Pro 89.9로 Voyage Rerank 3의 88.4, Rerank 4 Pro의 88.3을 앞선다.

속도는 Fast가 맡는다. A100 한 장에서 1,000토큰짜리 문서 약 187개를 초당 재순위하고 Pro의 2.9배 처리량이며 응답 시간이 거의 3배 빠르다. 모든 비교 수치는 Cohere가 만든 지표 RCP-nDCG@10으로 낸 것이다. Cohere는 9월 30일 별도 글에서 이 지표를 소개했고 기존 nDCG가 사람이 붙인 희소한 관련성 레이블에 의존해 새로 검색된 유용한 문서를 보상하지 못하는 한계를 보완한다고 설명한다. GitHub 설명에 따르면 LLM 판정자가 후보 풀을 순위 토너먼트로 정렬하고 다섯 가지 이진 기준을 적용한 뒤 문항 반응 모델로 보정한 점수를 이득으로 쓴다. 지표 자체는 공개되어 있지만 헤드라인 비교가 Cohere의 지표와 평가 환경에서 나온 것이라는 점은 변하지 않는다.

## Context Focus: 토큰 경제

에이전트가 더 많은 소스에서 더 긴 문서를 가져올수록 LLM에 넘기는 문맥이 늘지만 대개 문서 안에서 관련된 것은 몇 문장뿐이다. Context Focus는 한 번의 Rerank 호출에서 문서 단위 관련도와 점수가 붙은 텍스트 구간(문자 단위 span)을 함께 돌려준다. 임계값을 조절해 문맥 감소와 증거 보존의 균형을 잡고 그 구간만 LLM에 넘기거나 사용자에게 일치 이유로 강조 표시할 수 있다. 질의응답 데이터셋 30개에서 문맥의 절반을 덜어도 답변 품질이 2%p 떨어진 정도(96% 유지)였고 4분의 3을 덜어도 7%p(87% 유지)였으며 더 큰 절감은 품질을 일부 내주고 최대 10배까지 문맥을 줄일 수 있다고 한다.

검색 에이전트 실험은 단계별로 쌓았다. 키워드 검색(BM25)에서 정확도가 46%였고 Rerank 5 Pro를 더하면 49%였다. Context Focus를 기본 임계값 0.1로 켜면 과업당 토큰이 19% 줄고 정확도가 57%로 올랐다. 0.4에서는 토큰이 34% 줄었고 모든 데이터셋에서 토큰이 더 낮았으며 정확도는 58%였다. 전체 스택은 BM25 단독보다 토큰을 35% 적게 쓰고 정확도가 58% 대 46%였다. 여섯 개 딥서치 벤치마크에서는 토큰이 41% 적고 정확도가 39%에서 52%로 올랐다. 정확도가 오르는 이유는 노이즈가 줄어서라는 설명이 앞 단락에 있다.

## 보정된 점수

기존 재순위 모델의 점수는 정렬에는 쓸모 있어도 모델마다 의미가 달라 모델을 바꿀 때마다 임계값을 다시 맞춰야 했다. Rerank 5는 relevance_score가 문서가 쓸모 있을 확률로 읽히도록 보정되어, 0.7이 70% 확률을 뜻한다. 요청과 응답 형식은 그대로다. Pro와 Fast 모두 "쓸모 있을 가능성이 더 높음"의 기준선이 각각 0.50과 0.45 근방이다. 검증은 모델이 학습하지 않은 두 사람 판정 집합, 곧 블라인드 평가단과 NIST TREC Deep Learning 평가자의 판정으로 했다. 기대 보정 오차(ECE)가 두 판정 집합에서 모두 약 0.06이고 시험한 다른 재순위 모델은 거의 4배 이상이다. 예로 Voyage Rerank 3이 0.55로 준 문서는 사람 평가자에게 24%만 쓸모 있었다. 활용법으로는 상위 k개 고정 대신 임계값 이상만 넘기기, 임계값을 넘는 문서가 없으면 에이전트가 쿼리를 고쳐 쓰거나 모른다고 답하기, BRIGHT, NanoBEIR, ViDoRe V3 전반에서 기본 임계값이 Pro 기준 0.47~0.53 사이이므로 하나의 임계값을 쓰기를 든다.

## 대조해서 확인한 점

발표 글의 기본 사실, 곧 출시일, 두 등급, 플랫폼, 가격은 변경 기록과 제3자 보도와 맞는다. 경쟁 구도는 발표 글이 말하지 않는 부분이 있다. Voyage AI는 9월 30일 rerank-3와 rerank-3-lite를 내며 긴 문서 검색에서 rerank-2.5보다 3.35%, Cohere Rerank v4.0 Pro보다 13.84% 앞선다고 밝혔다. 발표 글의 "Voyage AI Rerank 3보다 앞선다"와 Voyage의 "Cohere v4 Pro보다 앞선다"는 서로 다른 데이터셋과 지표에서 나온 자기 주장이다. 이 노트는 두 회사의 수치를 직접 비교하지 못했다. 또 Voyage 모델은 MongoDB Atlas에도 통합된다. 이 블로그의 [MongoDB 메모리 발표 노트](https://raphael-shin.github.io/jungseob-blog/posts/alake-mongodb-architecting-agent-memory/)에서 다룬 Voyage 계열이다.

## 읽을 때 유의할 점

첫째, 지표와 평가 환경, 에이전트 실험이 모두 Cohere의 것이다. 판정자가 LLM인 지표에서 Cohere의 모델이 유리하게 평가될 수 있다는 의문은 열려 있으며 독립 재현은 확인하지 못했다. 둘째, 에이전트 실험은 모델 하나 데이터셋 몇 종, BM25 위에 쌓은 한 구성이다. 이미 좋은 하이브리드 검색을 쓰는 시스템에서 같은 이득이 날지는 알 수 없다. 셋째, Context Focus가 문맥을 줄여도 재순위 호출 자체의 비용과 지연이 더해진다. 글은 순비용을 계산하지 않는다. 넷째, 보정은 평가에 쓴 판정 집합의 기준에서의 보정이다. 사용자 도메인의 "쓸모 있음" 기준과 다르면 확률 해석이 어긋나므로 자기 데이터로 임계값을 확인해야 한다. 다섯째, 구절 단위로 자르면 앞뒤 문맥이나 여러 구절에 걸친 근거를 잃을 위험이 있다. 글의 품질 유지율은 질의응답 데이터셋 평균이다. 여섯째, 한국어는 2점 이상 향상 언어로만 언급될 뿐 절대 점수와 한국어 데이터셋은 공개 표에서 확인하지 못했다.

그래도 가져갈 질문은 선명하다. 우리 RAG에서 LLM에 넘기는 토큰 중 실제로 답에 쓰이는 비율은 얼마인가, 임계값 하나로 검색 결과의 양을 조절할 수 있다면 "없음"이라는 답을 허용하는 경로가 있는가, 모델을 바꿀 때 임계값을 다시 맞추는 비용은 얼마나 드는가, 자기 데이터로 Rerank 5와 기존 재순위기를 같은 지표로 비교해 본 적이 있는가.

## 참고 자료

[Cohere: Introducing Rerank 5 (2026-10-21)](https://cohere.com/blog/rerank-5): 발표 글 전체를 읽고 정리했다. 표와 차트의 세부 수치는 본문 서술로만 읽었다.

[Cohere 문서: Rerank v5 변경 기록](https://docs.cohere.com/changelog/rerank-v5): Context Focus와 보정 점수 안내를 검색 발췌로 확인했다.

[Cohere: RCP-nDCG@10 소개 (2026-09-30)](https://cohere.com/blog/rcp-ndcg): 지표의 동기를 검색 발췌로 확인했다.

[cohere-ai/rcp-ndcg (GitHub)](https://github.com/cohere-ai/rcp-ndcg): LLM 판정과 문항 반응 모델 구조를 검색 발췌로 확인했다.

[MarkTechPost: Cohere Releases Rerank 5 (2026-10-22)](https://www.marktechpost.com/2026/10/22/cohere-rerank-5-context-focus): 출시 보도와 에이전트 실험 수치를 검색 발췌로 확인했다.

[Voyage AI: rerank-3 and rerank-3-lite (2026-09-30)](https://blog.voyageai.com/2026/09/30/rerank-3/): Cohere Rerank v4.0 Pro와의 비교 주장을 검색 발췌로 확인했다. 본문은 읽지 못했다.
