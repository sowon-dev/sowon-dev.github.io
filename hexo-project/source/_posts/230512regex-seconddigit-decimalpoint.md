---
title: "[JS/jQuery]정규표현식 숫자 소수둘째자리까지 적용하기"
date: 2023-05-11 20:55:13
tags:
  - "정규표현식"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">정규표현식 숫자 소수둘째자리까지 적용하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    input태그에 소수점 둘째자리까지만 받고 싶었다. input number 타입을 쓰고 step=”0.01”을 쓰는 방법도 있지만 input타입을 text로 써야하는 상황이라 그냥 정규식을 사용했다.</p>
</div>

<!-- more -->

input태그에 소수점 둘째자리까지만 받고 싶었다. input number 타입을 쓰고 step=”0.01”을 쓰는 방법도 있지만 input타입을 text로 써야하는 상황이라 그냥 정규식을 사용했다.

# 숫자 소수점 둘째짜리만 입력허용하는 경우

```html
<input type="text" id="price" val="0" />
```

```js
$("#price").keyup(function(){
	let price = $(this).val();
	const regex = /(^/d+$)|(^d{1,}.\d{0,2}$)/g;
	let resultPrice = price.replace(regex, "");
	$(this).val(resultPrice);
});
```

  
  
  

# 숫자입력만 허용하는 경우

```html
<input type="text" id="price" val="0" />
```

```js
$("#price").keyup(function(){
	let price = $(this).val();
	const regex = /[^0-9]/g;
	let resultPrice = price.replace(regex, "");
	$(this).val(resultPrice);
});
```

이렇게 처리한다면 input태그에 숫자가 아닌 문자는 입력이 아예 안된다!

#[정규표현식](/tags/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D/)
