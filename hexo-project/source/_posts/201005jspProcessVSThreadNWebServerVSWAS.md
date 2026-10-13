---
title: "[OS] 프로세스(Process)와 스레드(Thread)의 차이 VS 웹서버(WEB SERVER) VS 웹어플리케이션서버(WAS, Web Application Server)"
date: 2020-10-04 17:20:56
tags:
  - "TIL"
  - "ITWILL(JAVA)"
categories:
  - Backend
  - Operating Systeming
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'프로세스(Process)와 스레드(Thread)의 차이 VS 웹서버(WEB SERVER) VS 웹어플리케이션서버(WAS, Web Application Server)'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    동작 원리와 장단점을 비교 파악하여 프로젝트 개발 상황에 적합한 방식을 선택할 수 있다.</p>
</div>

<!-- more -->

# [프로세스 VS 스레드](https://sowon-dev.github.io/2020/08/20/200820javai/#%EA%B0%9C%EB%85%90-%EC%9A%A9%EC%96%B4%EC%A0%95%EB%A6%AC)

  * 프로세스 : 주기억장치에 로드된 상태의 프로그램(실행되고 있는 프로그램)

    * 작업관리자의 백그라운드프로세스가 많을수록 컴터속도가 느려짐

    * 설치된 애플리케이션을 실행하게되면 운영체제(OS)로부더 메모리의 일정영역을 할당받고 CPU와 HDD를 이용해서 동작하는 것

  * 스레드(Thread) : 프로세스 동작의 최소 단위. 모든 프로세스는 하나 이상의 스레드로 구성

![https://maenco.tistory.com/](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbH58bs%2FbtrcADeeJMy%2FtEoRMXFppH6AkZ4lqyXjO1%2Fimg.png)

  
  
  

# 웹서버(WEB SERVER) VS 웹어플리케이션서버(WAS, Web Application Server)

  * 웹서버 : DB사용 불가능
    * 클라이언트측 정적데이터
    * 웹 브라우저 클라이언트로부터 HTTP 요청을 받아 정적인 컨텐츠(.html .jpeg .css 등)를 제공하는 컴퓨터 프로그램
    * Web Server의 예 : Apache Server, Nginx, IIS(Windows 전용 Web 서버) 등
  * WAS : DB사용 가능
    * 서버측 동적데이터 사용
    * DB 조회나 다양한 로직 처리를 요구하는 동적인 컨텐츠를 제공하기 위해 만들어진 Application Server
    * WAS의 예 : Ex) Tomcat, JBoss, Jeus, Web Sphere 등
  * 참고 : <https://gmlwjd9405.github.io/2018/10/27/webserver-vs-was.html>

#[TIL](/tags/TIL/)[ITWILL(JAVA)](/tags/ITWILL-JAVA/)
