---
layout: post
title: "Go HTTP/1 연결 재사용: 남은 응답 본문 처리하기"
date: "2026-10-15 22:59:29 +0900"
created: "2026-10-15T22:59:29+09:00"
source: "https://go.dev/blog/http-connection-reuse"
source_title: "Better HTTP/1 connection reuse"
author: jungseob
source_author: "Nicholas Husin and Damien Neil"
source_published: "2026-10-14"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "응답 본문을 닫을 때의 자동 처리와 연결 재사용의 한계."
tags: [knowledge, blog, web]
image:
  path: "https://go.dev/doc/gopher/gopher5logo.jpg"
  alt: "Go Gopher 로고"
---

## TL;DR

- HTTP/1은 읽지 않은 본문 때문에 연결을 버릴 수 있다.
- Go 1.27은 시간·용량 한도 안에서 남은 본문을 처리한다.
- 응답 본문을 닫는 책임은 여전히 호출자에게 있다.

## 본문이 남으면 연결도 재사용하지 못한다

HTTP/1은 같은 연결에서 응답을 순서대로 전달한다. 현재 본문을 끝까지 읽어야 다음 응답의 시작점을 찾을 수 있다. Go 1.26까지는 본문을 남긴 채 닫으면 연결을 버렸다. 상태코드만 확인하는 코드도 매번 연결을 새로 만들면서 TCP·TLS 연결 비용을 반복해서 부담할 수 있었다.

JSON 디코딩을 마쳤어도 본문을 모두 읽었다고 단정할 수 없다. 객체 뒤의 줄바꿈이 남으면 연결 재사용을 막을 수 있다. 남은 데이터를 읽어 버리는 처리는 이 문제를 해결하지만 공짜는 아니다. 큰 응답이나 느린 서버에서는 버릴 데이터를 기다리는 비용이 새 연결보다 커질 수 있다.

## 자동 처리에도 한도가 있다

Go 공식 블로그에 따르면 1.27의 Transport는 남은 HTTP/1 본문을 백그라운드에서 읽어 버린다. 한도는 50ms 또는 256KB이며, Connection: close가 있으면 생략한다. 처리가 다음 요청보다 늦으면 새 연결이 필요할 수 있다. 따라서 이 개선은 모든 요청의 연결 재사용을 보장하지 않는다.

HTTP/2는 스트림을 다중화하므로 같은 이유로 본문을 비울 필요가 없다. 공식 API 문서에서도 응답 본문을 닫는 책임은 호출자에게 남아 있다. Client와 Transport는 동시 사용이 가능하며 효율을 위해 재사용하도록 권장한다. 연결 재사용 개선을 본문 닫기나 클라이언트 수명 관리의 생략으로 해석해서는 안 된다.

## 참고 자료

[Better HTTP/1 connection reuse](https://go.dev/blog/http-connection-reuse)

[net/http API 문서](https://pkg.go.dev/net/http) — 본문 닫기와 Client·Transport 재사용 계약을 대조했다.
