---
title: "[Spring]RestTemplate(레스트템플릿)과 Websocket(웹소켓)차이점"
date: 2023-01-26 19:43:38
tags:
  - "차이"
  - "RestTemplate"
  - "Websocket"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'RestTemplate(레스트템플릿)과 Websocket(웹소켓)차이점'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    따라서 RestTemplate과 Websocket 차이점은 결국 REST API와 Websocket API 차이점이라고 볼 수 있다.</p>
</div>

<!-- more -->

RestTemplate은 간편하게 Rest 방식 API를 호출할 수 있는 라이브러리이고 Spring 3.0부터 지원한다.  
따라서 RestTemplate과 Websocket 차이점은 결국 REST API와 Websocket API 차이점이라고 볼 수 있다.

가장 잘 알고 있는 차이점은 REST API는 클라이언트의 요청이 없으면 서버는 먼저 말을 걸 수 없지만 웹소켓은 서버가 클라이언트에게 먼저 말(메세지)을 걸수있다.  
즉, REST API는 클라이언트의 요청이 있어야 서버 응답이 있는 반면에 Websocket API는 클라이언트 요청없이도 서버가 클라이언트에 응답할 수 있다.  
실무자입자에서는 어떠한 차이가 있을까?

  
  
  

# REST API와 Websocket API 차이점

  * REST API: 
    * 동기, 비동기 둘다 지원. 
    * 프레임워크가 에러보드까지 구현을 다 해놓아서 커넥션이 안정적이라고 하는편
  * Websocket API: 
    * 동기, 비동기 둘다 지원. 
    * 빠른 응답이 장점. 
    * 서버리소스가 많이 든다.
    * 커넥션 안정성(커넥션 끊을때까지 커넥션이 안 끊김)
    * 웹소켓을 쓰면 커멘드패턴에 따라서 규칙을 다 맞춰줘야함. 사람이 직접 해야하는 게 많아서 난이도가 있고 서버 리소스가 많이 들지만 커넥션이 매우 안정적임

  
  
  

# 참고

  * 부장님 지식

#[차이](/tags/%EC%B0%A8%EC%9D%B4/)[RestTemplate](/tags/RestTemplate/)[Websocket](/tags/Websocket/)
