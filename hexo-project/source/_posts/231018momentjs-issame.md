---
title: "[Moment.js] isSame 오늘날짜와 비교가 안되는 이유"
date: 2023-10-17 22:05:03
tags:
  - "Moment.js"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'isSame 오늘날짜와 비교가 안되는 이유'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    동작 원리와 장단점을 비교 파악하여 프로젝트 개발 상황에 적합한 방식을 선택할 수 있다.</p>
</div>

<!-- more -->

달력을 만들면서 오늘날짜와 일치하는 셀에는 음영을 넣고 싶었다.  
여기서 잠깐🤚  
모먼트js로 달력을 만들고싶다면 [포스팅:: 동적 달력(캘린더)만들기](https://sowon-dev.github.io/2022/08/30/220831js-calendar/)을 참조하면 된다.

# 기존코드

이번달 1일부터 for문을 돌면서 현재 날짜와 일치하면 class today를 추가해주는 코드를 구현했다. 

```js
const today = moment();
const firstDayOfMonth = moment({today.year(), today.month() + 1}).startOf('month');
let currentDate = firstDayOfMonth.clone().startOf('week'); //달력의 현재 셀 날짜

for (let i = 0; i < 7; i++) {
  let cell = $("<td></td>");
  
  // 오늘일자인 경우 class 추가하기
  if(currentDate.isSame(today){
    cell.addClass("today");
  }
  
  tableRow.append(cell);
  currentDate.add(1, 'days');
}
```

  
  
  

# 해결코드

isSame은 연월일뿐만 아니라 시분초도 같이 확인한 후 같은지 아닌지 판단한다.  
따라서 포맷도 `YYYY-MM-DD`로 맞춰주면서 시분초를 00으로 바꿔주는 `startOf('day')`를 사용하면 해결된다.

```js
// 오늘일자인 경우 class 추가하기
if(moment(currentDate.startOf('day'), "YYYY-MM-DD").isSame(moment(today.startOf('day'), "YYYY-MM-DD"))){
  cell.addClass("today");
}
```

#[Moment.js](/tags/Moment-js/)
