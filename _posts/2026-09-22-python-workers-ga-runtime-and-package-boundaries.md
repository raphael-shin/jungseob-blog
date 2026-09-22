---
layout: post
title: "Python Workers 정식 출시, 웹 프레임워크와 패키지가 만나는 Wasm의 경계"
date: "2026-09-22"
created: "2026-09-22T23:18:54+09:00"
source: "https://blog.cloudflare.com/python-workers-ga/"
source_title: "Python Workers are now generally available"
author: jungseob
source_author: "Gyeongjae Choi, Dominik Picheta, Hood Chatham"
source_published: "2026-09-21"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "Python Workers GA의 바인딩·웹 프레임워크·TCP 소켓 지원을 설명하고, 네이티브 확장 패키지와 ORM의 호환성 조건을 공식 문서와 대조한다."
tags:
  - knowledge
  - blog
  - Python
  - Cloudflare
  - WebAssembly
image:
  path: "https://blog.cloudflare.com/_emdash/api/media/file/01M31JM2B4K28B7C67PCT5PB2R.01M31JM35NW9707QDHV86F68M9.png"
  alt: "Cloudflare Python Workers 정식 출시 대표 이미지"
---

## TL;DR

- Python Workers가 정식 지원 언어로 올라서며 Cloudflare 바인딩과 주요 웹 프레임워크의 연결을 간소화했다. Python과 JavaScript 사이의 자료형 변환은 런타임과 SDK가 맡는다. 기존 Python 개발 방식을 활용하되 실행 환경은 Pyodide 기반 WebAssembly다.
- ASGI·WSGI 연결 계층이 Workers 요청을 Python 웹 앱으로 전달한다. 앱 안에서 Uvicorn이나 Gunicorn 서버를 별도로 띄울 필요가 없다. FastAPI·Django·Flask 지원은 이런 표준 인터페이스의 연결을 바탕으로 한다.
- TCP 소켓 연결이 열리면서 Hyperdrive를 통한 PostgreSQL·MySQL 접근도 가능해졌다. 공식 문서는 호환성 날짜를 2026-09-08 이후로 요구한다. 저수준 소켓 기능과 패키지별 차이는 남아 있으며 비동기 SQLAlchemy ORM은 아직 지원하지 않는다.
- PEP 783은 Wasm용 바이너리 패키지를 배포할 공통 기반을 마련했다. 그러나 모든 기존 Python 패키지가 그대로 실행된다는 뜻은 아니다. 순수 Python 패키지와 지원되는 PyEmscripten·Pyodide 패키지를 구분하고 네이티브 확장의 빌드를 확인해야 한다.

## JavaScript 변환 코드를 걷어낸 Python 바인딩

Cloudflare는 Python Workers 도입 이후 2년간 진행한 작업을 정식 출시로 묶었다. Python 앱은 Workers AI와 R2, D1, Hyperdrive뿐 아니라 Durable Objects와 Queues, Workflows 같은 플랫폼 기능을 바인딩으로 연결한다. Dynamic Workers로 다른 Worker 안에서 Python Worker를 만드는 방식도 출시 글에 포함됐다. Python이 정식 지원 언어가 됐다는 선언과 함께 기존 서비스에 접근하는 코드의 번거로움을 줄인 변화다.

이전에는 Queue에 Python 딕셔너리를 보내려 해도 `pyodide.ffi.to_js`와 JavaScript 객체 변환기를 직접 써야 했다. 이제 런타임과 Python SDK가 RPC 경계의 자료형 변환을 처리해 Python 딕셔너리를 그대로 전달할 수 있다. 개발자가 JavaScript 객체를 의식하며 접착 코드를 작성할 필요가 줄어든다. 다만 내부 실행 기반까지 일반 서버의 Python으로 바뀐 것은 아니다. Pyodide로 Wasm에 컴파일한 Python 인터프리터가 Workers 런타임 안에서 동작한다.

## 서버 프로세스 대신 ASGI·WSGI를 연결한다

일반 서버에서 FastAPI 앱을 실행할 때는 Uvicorn 같은 웹 서버가 연결을 받아 앱으로 요청을 전달한다. Python Workers에서는 Workers 플랫폼이 웹 서버 역할을 맡는다. `workers.asgi`는 들어온 요청을 ASGI 규약에 맞게 변환하고 앱의 응답을 Workers 쪽으로 돌려준다. `asgi.entrypoint(app)` 같은 진입점 연결로 앱 코드를 실행하므로 Worker 안에 별도 웹 서버를 띄우지 않는다.

동기식 웹 앱에는 `workers.wsgi` 연결 계층을 사용한다. Django나 Flask를 포함해 ASGI 또는 WSGI 계약을 따르는 프레임워크가 이 방식의 대상이다. 네트워크 연결과 트래픽 분산은 플랫폼이 담당하고 프레임워크는 앱 로직에 집중한다. 프레임워크 진입점을 연결할 수 있다는 사실과 앱의 모든 확장 모듈이 호환된다는 보장은 구분해야 한다. 후자는 실제 의존 패키지와 런타임 기능을 따로 확인해야 하는 문제다.

## TCP 소켓으로 이어진 데이터베이스 연결

