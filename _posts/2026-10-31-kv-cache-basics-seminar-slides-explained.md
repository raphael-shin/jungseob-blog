---
layout: post
title: "KV Cache 기초 세미나 34장을 쉽게 풀어 읽기, 토큰이 하나씩 나올 때 과거 계산을 저장하는 이유부터 PagedAttention과 prefix caching과 분리 서빙과 diffusion LLM까지"
date: "2026-10-31 21:11:31 +0900"
created: "2026-10-31T21:11:31+09:00"
source: "https://docs.google.com/presentation/d/1KlI7ubYbKLFxdP6JyBqRGEzx6-Rx1OvB/edit"
source_title: "KV Cache 기초.pptx (Google Slides, 34장)"
author: jungseob
source_author: "미상 (LLM 추론 기초 세미나 발표 자료)"
source_published: ""
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "LLM 추론 기초 세미나 슬라이드 「KV Cache 기초」 34장의 본문과 발표자 노트를 모두 읽고 장마다 캡처해 쉬운 말로 풀어 쓴다. 토큰을 하나씩 만드는 LLM이 과거 계산을 반복하는 낭비와 causal mask 덕분에 K·V를 저장해도 결과가 같은 이유, prefill과 decode의 병목 차이, TTFT와 TPOT과 ITL, 캐시 크기 공식과 Llama 3 8B 예시, GQA로 줄이기, PagedAttention과 continuous batching과 prefix caching, 분리 서빙, diffusion LLM에서 전제가 흔들리는 이유를 다룬다. 슬라이드의 수치를 직접 다시 계산하고 vLLM 논문과 arXiv 제목으로 대조했다."
image:
  path: "https://raphael-shin.github.io/jungseob-blog/assets/img/kv-cache-basics/slide-01.png"
  alt: "KV Cache 기초 세미나 표지 슬라이드"
tags:
  - knowledge
  - blog
  - AI
  - LLM
  - 추론
---

## TL;DR

- LLM은 토큰을 한 번에 하나씩 만들고, 방금 만든 토큰을 다시 입력 끝에 붙인다. 캐시가 없으면 매번 과거 전체의 K·V를 다시 계산하므로, 프롬프트 4토큰에 6스텝만 돌려도 39번 중 30번(77%)이 중복이고 길이 n까지 가면 낭비가 n² 규모로 커진다.
- 캐시가 정확한 이유는 causal mask 때문이다. 과거 토큰은 뒤에 무엇이 오든 영향을 받지 않아 K·V가 변하지 않으므로, 저장해 재사용해도 근사가 아니라 완전히 같은 결과가 나온다.
- 캐시는 계산을 메모리로 바꾸는 거래다. 크기는 2 × 레이어 × KV 헤드 × 헤드 차원 × 바이트 × 토큰 수이고, Llama 3 8B FP16에서 토큰당 128KiB, 8K 토큰 요청당 1GiB라서 배치 32면 32GiB로 모델 가중치(약 15GiB)의 두 배가 된다.
- 그래서 추론 엔진은 사실상 KV 메모리 관리 시스템이다. PagedAttention은 블록으로 쪼개 낭비를 줄이고, continuous batching은 스텝마다 요청을 갈아 끼우며, prefix caching은 같은 앞부분을 한 번만 계산한다.
- 이 규칙이 클러스터로 커지면 prefill과 decode를 다른 GPU로 나누는 분리 서빙이 되고, 양방향 attention을 쓰는 diffusion LLM에서는 전제가 깨져 근사 캐시나 블록 구조로 되살린다.

## 이 자료와 이 노트의 방식

Google Slides로 공유된 「KV Cache 기초」 세미나 자료이고 34장이다. 발표자 이름은 파일 어디에도 없어 확인하지 못했다. 슬라이드 본문과 발표자 노트(34장 모두 있다)를 내려받아 읽었고 모든 장을 이미지로 캡처했다. 표지는 이 글 맨 위 이미지로 썼고 2장부터 31장까지는 해당하는 대목에 붙였다. 32장부터 34장은 논문 목록이라 이미지 대신 글 끝의 참고 자료에 링크로 옮겼다.

