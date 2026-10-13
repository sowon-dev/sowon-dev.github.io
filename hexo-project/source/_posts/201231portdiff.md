---
title: "포트(port)란? HTTP port 80과 HTTPS 443의 차이"
date: 2020-12-30 19:31:06
tags:
  - "Port"
categories:
  - Backend
  - Network
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'포트(port)란? HTTP port 80과 HTTPS 443의 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    * IP와 PORT의 차이의 차이를 고려하여 상황에 맞게 적용해야 한다.</p>
</div>

<!-- more -->

## port 443과 80의 차이

  * http의 기본 포트: 80.
  * https의 기본 포트: 443.

```plain
http 프로토콜
http://www.google.com - http 프로토콜. 구글이 망하지만 않는다면 잘 접속된다.
http://www.google.com:80 - 80 포트를 명시했다. 잘 접속된다.
http://www.google.com:81 - 81 포트를 명시했다. 목적이 다른 포트이므로 접속이 안 된다.

https 프로토콜
https://www.google.com - https 프로토콜. 잘 접속된다.
https://www.google.com:443 - 443 포트를 명시했다. 잘 접속된다.
https://www.google.com:444 - 444 포트를 명시했다. 목적이 다른 포트이므로 접속이 안 된다.
```

  
  
  

## port란?

  * 포트(port) : 논리적인 접속장소  
특히 인터넷 프로토콜인 TCP/IP를 사용할 때에는 클라이언트 프로그램이 네트워크 상의 특정 서버 프로그램을 지정하는 방법으로 사용된다.  
네트워크 상에서 통신을 할 때 IP를 토대로 해당 서버가 있는 컴퓨터에 접근한다.  
그런데 대부분의 경우 하나의 컴퓨터에는 여러 개의 서버가 실행될 수 있다.  
컴퓨터에 여러 개의 서버가 실행되고 있다면, 어느 서버에 접속해야 하는지 컴퓨터에게 알려주어야 한다.  
이때 사용되는 것이 포트 번호이다.

  * HTTP의 경우 지정된 포트 번호가 있는데 이런 것들을 “잘 알려진 포트들” “Well-known port”이라고도 한다.

![https://captcha.tistory.com/5](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile6.uf.tistory.com%2Fimage%2F9953183E5B8FA49E0782C1)

포트 0 ~ 1023은 예약되어있다.  
나머지 65535개는 사용할 수 있다.

  * IP와 PORT의 차이
    * IP : 컴퓨터를 찾을 때 필요한 주소
    * Port : 그 컴퓨터 안에서 프로그램을 찾기 위한 수단.

  
  
  

## 참고

  * <https://johngrib.github.io/wiki/why-http-80-https-443/>
  * <https://study-recording.tistory.com/13>
  * <https://captcha.tistory.com/5>

#[Port](/tags/Port/)
