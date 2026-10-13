---
title: "spread operator (...) 점 세 개를 알아보자"
date: 2022-01-14 22:12:30
tags: []
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">spread operator (...) 점 세 개를 알아보자의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    객체와 배열의 병합에 사용할 수 있다.</p>
</div>

<!-- more -->

온점 세 개를 찍어서 표현하는 spread syntax(…)라고 한다.  
이 spread operator는 S2015에서 새로 추가된 systax으로 병합, 구조 분배 할당(destructuring)등에 다양하게 활용할 수 있다.

## 객체/배열 병합

객체와 배열의 병합에 사용할 수 있다.

```js
const newDBinfo = {
	DATABASE_HOST: '나혜석',
	DATABASE_PASSWORD: '나혜석123',
}

const config = {
	DATABASE_HOST: '유관순',
	DATABASE_PASSWORD: '유관순123',
	DATABASE_USERNAME: 'user',
	... newDBinfo,
}

const config2 = {
	... newDBinfo,
	DATABASE_HOST: '유관순',
	DATABASE_PASSWORD: '유관순123',
	DATABASE_USERNAME: 'user',

}

console.log(config)
/*
{
	DATABASE_HOST: "나혜석"
	DATABASE_PASSWORD: "나혜석123"
	DATABASE_USERNAME: "user"
	[[Prototype]]: Object
}
*/

console.log(config2)
/*
/*
{
	DATABASE_HOST: "유관순"
	DATABASE_PASSWORD: "유관순123"
	DATABASE_USERNAME: "user"
	[[Prototype]]: Object
}
*/
```

이 결과값으로 알 수 있듯 spread syntax(…)의 위치에 따라 덮어쓰기가 가능하다.

  
  
  

## 객체/배열 reset

객체와 배열을 자를 수 있다.

### 객체예시

```js
const person = {
	name: '유관순',
	age: '17',
}

const {age, ...independenceData} = person
console.log(independenceData)
/*
{name: "유관순"}
*/
```

  
  

### 배열 예시

```js
const [one, ...others] = [1,2,3]
console.log(one) // 1
console.log(others) // [2,3]
```
