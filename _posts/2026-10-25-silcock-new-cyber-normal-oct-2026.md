---
layout: post
title: "한 주에 몰린 사이버 사고 아홉 건은 새로운 정상인가, Drew Silcock의 PHP2Shell·eMudhra·LiteLLM 정리를 공식 공지와 보도로 대조한 정리"
date: "2026-10-25 17:07:33 +0900"
created: "2026-10-25T17:07:33+09:00"
source: "https://drew.silcock.dev/blog/is-this-the-new-cyber-normal/"
source_title: "Is this the new cyber normal?"
author: jungseob
source_author: "Drew Silcock"
source_published: "2026-10-23"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Drew Silcock이 2026년 10월 23일에 쓴 글을 정리한다. 한 주 사이에 PHP2Shell, eMudhra 인증서 키 유출, Railway 침해, GitLab 만점 취약점, musl, LiteLLM 악성 배포, PingCAP 유출, 리눅스 커널 취약점 오배포가 겹친 일을 훑고, 이것이 AI가 바꾼 새 정상인지 묻는다. 각 사고를 Mozilla, AWS, GitLab, LiteLLM, Railway, InfoQ 등의 공식 공지와 대조하고 필자의 평가와 갱신된 사실을 밝힌다."
image:
  path: "https://drew.silcock.dev/open-graph/blog/is-this-the-new-cyber-normal.png"
  alt: "Drew's Dev Blog 글 Is this the new cyber normal 대표 이미지"
tags:
  - knowledge
  - blog
  - 보안
  - AI
  - 오픈소스
---

## TL;DR

- Drew Silcock은 10월 17일 전후 한 주 동안 겹친 사고 아홉 건을 정리하고, 이것이 새로운 정상인지 아직 판단하지 못했다고 쓴다. 이 중 일부만 LLM으로 찾거나 만든 것이고 상당수는 사람이 찾은 고전적 취약점이라는 점을 짚는다.
- 가장 큰 사건 PHP2Shell은 PHP의 원격 코드 실행 취약점 두 건이다. 공개 전 유출과 연쇄 실수로 패치 몇 시간 전에 이미 공격이 시작되었고, 그는 LLM 때문에 소문에서 조직적 공격까지 걸리는 시간이 몇 주에서 몇 시간으로 줄었다고 본다.
- 대안은 세 가지다. NHS 방식의 비공개화는 저장소를 닫아도 과거 버전과 역공학이 남고, AI를 받아들여 더 좋은 모델을 먼저 돌리는 방식은 돈이 들며, 이상적인 표준 절차는 현실에 없다는 평가다. 그의 결론은 인터넷에 노출한 것은 뚫린다고 가정하고 계획하자는 것이다.
- 대조해 보면 사실 서술은 대체로 맞다. PHP2Shell은 AWS가 10월 17일 공격 시도를 포착했고, LiteLLM의 악성 1.107.0은 약 2시간 공개됐으며, PingCAP는 필자가 쓴 뒤 사용자 이름·이메일 등의 반출을 확인했다. 필자가 옮긴 "인터넷의 70%"는 Wiz 발표 제목의 표현으로 취약 비율로 확인되지 않았다.
- 이 노트는 필자의 글 전체와 사고별 공식 공지, 보안 매체 기사를 읽고 대조했다. 개별 취약점의 기술 분석은 하지 않았다.

## 글에 대하여

