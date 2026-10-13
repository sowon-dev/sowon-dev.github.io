---
title: "let과 const와 Var의 차이, 어떻게 쓰면 좋을까?"
date: 2022-01-14 21:56:47
tags: []
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'let과 const와 Var의 차이, 어떻게 쓰면 좋을까?'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    동작 원리와 장단점을 비교 파악하여 프로젝트 개발 상황에 적합한 방식을 선택할 수 있다.</p>
</div>

<!-- more -->

js에서 변수를 선언할때는 let과 const와 Var를 쓸 수 있다.  
이들 중 어떨때 무엇을 사용하면 좋을까?

이는 block scopting에 해답이 있다.

## Block scopting

아래 var로 선언한 예시를 보자.

```js
var x = 1
{
	var x = 2
	console.log(x) //2
}
console.log(x) //2
```

var는 block scoping 자체를 갖지 않기 때문에 두번째 x 선언자체가 첫번째 x의 로컬 scope로 가게된다.  
따라서 var로 선언한 두 변수는 같은 변수가 되고 가장 마지막에 선언한 값으로 결정된다.

이제 let과 const를 보자.  
let과 const는 같은 scoping 룰을 따른다.

```js
const x = 1
{
	const x = 2
	console.log(x) //2
}
console.log(x) //1
```

block 안과 밖을 구분하는 blcok scoping을 따른다.

  
  
  

## 결론

위의 예시에서 알 수 있듯 let과 const는 예측 가능성이 높고 유지보수성이 var보다 뛰어나다.  
따라서, 

  * const를 기본으로 사용하고 필요한 경우에 let을 사용하자
  * var는 절대 쓰지말자.
