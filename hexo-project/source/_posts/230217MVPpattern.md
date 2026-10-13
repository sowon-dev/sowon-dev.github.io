---
title: "MVC패턴과 MVP패턴 차이"
date: 2023-02-16 17:17:38
tags:
  - "디자인패턴"
  - "차이"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'MVC패턴과 MVP패턴 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    아무리 봐도 MVC와 차이가 느껴지지 않아 한참을 찾아보았다.</p>
</div>

<!-- more -->

박부장님과 김팀장님 셋이서 함께 치맥을 하던 중 부장님이 요즘은 무슨 공부를 하느냐고 물으셨다.  
그때그때 궁금한 것들을 공부하고 있지만 디자인 패턴이 흥미롭다고 말씀드렸더니 MVP패턴에 대해 알려주셨다.

흘려들을 순 없지! 바로 공부를 해보았다.  
아무리 봐도 MVC와 차이가 느껴지지 않아 한참을 찾아보았다.

# MVP이란

Model - View - Presenter로 이뤄진 디자인 패턴이다.  
MVC에서 Controller가 하는 역할을 Presenter가 한다고 보면 되는데 여기서 궁금증이 생긴다.  
그러면 MVC 쓰면 되지 왜 MVP를 쓸까?

  
  
  

## MVC Pattern과의 차이

![위키피디아](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/MVC-Process.svg/800px-MVC-Process.svg.png)

MVC패턴에서는 Model과 View가 서로 연결되어 있어 의존관계를 가지고 있다.

![위키피디아](https://upload.wikimedia.org/wikipedia/commons/d/dc/Model_View_Presenter_GUI_Design_Pattern.png)  
MVP패턴은 Model과 View는 서로 연결되지 않고 Presenter를 통해서 변화를 알 수 있게 된다.  
이렇게 화면과 비즈니스로직이 완전히 분리되면서 테스트가 용이해진다.

  * 장점: View와 Model을 분리시켜 MVC나 Apple의 MVC에서 하기 힘들었던 테스트가 용이
  * 단점: View와 Presenter의 의존관계가 강해지고 Controller 대신 Presenter가 복잡해짐

  
  
  

# MVP패턴에서 뷰가 업데이트 되는 과정

![https://medium.com/android-news/mvp-depp-dive-c6bb1903ace1](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*8ps4RHy13puZY4dK.png)

  1. 사용자가 View에서 액션을 한다.
  2. View는 Presenter에 액션이 들어왔다고 전달한다.
  3. Presenter는 View 액션대로 Model이나 Service를 구성한다.
  4. Update된 Presenter의 데이터를 View에 업데이트 한다.

  
  
  

# 참고

  * 팀장님 지식
  * <https://ykss.netlify.app/web/design_pattern/>
  * <https://medium.com/android-news/mvp-depp-dive-c6bb1903ace1>
  * <https://fomaios.tistory.com/entry/Design-Pattern-MVP-%ED%8C%A8%ED%84%B4%EC%9D%B4%EB%9E%80>

#[디자인패턴](/tags/%EB%94%94%EC%9E%90%EC%9D%B8%ED%8C%A8%ED%84%B4/)[차이](/tags/%EC%B0%A8%EC%9D%B4/)
