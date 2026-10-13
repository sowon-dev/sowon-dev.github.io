---
title: "[REST API]페이지 전달방식"
date: 2020-11-11 20:07:32
tags:
  - "ITWILL(JAVA)"
  - "RESTfulAPI"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">페이지 전달방식의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * URI가 원하는 리소스를 의미한다. (영어 복수형으로 주소를 사용)을 적용할 수 있다.</p>
</div>

<!-- more -->

## Rest 방식의 사용원칙

  * URI가 원하는 리소스를 의미한다. (영어 복수형으로 주소를 사용)
  * URI에는 식별할 수 있는 데이터를 전달하는것이 일반적인 방법
  * 예를들어 게시판 - CRUD 이라면 사용가능한 주소형태는 아래와 같다.
    * …/boards/123 => 123번 글을 조회 
    * …/boards/123/replies/11 => 123번글의 11번째 댓글 조회
    * …/boards/123/11 => 123번글의 11번째 댓글 조회
    * …/boards/ => 신규 글용 작성

  
  
  

## 페이지 전달방식

  * [`/작업명/기본키 + 메서드 + 데이터`] 형태로 REST방식으로 페이지 전달하면 된다.

예시 | 방식 | 용도  
---|---|---  
…/boards/123 | GET | 자료 조회용  
…/boards/123 | DELETE | 자료 삭제용  
…/boards/, …/boards/new/ | POST | 신규 자료 작성용  
…/boards/123 | PUT | 자료 전체 수정용  
…/boards/123 | PATCH | 자료 일부 수정용  
  
![https://www.seobility.net/en/wiki/REST_API](https://www.seobility.net/en/wiki/images/f/f1/Rest-API.png)

  * 크롬 웹 도구인 [ARC cookie exchange](https://chrome.google.com/webstore/detail/arc-cookie-exchange/apcedakaoficjlofohhcmkkljehnmebp?utm_source=chrome-ntp-icon)를 사용하면 편하게 방식을 구분할 수 있다.

#[ITWILL(JAVA)](/tags/ITWILL-JAVA/)[RESTfulAPI](/tags/RESTfulAPI/)
