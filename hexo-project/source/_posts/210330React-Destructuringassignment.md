---
title: "[리액트] this.state 귀찮을땐 구조분해"
date: 2021-03-29 15:46:15
tags: []
categories:
  - Frontend
  - React
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">this.state 귀찮을땐 구조분해의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    리액트를 클래스형 컴포넌트로 사용하게되면 계속 this.state를 써줘야하는 불편함이 있다.</p>
</div>

<!-- more -->

리액트를 클래스형 컴포넌트로 사용하게되면 계속 this.state를 써줘야하는 불편함이 있다.  
이를 구조분해문법으로 해결할 수 있다.

## 기존코드

```js
//기존
return (
    <>
		<h1>{this.state.value}</h1>
    	<h1>{this.state.answer}</h1>
	</>
)
```

  
  
  

## 구조분해문법사용 코드

```js
//구조분해문법사용
const { value, answer } = this.state;
return (
    <>
		<h1>{value}</h1>
        <h1>{answer}</h1>
	</>
)
```

  
  
  

## 참고

  * [제로초 리액트 무료강좌(웹게임)](https://youtube.com/playlist?list=PLcqDmjxt30RtqbStQqk-eYMK8N-1SYIFn)
