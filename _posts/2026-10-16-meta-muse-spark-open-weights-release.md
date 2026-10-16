---
layout: post
title: "Meta가 816B 오픈웨이트 모델 Muse Spark Open을 공개했다, 맥 스튜디오 두 대 구동 주장과 라이선스 조건, 자사 벤치마크 표의 읽는 법"
date: "2026-10-16 19:43:46 +0900"
created: "2026-10-16T19:43:46+09:00"
source: "https://research.meta.ai/blog/muse-spark-open"
source_title: "Introducing Muse Spark Open, The Most Capable US Open‑Weight Model to Date"
author: jungseob
source_author: "Meta Superintelligence Labs (Meta AI Research)"
source_published: "2026-10-15"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Meta Superintelligence Labs가 10월 15일 공개한 816B(활성 42B) 오픈웨이트 모델 Muse Spark Open을 정리한다. 공개 글과 모델 카드, Muse 라이선스 원문을 읽고 하드웨어 요구, 자사 벤치마크 표에서 앞서는 항목과 뒤처지는 항목, 라이선스의 표기·매출 조건, 독립 검증이 없다는 한계를 밝힌다."
image:
  path: "https://research.meta.ai/articles/muse-spark-open/social/muse-spark-1-2-open-weights-social-v2.webp"
  alt: "Meta의 Muse Spark Open 공개 글 소셜 이미지"
tags:
  - knowledge
  - blog
  - AI
  - 오픈웨이트
  - Meta
---

## TL;DR

- Meta Superintelligence Labs는 총 816B 파라미터(토큰당 활성 42B)에 100만 토큰 컨텍스트를 갖춘 멀티모달 모델 Muse Spark Open의 가중치를 공개하면서 "미국 최고 성능 오픈웨이트"라고 부른다. 입력은 텍스트·이미지·비디오·오디오이고 출력은 텍스트다.
- 메시지의 중심은 데스크톱 구동이다. Apple M5 Ultra 맥 스튜디오 두 대(각 최대 512GB 통합 메모리)를 MLX로 묶으면 돌아간다고 하지만, 공개 글에는 초당 토큰 수 같은 속도 수치가 없다. 모델 카드가 요구하는 GPU 메모리는 4비트판 700GB 이상, BF16은 2TB다.
- 모델 카드의 자사 벤치마크 표에서 Muse Spark Open은 에이전트·멀티모달 항목 여럿에서 앞서지만, 종합 지수와 터미널·SWE형 코딩 과제에서는 GLM 5.3과 Kimi K3에 뒤진다. 표는 Meta가 고른 비교군과 설정의 결과이며 독립 검증은 아직 없다.
- 라이선스는 사용·수정·증류·재배포를 허용하되 "Built with Muse Spark Open" 표기를 요구하고, 모델 API를 제3자에게 파는 매출 2,000만 달러 초과 사업자는 Meta와 별도 계약을 맺어야 한다. 가중치는 Hugging Face에서 수동 승인(gated)을 거쳐 받는다.
- 이 노트는 공개 글과 모델 카드·라이선스 전문(미러에서)을 읽었다. 공개 글의 벤치마크 이미지와 평가 방법론 보고서는 읽지 못했다.

## 글에 대하여

