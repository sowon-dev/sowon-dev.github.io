---
title: "ECMAScript"
date: 2022-04-18 02:49:53
tags:
  - "오늘또못알아듣고말았습니다"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">ECMAScript의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    요구사항을 구현하면서 Promise를 사용했는데 IE는 해당 기능을 지원하지 않아서 제대로 작동하지 않았던 것이다.</p>
</div>

<!-- more -->

오늘 고객사로부터 사이트의 달력이 제대로 작동되지 않는다는 연락을 받았다. 내 머신에서는 잘만 되는데 왜그럴까? 유심히 찾아보고있는데 팀장님께서 호환성 문제라고 말씀해주셨다.  
요구사항을 구현하면서 Promise를 사용했는데 IE는 해당 기능을 지원하지 않아서 제대로 작동하지 않았던 것이다.

이번 프로젝트에서는 IE는 지원하지 않기로 이미 협의했는데 고객사 담당자가 모르고 있었던 것! 이번 기회에 팀장님이 ES6에 대해 설명해주셨는데 더 궁금해서 찾아봤다.

## ES6

ES6이란 ECMAScript 2015 의 약어로 ES2015라고도 불린다.  
European Computer Manufacturer’s Association(이하 ECMA)에서 js와 Node.js의 기초가 되는 범용 프로그래밍 언어인 ECMAScript를 제정한다. 즉, 스크립트 언어[(링크)](https://sowon-dev.github.io/2020/05/27/200528javai/#스크립트언어)가 어떻게 생겨야 하는 지에 관한 기준이다.

  * 대표적인 ES6문법
    1. const변수와 let변수
    2. 화살표 함수
    3. 템플릿 리터럴:백틱을 사용해 문자열 내 변수 사용가능

```js
// 화살표함수와 템플릿 리터럴 예시
const myIntro = (name, mobile) => {
 return `안녕하세요. 이름은 ${name}이고 제 연락처는 ${mobile}입니다.`
}
```

    4. 프로미스(Promise)
    5. 객체 비구조화: 배열 또는 객체의 값을 새 변수에 쉽게 할당 가능

```js
// 객체 비구조화 예시
let {name, mobile} = user;
```

  
  
  

## JavaScript와 ECMAScript 관계

실상 두 용어는 혼용되곤 한다.  
왜냐하면 JavaScript는 1996년에 만들어졌고 이를 표준화하기 위해 ECMAScript가 1997년에 만들어졌다. 그 후 ECMAScript를 준수하면서 JavaScript가 발전해왔다.  
즉 서로가 서로를 바라보고 있는 셈이다.

  
  
  

## 배운점

사실 어떤 기능을 사용하건 다양한 브라우저의 호환성 문제를 항상 먼저 확인해야한다.  
크롬브라우저에서 된다고 모든 브라우저에서 다 되는 게 아니니까! 따라서 프로젝트기획때부터 어떤 브라우저 버전까지 지원할지를 명확히 하는 습관이 필요하다!  
난중에 시니어가 된 후 프로젝트 계약시 꼭 호환성 문제를 특약으로 명시해야겠다.

그나저나 만약 호환성문제가 있다면 사용했던 ES6기능을 눈물을 머금고 싹 다 걷어내야하는걸까??  
NOPE!  
세상에는 천재들이 많고 그 천재들이 이미 호환성 문제를 해결해주는 라이브러리들을 만들어놨기때문이다.  
예를 들어 IE에서 Promise를 사용하고 싶은 경우 bluebirdjs[(링크)](http://bluebirdjs.com/docs/getting-started.html)라는 라이브러리를 사용하면 된다.

  
  
  

## 참고

  * <https://en.wikipedia.org/wiki/ECMAScript>
  * <https://www.educative.io/edpresso/what-is-ecmascript>
  * <https://wormwlrm.github.io/2018/10/03/What-is-the-difference-between-javascript-and-ecmascript.html>
  * <https://www.freecodecamp.org/news/write-less-do-more-with-javascript-es6-5fd4a8e50ee2/>

#[오늘또못알아듣고말았습니다](/tags/%EC%98%A4%EB%8A%98%EB%98%90%EB%AA%BB%EC%95%8C%EC%95%84%EB%93%A3%EA%B3%A0%EB%A7%90%EC%95%98%EC%8A%B5%EB%8B%88%EB%8B%A4/)