Drew Silcock이 2026년 10월 23일에 개인 블로그에 올린 글이다. 필자는 자신이 보안 전문가가 아니어서 사고마다 외부 설명을 링크한다고 밝히고 영국 정부 관련 일을 한다는 단서를 각주에 단다. 구성은 사고 아홉 건, "이것이 새 정상인가", "무엇을 할 수 있나", 결론이며 개발 중인 이야기라 업데이트를 하겠다고 한다. 이 블로그의 [Sean Goedecke 글 노트](https://raphael-shin.github.io/jungseob-blog/posts/goedecke-slow-software-bad-design-not-languages/)가 AI와 소프트웨어 설계를 다뤘다면 이 글은 AI가 보안의 시간 축을 바꾸는지를 묻는다.

## 아홉 건의 사고

첫째 PHP2Shell(CVE-2026-109618과 CVE-2026-109619)은 PHP의 RCE 두 건으로, 캘리포니아의 Calif(OpenAI의 Patch the Planet 프로그램)와 Wiz가 GPT-5.6 Sol, Gemini 4 Argon 같은 프런티어 모델로 취약점을 찾고 익스플로잇을 만들었다고 필자는 쓴다. 그중 하나는 PHP 재단이 2024년 보안 감사에서 이미 발견했으나 실제 익스플로잇이 어렵다고 보고 우선순위에서 밀어 두었다는 점이 눈에 띈다. 필자는 LLM이 이론적 취약점 설명을 완전한 익스플로잇으로 바꾸는 데 특히 능하며 보안 패치 공지가 나가는 순간 에이전트가 diff를 읽고 취약점을 거슬러 올라간다고 본다. 공지 시점이 완전한 익스플로잇이 공개·비공개로 돌지 않는 마지막 날짜라고 가정하는 것이 합리적이라는 말이다. 사고 경위는 Hacker News에 petecooper가 엠바고를 모른 채 글을 올리고 PHP 그룹이 목요일 22일의 패치를 수요일 21일로 앞당겼지만 패치는 그다음 날에야 쓸 수 있을 예정이었고 PHP 재단은 Calif가 익스플로잇 영상을 공개했고 Chainguard가 엠바고 6시간 전에 수정을 올렸다고 비난했다는 것이다. 17시간 안에 여러 실수가 겹쳤다.

둘째 eMudhra는 같은 10월 20일 Mozilla가 인도 인증기관 eMudhra의 중간 인증서 8개를 차단한 일이다. 가명의 연구자 Wayne이 여러 기술 기업에 중간 인증서의 개인 키가 "115", "56", "4" 같은 형편없는 수였다고 보고했다. 필자는 AI로 찾았다는 징후는 없으나 Scott Helme가 Claude에 프롬프트 한 번으로 키를 복원했다고 전한다. 셋째 Railway는 10월 21일 환경 변수를 저장하는 시스템에서 비정상 활동을 발견하고 AI 추론 사업자를 겨냥한 조직적 공격의 일부라고 믿는다고 밝혔다. 넷째 GitLab은 10월 12일 CI/CD의 정규식 파싱에서 임의 코드 실행이 가능한 CVSS 10.0을 경고했고 21일 또 하나의 정규식 정수 오버플로 RCE(10.0)가 나왔다. 앞선 달에도 10.0이 있었고 세 건 모두 HackerOne 버그 바운티로 접수되었다. 필자는 AI로 찾았다는 증거가 없다고 밝히고 CVSS 3.1과 4.0 점수를 직접 비교할 수 없다고 각주를 단다.

다섯째 musl libc는 10월 21일 정규식 컴파일의 정수 오버플로로 서비스 거부, 아마 코드 실행이 가능하다는 보고다. 여섯째 LiteLLM은 3월에 이어 다시 악성 버전이 PyPI와 Docker 이미지에 올라간 사건으로, .pth 파일과 sitecustomize.py로 파이썬 시작 시 악성 페이로드를 자동 실행했다. Wiz 분석은 페이로드에 LLM이 작성한 흔적(장황한 변수명, 과잉 방어적 오류 처리 등)이 있다고 하며 LiteLLM은 공격자가 GitHub CLI 자격 증명으로 CI를 돌렸다고 밝혔다. 일곱째 PingCAP(TiDB 개발사)는 10월 19일 무단 접근을 공개하고 TiDB에 저장된 데이터가 영향받았다는 증거가 없다고 했으나 갈취 조직 FulcrumSec은 10.6TB를 빼냈다며 200GB 토렌트를 풀었다. 여덟째는 Zero Day Initiative가 10월 21~22일 밤 미패치 리눅스 커널 취약점 보고(CVSS 9.0 이상)를 비공개 목록이 아니라 공개 목록에 올린 일이다.

## 새로운 정상인가

필자는 이번 주가 비정상적으로 활발했다고 인정하되 지금 결론을 내리지 못한다. 그가 보는 요점은 세 가지다. 첫째, 온라인 논의는 AI에만 쏠리지만 대부분은 사람이 찾은 전통적 취약점이다. 둘째, 범죄·국가 조직이 AI로 더 빠르게 해킹한다는 증거는 분명하다. 셋째, 누구나 오픈소스에 에이전트를 돌려 취약점을 찾고 익스플로잇을 쓸 수 있다는 우려가 NHS England가 오픈소스 코드를 비공개로 돌린 결정의 배경이다. 대응책 세 가지를 장단점으로 평가한다. 비공개화는 코드가 온라인에 없으니 커밋 분석을 막지만 프로그래밍 언어 같은 것은 닫을 수 없고 유출되면 수년간의 공개 검증을 놓쳤으며 바이트코드나 컴파일된 바이너리도 LLM이 역공학하고 한 번 공개된 옛 버전은 남는다. Shellshock이 1989년부터 2014년까지 Bash에 있었다는 예가 붙는다. AI 수용은 더 좋은 모델을 먼저 더 많은 돈으로 돌리는 것으로, 많은 버그를 찾지만 비싸고 고칠 사람이 필요하다. 낙관적 접근은 표준화된 보고·처리 절차와 모든 회사의 우수한 보안 태세인데 그런 세계에 살지 않는다. 쉬운 개선으로 패치가 준비되기 전에 중대 취약점 세부를 알리지 말자는 것이 있지만 이번에는 의도치 않은 유출이 겹쳤다. 최소 배포 연령 같은 공급망 방어는 대규모 악용 취약점의 수정을 며칠 늦춰 공격자에게 시간을 준다는 모순도 지적한다.

## 대조해서 확인한 점

PHP2Shell의 큰 줄기는 공식 자료와 맞는다. CVE 레코드는 PHP Group이 2026년 10월 21일 게시했고 CVE-2026-109618은 메모리 부족 처리 중 longjmp 때문에 생기는 OOM 손상이다. 보도에 따르면 CVE-2026-109619는 낡은 전역 상태(stale global state) 문제이고 패치는 PHP 8.5.12, 8.4.27, 8.3.36, 8.2.35에 들어갔다. AWS Threat Intelligence는 MadPot 센서에서 10월 17일 공격 시도를 포착했다고 밝혔다. 엠바고 해제 예정 시각은 10월 21일 14시 UTC이고 그날 02시 UTC에 최초 개념 증명이 나타났다는 서술이다. AWS는 공격자가 사전에 정보를 어떻게 얻었는지 불명이라 말하고 패치-익스플로잇 간격이 AI 지원 분석으로 줄었다는 분석을 덧붙인다. 필자의 "시간이 몇 주에서 몇 시간으로"는 AWS의 판단과 같은 방향이다. 필자의 "인터넷의 70%에 영향"은 Wiz 발표 제목의 표현을 옮긴 것으로 보이며 PHP를 쓰는 사이트의 비중이지 취약한 설치 비율이 아니다. 이 노트는 정확한 취약 범위를 확인하지 못했다. 필자도 CVSS가 10.0으로 유출됐지만 실제 점수는 9.2라고 쓴다.

eMudhra는 Mozilla 블로그가 10월 17일 20시 6분 UTC에 신고를 받았고 10월 20일 8개 중간 인증서를 차단했다고 밝혀 필자와 맞는다. LiteLLM은 공식 공지가 10월 21일 이른 아침 릴리스 파이프라인이 침해되어 악성 v1.107.0이 올라갔고 PyPI에 약 2시간(11:39~13:23 UTC), Docker 이미지에 약 2시간 반 노출되었다고 밝힌다. 공지는 이후 일부 가정이 부정확했다고 정정 표기를 남긴다. 필자의 서술과 대체로 같다. Railway는 공식 블로그가 10월 21일 환경 변수를 저장하는 시스템에서 이상 징후를 탐지하고 무단 제3자가 암호화된 환경 변수에 접근해 일부는 복호화했을 수 있다고 쓴다. GitLab은 공식 패치 노트가 10월 21일 19.5.1 등 긴급 패치를 냈다고 한다.

PingCAP는 갱신이 필요하다. 필자가 인용한 "TiDB에 저장된 데이터가 영향받았다는 증거는 없다"는 PingCAP의 보고서 문구이고 지금도 유지된다. 다만 InfoQ(10월 25일)는 PingCAP가 이후 소스 코드와 고객 관련 데이터의 반출을 확인했고 반출 기록에 사용자 이름, 이메일, 조직·프로젝트 연결, SQL 편집기 텍스트와 오류 등이 포함된다고 전했다. FulcrumSec의 10.6TB, 약 18만 테넌트 조직, 11만 개 넘는 API 키 쌍, 413개 비공개 저장소 같은 주장은 독립 검증되지 않았다. 필자가 "10.6TB는 TiDB 데이터가 영향받지 않았다면 많은 양"이라고 지적한 것이 이후 확인된 방향과 맞는다. 리눅스 커널 건은 Phoronix가 10월 22일 보도했다. ZDI의 보고서 다섯 건이 공개 목록에 올라왔고 그중 ksmbd 두 건이 CVSS 9.0, skb_zerocopy 한 건이 로컬 루트라는 서술이다. 필자의 NHS 언급은 BMJ가 5월 11일부터 소프트웨어를 기본 비공개로 돌리는 정책을 보도했다는 점과 맞고 같은 BMJ 보도는 Mythos 같은 AI 모델이 NHS 시스템 해킹에 쓰일 수 있다는 우려를 이유로 든다. 영국 정부 지침은 비공개 저장소가 보안의 착각을 줄 수 있다고 경고하며 필자의 "어리석은 결정" 평가와 같은 방향이다.

## 읽을 때 유의할 점

첫째, 글은 서둘러 쓰였고 필자도 갱신과 문장 개선을 예고한다. PingCAP처럼 발행 후 사실이 바뀐 곳이 있다. 둘째, AI가 얼마나 기여했는지에 대한 서술은 사고마다 증거 수준이 다르다. PHP2Shell은 발견자가 모델 사용을 밝혔고 LiteLLM은 분석 업체가 LLM 작성 흔적을 지적했지만 나머지는 증거가 없다. 셋째, 구체적 처방(비공개화, AI 수용, 표준화) 평가는 필자의 의견이다. 넷째, "인터넷에 노출하면 뚫린다는 기대치"라는 결론은 보안 팀의 현실적 태도지만 서비스 설계 지침으로는 모호하다. 다섯째, 몇 건은 이 노트가 필자의 요약을 공식 문서로 완전히 대조하지 못했다. eMudhra의 인증기관 사업 철수 발표와 LiteLLM의 3월 사고는 필자의 서술만 확인했다.

그래도 가져갈 질문은 분명하다. 우리 서비스에서 패치 공지부터 적용까지 걸리는 시간은 공격 코드가 돌 때까지의 시간보다 짧은가, 엠바고가 깨졌을 때 임시 완화책을 즉시 쓸 수 있는가, 의존성 업데이트를 며칠 늦추는 정책과 긴급 패치를 즉시 적용하는 정책을 어떻게 병행하는가, 환경 변수와 CI 토큰 같은 비밀은 공급망 사고에서 얼마나 빨리 회전할 수 있는가.

## 참고 자료

[Drew Silcock: Is this the new cyber normal? (2026-10-23)](https://drew.silcock.dev/blog/is-this-the-new-cyber-normal/): 본문과 각주 전체를 읽고 정리했다.

[AWS 보안 블로그: Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/): 10월 17일 시도, 엠바고 시각, 분석을 읽었다.

[CVE Record: CVE-2026-109618](https://www.cve.org/CVERecord?id=CVE-2026-109618): 게시일과 OOM 손상 설명을 검색 발췌로 확인했다.

[Mozilla: Protecting Firefox users following the compromise of eMudhra intermediate certificates (2026-10-20)](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates): 신고 시각과 8개 중간 인증서 차단을 검색 발췌로 확인했다.

[LiteLLM: Security incident Oct 21, 2026](https://docs.litellm.ai/blog/security-incident-oct-21-2026): 악성 버전 노출 시간대와 정정 표기를 읽었다.

[Railway: Security Disclosure: Wednesday October 21st](https://blog.railway.com/p/security-disclosure-wednesday-october-21st): 환경 변수 접근 서술을 검색 발췌로 확인했다.

[GitLab: Critical Patch Release 19.5.1 (2026-10-21)](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/): 긴급 패치 릴리스를 검색 발췌로 확인했다.

[InfoQ: PingCAP Breach Exposes Customer Records and Source Code (2026-10-25)](https://infoq.com/news/2026/10/pingcap-cloud-data-breach): PingCAP의 확인 범위와 FulcrumSec 주장을 읽었다.

[Phoronix: Several Linux Kernel Vulnerabilities Accidentally Posted To Public Kernel Mailing List (2026-10-22)](https://www.phoronix.com/news/LKML-New-Trend-Vulnerabilities): ZDI 보고서의 공개 목록 게시를 검색 발췌로 확인했다.

[BMJ: NHS England 오픈소스 비공개화 보도 (2026-05-12)](https://www.bmj.com/content/393/bmj.s928): 5월 11일 시행 정책과 AI 모델 우려를 검색 발췌로 확인했다.
