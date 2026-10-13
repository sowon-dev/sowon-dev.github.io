---
title: "[Server]아파치 vs 톰캣 같은 거 아냐? 차이점"
date: 2022-09-05 19:05:43
tags:
  - "차이"
categories:
  - Backend
  - Server
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">웹 서버(Apache)는 HTTP 요청을 받아 HTML, 이미지 등 정적 컨텐츠를 클라이언트에 제공하는 역할을 담당한다.
    반면 WAS(Tomcat)는 DB 조회나 비즈니스 로직 등 동적 처리를 담당하며, 부하 분산과 보안을 위해 두 서버를 분리 구축하는 것이 권장된다.</p>
</div>

<!-- more -->

성과장님과 서버구축 관련 이야기를 나누다 아파치와 톰캣이 차이가 있다는 걸 알게되었다.  
띠용? 톰캣이 아파치 소프트웨어 재단에서 개발된 것이므로 아파치서버나 톰캣서버나 동일하다고 생각하고 있었다.  
구글링결과 아파치서버와 톰캣서버는 아주 큰 차이점이 있었고 이를 공부해봤다.

## 아피치 톰캣 다 같은 거 아냐?

NOPE!  
아파치(Apach)란 아파치 소프트웨어 재단 이름이다. 실무에서 아파치서버라고 부른다면 아파치 재단의 오픈소스로 만든 Web Server를 칭한다.  
우리가 헷갈리는 이유 WAS가 웹서버의 기능을 다 수행할 수 있기때문이다.  
하지만 서버과부하, 보안강화 등의 목적으로 WAS와 Web Server를 분리하는 프로젝트들도 있다.

| | Web Server | WAS(Web Application Server)  
---|---|---  
정의 | 웹 브라우저 클라이언트로부터 HTTP 요청을 받아 정적인 컨텐츠(.html .jpeg .css 등)를 제공하는 컴퓨터 프로그램 | DB 조회나 다양한 로직 처리를 요구하는 동적인 컨텐츠를 제공하기 위해 만들어진 Application Server  
데이터 | 클라이언트측 정적 데이터 | 서버측 동적 데이터  
DB데이터 사용 | 불가능 | 가능  
예시 | Apache Server, Nginx, IIS(Windows 전용 Web 서버)등 | Tomcat, JBoss, Jeus, Web Sphere 등  
  
  
  
  

## 잠시만 IIS도 동적페이지 생성이 가능한데 Web Server라고?

맞다. IIS는 Web Server와 WAS가 함께 있는 서버이다.  
ms진영에서는 IIS를 웹서버라고 부르며, 웹서버와 WAS를 딱히 구별하지 않는 듯 하다.  
IIS는 ms용, WAS는 범용이라 생각하면 되고 서로 바라보는 범위가 약간 다른 셈!

  
  
  

## 참고

  * [웹서버(WEB SERVER) VS 웹어플리케이션서버(WAS, Web Application Server)]()

#[차이](/tags/%EC%B0%A8%EC%9D%B4/)