기존 Wasm 샌드박스에서는 Python 드라이버가 호출하는 POSIX 네트워크 시스템 호출이 실제 소켓 연결로 이어지지 않았다. Cloudflare는 이를 Workers의 `connect` API로 연결하는 소켓 구현을 추가했다. 연결을 열고 바이트를 읽는 Python 연산을 런타임의 네트워크 호출로 번역하므로 드라이버가 그 내부를 직접 알 필요는 없다. Hyperdrive 바인딩에서 받은 호스트와 포트, 사용자와 데이터베이스 정보를 익숙한 드라이버에 전달하는 방식이 가능해졌다.

공식 Hyperdrive 문서는 Python Workers의 호환성 날짜를 `2026-09-08` 이상으로 설정하도록 요구한다. 검증한 PostgreSQL 드라이버는 asyncpg·pg8000·psycopg이며 MySQL 쪽은 aiomysql·pymysql이다. 문서가 우선 권장하는 드라이버는 각각 asyncpg와 aiomysql이다. 이는 명시적으로 시험한 조합의 목록이며 모든 TCP 기반 드라이버가 동일하게 동작한다는 보장은 아니다.

동기식 Python 소켓 호출도 내부에서는 비동기로 처리돼 다른 요청이 실행될 수 있다는 점이 특히 중요하다. 동기식 데이터베이스 작업을 직렬로 처리해야 한다면 공식 문서의 예처럼 잠금을 사용해 동시 접근을 막아야 한다. 일부 저수준 소켓 연산은 기대대로 동작하지 않을 수 있다. SQLAlchemy ORM도 현재는 동기식만 지원하고 비동기식은 greenlet 지원 부재로 제외된다. GA 이후에도 앱의 동시성 가정과 의존성을 점검해야 하는 이유다.

## 패키지 생태계를 여는 표준과 남아 있는 빌드 조건

C·C++·Rust 확장을 포함한 패키지는 일반 운영체제용 바이너리를 그대로 가져올 수 없다. Wasm 대상으로 교차 컴파일해야 하며 인터프리터와 ABI가 맞아야 한다. 과거에는 Cloudflare 팀이 이런 패키지를 직접 빌드하고 호스팅하는 부담을 떠안았다. Cloudflare는 특정 서비스 전용 패키지 모음보다 Pyodide를 함께 쓰는 생태계의 배포 기반을 넓히려 한다.

승인된 PEP 783은 `pyemscripten` 플랫폼 태그를 정의해 바이너리 wheel의 호환성을 표현한다. Emscripten 버전만 같아서는 부족하고 ABI에 영향을 주는 컴파일·링크 조건까지 맞아야 하므로 공통 플랫폼 정의가 필요하다. `pyodide-build`와 cibuildwheel 지원은 패키지 유지보수자가 이 표준에 맞는 빌드를 제공하도록 돕는다. 표준이 생겼다는 사실만으로 아직 배포되지 않은 wheel이 자동으로 생기지는 않는다.

현재 Python Workers 패키지 문서는 순수 Python 패키지와 PyPI의 PyEmscripten 패키지, Pyodide에 포함된 패키지를 지원 범위로 안내한다. 의존성은 `pyproject.toml`에 선언하고 pywrangler가 배포할 Worker 번들에 함께 묶는다. 로컬 개발에는 `uv run pywrangler dev`, 배포에는 `uv run pywrangler deploy`를 사용한다. 이 명령은 공식 문서의 개발 흐름이며 여기서 앱을 실행하거나 실제 배포한 결과는 아니다.

## AI 추론을 연결하고 작업의 상태를 나눈다

AI SDK를 쓰려면 모델 호출을 담당하는 HTTP 클라이언트부터 동작해야 한다. Cloudflare는 requests와 httpx가 Wasm 환경에서 JavaScript `fetch` API로 요청을 보낼 수 있도록 상류 프로젝트에 기여했고 소켓 지원도 보완했다. 이를 바탕으로 openai·langchain·mcp 같은 라이브러리를 사용할 수 있다. Workers AI의 GPU 추론이나 AI Gateway를 연결하는 방식이며 Python Worker 자체가 GPU 런타임이 됐다는 설명은 아니다.

출시 글의 이미지 생성 예제는 요청을 Queue에 넣고 Workflows로 추론 과정을 조율한 뒤 결과를 R2에 저장한다. Bluesky Jetstream 예제는 WebSocket 연결과 장기 상태에 Durable Object를 결합한다. 공식 MCP 패키지를 이용한 서버와 Workers AI·Vectorize 기반 RAG도 예제로 제공한다. 이들은 플랫폼 기능을 조합하는 구현 패턴이며 출시 글이 별도의 성능 비교 수치로 검증한 결과는 아니다. Cloudflare는 성능과 메모리 효율, 지원 패키지 확대를 후속 과제로 남겼다.

## 참고 자료

[Cloudflare — Python Workers are now generally available](https://blog.cloudflare.com/python-workers-ga/)

[Python Workers 패키지 지원](https://developers.cloudflare.com/workers/languages/python/packages/)

[Hyperdrive와 Python Workers의 드라이버·호환성 제한](https://developers.cloudflare.com/hyperdrive/examples/python-workers/)

[PEP 783 — Emscripten Packaging](https://peps.python.org/pep-0783/)
