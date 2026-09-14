---
layout: post
title: "S3의 URL 뒤에서는 무슨 일이 일어날까 — 객체 키·부분 읽기·데이터 복구"
date: "2026-09-15"
created: "2026-09-15T08:35:39+09:00"
source: "https://www.youtube.com/watch?v=sRrnRVkmTsQ"
source_title: "S3 doesn't work the way you think"
author: jungseob
source_author: "PlanetScale"
source_published: "2026-09-14"
type: blog-knowledge-note
published: true
render_with_liquid: false
categories: [지식 노트]
description: "PostgreSQL에 저장한 영상을 S3로 옮기는 데모에서 출발해 객체 키와 Range 요청, 분산 저장과 삭제 코딩을 설명한다. 버킷의 평면 구조, 가용 영역, 내구성에 관한 단순화는 공식 문서로 보완한다."
tags:
  - knowledge
  - blog
  - amazon-s3
  - object-storage
  - distributed-storage
  - postgresql
  - youtube
image:
  path: "https://i.ytimg.com/vi/sRrnRVkmTsQ/maxresdefault.jpg"
  alt: "PlanetScale의 Amazon S3 내부 구조 설명 영상"
---

## TL;DR

- 영상 바이트를 S3에서 직접 읽으면 데이터베이스와 애플리케이션 서버가 맡던 전송 처리를 줄일 수 있다. 브라우저의 부분 읽기는 HTTP Range 요청으로 처리한다. 다만 객체 URL을 안다고 접근 권한까지 생기는 것은 아니다.
- S3 범용 버킷의 `videos/video1.mp4`는 폴더 안 파일을 가리키는 경로처럼 보이지만 전체가 하나의 객체 키다. 슬래시도 키에 포함된다. 평면 구조는 버킷 안의 논리적 이름 공간을 뜻하며 S3 전체가 하나의 전역 키 공간이라는 의미는 아니다.
- 저장 계층은 데이터를 여러 장치에 분산하고 복구용 중복 정보를 활용한다. 삭제 코딩은 일부 조각이 사라져도 남은 조각으로 데이터를 읽을 수 있게 한다. 서비스는 오류를 감지하고 줄어든 중복성을 복구하는 작업도 계속 수행한다.
- S3 Standard의 11 nines는 데이터 내구성 설계 목표다. 요청이 항상 성공한다는 가용성 수치와는 다르다. 다중 AZ 저장도 모든 클래스에 똑같이 적용되지 않으며 버전 관리 같은 사용자 실수 대비책은 별도로 필요하다.

## 데이터베이스가 하던 영상 전송을 S3로 옮긴다

PlanetScale의 데모는 약 4GB의 영상을 PostgreSQL large object로 저장한 플레이어에서 시작한다. 브라우저가 영상의 특정 부분을 요청하면 Express 서버가 해당 바이트를 데이터베이스에서 읽어 반환한다. 영상 태그 하나를 재생하기 위해 서버가 요청 범위와 읽기 길이를 계산하고 데이터를 중계하는 구조다. 파일을 S3에 업로드한 뒤 영상 태그의 `src`를 객체 URL로 바꾸자 이 데모에서는 해당 Node 서버 없이도 재생과 탐색이 동작한다.[1]

여기서 약 200만 개라는 수치는 독립된 영상이나 large object의 개수로 읽으면 안 된다. 화면에는 특정 `loid`에 속한 `pg_largeobject` 행을 세는 쿼리가 나오며 PostgreSQL 문서에서도 한 large object를 작은 페이지들로 나눠 각 행에 저장한다고 설명한다. 페이지 크기는 일반적으로 2kB이고 각 행은 객체 식별자와 페이지 번호로 구분된다. 즉 데모는 한 영상에 속한 많은 페이지를 다루는 사례이며 이 행 수만으로 PostgreSQL이 대용량 데이터를 저장할 수 없다고 결론 내릴 수는 없다.[1][7]

달라진 것은 바이트를 전달하는 주체다. 데이터베이스에서 바이트를 꺼내 HTTP 응답으로 만드는 일을 애플리케이션이 직접 맡는 대신 객체 저장 서비스의 읽기 기능을 이용한다. 원본 영상은 파일 전체를 저장하는 용도와 관계형 데이터 조회의 역할을 나누는 예를 보여준다. 다만 동시 접속자 수나 처리량을 비교한 성능 실험은 제시하지 않으므로, 특정 구현의 복잡성이 줄었다는 관찰과 모든 데이터베이스 저장 방식에 대한 성능 판정은 구분해야 한다.[1]

