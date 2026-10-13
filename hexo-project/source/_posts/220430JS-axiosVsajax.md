---
title: "ajax랑 axios는 무슨 차이가 있을까?"
date: 2022-04-30 05:20:43
tags: []
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'ajax랑 axios는 무슨 차이가 있을까?'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    이 둘의 차이점은 무엇일까?의 차이를 고려하여 상황에 맞게 적용해야 한다.</p>
</div>

<!-- more -->

프로젝트를 진행하다보면 클라이언트와 서버간의 데이터를 요청응답받기 위해 HTTP통신을 하게 된다.  
이때 자주 사용하는 라이브러리로는 jQuery.ajax와 axios가 있다.  
이 둘의 차이점은 무엇일까?

## ajax는 라이브러리인가?

wikipedia[(링크)](https://en.wikipedia.org/wiki/Ajax_%28programming%29)에 따르면 ajax는 라이브러리가 아니라 비동기 통신 웹 개발 기술이다.

```html
Ajax (also AJAX /ˈeɪdʒæks/; short for "Asynchronous JavaScript and XML")[1][2] is a set of web development techniques that uses various web technologies on the client-side to create asynchronous web applications. 
With Ajax, web applications can send and retrieve data from a server asynchronously (in the background) without interfering with the display and behaviour of the existing page. 
By decoupling the data interchange layer from the presentation layer, Ajax allows web pages and, by extension, web applications, to change content dynamically without the need to reload the entire page.
[3] In practice, modern implementations commonly utilize JSON instead of XML.

Ajax is not a technology, but rather a programming concept. 
HTML and CSS can be used in combination to mark up and style information. 
The webpage can be modified by JavaScript to dynamically display—and allow the user to interact with the new information. 
The built-in XMLHttpRequest object is used to execute Ajax on webpages, allowing websites to load content onto the screen without refreshing the page. 
Ajax is not a new technology, nor is it a new language. Instead, it is existing technologies used in a new way.

by wikipedia ajax
```

이 기술을 구현한 라이브러리가 바로 jQuery.ajax()와 axios이다.

  
  
  

## jQuery.ajax()

사용법은 아래와 같다.

```js
$.ajax({
  method: "POST",
  url: "some.php",
  data: { name: "John", location: "Boston" }
})
  .done(function( msg ) {
    alert( "Data Saved: " + msg );
  });
```

  
  
  

## axios

axios 공식문서[(링크)](https://axios-http.com/docs/intro)에 따르면 axios는 node.js와 브라우저를 위한 프로미스기반의 HTTP통신 라이브러리이다.

```
Axios is a promise-based HTTP Client for node.js and the browser. 
It is isomorphic (= it can run in the browser and nodejs with the same codebase). 
On the server-side it uses the native node.js http module, while on the client (browser) it uses XMLHttpRequests.
```

사용법 예시는 아래와 같다.

```js
const axios = require('axios');

// Make a request for a user with a given ID
axios.get('/user?ID=12345')
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });

// Optionally the request above could also be done as
axios.get('/user', {
    params: {
      ID: 12345
    }
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  })
  .then(function () {
    // always executed
  });  

// Want to use async/await? Add the `async` keyword to your outer function/method.
async function getUser() {
  try {
    const response = await axios.get('/user?ID=12345');
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}
```

  
  
  

## fetch도 있던데?

fetch는 axios와 마찬가지로 promise기반 비동기 HTTP 클라이언트이다. 모던 브라우저에 내장되어있기에 바로 사용할 수 있다.  
사용법은 axios와 거의 유사하고 성능은 fetch가 조금 빠르다고 한다[(링크)](https://meticulous.ai/blog/fetch-vs-axios/).  
실무에선 아직 한 번도 사용해본적이 없는데 fetch는 몇몇 브라우저에선 지원이 안되기때문이다[(링크)](https://caniuse.com/fetch). 

```js
fetch(url, {
  method: 'GET', // other options: POST, PUT, DELETE, etc.
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({}),
}).then((response) => response.json())
  .then((data) => console.log(data))
```

  
  
  

## 참고하면 좋은 글

  * [Ajax 는 라이브러리 인가요?](https://velog.io/@leehaeun0/Ajax-%EB%8A%94-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-%EC%9D%B8%EA%B0%80%EC%9A%94)
