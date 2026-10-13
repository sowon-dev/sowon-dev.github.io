---
title: "[JS] DOMContentLoaded와 window.onload차이(ft.페이지 라이프사이클Page Lifecycle)"
date: 2024-01-08 19:56:23
tags: []
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'DOMContentLoaded와 window.onload차이(ft.페이지 라이프사이클Page Lifecycle)'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    window.onload와 DOMContentLoaded 이벤트는 페이지 라이프사이클과 관련이 있고 차이점이 존재한다.</p>
</div>

<!-- more -->

화면작업을 하면서 페이지로드가 다 된 후 클릭이벤트를 실행하고 싶었다.

DOMContentLoaded를 쓰다가 window.onload와는 뭐가 다른지 궁금해서 찾아보게되었다.

# ✏️ DOMContentLoaded와 window.onload 차이

window.onload와 DOMContentLoaded 이벤트는 페이지 라이프사이클과 관련이 있고 차이점이 존재한다.

  
  
  

## 1\. window.onload 이벤트

페이지에 있는 모든 자원, 이미지와 스크립트를 포함하여 모두 로드되었을 때 발생한다.  
전체 페이지가 완전히 로드된 후에 제공된 함수가 실행된다.

```js
window.onload = function() {
    // 여기에 코드 작성
};
```

  
  
  

## 2\. DOMContentLoaded 이벤트

HTML 문서가 완전히 로드되고 파싱된 후에 발생하며 스타일시트, 이미지, 서브프레임의 로드를 기다리지 않는다.  
DOM을 조작하거나 상호작용하는 스크립트를 실행하고자 할 때 주로 사용되며, window.onload보다 빠른 시점에 발생한다.

```js
document.addEventListener('DOMContentLoaded', function() {
    // DOM이 준비되면 실행할 코드
});
```

대부분의 경우에는 DOMContentLoaded를 사용하는 것이 좋다.  
외부 자원이 모두 로드되기를 기다리지 않고 최대한 빨리 JavaScript를 실행할 수 있어 사용자가 기다리지않고 빠르게 페이지를 제공할 수 있기 때문이다.  
만약 모든 외부 자원의 로드를 기다려야 하는 특별한 상황이 있다면 window.onload을 사용할 수 있겠지만, 대부분의 개발에서는 주로 DOMContentLoaded를 더 많이 사용한다.

  
  
  

# ✏️ DOMContentLoaded와 ready 차이

두 이벤트는 동일한 목적이다.  
둘 다 DOM이 완전히 로드되고 스크립트 실행히 가능한 시점을 감지하는 것을 목표로 한다.  
차이점은 jQuery라이브러리 사용유무이다.

  
  
  

## 1\. DOMContentLoaded 이벤트

```js
document.addEventListener('DOMContentLoaded', function() {
    // DOM이 준비되면 실행할 코드
});
```

이벤트 리스너를 사용하는 방법은 pure JS(Vanilla JS)를 사용하는 방법이다.  
이벤트 리스너를 통해 DOMContentLoaded 이벤트를 감지하고 그 때 실행할 코드를 정의한다.  
이벤트 리스너는 여러 개 등록 가능하다.

  
  
  

## 2\. jQuery 라이브러리 사용

```js
$(document).ready(function() {
    // DOM이 준비되면 실행할 코드
});
```

위 문법을 더 단축해서 사용할 수 있다.

  * 단축된 jQuery 문법

```js
$(function() {
    // DOM이 준비되면 실행할 코드
});
```

  
  
  

# ✏️ 페이지 라이프사이클(Page Lifecycle)

![MDN-Navigation and resource timings](https://developer.mozilla.org/en-US/docs/Web/Performance/Navigation_and_resource_timings/screen_shot_2019-05-03_at_1.06.27_pm.png)

자바스크립트이 페이지 라이프사이클은 아래와 같다

  1. 문서 객체 모델 (DOM) 생성: HTML 문서의 파싱이 끝나면 브라우저는 DOM을 생성
  2. DOMContentLoaded: HTML 전체가 로드되고 DOM트리가 완성되었지만 이미지, stylesheets등의 외부리소스는 아직 로드되지 않은 상태
  3. 이미지, stylesheets등의 외부리소스 업로드
  4. load: HTML뿐만 아니라 이미지, stylesheets등의 외부리소스까지 로드가 완료된 상태
  5. beforeunload: 사용자가 페이지를 떠나려 하는 상태
     1. 페이지를 떠날 때 사용자에게 확인 메시지를 표시할 수 있는 기회를 제공한다
  6. unload: 페이지가 완전히 로딩된 후 사용자가 브라우저에서 페이지를 나간 상태
     1. 주로 사용자가 페이지를 닫거나 새로고침할 때 실행되는 코드에 사용한다.

각각 예시를 보자

```js
// 1. DOMContentLoaded 이벤트
document.addEventListener('DOMContentLoaded', function() {
    // DOM이 준비되면 실행할 코드
});

// 2. load 이벤트
window.onload = function() {
    // 이미지, 스크립트까지 준비되면 실행할 코드
};

// 3. beforeunload
window.addEventListener('beforeunload', function (event) {
    // 확인 메시지를 사용자에게 표시할 수 있는 기회
    const confirmationMessage = '정말로 떠나시겠습니까?';
    event.returnValue = confirmationMessage; // Standard for most browsers
    return confirmationMessage; // For some older browsers
});

// 4. unload
window.addEventListener('unload', function () {
    // 페이지가 완전히 로딩된 후에 실행되는 코드
});
```

  
  
  

# 참고

  * [모던자바스크립트-onload](https://javascript.info/onload-ondomcontentloaded)