## URL의 경로처럼 보이는 부분도 하나의 객체 키다

영상에서 다루는 일반적인 S3 주소에는 버킷 이름과 리전, 객체 키가 드러난다. 예를 들어 `bucket-name.s3.us-east-1.amazonaws.com/videos/video1.mp4`라는 형태에서 `videos/video1.mp4` 전체가 키다. `us-east-1`은 미국 버지니아 북부 리전을 가리키며 특정 디스크나 단일 건물의 주소를 뜻하지 않는다. 개발자는 이 논리적 식별자로 데이터를 요청하고 실제 저장 위치의 관리는 서비스에 맡긴다.[1]

S3 범용 버킷은 파일시스템처럼 하위 폴더를 따라 내려가는 구조가 아니다. 콘솔이 `videos/`를 폴더처럼 보여주는 것은 공통 접두사와 구분자를 이용해 객체를 묶기 때문이다. 슬래시는 키 문자열의 일부이며 AWS 문서도 객체 키가 버킷 안에서 객체를 식별한다고 명시한다. 따라서 서로 다른 버킷에 같은 키를 둘 수 있고 S3 전체의 모든 객체가 버킷 구분 없이 하나의 이름 공간에 들어간다고 이해하면 안 된다.[2]

## 권한 검사와 부분 읽기는 서로 다른 문제다

영상은 요청이 DNS를 거쳐 프런트엔드에 도착하고 권한 검사와 인덱스 조회를 통해 저장 계층으로 연결되는 흐름을 그린다. S3 엔지니어 Andy Warfield의 공개 설명도 REST API를 받는 프런트엔드, 이름 공간 서비스, 저장 장치 집합, 백그라운드 작업 계층을 구분한다. 이 구조에서 사용자가 지정한 객체 이름을 실제 데이터 접근으로 연결하는 역할과 요청을 허용할지 결정하는 역할이 함께 필요하다. 다만 이 도식은 주요 역할을 이해하기 위한 설명이다. 전체 내부 구현의 명세를 그대로 펼쳐 놓은 것은 아니다.[1][6]

브라우저에서 URL을 복사해 재생하는 장면에는 접근 권한이라는 전제가 있다. S3 객체는 기본적으로 비공개이므로 객체 주소만 알아서는 내용을 읽을 수 없다. 공개 읽기를 명시적으로 허용했거나 권한을 가진 주체가 발급한 사전 서명 URL처럼 읽기를 허용하는 방식이 필요하다. 사전 서명 URL은 정해진 시간 동안 객체를 읽을 권한을 전달하므로, 데모에서 서버를 없앴다는 말이 사용자 인증이나 접근 정책까지 불필요해졌다는 뜻은 아니다.[4]

영상의 재생 위치를 옮길 때는 브라우저가 필요한 바이트 범위를 요청할 수 있다. S3의 `GetObject`는 HTTP `Range` 헤더를 지원하며 공식 예제에서도 요청한 범위를 `206 Partial Content`로 반환한다. S3는 클라이언트의 HTTP 요청을 처리한다. HTML 영상 태그의 내부 상태를 직접 읽지는 않는다. 이 논리적인 바이트 범위와 저장 장치에 배치된 내부 데이터 조각은 서로 다른 층위이므로, 화면에서 이동한 구간이 특정 디스크 조각 하나에 곧바로 대응한다고 가정할 필요는 없다.[3]

## 복구용 조각과 분산 배치로 장치 고장에 대비한다

영상은 파일을 여러 데이터 조각으로 나누고 패리티 조각을 더해 서로 다른 장소에 저장하는 그림을 사용한다. 이 방식의 핵심은 고장 나지 않는 장치 하나를 찾는 대신 일부 장치가 고장 나도 원본을 복구할 정보를 남기는 데 있다. Warfield는 S3에서 복제뿐 아니라 삭제 코딩(erasure coding)도 사용한다고 설명한다. 데이터를 나눈 조각과 추가 패리티 조각 중 필요한 수가 남아 있으면 객체를 읽을 수 있으므로, 전체 사본을 여러 개 보관하는 방식보다 저장 공간의 중복 비용을 줄일 수 있다.[1][6]

