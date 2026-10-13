---
title: "[리액트] 반복문map, import와 require차이, 자잘한 팁"
date: 2021-03-29 17:02:15
tags: []
categories:
  - Frontend
  - React
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'반복문map, import와 require차이, 자잘한 팁'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    동작 원리와 장단점을 비교 파악하여 프로젝트 개발 상황에 적합한 방식을 선택할 수 있다.</p>
</div>

<!-- more -->

리액트의 자잘한 팁을 정리해보았다.

## 자잘한 팁

  * state에 객체 구조를 안쓰는 것이 좋다
  * render안에는 절대 setState()를 쓰지않는다 → setState()되면 랜더링이 실행되기때문에 랜더링이 실행되면 또 setState()가 실행되고 이 부분이 무한 반복되기때문.
  * 부모한테서 받은 props를 바꾸고싶을때는 useState()를 이용하여 state로 만들고 그 state를 바꿔준다 → 자식이 props를 바꾸면 부모 props도 바뀌기때문.
  * Props는 상속이다. Props를 보면 항상 그 부모 컴포넌트를 생각해야한다. 그 부모 컴토넌트의 조상 컴포넌트가 있을 수 있다.

  
  
  

## 리액트 용어정리

용어 | 설명  
---|---  
리액트 redux | 리액트의 컴포넌트가 많아지면 컴포넌트간의 교류가 빈번해진다. 중앙에 데이터 저장소를 만들고 그 저장소의 데이터가 변경되면 관련된 모든 컴포넌트에 영향을 미친다.  
리액트 server side rendering | 서버쪽에서 웹페이지를 완성한 후에 클라이언트로 완성된 html 전송하는 걸로 애플리케이션 구동가능 → 초기구동시간 단축가능 + 로딩필요없는 애플리케이션 가능 + 검색엔진로봇이 웹페이지 분석가능  
리액트 native | 하나의 코드로 거의 모든 플랫폼에서 동작하는 애플리케이션을 만들 수 있다.  
  
  
  
  

## 리액트의 반복문

  * 리액트의 반복문은 map을 사용할 것  
배열을 1대1로 짝짓는 것이 map이다.  
map은 입력과 출력의 값이 동일해야한다 → 배열의 요소를 지우고 싶다면 filter를 써야한다.

  
  
  

## import와 require차이

외부라이브러리를 불러오는 방법은 2가지가 있다.  
외부라이브러리인 MomentJS를 불러온다고 가정해보자.

```js
//1번방법
//노드의 문법으로 require써야한다.
const moment = require("moment")

//2번방법
//바벨이 import 쓴 부분을 자동으로 require로 바꿔주기때문에 require와 import 리액트에서는 둘 다 쓸 수 있다
import moment from "moment"
```

require 방법 | import 방법  
---|---  
NodeJS에서 사용되고 있는 CommonJS 키워드 | ES6(ES2015)에서 새롭게 도입된 키워드  
복수객체내보내기: `exports.객체명 = 객체명` | 복수객체내보내기: `export { 객체명 }`  
단일객체내보내기: `module.exports = 객체명` | 단일객체내보내기: `export default`키워드사용  
[자바스크립트 CommonJS 모듈 내보내기/불러오기 (require) 예시](https://www.daleseo.com/js-module-require/) | [자바스크립트 ES6 모듈 내보내기/불러오기 (import) 예시](https://www.daleseo.com/js-module-import/)  
  
두 방법 중 실무에서 더 많이 사용하는 방법은 import 방법이다.  
아무래도 ES6 모듈 시스템이 좀 더 최신이므로 CommonJS 방식 대비 여러 강점이 있다.

  * CommonJS 대비 ES6모듈 시스템의 강점
    * 모듈관리 전용 키워드 사용(import,from,export,default)하여 코드 가독성 높음
    * 비동기방식으로 성능과 메모리부분이 유리
    * Named Parameter기능지원

  
  
  

## 참고

  * [제로초 리액트 무료강좌(웹게임)](https://youtube.com/playlist?list=PLcqDmjxt30RtqbStQqk-eYMK8N-1SYIFn)
  * [제로초 ES2015(ES6) 모듈 시스템](https://www.zerocho.com/category/ECMAScript/post/579dca4054bae71500727ab9)
