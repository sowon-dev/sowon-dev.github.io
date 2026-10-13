---
title: "[리액트] state나 props 변경시 성능향상 방법"
date: 2021-03-23 15:00:00
tags: []
categories:
  - Frontend
  - React
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">state나 props 변경시 성능향상 방법의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    이게 쌓이면 성능이 저하된다. 이를 해결하는 방법을 알아보자.</p>
</div>

<!-- more -->

## React어플리케이션 성능향상 방법

React에서 state나 props가 변경되었을때 render가 진행되는데 값이 없는 setState() 호출에도 rendering이 된다.  
이게 쌓이면 성능이 저하된다. 이를 해결하는 방법을 알아보자.

  
  
  

### class인 경우

state나 props가 변경되었을때 성능을 위해 shouldComponentUpdate(){} 또는 PureComponent를 쓸 수 있다.  
PureComponent란 shouldComponentUpdate()를 구현해놓은 컴포넌트이다.  
shouldComponentUpdate()는 배열이나 객체에 변경이 있는 경우 변경사항을 인지하지 못할 수 도 있다. → 새로운 배열을 만들고 싶다면 `[...기존arr, 1]` 복사해서 사용해야한다.  
따라서 shouldComponentUpdate()보다는 PureComponent 를 쓰는 것이 좋다.

```js
shouldComponentUpdate(prevProps, prevState) {
    return this.props.data !== prevProps.data;
  }

//더 편하게
import React, { PureComponent } from 'react';
```

  
  
  

### Hooks인 경우

PureComponent와 shouldComponentUpdate가 없다. 그대신 memo(memoization의 약자)를 사용한다.  
훅스할때는 state들을 최상위로 빼야한다. 그렇지 않고 if조건문에 state를 넣으면 에러가 발생한다.

```js
//함수 컴포넌트. 이건 그냥 함수 컴포넌트
import React, { memo } from "react";

const Ball = memo(({ number }) => {
  let background;
  if (number <= 10) {
    background = "red";
  } else {
    background = "green";
  }
}

//Hooks :  useRef, useState, useCallback등을 사용하고 함수 컴포넌트인 것
import React, { useRef, useState, useCallback } from "react"; 
const Ball = memo(({ number }) => {
  let background;
  if (number <= 10) {
    background = "red";
  } else {
    background = "green";
  }
}
```
