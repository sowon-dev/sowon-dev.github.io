---
title: "[JavaScript/jQuery]제이쿼리 선택자(Selector) 비교"
date: 2023-07-16 19:33:41
tags:
  - "jQuery"
  - "차이"
  - "VanillaJS"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'제이쿼리 선택자(Selector) 비교'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    VanillaJS와 jQuery는 최대 10배 속도차이가 발생난다고 한다.</p>
</div>

<!-- more -->

VanillaJS와 jQuery는 최대 10배 속도차이가 발생난다고 한다.

그래서 이번에 손에 익힐겸 jQuery보다 VanillaJS를 사용하려고 노력해봤다. 제일 헷갈리는 부분은 선택자부분이었다.

# 선택자(Selector)

JavaScript | jQuery  
---|---  
document.getElementById(아이디명) | $(#아이디명)  
document.getElementsByClassName(클래스명) | $(.클래스명)  
document.getElementsByTagName(태그명) | $(태그명)  
  
  * querySelector: 매칭된 첫번째 element 반환, 조회값 없을땐 `null` 반환
  * querySelectorAll: 매칭된 모든 element를 NodeList로 반환, 조회값 없을땐 `[]` 반환

  
  
  

# 코드

```js
// 모든 요소
$("*")
document.querySelectorAll("*")

// ID명이 password인 요소 선택 
$("#password")
document.querySelector("#password")
document.getElementById('password')
window['password']

// Class 명이 'btn'인 요소 선택
$(".btn")
document.querySelectorAll(".btn")
document.getElementsByClassName('btn')

// attribute요소 선택
$('a[target=_blank]')
document.querySelectorAll('a[target=_blank]')

// input의 value값이 'address'인 요소 선택
$("input[value='address']")
document.querySelector("input[value='address']")
```

  
  
  

# 참고

  * [You-Dont-Need-jQuery 깃헙 리포](https://github.com/camsong/You-Dont-Need-jQuery)

#[jQuery](/tags/jQuery/)[차이](/tags/%EC%B0%A8%EC%9D%B4/)[VanillaJS](/tags/VanillaJS/)
