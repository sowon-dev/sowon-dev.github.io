---
title: "[톰캣서버]Tomcat 내부 구조와 설정파일"
date: 2022-03-07 02:55:29
tags:
  - "Tomcat"
categories:
  - Backend
  - Server
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Tomcat 내부 구조와 설정파일의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * 톰캣설치경로/conf/server.xml : 톰캣 서버 설정 파일을 적용할 수 있다.</p>
</div>

<!-- more -->

클라이언트가 요청을 보내면 톰캣 내부에서는 어떤 일이 일어날까?

## 톰캣 서버 내부 구조

![https://flylib.com/books/4/15/1/html/2/id_9807/fig21_01.jpg](https://flylib.com/books/4/15/1/html/2/id_9807/fig21_01.jpg)

Tomcat Server안에 Service가 있고 그 서비스를 처리하는 것이 Engine(Catalina)이다.  
Engine안에는 Host가 여러 개가 있을 수 있다.  
Host안에는 여러 개의 Context가 있을 수 있다.  
여기사 Context란 쉽게 말해 스프링프로젝트라고 생각하면 된다.  
Context안에 있는 Servlet이 여러개 있는데 각 Servlet은 쉽게 Controller로 생각할 수 있다.

![https://gmlwjd9405.github.io/2018/10/27/webserver-vs-was.html](https://gmlwjd9405.github.io/images/web/web-service-architecture.png)

클라이언트가 먼저 url을 요청하면 Thread Pool로 간다. Thread Pool은 요청을 받은 후에 만들면 늦으니까 요청을 받기 전 미리 만들어 놓는다.  
그 중 요청을 처리하고 있지 않은 Thread 하나가 요청을 받게된다.  
요청 프로토콜에 따라 Connector가 동일한 프로토콜을 연결해주며 보통 HTTP1.1 프로토콜이다.  
프로토콜이 프로세스를 처리해서 Engline(Catalina)을 거치고 요청 받은 Host안의 Context까지 찾은 다음 해당 Servlet을 호출한다.  
Dispatcher Servlet이 요청받은 Controller의 method를 찾아 호출한다.

  
  
  

## 설정파일

  * 톰캣설치경로/conf/server.xml : 톰캣 서버 설정 파일
  * 톰캣설치경로/conf/web.xml : 톰캣의 모든 프로젝트의 공통설정 파일
  * 프로젝트이름/WEB-INF/web.xml : 프로젝트(Context)의 개별 설정

공통설정파일이 먼저 적용된 후 프로젝트 개별 설정파일이 적용된다.

  
  
  

## 참고

  * <https://tomcat.apache.org/tomcat-9.0-doc/architecture/overview.html>
  * <https://gmlwjd9405.github.io/2018/10/27/webserver-vs-was.html>
  * [웹서버(WEB SERVER) VS 웹어플리케이션서버(WAS, Web Application Server)](https://sowon-dev.github.io/2020/10/04/201005jspProcessVSThreadNWebServerVSWAS/#%EC%9B%B9%EC%84%9C%EB%B2%84-WEB-SERVER-VS-%EC%9B%B9%EC%96%B4%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98%EC%84%9C%EB%B2%84-WAS-Web-Application-Server)
  * [Servlet : Servlet용어정리](https://sowon-dev.github.io/2020/08/16/200817jspi/#Servlet%EA%B8%B0%EC%B4%88)

#[Tomcat](/tags/Tomcat/)
