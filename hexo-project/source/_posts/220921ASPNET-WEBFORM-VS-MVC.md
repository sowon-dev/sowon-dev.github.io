---
title: "[ASP.NET] 웹폼(WebForm) VS MVC"
date: 2022-09-20 19:49:51
tags:
  - "C#"
  - "차이"
categories:
  - Backend
  - .NET
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'웹폼(WebForm) VS MVC'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    그래서 웹폼과 MVC이 어떤 차이가 있는지 비교해봤다.</p>
</div>

<!-- more -->

이번 프로젝트에서는 웹폼(WebForm)기반으로 개발하게 되었다. MVC 패턴에만 익숙한 내게 웹폼(WebForm)은 생소했다.  
그래서 웹폼과 MVC이 어떤 차이가 있는지 비교해봤다.

# WebFrom VS MVC

![https://pediaa.com/what-is-the-difference-between-webform-and-mvc/](https://pediaa.com/wp-content/uploads/2018/10/Difference-Between-Webform-and-MVC-Comparison-Summary-743x1024.jpg)

가장 큰 차이점은 웹폼(WebForm)은 전통적인 이벤트 중심 개발모델이고 MVC는 Model, View, Controller 기반의 개발모델이다.

  * 웹폼 프로세스(로그인예시)
    1. 사용자가 로그인폼에 로그인정보 입력 후 로그인버튼 클릭
    2. form데이터들이 POST방식으로 서버에 전송
    3. ASP.NET 실행 엔진을 통해 파싱(데이터 구문 분석과정) -> 클라이언트에서 로그인버튼이 클릭되었음을 확인
    4. 로그인버튼에 연결된 이벤트 핸들러 메서드를 찾아 호출
    5. 실행결과를 HTML코드로 클라이언트에게 전달
    6. 로그인 완료 또는 실패.
  * 웹폼 장점
    * 데이터 Control이 내장되어 있어 강력한 데이터 엑세스로 신속한 개발 가능.
    * 단일 파일 페이지 모델: 코드와 태그를 한 파일에서 확인할 수 있으며 파일일간의 종속성이 없다.
  * 웹폼 단점
    * 개발자 설계 능력에 따라 웹폼 프로젝트 유지보수 강도가 정해진다. 
    * 이벤트 중심으로 전체 흐름을 파악하기 어렵다.
    * 테스트 자동화가 어렵다. 
    * SEO에 친화적이지 않다.

  
  
  

# 참고

  * [What is the Difference Between Webform and MVC](https://pediaa.com/what-is-the-difference-between-webform-and-mvc/)
  * [Difference Between ASP.NET MVC and Web form](https://askanydifference.com/difference-between-asp-net-mvc-and-web-form-with-table/)
  * [ASP.NET WebForm, MVC](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=islove8587&logNo=220489016761)
  * [asp.net 웹폼에 대하여..](https://only1004.tistory.com/6)

#[C#](/tags/C/)[차이](/tags/%EC%B0%A8%EC%9D%B4/)
