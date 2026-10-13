---
title: "[JS]scope 스코프"
date: 2022-05-16 19:12:43
tags: []
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">scope 스코프의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * let 또는 const 키워드 사용을 적용할 수 있다.</p>
</div>

<!-- more -->

이번에 프로젝트를 진행하면서 버그가 발생했는데 알고보니 스코프문제였다.  
이번 기회에 스코프에 대해 확실히 정리해보고자 한다.

## 스코프란?

w3school에 따르면[(링크)](https://www.w3schools.com/js/js_scope.asp) Scope란 변수의 유효한 범위이다.

< 스코프종류 >

  1. Global scope
  2. Local Scope
     1. Block scope
     2. Function scope

ES6이전에는 js는 Global Scope and Function Scope만 있었다.  
ES6전에는 var만 있었는데 ES6이후로 let과 const가 생겨나면서 block scope 개념도 함께 생겨났다.

  
  
  

## 1 Global scope 블록스코프

이름그대로 변수가 전역에 선언된 경우이다.  
어디서든 접근이 가능하다. 어디서나 접근가능하기때문에 편리한 장점이 있지만 코드가 길어질수록 휴먼에러가 날 확률이 높아진다.

```js
let carName = "Volvo";
// code here can use carName

function myFunction() {
// code here can also use carName
}
```

  
  
  

## 2 Block scope 블록스코프

블록스코는 `브라켓{}`블록안에서만 변수가 유효할때를 뜻한다. 아래 비교예시를 보자.

  * var 키워드 사용

```js
{
  var x = 2;
}
// x CAN be used here
```

  * let 또는 const 키워드 사용

```js
{
  let x = 2;
}
// x can NOT be used here
```

위 두 예시의 차이에서 알 수 있듯이 `브라켓 {}`을 벗어나도 선언한 변수를 호출할 수 있는지 없는지로 블록스코프인지를 확인할 수 있다.  
var변수는 블록스코프가 아니기때문에 변수관리에 있어 문제를 초래하기도 한다.

  
  
  

## 3 Function Scope 로컬스코프

말그대로 함수 안에서 선언한 변수로 함수안에서만 호출가능하고 함수 밖에서는 호출할 수 없다.

```js
// code here can NOT use carName

function myFunction() {
  let carName = "Volvo";
  // code here CAN use carName
}

// code here can NOT use carName
```

  
  
  

## Static Scoping (Lexical Scoping)

JavaScropt, C, Java 등에서는 Static Scoping을 따른다. 즉, 함수를 어디서 선언했는지에 따라 상위 스코프를 결정하는 것이다.  
var를 사용하여 변수를 선언했을때 어떻게 값이 나올까?

```js
var num = 7;
function a(){
    var num = 17;
    b();
}
function b(){
    console.log(num);
}
 
a(); //값은?
b(); //값은?
```

  * output

```js
7
7
```

a()의 호출값이 17이 아니고 왜 7인 걸까?

함수가 언제 호출되는지에 따르는 게 아니라 함수를 어디에 선언했냐에 따라 상위 스코프가 결정되기 때문이다.  
num은 이미 두 함수보다 먼저 선언했으므로 7은 17로 덮어써지지않고 그대로 7로 출력된다.

> 참고로 함수 호출에 따라 스코프가 결정되는 것을 Dynamic Scope라고 한다. Perl, Bash Shell 등에서 사용된다.
