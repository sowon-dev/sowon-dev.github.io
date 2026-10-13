---
title: "[리액트] reducer, action, dispatch의 관계"
date: 2021-03-29 18:00:26
tags: []
categories:
  - Frontend
  - React
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">reducer, action, dispatch의 관계의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * action은 기본적으로 대문자+스네이크표기법 사용을 적용할 수 있다.</p>
</div>

<!-- more -->

리액트는 기본적으로 하나의 루트 컴포넌트(보통 App.js)에서 상태를 관리한다.  
리액트의 컴포넌트가 많아지면 컴포넌트간의 교류가 빈번해진다. 중앙에 데이터 저장소를 만들고 관리하면 더 편하다. 그것이 바로 Redux이다.  
리덕스의 데이터가 변경되면 관련된 모든 컴포넌트에 영향을 미친다.

## reducer, action, dispatch의 관계

  * state안에 데이터가 있다면 → 직접 수정 불가능
  * 수정하고 싶으면 action을 만들어서 수정해야함
  * action을 만든 후 dispatch에 하면 state 수정가능
    * action은 기본적으로 대문자+스네이크표기법 사용
  * reducer : state를 어떻게 바꾸는 지를 switch 문을 사용하여 적으면 됨

![제로초 리액트 무료강좌\(웹게임\)](/img/210330redux.PNG)

  
  
  

## Dispatch 방법

  1. props 사용
     * 단점 : 부모-자식 컴포넌트 구조에서는 계속 dispatch를 넘겨줘야하므로 번거롭다.
     * 즉, List → Table → Tr → Td 구조에서 Td에서 dispatch를 사용하고 싶다면 불필요하게 Table, Tr에도 dispatch를 넘겨줘야한다.

```jsx
//List에서 Td로 바로 dispatch넘겨줄수가 없으므로 Table로 넘겨주기
<Table dispatch={dispatch} />

//Table에서 Tr로 넘겨주기
<Tr dispatch={dispatch} />

//Tr에서 Td로 넘겨주고 
<Td dispatch={dispatch} />

//Td에서 dispatch 사용하기
const onClickForm = useCallback(() => {
	dispatch({ type: CLICK_CELL, row: rowIndex, cell: cellIndex });
  }, []);
```

  2. context API사용

```jsx
//초기값
export const TableContext = createContext({
  tableData: [],
  halted: true,
  dispatch: () => {},
});

const Minesweeper = () => {
  const [state, dispatch] = useReducer(reducer, initialState);
  const value = useMemo(() => ({ tableData: state.tableData, dispatch }), [
	state.tableData,
  ]);
  return (
	// 자식컴포넌트들이 tableData와 dispatch에 접근 가능
	<TableContext.Provider value={value}>
	  <Form />
	  <div>{timer}</div>
	  <Table />
	  <div>{result}</div>
	</TableContext.Provider>
  );
};

// 자식 컴포넌트에서 사용하는 법
const onClickBtn = userCallback(() => {
	dispatch({ type: START_GAME, row, cell, mine });
  }, [row, cell, mine]);
```

  
  
  

## 참고

  * [제로초 리액트 무료강좌(웹게임)](https://youtube.com/playlist?list=PLcqDmjxt30RtqbStQqk-eYMK8N-1SYIFn)
  * [리덕스(Redux)를 왜 쓸까? 그리고 리덕스를 편하게 사용하기 위한 발악 (i)](https://velopert.com/3528)