쉽게 풀어 쓰기 위해 이 노트가 슬라이드 밖에서 보탠 것은 비유다. 도서관, 식당, 버스 같은 비유는 모두 이 노트의 설명이고 슬라이드에는 없다. 숫자와 구조는 슬라이드와 발표자 노트를 따랐으며 직접 다시 계산한 값은 따로 밝혔다. 같은 주제를 가격 쪽에서 다룬 이 블로그의 [DeepSeek KV 캐시와 서구 연구소의 캐시 가격 노트](https://raphael-shin.github.io/jungseob-blog/posts/deepseek-kv-cache-and-western-labs-cache-prices/)와 함께 보면 좋다.

## 1부: 왜 캐시가 필요한가

![2장 아젠다: 오늘 다룰 다섯 가지](/assets/img/kv-cache-basics/slide-02.png)
발표는 다섯 부분이다. 왜 필요한가, attention과 Q·K·V, 계산과 메모리, 추론 엔진, 그리고 확장과 diffusion LLM이다. 발표자 노트는 오늘 이야기가 "토큰이 하나 생성될 때마다 K와 V가 한 줄씩 쌓이는 것"이라는 한 문장으로 모인다고 한다.

![3장 LLM은 토큰을 한 번에 하나씩 생성한다](/assets/img/kv-cache-basics/slide-03.png)
LLM은 다음 토큰 하나를 맞히는 모델이다. "오늘 날씨가"를 넣으면 "정말"을 내고 그 "정말"을 뒤에 붙여 "오늘 날씨가 정말"을 다시 넣으면 "맑고"를 낸다. 끝말잇기를 하는데 매번 첫 글자부터 다시 읽고 시작하는 모습을 떠올리면 된다. 이것이 자기회귀 생성이고 스텝마다 입력이 1토큰씩 길어진다. 이때 세 번째 스텝에서 "오늘 날씨가 정말"을 또 처리해야 하느냐는 질문의 답이 KV Cache다.

![4장 캐시가 없으면 매 스텝 과거 전체를 다시 계산한다](/assets/img/kv-cache-basics/slide-04.png)
캐시가 없으면 답은 "처리해야 한다"이고 낭비가 크다. 슬라이드의 예는 프롬프트 4토큰에 6스텝이다. 토큰별 K·V 계산을 모두 세면 4+5+6+7+8+9 = 39번이고 그중 새로 필요한 것은 처음 4번과 이후 스텝당 1번인 9번뿐이라 나머지 30번이 이미 했던 계산이다. 30을 39로 나누면 약 77%이며 슬라이드의 숫자가 맞는다. 길이 n까지 생성하면 1+2+…+n ≈ n²/2라서 길수록 낭비가 제곱으로 커진다.

## 2부: Attention과 Q·K·V

![5장 각 토큰은 세 개의 벡터 Q, K, V로 투영된다](/assets/img/kv-cache-basics/slide-05.png)
attention 층에 들어온 토큰은 학습된 세 가중치 행렬 W_Q, W_K, W_V와 곱해져 세 벡터가 된다. 발표자 노트의 검색 엔진 비유가 가장 쉽다. Q(Query)는 검색어, K(Key)는 문서의 색인, V(Value)는 문서 본문이다. 도서관 비유로 옮기면, Q는 "이런 내용을 찾고 싶어요"라고 적은 질문 쪽지이고 K는 책마다 붙은 색인 카드이며 V는 책 속 내용이다. 내 질문 쪽지와 모든 색인 카드를 맞춰 보고 잘 맞는 책의 내용을 더 많이 섞어 가져온다. 이 투영은 모든 레이어와 모든 헤드에서 따로 일어난다는 점이 뒤의 캐시 크기 계산에 그대로 들어간다.

![6장 Attention은 행렬 곱 두 번과 softmax 한 번](/assets/img/kv-cache-basics/slide-06.png)
수식은 softmax(Q·Kᵀ/√d)·V 하나다. Q와 K를 곱하면 "누가 누구와 얼마나 비슷한가"를 적은 n×n 점수표가 나오고 softmax가 각 행을 합이 1인 가중치로 바꾸며 그 가중치로 V를 섞어 출력을 만든다. 점수표의 한쪽 삼각형이 회색인 이유가 다음 장이다.

![7장 causal mask: 각 토큰은 자신과 과거만 본다](/assets/img/kv-cache-basics/slide-07.png)
글을 이어 쓰는 디코더형 LLM은 자신과 앞쪽 토큰만 볼 수 있다. 미래 칸에 −∞를 넣어 두면 softmax를 지난 뒤 가중치가 0이 되어, 뒤에 무엇이 오든 이 토큰의 결과에 영향이 없다. 일기에 비유하면 어제의 일기는 오늘 무슨 일이 생겨도 다시 쓰이지 않는다. 그래서 어떤 토큰의 hidden state와 거기서 나오는 K·V는 뒤에 토큰이 붙어도 절대 변하지 않는다. 이것이 KV Cache가 정확한 이유이며 발표자 노트도 "근사가 아니라 완전히 같은 결과"라고 강조한다.

![8장 핵심 관찰: 다음 스텝에서 새로 필요한 건 마지막 한 행뿐이다](/assets/img/kv-cache-basics/slide-08.png)
step t와 step t+1의 점수표를 겹쳐 보면 위쪽 t개 행은 완전히 같고 새로 필요한 것은 맨 아래 한 행이다. 새 토큰의 질문 쪽지 하나를 모든 색인 카드와 맞춰 보는 일이다. 그러려면 과거의 K와 V는 계속 필요하니 저장해 둔다. 반면 과거 토큰의 Q는 한 번 쓴 질문 쪽지라서 다시 쓰이지 않으므로 Q는 저장하지 않는다. "Q cache"는 없다는 점이 자주 나오는 질문이라고 발표자 노트가 짚는다.

## 3부: 계산 흐름과 메모리

![9장 KV Cache를 쓰는 decode 한 스텝](/assets/img/kv-cache-basics/slide-09.png)
캐시를 쓰는 decode 한 스텝은 네 단계다. 새 토큰 하나의 q, k, v를 만들고 k와 v를 캐시 끝에 붙이고 q 하나로 캐시 전체와 attention을 계산하고 출력을 다음 레이어로 보낸다. 새로 투영하는 것은 토큰 1개분이지만 attention은 매 스텝 캐시 전체(t개)를 읽는다는 점이 뒤의 병목으로 이어진다.

![10장 코드로 보면: prefill과 decode](/assets/img/kv-cache-basics/slide-10.png)
같은 내용을 의사 코드로 옮긴 장이다. prefill에서는 프롬프트 전체 X로 K_cache와 V_cache를 한 번에 만들고 decode에서는 새 토큰의 q, k, v만 만들어 k와 v를 캐시에 붙인 뒤 q@K_cache.T로 점수를 구한다. 슬라이드는 한 레이어, 한 헤드만 보이고 norm, RoPE, 잔차 연결, MLP를 생략한 단순화라고 밝힌다. 실제 엔진은 매번 concat하지 않고 미리 잡아 둔 메모리 블록에 슬롯 단위로 써 넣는다.

![11장 추론은 두 단계: prefill이 채우고 decode가 늘린다](/assets/img/kv-cache-basics/slide-11.png)
추론은 숙제를 푸는 일에 비유할 수 있다. prefill은 문제지 전체를 한꺼번에 읽고 이해하는 단계이고 decode는 답안을 한 글자씩 쓰는 단계다. 다음 표는 두 단계의 차이를 14장 정리표와 11~13장에서 모았다.

| 항목 | Prefill | Decode |
| --- | --- | --- |
| 하는 일 | 프롬프트 n개를 한꺼번에 처리하고 KV를 채운다 | 직전 토큰 1개를 처리하고 KV 한 줄을 붙인다 |
| 연산 형태 | 행렬 × 행렬(큰 GEMM) | 벡터 × 행렬(배치하면 GEMM) |
| 병목 | 대개 연산(compute-bound) | 대개 메모리 대역폭(memory-bound) |
| 대표 지표 | TTFT | TPOT, ITL |
| 주요 최적화 | prefix caching, chunked prefill | 큰 배치, GQA, FP8 KV, speculative decoding |

연산이 병목이라는 것은 요리사 손이 너무 바쁜 상태이고 메모리 대역폭이 병목이라는 것은 요리는 금방 되는데 재료를 창고에서 가져오는 데 시간이 다 드는 상태다. decode는 토큰 하나를 만들 때도 모델 가중치 전체와 캐시 전체를 읽어야 하므로 후자에 가깝다. 이 점이 뒤에서 여러 요청을 묶는 배칭이 중요한 이유가 된다.

![12장 Prefill 자세히: 프롬프트 전체로 KV를 채운다](/assets/img/kv-cache-basics/slide-12.png)
prefill은 임베딩 뒤 레이어 1부터 L까지를 차례로 통과한다. 각 레이어에서 n개 토큰의 q, k, v를 한 번에 계산하고 k·v를 캐시 블록에 쓰고 n×n causal attention과 MLP를 지나 다음 레이어로 보낸다. 발표자 노트가 강조하는 점은 K·V만 따로 구할 수 없다는 것이다. 레이어 2의 K·V는 레이어 1의 attention과 MLP 출력에서 나오기 때문에 모델을 끝까지 돌려야 한다. 마지막 위치에만 lm_head를 적용해 첫 토큰을 뽑고 이 시점의 캐시에는 프롬프트 n개분만 있다. 첫 토큰 "정말"의 K·V는 다음 decode 스텝에서 추가된다. 노트는 예외도 적는다. 프롬프트 전체가 prefix 캐시에 맞아도 KV만으로는 다음 토큰의 logits를 얻을 수 없어, vLLM은 마지막 토큰 하나를 다시 계산한다.

![13장 Decode 자세히: 캐시를 읽고 한 줄씩 쓴다](/assets/img/kv-cache-basics/slide-13.png)
decode는 입력이 직전 토큰 1개이고 첫 스텝의 입력이 prefill이 낸 첫 토큰이라서 그 K·V가 이때 처음 캐시에 들어간다. 레이어마다 읽고 쓰기를 반복하고 마지막에 lm_head로 다음 토큰을 뽑아 EOS나 최대 길이까지 되풀이한다. 토큰 하나를 위해 가중치와 캐시를 통째로 읽으므로, 한 번 읽은 가중치를 여러 요청이 나눠 쓰도록 배치로 묶으면 처리량이 크게 오른다. 다만 KV Cache는 요청마다 따로 읽어야 해서 배치가 커질수록 캐시 읽기의 비중이 커진다.

![14장 Prefill과 Decode 한눈에](/assets/img/kv-cache-basics/slide-14.png)
앞의 표가 이 장의 내용이다. 두 단계는 병목이 달라 최적화 방향도 다르다. prefill은 계산 자체를 줄이는 prefix caching과 긴 프롬프트를 쪼개 다른 요청을 방해하지 않게 하는 chunked prefill이 대표적이고 decode는 배치를 키우고 읽을 KV를 줄이는 GQA와 FP8, 한 번에 여러 토큰을 검증하는 speculative decoding이 대표적이다. 이 성격 차이가 5부의 분리 서빙으로 이어진다.

![15장 지연 지표 세 가지: TTFT, TPOT, ITL](/assets/img/kv-cache-basics/slide-15.png)
식당에 비유하면 TTFT는 주문한 뒤 첫 접시가 나오기까지의 시간이고 이후 접시와 접시 사이의 간격이 ITL이며 그 간격의 평균이 TPOT이다. TTFT는 큐 대기와 prefill로 이루어져 프롬프트가 길거나 prefix 캐시가 맞지 않으면 커진다. ITL은 일정하지 않다. 다른 요청의 긴 prefill이 같은 배치에 끼어들면 그 스텝만 튀므로 평균보다 P99 같은 분포로 본다. 전체 지연은 TTFT + TPOT × (N − 1)이다. 발표자 노트는 측정 도구마다 ITL과 TPOT을 섞어 쓰니 정의부터 확인하라고 덧붙인다.

![16장 K·V 계산량: n²에서 n으로](/assets/img/kv-cache-basics/slide-16.png)
캐시를 쓰면 K·V 투영은 스텝당 1개라서 n² 규모에서 n으로 줄어든다. 다만 attention 점수 계산은 여전히 스텝마다 t개의 키를 읽으므로 누적 비용이 n²이다. 슬라이드의 표현으로 KV Cache는 연산을 메모리로 바꾼 거래이고 이제 병목은 메모리 용량과 대역폭이다. 계산 시간을 아끼는 대신 풀이 노트를 계속 쌓아 두는 셈이다.

![17장 KV Cache 크기 계산 공식](/assets/img/kv-cache-basics/slide-17.png)
크기 공식은 2 × 레이어 수 × KV 헤드 수 × 헤드 차원 × dtype 바이트이며 토큰 하나당 크기다. 맨 앞의 2는 K와 V 두 벡터를 저장한다는 뜻이고 Q를 저장하지 않으므로 3이 아니다. 맨 뒤의 2B는 FP16 한 값이 2바이트라는 뜻으로 다른 2다. Llama 3 8B를 레이어 32, KV 헤드 8, 헤드 차원 128, FP16 조건으로 계산하면 2 × 32 × 8 × 128 × 2 = 131,072바이트이므로 128KiB가 맞다. 여기에 8,192토큰을 곱하면 정확히 1GiB, 동시 요청 32개면 32GiB다. 비교로 든 Llama 2 7B는 KV 헤드가 32개라 같은 계산에서 토큰당 512KiB로 4배다. 이 노트는 이 숫자들을 직접 다시 곱해 확인했다.

![18장 배치가 커지면 KV Cache가 모델 가중치보다 커진다](/assets/img/kv-cache-basics/slide-18.png)
모델 가중치는 80억 개 파라미터에 FP16이라 약 15GiB로 고정이다. 반면 KV Cache는 요청 수와 문맥 길이에 비례해 늘어 배치 8이면 8GiB, 32면 32GiB로 가중치의 두 배, 64면 64GiB가 되어 80GB GPU 한 장에 가중치와 함께 들어가지 않는다. GPU 메모리는 가중치, KV Cache, 활성값이 나눠 쓰므로, 남은 메모리를 KV Cache에 얼마나 잘 쓰느냐가 동시 처리량을 정한다.

![19장 KV 헤드를 공유해 캐시를 줄인다: MHA, GQA, MQA](/assets/img/kv-cache-basics/slide-19.png)
공식에서 줄일 수 있는 항목이 KV 헤드 수다. 원래 multi-head attention(MHA)은 Q 헤드마다 자기 K·V를 가진다. 학생 여덟 명이 사전을 한 권씩 따로 가지는 격이다. GQA는 Q 헤드 여럿이 KV 한 그룹을 공유해(Q 8 대 KV 2) 사전을 두 권만 두고 돌려 본다. 캐시는 MHA의 4분의 1이고 Llama 3, Mistral, Qwen이 쓴다. MQA는 K·V를 하나만 두어(Q 8 대 KV 1) 8분의 1이 되며 PaLM과 Falcon이 쓴다. 슬라이드는 이 밖에 KV 양자화(FP8, INT4), DeepSeek의 MLA(잠재 벡터로 압축), 슬라이딩 윈도와 토큰 축출(StreamingLLM, H2O)을 소개한다.

## 4부: 추론 엔진이 캐시를 관리하는 방식

![20장 최대 길이만큼 연속 예약하면 단편화로 메모리를 낭비한다](/assets/img/kv-cache-basics/slide-20.png)
초기 서빙 시스템은 얼마나 생성할지 모르니 요청마다 최대 길이만큼 연속된 공간을 미리 잡았다. 영화관에서 단체 예약을 하면서 최대 인원 수만큼 붙은 좌석을 잡아 놓는 것과 같다. 쓰지 않는 예약 좌석이 남는 내부 단편화, 요청마다 크기가 달라 사이사이 못 쓰는 틈이 생기는 외부 단편화, 같은 프롬프트도 요청마다 복사해야 하는 공유 불가가 겹친다. 슬라이드는 vLLM 논문(SOSP 2023)을 인용해 기존 시스템이 KV 메모리의 20.4~38.2%만 실제 토큰 저장에 썼다고 한다. 이 노트가 논문 본문(그림 2)을 열어 확인했고 같은 그림에서 vLLM은 약 96.3%로 나온다.

![21장 PagedAttention: KV Cache를 고정 크기 블록으로 나눈다](/assets/img/kv-cache-basics/slide-21.png)
PagedAttention은 운영체제의 가상 메모리를 빌려 온다. 캐시를 고정 크기 블록(예시는 4토큰, vLLM 기본값은 16)으로 쪼개고 요청마다 block table로 논리 블록과 물리 블록을 잇는다. 슬라이드의 요청 A는 논리 블록 0, 1, 2가 물리 #7, #1, #3에 흩어져 있고 마지막 블록은 4칸 중 2칸만 찼다. 영화관 비유로는 단체석을 붙여 잡지 않고 낱개 좌석을 흩어 받되 표 한 장(block table)에 좌석 번호를 순서대로 적어 두는 방식이다. 낭비는 마지막 블록의 빈칸뿐이고 블록이 차면 하나씩 더 받는다. 기본값 16은 논문이 GPU를 충분히 쓰면서 단편화는 작게 하는 크기로 골랐다고 밝힌 값이다.

![22장 Continuous batching: 스텝마다 요청이 들어오고 나간다](/assets/img/kv-cache-basics/slide-22.png)
블록 단위로 메모리를 주고받을 수 있으니 스케줄러가 매 스텝 배치를 다시 짠다. 전세버스는 모두가 종점에 닿을 때까지 기다리지만 정류장마다 내리고 타는 노선버스는 자리가 비는 즉시 다음 손님이 탄다. 끝난 요청의 블록은 바로 free list로 돌아가 대기 요청이 다음 스텝에 합류한다. 블록이 모자라면 일부 요청을 선점해 블록을 회수한 뒤 나중에 다시 계산하거나 CPU 메모리에서 되돌려 온다. prefill과 decode를 한 배치에 섞는 것은 별도의 스케줄링 정책(예: chunked prefill)이라고 슬라이드가 구분한다.

![23장 Prefix caching: 같은 앞부분은 한 번만 계산한다](/assets/img/kv-cache-basics/slide-23.png)
여러 요청이 같은 시스템 프롬프트로 시작하면 그 부분의 KV 블록을 한 벌만 두고 요청들의 block table이 같은 물리 블록을 가리키게 한다. 같은 교과서를 반 학생 모두가 돌려 보고 각자 자기 질문만 따로 적는 모습이다. 참조 카운트가 3이 되고 각 요청은 자기 질문 부분만 새로 계산해서, 공유 부분의 prefill을 건너뛰어 TTFT가 줄고 메모리도 한 벌만 쓴다. 공유 블록에 써야 하면 copy-on-write로 복사한다. 멀티턴 대화, 긴 시스템 프롬프트, few-shot, 에이전트에 잘 맞고 vLLM은 블록 해시(APC), SGLang은 RadixAttention으로 구현한다.

![24장 KV Cache는 어떻게 찾나](/assets/img/kv-cache-basics/slide-24.png)
찾는 방법은 두 층이다. 한 요청 안에서는 검색이 아니라 계산이다. 토큰 위치 9를 블록 크기 4로 나눈 몫 2가 논리 블록이고 나머지 1이 칸 번호이며 block_table[2]가 #3이므로 물리 블록 #3의 슬롯 1이다. 다른 요청이 만든 캐시를 재사용할 때는 해시를 조회한다. 꽉 찬 블록마다 "앞 블록의 해시 + 이 블록의 토큰"으로 해시를 만들어 앞에서부터 차례로 조회하고 맞으면 공유하며 처음 틀리는 곳부터 새로 prefill한다. 앞 블록의 해시가 체인으로 들어가므로 같은 토큰이라도 앞부분이 다르면 맞지 않는다. 앞 문맥이 다르면 K·V 값도 다르기 때문에 이것이 정확한 동작이라고 발표자 노트가 설명한다. 참조 중이지 않은 블록만 메모리가 필요할 때 LRU로 축출하고 SGLang은 radix tree에서 가장 긴 공통 prefix를 찾는다.

![25장 한 요청의 여정: KV 블록을 빌리고 돌려준다](/assets/img/kv-cache-basics/slide-25.png)
한 요청의 흐름으로 묶으면 이렇다. 요청이 오면 스케줄러가 빈 블록이 충분한지 보고 KV Cache Manager가 prefix 캐시에서 재사용할 블록을 찾고 나머지를 새로 받는다. prefill로 miss 구간을 채워 첫 토큰을 내고 decode 루프에서 한 칸씩 늘리며 블록이 차면 하나를 더 받고 끝나면 블록을 돌려준다. 엔진은 스케줄러, 블록 풀과 free list와 해시 테이블과 block table을 맡는 KV Cache Manager, block table을 받아 커널을 돌리는 Model Runner로 이루어진다.

![26장 더 나아가기: 요즘 엔진이 KV Cache로 하는 일](/assets/img/kv-cache-basics/slide-26.png)
요즘 엔진이 캐시로 하는 일은 네 가지다. chunked prefill은 긴 프롬프트를 조각내 decode와 섞어 처리해 decode 지연의 튐을 줄이며 청크 크기로 TTFT와 ITL을 절충한다. prefill과 decode를 다른 GPU에서 돌리고 만든 KV를 네트워크로 넘기는 분리 서빙이 있다. KV offload는 GPU에서 밀려난 블록을 CPU와 SSD, 원격 저장소에 두었다가 맞으면 다시 불러온다. KV 양자화는 FP8로 용량을 절반으로 줄여 같은 GPU에 더 많은 요청과 긴 문맥을 담는다. 모두 캐시를 어디에, 얼마나 작게, 얼마나 오래 둘 것이냐의 문제다.

## 5부: 클러스터로, 그리고 전제가 깨질 때

![27장 Disaggregated serving: prefill과 decode를 다른 GPU로](/assets/img/kv-cache-basics/slide-27.png)
prefill은 연산, decode는 메모리 대역폭이 병목이라 한 GPU에 섞으면 서로 방해한다. 식당에서 재료 손질팀과 조리팀을 나누고 손질이 끝난 재료를 운반하는 것과 같다. 분리 서빙은 prefill 풀과 decode 풀을 나누고 prefill 노드가 만든 KV 블록을 RDMA나 NVLink로 decode 노드에 넘긴다. KV 인식 라우터는 prefix가 많이 겹치는 노드로 요청을 보내고 밀려난 블록은 전역 KV 풀(Mooncake Store, LMCache 등)에 둔다. 단일 엔진의 구조가 그대로 커진 것이다. block table은 노드 간 블록 전송이 되고 해시 테이블은 클러스터 전역 인덱스가 되며 LRU 축출은 CPU와 SSD로 이어지는 계층형 풀이 된다. 해시 키는 내용 기반이어서 모델과 입력 조건이 같으면 어느 노드에서 계산해도 같은 값이 나온다. 그래서 vLLM은 해시에 토큰 외에 LoRA ID나 멀티모달 입력 해시도 넣고 전송하려면 dtype과 메모리 배치도 맞아야 한다.

![28장 전송할까, 다시 계산할까: KV 크기가 곧 네트워크 비용](/assets/img/kv-cache-basics/slide-28.png)
나누면 KV를 네트워크로 옮겨야 하고 크기는 앞의 공식으로 바로 나온다. Llama 3 8B, 8,192토큰 프롬프트는 1GiB이고 400Gb/s(50GB/s) 링크에서 이론상 약 21밀리초다. 1GiB를 50GB/s로 나누면 약 21.5ms라서 이 노트가 계산한 값도 같다. 레이어 단위로 계산과 겹치면 체감은 더 줄어든다. 토큰당 전송량은 Llama 2 7B는 MHA와 FP16 조건에서 512KiB, Llama 3 8B는 GQA와 FP16 조건에서 128KiB이고 같은 모델에 FP8 KV를 쓰면 64KiB로 8분의 1이 된다. GQA, MLA, FP8처럼 KV를 줄이는 기법이 곧 전송량 절감이라서 DeepSeek 계열이 MLA와 분리 서빙을 함께 쓴다는 것이 발표자 노트의 설명이다. 분리가 유리한 때는 긴 프롬프트, 엄격한 TTFT·TPOT 목표, 큰 클러스터이고 짧은 프롬프트나 작은 규모에서는 전송 오버헤드와 운영 복잡도(노드 비율, KV 배치 변환)가 이득보다 클 수 있다.

![29장 Diffusion LLM: causal mask가 사라지면 K·V가 매 스텝 바뀐다](/assets/img/kv-cache-basics/slide-29.png)
diffusion LLM(LLaDA, Dream, Mercury, Gemini Diffusion)은 응답 길이만큼 빈칸(MASK)을 깔아 놓고 양방향 attention으로 전체를 보며 확신이 높은 칸부터 여러 개를 동시에 채운다. 낱말 퍼즐에서 한 칸을 채우면 그 칸과 얽힌 다른 칸의 해석이 모두 달라지는 것과 비슷하다. 앞에서 KV Cache가 정확한 이유는 causal mask가 과거 K·V를 고정해 주기 때문이라고 했는데, 여기서는 모두가 모두를 보므로 한 칸이 바뀔 때마다 모든 토큰의 hidden state와 K·V가 조금씩 바뀐다. 그래서 과거 KV 전체를 그대로 재사용하기 어렵고 순수하게 하면 매 스텝 전체를 다시 계산하며 병목은 메모리 대역폭에서 연산으로 옮겨 간다.

![30장 그래도 KV Cache는 다시 돌아온다: 근사 캐시와 블록 diffusion](/assets/img/kv-cache-basics/slide-30.png)
캐시가 사라진 것은 아니고 되돌아오는 흐름이다. 첫째는 근사 캐시다. 프롬프트와 이미 확정된 토큰의 K·V는 스텝 사이에 거의 변하지 않는다는 관찰을 이용해 캐시해 두고 가끔만 갱신한다(Fast-dLLM, dKV-Cache, dLLM-Cache). 품질 손실이 작은 대신 근사이다. 둘째는 블록 diffusion이다. 블록 사이는 자기회귀처럼 causal로, 블록 안에서만 diffusion을 하면 끝난 블록의 K·V가 고정되어 블록 단위로 정확한 캐시가 다시 성립한다(BD3-LM). 오늘 배운 원리인 "과거가 고정되면 캐시할 수 있다"가 여기서도 설계 기준이다. 서빙 쪽은 페이징과 스텝 단위 스케줄링 원리를 그대로 쓸 수 있지만 반복 갱신과 병렬 토큰 생성에 맞는 스케줄링과 캐시 관리는 아직 열린 문제라고 발표자 노트가 말한다. 소개한 모델과 기법 이름은 2026년 중반 기준이니 최신 현황은 따로 확인하라는 단서도 붙어 있다.

## 정리

![31장 KV Cache, 다섯 문장으로](/assets/img/kv-cache-basics/slide-31.png)
다섯 문장으로 줄이면 이렇다. causal mask 덕분에 과거 K·V는 변하지 않으니 저장해 재사용한다(Q는 저장하지 않는다). prefill이 캐시를 채우고 decode는 캐시 전체를 읽으며 한 줄씩 늘린다. 크기는 2 × 레이어 × KV 헤드 × 헤드 차원 × 바이트 × 토큰 수라서 금세 가중치보다 커진다. 추론 엔진의 핵심은 KV 메모리 관리이며 페이징, continuous batching, prefix caching이 그 도구다. 분리 서빙은 KV를 클러스터 자원으로 옮기고 diffusion LLM은 근사 재사용이나 블록 구조로 정확한 재사용을 되살린다.

## 읽을 때 유의할 점

첫째, 슬라이드의 모델 수치는 Llama 3 8B와 Llama 2 7B의 구조(레이어, KV 헤드, 헤드 차원)에 기댄다. 이 노트는 공식에 넣어 계산이 맞는지 확인했지만 두 모델의 구조 값 자체를 모델 카드에서 대조하지는 않았다. 둘째, "21ms"는 링크 이론 대역폭으로 나눈 값이라서 실제 전송 지연이 아니고 프로토콜 오버헤드와 계층 겹침은 반영하지 않는다. 셋째, prefill이 대개 연산 병목이고 decode가 대개 메모리 병목이라는 서술은 슬라이드도 "대개"라고 단서를 달며 배치와 문맥 길이에 따라 달라진다. 넷째, 5부의 시스템과 모델 이름은 자료가 2026년 중반 기준이라고 밝히고 있어 현황이 바뀌었을 수 있다. 다섯째, 자료의 작성자를 확인하지 못했다. 이 노트의 이미지는 공유 링크로 열 수 있는 자료에서 캡처한 것이며 작성자가 원치 않으면 내려야 한다.

## 참고 자료

[KV Cache 기초 세미나 슬라이드 (Google Slides, 34장)](https://docs.google.com/presentation/d/1KlI7ubYbKLFxdP6JyBqRGEzx6-Rx1OvB/edit): 본문과 발표자 노트 전체를 읽고 장마다 캡처했다.

[Attention Is All You Need (Vaswani 외, NeurIPS 2017)](https://arxiv.org/abs/1706.03762): Q·K·V와 attention의 출발점이다. 32장의 목록으로 arXiv 제목을 대조했다.

[Fast Transformer Decoding: One Write-Head is All You Need (Shazeer, 2019)](https://arxiv.org/abs/1911.02150): MQA다.

[GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints (Ainslie 외, EMNLP 2023)](https://arxiv.org/abs/2305.13245): GQA다.

[DeepSeek-V2 (DeepSeek-AI, 2024)](https://arxiv.org/abs/2405.04434): MLA가 소개된 논문이다.

[Efficient Streaming Language Models with Attention Sinks (Xiao 외, ICLR 2024)](https://arxiv.org/abs/2309.17453): StreamingLLM이다.

[H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models (Zhang 외, NeurIPS 2023)](https://arxiv.org/abs/2306.14048): 토큰 축출이다.

[Orca (Yu 외, OSDI 2022)](https://www.usenix.org/conference/osdi22/presentation/yu): 스텝 단위 스케줄링이다. 이 노트는 링크만 옮겼고 열어 보지 않았다.

[Efficient Memory Management for Large Language Model Serving with PagedAttention (Kwon 외, SOSP 2023)](https://arxiv.org/abs/2309.06180): 20.4~38.2% 수치와 블록 크기 16 기본값을 본문에서 확인했다.

[SGLang: Efficient Execution of Structured Language Model Programs (Zheng 외, NeurIPS 2024)](https://arxiv.org/abs/2312.07104): RadixAttention이다.

[Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve (Agrawal 외, OSDI 2024)](https://arxiv.org/abs/2403.02310): chunked prefill이다.

[DistServe (Zhong 외, OSDI 2024)](https://arxiv.org/abs/2401.09670): prefill과 decode 분리다.

[Splitwise: Efficient generative LLM inference using phase splitting (Patel 외, ISCA 2024)](https://arxiv.org/abs/2311.18677): 단계별 하드웨어 분리다.

[Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving (Qin 외, 2024)](https://arxiv.org/abs/2407.00079): Kimi의 분리 서빙과 KV 풀이다.

[Large Language Diffusion Models (Nie 외, 2025)](https://arxiv.org/abs/2502.09992): LLaDA다.

[Block Diffusion (Arriola 외, ICLR 2025)](https://arxiv.org/abs/2503.09573): BD3-LM이다.

[Fast-dLLM (Wu 외, 2025)](https://arxiv.org/abs/2505.22618): 블록 단위 근사 KV Cache와 병렬 디코딩이다.

[dKV-Cache (Ma 외, 2025)](https://arxiv.org/abs/2505.15781): 확정된 토큰을 한 스텝 늦게 캐시한다.

[dLLM-Cache (2025)](https://arxiv.org/abs/2506.06295): 프롬프트와 응답을 다른 주기로 갱신한다.
