---
title: "Framework VS Library 프레임워크와 라이브러리의 차이"
date: 2020-12-03 23:44:14
tags:
  - "TIL"
  - "Journal"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'Framework VS Library 프레임워크와 라이브러리의 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    실행주체에 있어 차이점이 있다.</p>
</div>

<!-- more -->

## 프레임워크와 라이브러리 차이점

실행주체에 있어 차이점이 있다.

  * 라이브러리 : **I** call 라이브러리

    * 내가 필요할 때마다 라이브러리를 실행시킬수있다.
    * 내가 원하는 대로 수정이 가능하다.
    * 비유하자면 Ikea(아이키아)
  * 프레임워크 : **Framework** calls 내가 작성한 코드

    * 프레임워크가 내가 작성할 코드를 실행시킨다.
    * 프레임워크의 규칙을 잘 따라야지만 내 코드가 정상 작동한다.
    * 비유하자면 모델하우스
  * 공통점 : 프레임워크와 라이브러리 모두 누군가가 자주 발생하는 문제들을 해결하거나 더 좋은 코드를 위해 미리 만들어 둔 코드이다. 

> In summary  
> Frameworks and libraries are both code written by someone else that helps you perform some common tasks in a less verbose way.  
> A framework inverts the control of the program. It tells the developer what they need. A library doesn’t. The programmer calls the library where and when they need it.  
> The degree of freedom a library or framework gives the developer will dictate how “opinionated” it is.  
> By [The Difference Between a Framework and a Library By freecodecamp](https://www.freecodecamp.org/news/the-difference-between-a-framework-and-a-library-bd133054023f/)

  
  
  

## 참고

  * 라이브러리? 프레임워크? 차이점 아직도 모름? 5분 순삭. BY 노마드코더

  * [The Difference Between a Framework and a Library By freecodecamp](https://www.freecodecamp.org/news/the-difference-between-a-framework-and-a-library-bd133054023f/)

#[TIL](/tags/TIL/)[Journal](/tags/Journal/)