Meta AI Research 블로그가 2026년 10월 15일에 올린 공개 글이다. 작성자는 Meta Superintelligence Labs로 표기된다. 본문은 짧고 벤치마크는 이미지로 실려 읽지 못했다. 모델 카드는 Hugging Face가 승인 없이는 열리지 않아(401), 같은 카드를 담은 ModelScope 미러에서 읽었다. 라이선스 전문과 벤치마크 표, 안전 평가 절이 여기서 확인된다. 이 블로그의 [Cheeky Pint Zuckerberg 노트](https://raphael-shin.github.io/jungseob-blog/posts/cheeky-pint-zuckerberg-wang-muse-wonder/)와 [Wang × Senra 노트](https://raphael-shin.github.io/jungseob-blog/posts/wang-senra-creating-muse/)가 같은 Muse 계열을 다룬다.

## 공개된 것

공개 글에 따르면 모델은 코딩과 에이전트 작업을 목표로 하며 장기 과제와 복잡한 소프트웨어 엔지니어링, 다단계 추론에 강하다고 한다. 가중치는 Amazon SageMaker AI, Google Cloud Model Garden, Hugging Face, Microsoft Foundry Models에서 받을 수 있고 API로는 Baseten, Fireworks AI, Groq, Modal, Nebius, OpenRouter, Together AI에서 쓸 수 있다. SGLang, vLLM, TensorRT-LLM, Transformers, MLX, llama.cpp, Unsloth를 지원하고 PyTorch의 TorchTitan으로 후속 학습이 가능하다. SGLang에는 자동 조정 Helion GPU 커널이 들어 NVIDIA·AMD GPU에서 커널 수준 1.03~3.95배, AMD MI350에서 종단 3% 속도 향상이라고 Meta는 밝힌다.

모델 카드의 구조는 62개 층, 은닉 차원 8,192, 층마다 전문가 256개 중 8개를 고르는 희소 전문가 혼합(MoE)이다. 전문가가 전체 파라미터의 약 97%를 차지한다. 이미지·비디오는 1.8B 지각 인코더가 토큰으로 바꾼다. 활성 파라미터가 42B여서 속도는 중형 모델에 가깝지만 모든 전문가가 메모리에 올라가므로 필요한 메모리는 816B 모델 몫이라고 Hugging Face 블로그가 설명한다. 기준 설정은 온도 1.0, top_p 1.0이며 복잡한 문제에는 추론 강도 high나 xhigh를 권한다.

## 맥 스튜디오 두 대

Meta가 내세우는 서사는 "집에서 돌리는 최전선급 모델"이다. M5 Ultra 맥 스튜디오 한 대의 통합 메모리가 최대 512GB이고 메모리 대역폭이 초당 1.2TB여서 두 대면 1TB급이 되며 토큰마다 읽는 작은 몫(활성 파라미터)을 감당할 수 있다는 논리다. Meta는 온디바이스에서 오픈소스 Mastodon 클라이언트 Ice Cubes에 iOS 변경을 반영하고(버그 수정, 기능 추가, 전체 빌드), DaVinci Resolve를 구동해 영상을 프레임 단위로 검토하고 가장 좋은 장면을 세로로 자르게 했다고 소개한다. 다만 이 데모의 속도, 지연, 성공률은 글에 없고 이 노트는 Meta 시연을 재현하지 못했다. 제3자 보도(technology.org)는 4비트판 체크포인트가 약 530GB이고 서버에서는 약 700GB의 GPU 메모리가 필요하다고 전하는데, 모델 카드의 700GB 이상(4비트)·2TB(BF16) 요구와 숫자가 다르다. 체크포인트 크기와 구동에 필요한 메모리(KV 캐시 등)의 차이일 수 있으나 확인하지 못했다.

## 벤치마크 표를 읽는 법

모델 카드의 표는 Inkling, Nemotron 3 Ultra, Beam, Mistral Large 4, Qwen3.8-2.4T-A95B, GLM 5.3, Kimi K3와 비교한다. Muse Spark Open은 xhigh 설정이다. 이 노트가 표를 직접 읽은 결과를 항목별로 적는다.

앞서는 항목은 JobBench 61.8(GLM 5.3 61.4, Kimi K3 54.3), MCP-Atlas 89.2, HLE-Diamond(도구 없음) 26.1, AA Omniscience 25, ZeroBench 50.0, SimpleVQA 73.6, IntPhys2 68.3이다. 뒤처지는 항목은 Artificial Analysis Intelligence Index 39(GLM 5.3 45, Kimi K3 44, Qwen 40, Mistral Large 4 38 바로 위), Terminal-Bench 2.1 76.4(Kimi K3 85.0, GLM 5.3 83.9, Qwen 82.0, Beam 80.1), DeepSWE 1.1 60(Kimi K3 68, GLM 5.3 67), GPQA Diamond 89.0(Qwen과 Kimi K3 93.5), OSWorld Verified 80.4(Kimi K3 84.8), GDPVal-AA v2 1401(GLM 5.3 1653, Qwen 1613)이다.

요컨대 에이전트 작업의 일부와 멀티모달 일부에서 앞서고 코딩 전반과 종합 지표에서는 중국 업체 모델들에 뒤진다. 같은 표에서 Inkling과 Nemotron 3 Ultra에는 모든 항목에서 앞서지만 이 둘은 상당수 칸이 비어 있다. "미국 최고"라는 주장은 표에 오른 비교군 안에서의 말이며 이 노트는 Beam 등 일부 모델의 국적과 표에 없는 모델을 확인하지 못했다. 비교 설정도 다르다(예컨대 일부는 "preferred harness", 일부는 도구 사용 여부). 표는 Meta가 고른 모델과 Meta가 돌린(또는 정리한) 결과이고 기술 보도도 독립 검증은 아직 없다고 쓴다. 평가 방법론 보고서는 읽지 못했다.

## 안전 평가

모델 카드는 콘텐츠 안전, 에이전트 위험, 프라이버시, 준비성(화학·생물, 사이버, 통제 상실) 네 영역을 평가했고 Meta의 슈퍼인텔리전스 스케일링 프레임워크의 출시 기준을 충족했다고 쓴다. 수치로는 내부 사이버 벤치마크에서 탈옥의 99.2%를 거부했다(Kimi K3는 같은 설정에서 75.5%), SecureBio BioTIER 거부 98% 이상, MASK 정직률 98.1%, Agentic Misalignment 오작동 0%다. 표의 FORTRESS 적대 평가에서 Muse Spark Open은 ARS 5.8로 비교군 중 가장 낮고(낮을수록 좋음) ORS 17.4는 비교군 중 가장 높다. 두 지표의 정의는 방법론 보고서에 있어 읽지 못했고 ORS가 과잉 거부를 뜻할 가능성은 이 노트의 추정이다. 비교 상대로 거의 Kimi K3만 쓴 점도 유의한다. 모델 카드가 스스로 쓰듯 이 평가는 출시된 체크포인트에만 해당하며 수정(미세조정) 후에는 달라질 수 있다.

## 라이선스

라이선스 전문(Muse Model License, 2026-10-15 판)은 무료로 사용·복사·수정(미세조정 포함)·파생물 제작·증류·병합·게시·배포·재라이선스·판매를 허락하되 네 가지 조건을 붙인다.

첫째, 저작권 고지와 라이선스, 사용 정책(Usage Policy)을 모든 사본과 파생물에 포함하고 준수해야 한다. 둘째, 소프트웨어나 파생물을 쓰는 제품·서비스의 UI나 문서·웹사이트·설정 메뉴에 "Built with Muse Spark Open"을 눈에 띄게 표시해야 한다. 파생물은 이 소프트웨어나 그 출력으로 만들거나 훈련하거나 증류하거나 개선한 모든 AI 모델을 뜻한다. 셋째, 제3자에게 AI 모델을 API 등으로 제공하는 사업(Model as a Service)을 하면서 사업자와 계열사의 합산 총매출이 12개월 연속 2,000만 달러를 넘으면 Meta에 알리고 별도 서면 계약을 체결해야 한다. 내부 사용, 연구, MaaS가 아닌 상업 활동, 자사 제품의 기능을 구동하는 용도는 이 조건에 해당하지 않는다. 넷째, Meta는 출력의 소유권을 주장하지 않는다.

사용 정책은 군사·전쟁·핵 산업·ITAR 대상, 임계 인프라·교통·중장비 운용, 면허 없는 전문직 행위(금융·법률·의료), 사람이 생성한 것이라는 허위 표시, 만 18세 미만 대상 등을 금지한다. 가중치는 이름·생년월일·국가·소속을 입력하고 승인을 받아야 한다(Hugging Face 수동 승인). Hugging Face 태그는 license:other다. 한 개발자가 X에서 Llama 3 라이선스보다 나쁘다고 평한 글이 검색에 잡혔으나 발췌만 읽었고 법률 해석은 이 노트의 범위가 아니다. 파생물 정의가 출력으로 훈련된 모델까지 포함하므로 증류와 합성 데이터 활용 시 표기·사용 정책 의무가 따라올 수 있다는 점을 점검해야 한다.

## 읽을 때 유의할 점

첫째, 공개 글과 모델 카드는 모두 Meta의 자기 보고다. "가장 유능한 미국 오픈웨이트"는 Meta가 고른 비교군에서의 서술이며 모델 카드가 요구하는 안전 조건도 Meta의 평가 틀에서 나온 것이다. 둘째, 맥 스튜디오 구동은 구체 속도가 없어 "돌아간다"와 "쓸 만하게 돌아간다"가 구분되지 않는다. 셋째, 라이선스는 완전한 오픈소스 정의가 아닌 조건부 허용이며 Meta 스스로 "limited commercial terms"라고 부른다. 넷째, 모델 카드는 학습 데이터에 공개 출처, 인터넷 크롤링, 제3자 확보분, Meta 제품·서비스에서 파생된 데이터, 합성 데이터가 들어 있다고 쓴다. 이 블로그의 [Nieman Lab 노트](https://raphael-shin.github.io/jungseob-blog/posts/nieman-meta-commercial-terms-scraping-news-sites/)가 다룬 같은 날의 약관 변경과 이 학습 데이터 서술의 직접 연결은 확인되지 않았다.

그럼에도 가져갈 점검 질문은 선명하다. 내 작업에서 에이전트 과제와 코딩 과제 중 무엇이 중요한가(표에서 강약이 갈린다), 700GB 이상 메모리를 감당할 하드웨어나 호스팅 제공자가 있는가, 라이선스의 표기·MaaS 매출 조건이 내 제품 모델에 걸리는가, 증류나 합성 데이터 용도가 있다면 파생물 정의를 법무와 검토했는가, 독립 평가가 나오기 전에 어떤 결정을 미룰 것인가. 이 블로그의 [Mistral Large 4 노트](https://raphael-shin.github.io/jungseob-blog/posts/mistral-large-4-open-weight-preview/)와 함께 읽으면 오픈웨이트 경쟁 구도가 보인다.

## 참고 자료

[Meta Superintelligence Labs — Introducing Muse Spark Open (Meta AI Research, 2026-10-15)](https://research.meta.ai/blog/muse-spark-open) — 본문을 읽고 정리했다. 벤치마크 이미지와 평가 방법론 보고서는 읽지 못했다.

[Muse Spark Open Model Card (ModelScope 미러)](https://www.modelscope.cn/models/meta-models/Muse-Spark-Open-816B-A42B) — Hugging Face 원본은 승인 없이 열리지 않아 미러에서 모델 카드, 벤치마크 표, 안전 평가, 라이선스 전문을 읽었다.

[Hugging Face — Welcome Muse Spark Open](https://huggingface.co/blog/meta-muse-spark-open) — 구조와 메모리 요구, 추론 지원 설명의 앞부분을 읽었다.

[technology.org — Meta Releases 816B Open-Weight Muse Spark Open](https://www.technology.org/2026/10/16/meta-muse-spark-open-816b-open-weight-mac-studio) — 독립 검증이 아직 없다는 서술과 체크포인트 크기를 확인했다. 검색 결과 발췌로 읽었다.
