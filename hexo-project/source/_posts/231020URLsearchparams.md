---
title: "[JS] URL 파라미터(쿼리파라미터Query Parameter)가져오기"
date: 2023-10-19 15:26:14
tags: []
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">URL 파라미터(쿼리파라미터Query Parameter)가져오기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    정말 초간단한 Query Parameter 가져오는 방법은 URL객체를 사용하는 것이다.</p>
</div>

<!-- more -->

정말 초간단한 Query Parameter 가져오는 방법은 URL객체를 사용하는 것이다.

네이버 검색을 예로 들어보자.  
아래와 같은 URL에서 `query=가나다`만 가져오고 싶다면 어떻게 해야할까?

```console
https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=가나다
```

  
  
  

# URLSearchParams

URLSearchParams 객체를 활용하면 된다!

```js
const urlParams = new URLSearchParams(window.location.search);
const query = urlParams.get('query'); 
console.log(query)
//output: 가나다
```

해결!

  
  
  

# 참고

  * [MDN URLSearchParams 객체](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)
  * [js에서 URL 파라미터(쿼리파라미터Query Parameter)가져오기](https://sowon-dev.github.io/2023/10/19/231020URLsearchparams/)
  * [jsp에서 URL 파라미터(쿼리파라미터Query Parameter)가져오기(ft.EL표현식)](https://sowon-dev.github.io/2024/01/07/240108jsp-el-queryparam/)
