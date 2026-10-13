---
title: "[디자인패턴] 옵저버 패턴(observer pattern)이란? 개념,정의"
date: 2023-01-24 22:13:16
tags:
  - "디자인패턴"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">옵저버 패턴(observer pattern)이란? 개념,정의의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * 주로 분산 이벤트 핸들링 시스템을 구현하는 데 사용된다.</p>
</div>

<!-- more -->

오늘 김팀장님 코드를 보다가 옵저버 패턴을 만났다. 디자인패턴을 잘 모르기때문에 이참에 공부해보았다.

여담으로, 공부해봤지만 디자인 패턴은 여전히 어렵다.

# 옵저버 패턴(Observer pattern)이란?

영단어 observer 뜻 그대로 관찰자와 관련된 패턴이다. 객체의 상태 변화를 관찰하는 관찰자들(옵저버)을 목록에 등록해놓고 상태 변화가 있을때마다 메서드 등을 통해 객체가 직접 목록의 각 옵저버에게 통지(notify)하는 디자인 패턴이다.

![출처 - 나무위키](https://upload.wikimedia.org/wikipedia/commons/8/8d/Observer.svg)

  * 주로 분산 이벤트 핸들링 시스템을 구현하는 데 사용된다. 
  * 발행/구독 모델로 알려져 있기도 하다.
  * 코틀린에서는 Observer(옵저버)대신 Listener(리스너) 용어를 사용한다.

자바에서는 옵저버패턴을 위한 클래스와 인터페이스를 제공한다.

  * [docs.oracle - Interface Observer](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Observer.html)
  * [docs.oracle - Class Observable](https://docs.oracle.com/javase/8/docs/api/index.html?java/util/Observable.html)

쉽게 이해할 수 있는 예시는 유튜브 채널(Subject)과 구독자들(Observer)간의 관계이다.  
유튜브 채널 관리자가 영상을 업로드하면 구독자들에게만 알람이가 가고 구독자가 아닌 사람들에게는 아무런 영향을 끼치지않는다.  
즉, 객체(Subject)의 상태가 변화하면 Observer 목록에 있는 각 Observer에게 통지(notify)한다.

  
  
  

# 리액트도 옵저버?

옵저버패턴을 알수록 리액트가 자꾸 떠올랐다.  
[Seungho Lee - 리덕스(Redux)와 Observer 패턴](https://medium.com/@shlee1353/리액트-리덕스-redux-와-observer-패턴-a4aae3468a25)에서 왜 자꾸 리액트가 떠올랐는지 확인할 수 있었다.

> 리액트 사용시 데이터 관리를 손쉽게 하기 위해 리덕스(redux)를 사용하며, 이는 옵저버 패턴을 기반으로 제작되었습니다. 리덕스 스토어(store)는 애플리케이션의 상태트리(state tree)를 관리하고 있습니다. 스토어 내부에서 상태값이 변하면 그것에 대한 액션을 보내줘야합니다.  
> 출처: [Seungho Lee - 리덕스(Redux)와 Observer 패턴](https://medium.com/@shlee1353/리액트-리덕스-redux-와-observer-패턴-a4aae3468a25)

리액트의 리덕스는 옵저버패턴으로 디자인된 것이었다!  
지식이 연결되는 느낌! 재밌다!

  
  
  

# 참고

  * [위키백과 - 옵서버 패턴](https://ko.wikipedia.org/wiki/%EC%98%B5%EC%84%9C%EB%B2%84_%ED%8C%A8%ED%84%B4)
  * [haero_kim - 옵저버 패턴 개념 떠먹여드립니다](https://velog.io/@haero_kim/옵저버-패턴-개념-떠먹여드립니다)
  * [hanna2100 - 디자인패턴 2.옵저버 패턴 개념과 예제](https://velog.io/@hanna2100/디자인패턴-2.-옵저버-패턴-개념과-예제-observer-pattern)

#[디자인패턴](/tags/%EB%94%94%EC%9E%90%EC%9D%B8%ED%8C%A8%ED%84%B4/)
