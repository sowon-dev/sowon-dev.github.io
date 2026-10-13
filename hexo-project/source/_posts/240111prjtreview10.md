---
title: "예약, 대관, 대여프로그램 프로젝트를 끝내며 내가 배운 것"
date: 2024-01-10 15:13:12
tags:
  - "회고록"
categories:
  - Reflections
  - 회고록
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'예약, 대관, 대여프로그램 프로젝트를 끝내며 내가 배운 것'에 참여하고 주요 발표 내용과 배운 점을 정리한 글이다.
    이번 플젝은 시간이 촉박한데 해야할 작업들은 방대해서 시간분배가 중요했다.</p>
</div>

<!-- more -->

이번 프로젝트에서는 예약, 대관, 대여프로그램을 주 업무로 맡았다.

프로젝트마다 예약,대관,대여등을 도맡으면서 일정과 관련된 DB설계와 달력표현부분은 이제 익숙해졌다.  
또한 동적 테이블도 편한게 만들 수 있게 되었다.  
이번에는 처음으로 JsRender를 활용했는데 template을 활용한 데이터바인딩이 너무 편해서 좋았다.  
이번 플젝은 시간이 촉박한데 해야할 작업들은 방대해서 시간분배가 중요했다.  
집중해서 자잘한 업무를 빨리 쳐내고 큰 작업을 진득하게 구현하기 위해 노력했는데 결론적으로 잘 되서 다행이다.

# keep

현재 만족하고 있는 부분과 계속해서 이어갔으면 하는 부분

  1. `대관,대여,예약 기능 구현시 moment.js 활용`
     * 대관,예약 기능 구현시 moment.js 활용하여 날짜와 시간을 효과적으로 다뤘고 달력은 현재 프레임워크 내 경량라이브러리로 적합한 JsRender를 선택하여 코드 반복을 최소화하고 효율적으로 작성했다. JsRender를 이번에 처음 써봤는데 데이터바인딩이 너무 편해서 앞으로도 달력만들때 쭉 쓰고싶다. 다만 JsRender가 업데이트가 활발하게 되고있지않아 jsp말고 Vue.js, React, Angular와 같은 라이브러리 및 프레임워크를 다루고싶다.
  2. `jQuery 비중을 줄이고 바닐라JS 사용`
     * 속도향상을 위해 jQuery 사용을 줄이고 바닐라JS를 일부러 사용했다. 바닐라JS는 제이쿼리보다 코드는 길어지지만 제이쿼리API를 다녀오지않아도 되기에 속도가 빠르다. 이미 손에 익어버린 jQuery를 의식적으로 바닐라JS를 사용하려니 중간중간에 코드 검색이 필요해서 처음에는 시간이 걸렸지만 프로젝트 후반에 갈수록 코딩속도가 붙었다. 앞으로도 바닐라JS를 의식적으로 사용해야겠다. 
  3. `Mybatis에서 resultMap 사용`
     * Mybatis에서 객체안에 객체를 매핑하기 위해 resultMap를 사용하여 유연한 맵핑이 가능하도록 구현했으며 코드재사용과 유지보수와 디버깅이 편하도록 작성했다. 사실 resultMap이 익숙하지 않아서 resultType에 dto 맞춰서 사용할까하다가 resultMap도 익숙해질수있도록 실무에 써보자!라고 판단했고 결과적으로 resultMap을 실무에서 한 번 써보고나니 자신감이 생겼고 다음에도 언제든지 사용할 수 있게 되었다.
  4. `observer`
     * 동적 웹페이지에서 비동기적인 DOM조작을 잡기 위해서 Mutation Observer를 이용했다. 이를 위해 페이지라이프사이클을 추가로 공부했다. DOM에 대해서 더 공부가 필요하다.
  5. `외부API연동을 위한 RestTemplate 활용`
     * 지난 프로젝트에서 진득하게 공부했던 RestTemplate을 활용하여 쉽게 외부API인 문자전송 서비스를 구현했다.

  
  
  

# Problem

개선이 필요하다고 생각되는 부분

  1. `네트워크 지식`
  2. `통합예약 설계에 겁먹은 점`
  3. `DOM`

  
  
  

# Try

Problem의 해결책이 될 수 있는 부분

  1. 네트워크 공부를 하면서 겸사겸사 네트워크 관리사2급과 리눅스마스터 자격증을 취득할 것이다. 
     * ONE ACTION: 24년 제01회 필기 2024-02-25, 실기 2024-03-31 최종 합격발표 2024-04-09
  2. 설계는 경험이 제일 중요하다고 생각하는데 경험이 없기에 지레 겁먹고있다. 경험을 늘리는 방법을 고민해봤는데 사이드프로젝트와 책이라고 생각한다. 따라서 올해 데이터베이스 설계 책 상반기에 1권을 읽고 후기글을 작성해야겠다. 하반기는 [파워오브데이터베이스](https://www.yes24.com/Product/Goods/69775589), [가장 쉬운 데이터베이스 설계 책](https://www.yes24.com/Product/goods/12191214?art_bl=7769257) 중 고민해보고 읽을 것
     * ONE ACTION: 그림으로 공부하는 TCP/IP구조 
  3. DOM 문서객체모델 포스팅 1건이상 하기
     * ONE ACTION: [What, exactly, is the DOM?](https://bitsofco.de/what-exactly-is-the-dom/) 번역 포스팅, [DOM tree](https://javascript.info/dom-nodes) 번역 포스팅

  
  
  

# 관련 포스팅

  * [분명 success인데 왜 계속 error로 가는걸까?](https://sowon-dev.github.io/2023/09/10/230911ajax-sucess-error/)
  * [IMG태그 기본이미지설정(DEFAULT IMG, ONERROR속성) 에러 해결](https://sowon-dev.github.io/2023/10/15/231016imgtag-onerrer/)
  * [isSame 오늘날짜와 비교가 안되는 이유](https://sowon-dev.github.io/2023/10/17/231018momentjs-issame/)
  * [moment String을 Controller에서 LocalDateTime으로 받기](https://sowon-dev.github.io/2023/10/18/231019momentjs-to-localdatetime/)
  * [URL 파라미터(쿼리파라미터Query Parameter)가져오기](https://sowon-dev.github.io/2023/10/19/231020URLsearchparams/)
  * [mybatis update시 모두 if test를 써야 할 경우](https://sowon-dev.github.io/2023/11/14/231114mybatis-if-update-all/)
  * [mybatis 객체 안에 객체 매핑하기](https://sowon-dev.github.io/2023/11/14/231114mybatis-resultMap-manyassociation/)
  * [radio/checkbox 클릭 안 되는 오류가 label for 때문이라고?](https://sowon-dev.github.io/2023/11/14/231115lable-for/)
  * [observer 사용하기](https://sowon-dev.github.io/2023/11/20/231121js-observer/)
  * [글씨쓸때마다 바이트 계산하기](https://sowon-dev.github.io/2024/01/01/240102byte-check/)
  * [URL 파라미터(쿼리파라미터Query Parameter)가져오기(ft.EL표현식)](https://sowon-dev.github.io/2024/01/07/240108jsp-el-queryparam/)
  * [DOMContentLoaded와 window.onload차이(ft.페이지 라이프사이클Page Lifecycle)](https://sowon-dev.github.io/2024/01/08/240109domcontentloaded-vs-onload/)

#[회고록](/tags/%ED%9A%8C%EA%B3%A0%EB%A1%9D/)
