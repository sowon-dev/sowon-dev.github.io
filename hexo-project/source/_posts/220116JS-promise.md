---
title: "Promise 프로미스"
date: 2022-01-16 05:31:03
tags: []
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Promise 프로미스의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    Promise객체는 자바스크립트에서 비동기 처리에 사용되는 객체이다.</p>
</div>

<!-- more -->

프로미스에 대해 알아보자.

## 개념

Promise객체는 자바스크립트에서 비동기 처리에 사용되는 객체이다.

  
  
  

## 프로미스의 3가지 상태

용어 | 뜻 | 설명  
---|---|---  
Pending | 대기 | 비동기처리를 하지도, 거부하지도 않은 초기 상태  
Fulfilled | 이행 | 비동기처리가 성공적으로 완료됨  
Rejected | 거부 | 비동기처리가 실패함  
  
![https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/promises.png)

  
  
  

## 실무사용

실무에서는 ajax등의 비동기를 동기화시킬때 사용한다.  
예를 들어 onclick이벤트시 A메서드를 무조건 실행하고 난 뒤 B메서드를 실행하고 싶다면 콜백함수를 사용하면 되는데 만약 A함수를 호출한 뒤 B함수, 그 뒤 C함수 그 뒤 D함수를 사용해야한다면 콜백지옥이 펼쳐질것이다. 이를 예방하기 위해서 프로미스를 사용할 수 있다.

```js
$(document).ready(function() {
	$("a[data-role=formTag]").click(async function() {
    	await customFormValidation('성명', 'name');
    	await customFormValidation('연락처', 'mobile');
    	await customFormValidation('나이', 'age');
		
		$('form').submit();
	}
});

function customFormValidation(label, inputName){
  return new Promise(function (resolve, reject) {
  if($('form').find('input[name='+inputName+']').val() == '' || 			  
  	$('form').find('input[name='+inputName+']').val() == 0){
    	$('form').find('input[name='+inputName+']').parents('dd').addClass("reconfirm");
    	$('form').find('input[name='+inputName+']').focus();
   		resolve(false)
    	return false;
  	} else {
    	$('input[name='+inputName+']').parents('dd').removeClass("reconfirm");
    	resolve(true)
  	}
  })
}
```

  
  
  

## 참고

  * <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise>
