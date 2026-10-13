---
title: "[JSP] get방식과 post방식 차이점"
date: 2020-10-04 17:33:46
tags:
  - "TIL"
  - "ITWILL(JAVA)"
categories:
  - Backend
  - JSP
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'get방식과 post방식 차이점'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    동작 원리와 장단점을 비교 파악하여 프로젝트 개발 상황에 적합한 방식을 선택할 수 있다.</p>
</div>

<!-- more -->

## [get 방식 VS post 방식](https://sowon-dev.github.io/2020/06/16/200617jspi2/#%ED%8E%98%EC%9D%B4%EC%A7%80-%EC%9D%B4%EB%8F%99%EB%B0%A9%EC%8B%9D-%EB%91%90%EA%B0%80%EC%A7%80-get%EB%B0%A9%EC%8B%9D%EA%B3%BC-post%EB%B0%A9%EC%8B%9D)

  * get 

    * 전달되는 데이터를 주소줄(URL)에 적어서 전달
    * 파라미터의 길이 제한 : 256byte
    * 처리 속도가 빠름
    * 보안성이 나쁨
  * post

    * 전달되는 데이터를 본문(Body)에 담아서 전달=>주소줄X
    * 파라미터의 길이 제한 : 없음.
    * 처리 속도가 느림
    * 보안성이 좋음

#[TIL](/tags/TIL/)[ITWILL(JAVA)](/tags/ITWILL-JAVA/)
