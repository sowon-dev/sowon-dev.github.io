---
title: "[리액트] Hooks API로 생명주기 관리"
date: 2021-03-23 15:00:00
tags: []
categories:
  - Frontend
  - React
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Hooks API로 생명주기 관리의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    즉, 리액트 Hooks란 함수형 컴포넌트에서 생명주기 관리를 도와주는 기능이다.</p>
</div>

<!-- more -->

## Hooks 컴포넌트 상태관리 함수

리액트에는 클래스형 컴포넌트와 함수형 컴포넌트가 있다. 클래스 컴포넌트는 state를 가지고 다니는 반면에 함수형 컴포넌트는 그렇지않다.  
리액트 Hooks를 통해 함수형 컴포넌트에서 상태관리를 할 수 있게 되었다.  
즉, 리액트 Hooks란 함수형 컴포넌트에서 생명주기 관리를 도와주는 기능이다.

  
  
  

## [기본적인 Hooks](https://ko.reactjs.org/docs/hooks-reference.html#basic-hooks)

useState | useEffect | useContext  
---|---|---  
컴포넌트 상태 관리 | 컴포넌트가 렌더링될 때마다 어떠한 작업을 수행하도록 개입 | 컴포넌트 간의 전역 상태를 관리  
- | 클래스형컴포넌트의 componentDidMout+componentDidUpdate기능을 합친 형태 | -  
  
![https://velog.io/@gwak2837/React-Hooks%EC%9D%98-%EC%9D%B4%ED%95%B4](https://media.vlpt.us/images/gwak2837/post/491f1b4b-1a5c-4140-89c6-2d61cce066fc/image.png)

  
  
  

## [추가 Hooks](https://ko.reactjs.org/docs/hooks-reference.html#additional-hooks)

### useReducer

  * state갯수를 줄여주는 역할
  * 테이블구조에서 Td 넘겨줄 데이터가 많기 때문에 useReducer를 이용하여 한번에 넘겨줄 수 있다.
  * state변경시 불변성이 중요하기때문에 얕은 복사를 사용한다.

```js
const initialState = {
  winner: "",
  turn: "O",
  tableData: [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
  ],
  recentCell: [-1, -1], //초기화는 없는 칸으로 설정
};

const TictactoeHooks = () => {
  const [state, dispatch] = useReducer(reducer, initialState);
}
```

  
  

### useRef

  * 일반 값을 기억
  * 값이 바뀌어도 랜더링하고 싶지않은 값들은 useRef 넣어서 사용한다. -> 성능 최적화.
  * 값이 바뀌기는 하지만 화면에 영향을 미치지않을때 useRef 사용
  * useRef를 사용하면 변한 값이 저장은 되지만 랜더링 되지않는다 → useRef뒤에 setState()로 호출하는 순간 랜더링이 된다.

  
  

### useMemo

  * 복잡한 함수 결과값(리턴값)을 기억

  
  

### useCallback

  * 함수 자체를 기억
  * 함수 생성 자체가 비용이 클때 사용
  * 함수 자체를 기억하기때문에 변경값이 있는 경우에 인지하지 못한다. 따라서 [] input에 변경되는 state를 넣어줘야 정상적으로 변경값을 인지한다.

  
  
  

## useEffect 과 useLayoutEffect 차이

둘의 가장 중요한 차이는 실행시점이다.

useEffect | useLayoutEffect  
---|---  
컴포넌트 렌더링 → 화면 업데이트 → useEffect실행 | 컴포넌트 렌더링 → useLayoutEffect 실행 → 화면 업데이트  
화면resize등 화면이 완전히 바뀌고 난 후에 실행 | 화면resize등 전에 실행  
비동기적으로 실행됨 | 동기적으로 실행됨  
| 렌더링 직후 DOM요소의 값을 읽을 때 유용함(scroll position등)  
DOM과 인터렉션이 없는 경우에 사용(대부분 경우) | DOM을 mutate할 경우에 사용 but 실무에서 사용할 경우가 드물다  
  
  
  
  

## 참고

  * [리액트, 제대로 알고 개발하기 pt.2 ( Hooks는 쓰레기? )](https://velog.io/@snowman39/%EB%A6%AC%EC%95%A1%ED%8A%B8-%EC%A0%9C%EB%8C%80%EB%A1%9C-%EC%95%8C%EA%B3%A0-%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B8%B0-pt.2-Hooks%EB%8A%94-%EC%93%B0%EB%A0%88%EA%B8%B0)
  * [제로초 리액트 무료강좌(웹게임)](https://youtube.com/playlist?list=PLcqDmjxt30RtqbStQqk-eYMK8N-1SYIFn)
