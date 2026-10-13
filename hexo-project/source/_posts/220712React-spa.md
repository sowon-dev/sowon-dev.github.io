---
title: "[리액트]SPA 동작 순서"
date: 2022-07-11 23:33:34
tags: []
categories:
  - Frontend
  - React
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">SPA 동작 순서의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    SPA는 Single Page Application의 약자로 한 번 웹 페이지를 로딩하면 사용자가 새로고침하지 않는 이상 페이지를 새로 로딩하지 않는 애플리케이션을 의미한다.</p>
</div>

<!-- more -->

SPA는 Single Page Application의 약자로 한 번 웹 페이지를 로딩하면 사용자가 새로고침하지 않는 이상 페이지를 새로 로딩하지 않는 애플리케이션을 의미한다.  
이게 무슨 의미일까?

## React 동작순서

  1. index.html 렌더링
     * HTML이 body태그를 렌더링하다가 마지막에 bundle.js 스크립트를 로딩하게 되고 거기에 index.js가 포함되어있음.
  2. index.js 실행
     * ReactDOM.render() 함수가 실행됨 -> 매개변수가 `<APP />`이라서 해당 element를 렌더링하게 됨.
  3. root element 하위에 React.js가 생성한 HTML element 추가됨
     * ReactDOM이 내부 컴포넌트들을 root 엘리먼트에 렌더링함.
  4. root element 하위 element 렌더링

  
  
  

## SPA에서 페이지를 변경하고 싶다면?

root의 하위 엘리먼트를 다른 HTMl로 수정해야한다.  
HOW?  
fetch나 ajax등의 함수로 서버에 데이터를 요청한 뒤 응답 데이터를 받음 -> js내에서 HTML 재구성된다.

이렇게 서버에게 새 HTML 페이지를 요청하지 않고 데이터를 받은 다음에 js가 동적으로 HTML 재구성해서 만드는 클라이언트 애플리케이션을 SPA라고 한다.  
이 렌더링 과정을 Client-side Rendering이라고 함.

  * [참고: SSR과 CSR 중 뭐를 우선순위로 두는 게 좋을까?](https://sowon-dev.github.io/2022/01/19/220119prjtreview/#Keep)
