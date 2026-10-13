---
title: "Async await를 Deferred로 걷어내기"
date: 2022-04-24 05:01:06
tags: []
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Async await를 Deferred로 걷어내기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    Deferred는 제이쿼리에서 프로미스를 사용할때 쓰는 객체이다.</p>
</div>

<!-- more -->

ES6문법으로 작업한 내용을 다 걷어내고 ES5문법에 맞춰 작업할 일이 생겼다.  
Async await를 쓴 것들을 싹 걷어냈다.

ES6에서 ES5로 바로 문법을 변환해주는 사이트[(링크)](https://es6console.com/)도 있다.  
이런 일은 사실 생기면 안 되는건데… 인생은 어쩔수없다.

## Async await 사용

```js
function setSelectBox(nextSelectTagId, parntsId) {
	return new Promise(function(resolve, reject) {
	  $.get("/admin/tree?parntsId=" + parntsId, function(data, status) {
		// 코드생략
		resolve();
	  });
	});
}
```

위 함수는 아래처럼 사용가능하다.

```js
async function show(e) {
	var checkedDateset = e.dataset;
	await setSelectBox('lev2ClId', checkedDateset.clid1);
	await setSelectBox('lev3ClId', checkedDateset.clid2);
	// 코드 생략
}
```

  
  
  

## Deferred

Promise 선언한 부분은 Deferred로 대체했다.  
Deferred는 제이쿼리에서 프로미스를 사용할때 쓰는 객체이다.  
먼저 `$.Deferred()`로 deferred 객체를 만들고 성공시 resolve호출하면 프로미스의 done이 연결되고, 실패시 reject를 호출하면 fail로 연결된다.  
그리고 함수의 리턴은 항상 `dfd.promise();`로 해야한다.

```js
function setSelectBox(nextSelectTagId, parntsId) {
	var dfd = $.Deferred();
	$.get("/admin/tree?parntsId=" + parntsId, function(data, status) {
		// 코드생략
		dfd.resolve();
	});

	return dfd.promise();
}
```

위 함수를 아래처럼 사용하면 된다.

```js
function show(e) {
	var checkedDateset = e.dataset;
	setSelectBox('lev2ClId', checkedDateset.clid1).then(function() {
    	return setSelectBox('lev3ClId', checkedDateset.clid2); 
    }).then(function() {
		// 코드 생략
	}
}
```
