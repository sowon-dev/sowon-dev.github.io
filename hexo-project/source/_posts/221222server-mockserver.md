---
title: "[Server]Mock Server(목서버)는 어때요?"
date: 2022-12-21 19:52:19
tags:
  - "오늘또못알아듣고말았습니다"
categories:
  - Backend
  - Server
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Mock Server(목서버)는 어때요?의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    jUnit에 관해서는 이전에 작성한 Junit 포스팅을 참고하면 된다.</p>
</div>

<!-- more -->

오늘 회의에서 신규서비스 테스트를 위해 Mock서버, jUnit단위테스트 등의 이야기가 나왔다.  
외부 API를 테스트를 하려면 어떻게 해야할까?

jUnit에 관해서는 이전에 작성한 [Junit](https://sowon-dev.github.io/2021/08/12/210813Spring-junit/#Mock) 포스팅을 참고하면 된다.  
그럼 목서버는 무엇일까?

# 먼저 MOCK(목)이 뭘까?

> 실제 사용되어야하는 객체의 대체객체로 실제 객체를 만들어서 하기엔 시간이 부족하고 비용이 높은 경우, 구현이 까다로울 경우에 가짜 객체를 만들어서 사용하는데 그중 하나가 Mock객체이다.  
> Mock객체: 행위를 검증하기 위해 사용되는 객체  
> 직접 만들거나 스프링프레임워크를 통해서 간단하게 만들수 있음  
> 출처: [Junit - Mock 객체](https://sowon-dev.github.io/2021/08/12/210813Spring-junit/#Mock)

  
  
  

# Mock 서버란?

> For any system you integrate with via HTTP or HTTPS MockServer can be used as:  
> a mock configured to return specific responses for different requests  
> a proxy recording and optionally modifying requests and responses  
> both a proxy for some requests and a mock for other requests at the same time  
> When MockServer receives a request it matches the request against active expectations that have been configured.  
> Then, if no matches are found, it proxies the request if appropriate; otherwise a 404 is returned.  
> For each request received the following steps happen:  
> find matching expectation and perform action  
> if no matching expectation proxy request  
> if not a proxy request return 404  
> An expectation defines the action that is taken, for example, a response could be returned.  
> 출처: <https://www.mock-server.com/>

간단하게 말하자면, 실제 서버처럼 HTTP나 HTTPS 요청과 응답을 주고 받을 수 있는 가짜 서버이다. 

  * 다양한 요청에 특정한 반응을 반환하도록 구성할 수 있음
  * 프록시를 기록하고 선택적으로 요청과 응답을 수정할 수 있음
  * 목서버가 예상되는 요청을 받았을땐 이미 작성된 특정 반응을 반환하고 예상되지 않는 요청인 경우 404를 리턴한다.

  
  
  

# 왜 목서버를 사용할까?

크게 3가지 이유가 있다.

  * testing via HTTP or HTTPS, such as a REST or RPC service.
    * 만약 스펙만 존재하고 실제 동작하지 않는 API를 염두하고 해당 API의 데이터를 받는 부분을 개발해야 한다면 어떻게 해야할까? 이럴 때 필요한 것이 가상의 서버, 바로 Mock Server이다.
  * de-coupling development
  * isolate single service

  
  
  

# 목서버를 만드는 방법

구글링했을때 가장 많이 나오는 방법은 PostMan을 활용하는 것이다. 하지만 무료요금제인 경우 한달에 1000건 요청제한이 있다.  
[Postman 으로 Mock Server 구축하기](https://way-be-developer.tistory.com/239)글을 참고!

  
  
  

# 출처

  * <https://opennote46.tistory.com/208>
  * <https://www.mock-server.com/>
  * [Junit - Mock 객체](https://sowon-dev.github.io/2021/08/12/210813Spring-junit/#Mock)
  * <https://devvkkid.tistory.com/219>
  * [우아한마켓 - 외부 API를 어떻게 테스트 할 것인가?](https://velog.io/@kyle/%EC%99%B8%EB%B6%80-API%EB%A5%BC-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%95%A0-%EA%B2%83%EC%9D%B8%EA%B0%80)

#[오늘또못알아듣고말았습니다](/tags/%EC%98%A4%EB%8A%98%EB%98%90%EB%AA%BB%EC%95%8C%EC%95%84%EB%93%A3%EA%B3%A0%EB%A7%90%EC%95%98%EC%8A%B5%EB%8B%88%EB%8B%A4/)