영상에 그려진 조각의 개수나 배치도를 모든 S3 객체의 고정된 저장 규칙으로 읽어서는 안 된다. 공개된 엔지니어링 설명은 객체마다 서로 다른 디스크 집합에 배치해 한 디스크에 요청이 몰리지 않도록 한다는 점도 강조한다. 중복성은 장애 복구에 필요한 정보를 남기는 동시에 바쁜 장치를 피해 읽을 선택지를 만들 수 있다. 저장 용량과 내구성뿐 아니라 I/O 부하를 여러 장치에 나누는 문제까지 연결되는 구조다.[6]

## 다중 AZ와 11 nines에는 적용 범위가 있다

S3 Standard를 비롯한 여러 저장 클래스는 한 리전의 최소 세 가용 영역(AZ)에 걸쳐 여러 장치에 객체를 중복 저장한다. AZ는 반드시 건물 하나가 아니라 전력·네트워크·연결성을 갖춘 하나 이상의 데이터센터로 구성될 수 있다. 따라서 영상의 세 건물 그림은 장애 범위를 분리한다는 개념을 보여주는 표현으로 이해하는 편이 정확하다. 반면 S3 One Zone-IA는 한 AZ 안의 여러 장치에 저장하므로 다중 AZ 보호를 모든 저장 클래스의 공통 속성으로 넓혀서는 안 된다.[5]

내구성은 데이터가 보존되는 성질이고 가용성은 필요할 때 접근할 수 있는 성질이다. AWS 문서의 S3 Standard 설계 목표는 연간 99.999999999%의 내구성과 99.99%의 가용성으로 구분된다. 높은 내구성은 체크섬을 통한 무결성 검사와 장애 감지, 손상된 중복성의 빠른 복구를 포함한 운영에 의존한다. 패리티 계산 한 번으로 끝나는 일이 아니다. 삭제나 덮어쓰기 같은 사용자·애플리케이션 실수에 대비하려면 버전 관리 등 별도의 데이터 보호 기능도 함께 고려해야 한다.[5]

영상 도입의 규모 수치는 AWS가 2026년 3월 공개한 500조 개 이상의 객체와 전 세계 초당 2억 건 이상의 요청이라는 설명에서도 확인된다. 이는 서비스 전체의 집계이며 개별 버킷의 보장 처리량이나 하나의 전역 키 공간 크기를 뜻하지 않는다.[8] 사용자는 객체 하나를 저장하고 URL로 읽지만 그 뒤에서는 이름 해석, 접근 제어, 분산 배치, 중복 정보와 복구 작업이 함께 움직인다. 단순한 읽기·쓰기 인터페이스가 물리적인 저장 장치와 장애 대응의 복잡성을 숨겨주는 것이 이 영상이 보여주는 S3의 핵심이다.[1][6]

## 참고 자료

[1] <https://www.youtube.com/watch?v=sRrnRVkmTsQ> — S3 doesn't work the way you think — PlanetScale

[2] <https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html> — Naming Amazon S3 objects — AWS

[3] <https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html> — GetObject — Amazon S3 API

[4] <https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html> — Sharing objects with presigned URLs — AWS

[5] <https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html> — Data protection in Amazon S3 — AWS

[6] <https://www.allthingsdistributed.com/2023/07/building-and-operating-a-pretty-big-storage-system.html> — Building and operating a pretty big storage system called S3 — Andy Warfield

[7] <https://www.postgresql.org/docs/current/catalog-pg-largeobject.html> — pg_largeobject — PostgreSQL Documentation

[8] <https://aws.amazon.com/blogs/aws/twenty-years-of-amazon-s3-and-building-whats-next> — Twenty years of Amazon S3 and building what’s next — AWS News Blog

영상의 영어 자동자막을 통독하고 PostgreSQL 조회 화면은 프레임 OCR로 확인했다. 내부 구조의 설명은 공개된 S3 엔지니어링 글과 AWS·PostgreSQL 문서를 대조해 보완했으며, 비공개 구현의 세부 배치를 확인한 것은 아니다.
