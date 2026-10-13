---
title: "[리액트]컴포넌트 생명주기"
date: 2021-03-22 15:00:00
tags: []
categories:
  - Frontend
  - React
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">컴포넌트 생명주기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    핵심 설정과 구현 코드를 단계별로 파악하여 상황에 맞게 유연하게 활용할 수 있다.</p>
</div>

<!-- more -->

컴포넌트 라이프 사이클 순서는 아래와 같다.

## 컴포넌트 라이프 사이클 순서

  * constructor → componentWillMount → render → ref → componentDidMount
  * componentWillMount 는 실무에서 잘 쓰지않는다.’
  * 위의 순서 끝난 뒤 setState/props 바뀌는 경우 → shouldComponentUpdate(true) → render → componentDidUpdate
  * 부모컴포넌트가 나를 없앤 경우 → componentWillUnmount → 소멸

![https://gseok.gitbooks.io/react/content/bd80-bd84-bd80-bd84-c9c0-c2dd-b4e4/react-component-lifecycle-api-c815-b9ac.html](https://gseok.gitbooks.io/react/content/assets/react-life-cycle-2.png)

  
  
  

## component함수

![https://www.zerocho.com/category/React/post/579b5ec26958781500ed9955](https://cdn.filestackcontent.com/ApNH7030SAG1wAycdj3H)

  * `componentDidMount()` : render가 `처음` 성공적으로 실행된 후 바로 `componentDidMount()` 가 실행된다. 리랜더링일땐 실행되지 않는다.
    * 비동기 요청
    * eX) setInterval()
  * `componentDidUpdate()` : 리랜더링된 후 실행.
  * `componentWillUnmount()`: 컴포넌트가 제거되지 직전 비동기요청을 `componentWillUnmount()` 로 할 수 있다.
    * 비동기 요청 정리
    * 완료되지않은 비동기요청을 여기서 정리해줘야함.

```js
//class버전

interval;

  componentDidMount() { // 컴포넌트가 첫 렌더링된 후, 여기에 비동기 요청을 많이 해요
    this.interval = setInterval(this.changeHand, 100);
  }

  componentWillUnmount() { // 컴포넌트가 제거되기 직전, 비동기 요청 정리를 많이 해요
    clearInterval(this.interval); // 완료되지않은 비동기요청을 여기서 정리해줘야한다
  }

//Hooks버전
const interval = useRef();

  //useEffect는 componentDidMount, componentDidUpdate, componentWillUnmount에 대해 1대1대응은 아니지만 셋의 역할을 하나로 합쳤다고 할수있다.
  //componentDidMount, componentDidUpdate역할
  useEffect(() => {
    interval.current = setInterval(changeHand, 100); //0.1초
    return () => {
      //componentWillUnmount역할
      clearInterval(interval.current);
    };
  }, [imgCoord]); //빈 배열이면 componentDidMount역할만 수행
//배열에 다시 실행 할 값을 넣어주면componentDidMount + componentDidUpdate역할

//Hooks버전에서 componentDidMount만 사용하고 싶다면?
useEffect(() => {
    //ajax
  }, []); //빈배열로 놔두기

//Hooks버전에서 componentDidMount 말고 componentDidUpdate만 사용하고 싶다면?
const mounted = useRef(fasle);
  useEffect(() => {
    if (!mounted.current) {
      mounted.current = true;
    } else {
      //ajax 처리
    }
  }, []); //배열에는 바뀌는 값입력
```

  
  
  

## 참고

  * [제로초 리액트 무료강좌(웹게임)](https://youtube.com/playlist?list=PLcqDmjxt30RtqbStQqk-eYMK8N-1SYIFn)
