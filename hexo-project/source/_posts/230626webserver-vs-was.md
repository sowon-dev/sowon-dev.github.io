---
title: "아파치와 톰캣 분리한다고요?(ft. Web Service Architecture 차이)"
date: 2023-06-25 19:47:55
tags:
  - "오늘또못알아듣고말았습니다"
  - "차이"
categories:
  - Backend
  - Server
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'아파치와 톰캣 분리한다고요?(ft. Web Service Architecture 차이)'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    기본적인 차이점이다.</p>
</div>

<!-- more -->

오늘 커피챗에서 이번 프로젝트 서버 설계에 대한 이야기가 나왔다. 아파치와 톰캣을 분리한다고 하셨다. 

가볍게 스쳐 지나간 주제지만 [아파치 vs 톰캣 포스팅](https://sowon-dev.github.io/2022/09/05/220906Tomcat-vs-Apatch/)이 떠오르면서 분리하면 어떻게 서버가 도는 건지 궁금해졌다.

# Web Service Architecture 종류

  * Client -> WAS -> DB
  * Client -> Web Server -> DB
  * Client -> Web Server -> WAS -> DB

가장 많이 사용하는건 1번 WAS이다. 왜냐하면 WAS가 Web Server의 기능을 대부분 수행할 수 있기때문이다.  
그럼에도 불구하고 이번 프로젝트에서 3번을 사용한다고 한다.

  
  
  

# 왜 Web Server와 WAS를 분리하는 걸까?

  1. 보안강화: WAS는 DB와 바로 연결되기때문에 WEB SERVER와 WAS를 분리하여 WEB SERVER를 외부서버에 두고 WAS와 DB서버를 내부 서버에 두면 보안을 강화할 수 있다.
  2. 서버부하방지: WAS는 DB조회나 서비스로직을 처리하느라 항상 바쁘기에 단순한 정적페이지는 WEB SERVER를 이용하면 빠르게 사용자에게 보여주고 WAS 부하를 방지할 수 있다.
  3. 로드밸런싱을 위한 여러 대 WAS 연결 가능
  4. 여러 웹 어플리케이션 서비스 가능: 예를들어 PHP APPLICATION과 JAVA APPLICATION 함께 사용 가능하다.

이번 프로젝트는 사이트가 많은 편인데 정적 페이지도 많으므로 서버 부하가 예상되기에 WEB SERVER를 WAS앞에 두고 DB나 서비스로직이 필요할때마다 WAS를 호출하는 형태로 사용하기 위해 분리한다고 하셨다.  
아하~ 유레카😎

  
  
  

# [웹서버(WEB SERVER) VS 웹어플리케이션서버(WAS, Web Application Server)](https://sowon-dev.github.io/2020/10/04/201005jspProcessVSThreadNWebServerVSWAS/#%EC%9B%B9%EC%84%9C%EB%B2%84-WEB-SERVER-VS-%EC%9B%B9%EC%96%B4%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98%EC%84%9C%EB%B2%84-WAS-Web-Application-Server)

기본적인 차이점이다.

  * 웹서버 : DB사용 불가능
    * 클라이언트측 정적데이터
    * 웹 브라우저 클라이언트로부터 HTTP 요청을 받아 정적인 컨텐츠(.html .jpeg .css 등)를 제공하는 컴퓨터 프로그램
    * Web Server의 예 : Apache Server, Nginx, IIS(Windows 전용 Web 서버) 등
  * WAS : DB사용 가능
    * 서버측 동적데이터 사용
    * DB 조회나 다양한 로직 처리를 요구하는 동적인 컨텐츠를 제공하기 위해 만들어진 Application Server
    * WAS의 예 : Ex) Tomcat, JBoss, Jeus, Web Sphere 등

  
  
  

# 참고

  * 송과장님 지식
  * [웹서버(WEB SERVER) VS 웹어플리케이션서버(WAS, Web Application Server)](https://sowon-dev.github.io/2020/10/04/201005jspProcessVSThreadNWebServerVSWAS/#%EC%9B%B9%EC%84%9C%EB%B2%84-WEB-SERVER-VS-%EC%9B%B9%EC%96%B4%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98%EC%84%9C%EB%B2%84-WAS-Web-Application-Server)
  * [아파치 vs 톰캣 같은 거 아냐? 차이점](https://sowon-dev.github.io/2022/09/05/220906Tomcat-vs-Apatch/)
  * [HeeJeong Kwon - Web Server와 WAS의 차이와 웹 서비스 구조](https://gmlwjd9405.github.io/2018/10/27/webserver-vs-was.html)

#[오늘또못알아듣고말았습니다](/tags/%EC%98%A4%EB%8A%98%EB%98%90%EB%AA%BB%EC%95%8C%EC%95%84%EB%93%A3%EA%B3%A0%EB%A7%90%EC%95%98%EC%8A%B5%EB%8B%88%EB%8B%A4/)[차이](/tags/%EC%B0%A8%EC%9D%B4/)
