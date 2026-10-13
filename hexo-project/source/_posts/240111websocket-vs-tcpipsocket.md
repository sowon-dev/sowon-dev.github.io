---
title: "[네트워크] Socket(소켓) vs Websocket(웹소켓) 차이점"
date: 2024-01-10 16:46:25
tags:
  - "차이"
  - "Websocket"
categories:
  - Backend
  - Network
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'Socket(소켓) vs Websocket(웹소켓) 차이점'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    이참에 둘 차이를 공부해봤다.</p>
</div>

<!-- more -->

오늘 팀장님과 커피챗을 하면서 소켓이야기를 했다.  
내가 알고 있는 소켓은 클라이언트의 요청없이 서버가 응답하는 것이였는데 오늘 팀장님 말씀을 들어보니까 뭔가 다른 내용이었다.

알고보니 팀장님은 소켓통신을 얘기하셨는데 내가 웹소켓으로 오해했기때문이다.  
이참에 둘 차이를 공부해봤다.  
내가 제일 부족한 부분은 네트워크인 듯하다. 올해는 이 부분에 대해 집중적으로 공부해봐야겠다. 

# Socket(소켓)

![해시넷](/img/240111OSI7LayerAndTCPIP.jpg)

  * OSI 7계층은 네트워크를 관리하는 계층이다. 계층별 각 프로토콜, 즉 통신규약이 존재한다. 프로토콜을 구현하려면 구체적인 구현부인 함수가 필요하다.
  * 소켓이란? 별도의 구현없이 소켓을 이용하여 프로토콜 함수의 BODY를 만들 수 있다. 일반적으로 TCP/IP를 사용한다. 
    * 연결역할: 일종의 endpoint로 IP와 서비스포트를 통해서 두 개의 소프트웨어를 연결한다.
    * 데이터송수신역할: 두 개의 소프트웨어를 연결하고 데이터를 송수신한다.
    * 종류: 클라이언트 소켓, 서버 소켓
  * TCP/IP 4계층 중 전송계층에서 사용됨
    * TCP통신이란? [TCP통신 vs UDP통신 차이점](https://sowon-dev.github.io/2021/07/30/210730TCPVSUDP/)

  
  
  

# Websocket(웹소켓)과의 차이점

  * [웹소켓](https://sowon-dev.github.io/2023/01/26/230127resttemplate-vs-websocket/)이란? 서버가 클라이언트에게 먼저 말(메세지)을 걸 수 있다. 즉, 클라이언트 요청없이도 서버가 클라이언트에 응답가능!
  * Socket(소켓)과 차이점? 
    * 동작계층: 소켓은 인터넷프로토콜을 기반하므로 TCP가 속한 OSI 4계층에서 이루어지고 웹소켓은 TCP에 의존하지만 HTTP기반이므로 7계층에서 이루어짐
    * 데이터형식: TCP에 기반한 소켓통신은 단순히 바이트로 이루어진 데이터, 웹소켓통신은 메시지형식의 데이터

사실 소켓과 웹소켓은 완전 다른 개념이 아니다. 소켓통신을 웹어플리케이션에 맞게 디자인한 것이 웹소캣이다.

  
  
  

# 여담

팀장님께 네트워크 공부를 어떻게 하면 좋을지 조언을 부탁드리니 [네트워크관리사 자격증](https://www.icqa.or.kr/cn/page/network)이 있다고 알려주셨다.  
올해는 이 자격증을 취득해봐야겠다!

  
  
  

# 참고

  * [RestTemplate(레스트템플릿)과 Websocket(웹소켓)차이점](https://sowon-dev.github.io/2023/01/26/230127resttemplate-vs-websocket/)
  * [TCP통신 vs UDP통신 차이점](https://sowon-dev.github.io/2021/07/30/210730TCPVSUDP/)
  * [Konseo - 소켓과 웹소켓](https://velog.io/@rhdmstj17/%EC%86%8C%EC%BC%93%EA%B3%BC-%EC%9B%B9%EC%86%8C%EC%BC%93-%ED%95%9C-%EB%B2%88%EC%97%90-%EC%A0%95%EB%A6%AC-1)

#[차이](/tags/%EC%B0%A8%EC%9D%B4/)[Websocket](/tags/Websocket/)
