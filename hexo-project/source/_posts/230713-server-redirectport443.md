---
title: "[톰캣Tomcat]SSL이 뭐길래(ft.HTTPS와 비교, 차이점)"
date: 2023-07-12 19:48:06
tags:
  - "차이"
categories:
  - Backend
  - Server
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'SSL이 뭐길래(ft.HTTPS와 비교, 차이점)'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    동작 원리와 장단점을 비교 파악하여 프로젝트 개발 상황에 적합한 방식을 선택할 수 있다.</p>
</div>

<!-- more -->

톰캣에서 SSL을 적용했는데 개발 중에는 적용된 HTTPS를 없애고 HTTP로만 통신하고싶어서 `server.xml`에서 포트를 변경했다.

# 코드

SSL을 미적용하기 위해서 redirectPort포트를 443에서 8443으로 변경했다.

  * server.xml

```xml
// SSL적용
<Connector connectionTimeout="20000" port="80" protocol="HTTP/1.1" redirectPort="443" />

// SSL미적용
<Connector connectionTimeout="20000" port="8080" protocol="HTTP/1.1" redirectPort="8443" />
```

해결은 간단하게 되었지만 SSL이 단순히 인증서라고 생각하고있었는데 정확히 무엇인지 알고싶어졌다.

  
  
  

# 기본부터 하자! HTTP VS HTTPS

HTTP는 Hypertext Transfer Protocol의 약자이며 하이퍼텍스트란 링크와 링크로 이루어진 텍스트를 의미하며 그 중 대표적인 것이 HTML이다.  
즉, Hypertext 인 HTML을 전송하기 위한 통신규약을 의미한다.  
HTTPS에서 마지막의 S는 Over Secure Socket Layer의 약자로 보안이 강화된 HTTP이다. 

![](https://media.geeksforgeeks.org/wp-content/uploads/20211117141004/HTTPSdrawio-660x368.png)  
HTTP는 암호화되지 않은 방법으로 데이터를 전송하기 때문에 서버와 클라이언트가 주고 받는 메시지를 빼앗기가 쉽다.  
예를들어 로그인을 위해서 서버로 비밀번호를 전송하거나, 또는 중요한 기밀 문서를 열람하는 과정에서 악의적인 감청이나 데이터의 변조등이 일어날 수 있다. 이를 보안한 것이 HTTPS다.  
이 블로그도 보안(Secure)된 HTML인 `https://sowon-dev.github.io/`이다.

  
  
  

# HTTPS VS SSL

SSL는 Secure Socket Layer의 약어로 암호화 소켓층이다.  
![https://wpmudev.com/blog/securing-website-https-ssl/](https://wpmudev.com/blog/wp-content/uploads/2021/11/004-https-stack-diagram-vJGB-1050x609.png)  
SSL이라는 통신 방법 위에서 동작하는 서비스 중에 하나가 HTTP이다. 그리고 HTTP가 SSL을 이용하면 HTTPS가 된다.

  
  
  

# SSL VS TLS

같은 말!  
TLS 1.0은 SSL 3.0을 따른다.

  
  
  

# 참고

  * <https://www.geeksforgeeks.org/difference-between-http-and-https/>
  * [생활코딩 - HTTPS와 SSL 인증서](https://opentutorials.org/course/228/4894)

#[차이](/tags/%EC%B0%A8%EC%9D%B4/)
