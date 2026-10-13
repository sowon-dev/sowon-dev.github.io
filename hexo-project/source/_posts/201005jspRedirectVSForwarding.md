---
title: "[JSP] Redirect방식과 Forwarding방식 차이점"
date: 2020-10-04 18:12:45
tags:
  - "TIL"
  - "ITWILL(JAVA)"
categories:
  - Backend
  - JSP
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'Redirect방식과 Forwarding방식 차이점'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    동작 원리와 장단점을 비교 파악하여 프로젝트 개발 상황에 적합한 방식을 선택할 수 있다.</p>
</div>

<!-- more -->

## [Redirect VS Forwarding](https://sowon-dev.github.io/2020/08/31/200831jspi2/#src%ED%8F%B4%EB%8D%94%EC%95%84%EB%9E%98%EC%97%90-%EC%83%88%EB%A1%9C%EC%9A%B4-%ED%8C%A8%ED%82%A4%EC%A7%80%EC%99%80-BoardFrontController-java%EC%83%9D%EC%84%B1)

  * sendRedirect방식
    * 페이지 이동 O 주소 변경 O (가상주소끼리의 이동)
    * session,application 영역의 데이터 전달 가능
    * 사용처: 주소와 화면의 전환이 동시에 일어날때 (가상주소 .bo -> 가상주소로 .bo)
  * Forwarding방식
    * 페이지 이동 O 주소 변경 X (jsp 뷰 페이지로 이동) 
    * request,response,session,application 영역의 데이터 전달가능
    * 사용처: 주소는 그대로인데 화면이 바뀔때 (가상주소 .bo에서 request객체정보를 가지고 이동하면서 .jsp를 보여줌)

#[TIL](/tags/TIL/)[ITWILL(JAVA)](/tags/ITWILL-JAVA/)
