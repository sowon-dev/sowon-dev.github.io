---
title: "클로저(Closure)란"
date: 2022-01-05 05:44:34
tags:
  - "Node.js"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">클로저(Closure)란의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    핵심 설정과 구현 코드를 단계별로 파악하여 상황에 맞게 유연하게 활용할 수 있다.</p>
</div>

<!-- more -->

탄탄한 자바스크립트 기본기를 다지기 위해 클로저에 대해 알아보자.

## Closure

closure = function + environment  
클로저는 외부 변수를 기억하고 이 외부 변수에 접근할 수 있는 함수를 의미한다.  
함수(function)가 하나 생길때마다 클로저는 하나씩 생성된다.  
일반적으로 외부 함수의 실행이 끝나면 외부 함수가 소멸된다. 하지만 클로저는 외부 함수가 소멸된 이후에도 내부 함수가 외부함수의 변수에 접근할 수 있는 구조이다.

아래 문제를 풀어보자

```js
function 이름부르기() {
  let name = "나혜석";

  return function() {
    alert(name);
  };
}

let name = "권기옥";

// create a function
let 인사 = 이름부르기();

// 나혜석과 권기옥 중 누구의 이름이 불리게 될까?
인사();
```

여기서 정답은 바로 `나혜석`이다.  
만약 이름부르기함수에서 `let name = "나혜석";`이 없었다면 alert창은 `권기옥`으로 나올 것이다.

어떻게 이게 가능한걸까?  
바로 자바스크립트의 함수는 숨겨진 프로퍼티인 [[Environment]]를 이용해 자신이 어디서 만들어졌는지를 기억하기 때문이다.

  
  
  

## 참고

  * <https://ko.javascript.info/closure>
  * <https://edu.goorm.io/learn/lecture/557/%ED%95%9C-%EB%88%88%EC%97%90-%EB%81%9D%EB%82%B4%EB%8A%94-node-js/lesson/21731/%ED%81%B4%EB%A1%9C%EC%A0%80>

#[Node.js](/tags/Node-js/)
