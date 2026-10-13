---
title: "[JS]Web Storage vs 쿠키(Cookie) vs 세션(Session) vs 캐시(Cache)"
date: 2022-11-21 04:27:19
tags: []
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">브라우저 저장소인 localStorage와 sessionStorage는 문자열 기반의 Key-Value 데이터를 클라이언트에 저장하며 CSRF로부터 안전하다.
    반면 쿠키는 요청마다 서버로 자동 전송되고 세션은 서버 메모리를 소비하므로 데이터 영구성과 목적에 맞게 분리해 활용해야 한다.</p>
</div>

<!-- more -->

레거시프로젝트의 소스코드를 분석하다가 Web Storage를 만났다.  
localStorage와 sessionStorage를 둘 다 사용하고 있었기에 둘 차이가 궁금해졌다.

구글링할수도록 쿠키, 세션, 캐시까지 다양한 개념이 나오길래 이참에 다 정리해봤다.

# Web Storage

  * 클라이언트에 저장
  * Key-Value 형태
  * 쿠키와 달리 서버에 전송안함
  * CSRF로부터 안전 why? Origin단위로 접근이 제한되기때문에.
  * 쿠키(4GB)보다 큰 저장용량(5GB)지원
  * 문자형(String) 데이터 타입만 지원
  * 종류
    * localStorage: 사용자가 데이터를 지우지 않는 이상, 브라우저나 OS를 종료해도 계속 브라우저에 남아있음 (영구성) 단, 동일한 브라우저를 사용할 때만 해당
    * sessionStorage: 브라우저 탭에도 종속되기 때문에, 윈도우나 브라우저 탭을 닫을 경우 제거

  
  
  

## Origin 오리진이란?

오리진 = 프로토콜 + 도메인 + 포트

  
  
  

# 비교

| | localStorage | sessionStorage | Cookie | Session  
---|---|---|---|---  
저장위치 | 클라이언트 | 클라이언트 | 클라이언트 | 서버  
저장형식 | String | String | String | Obejct  
전송 | 서버전송x   
-> 서버 부담없음 | 서버전송x   
-> 서버 부담없음 | 매번 서버에 자동 전송   
-> 크기가 크면 서버에 부담 | 서버에서 클라이언트를 구분하기 위해 세션 ID를 부여   
-> 사용자가 많아질수록 서버 메모리를 많이 차지  
유효기간 설정 | 불가능 | 불가능 | 가능 | 가능(기본 30분)  
데이터영구성 | 브라우저 종료해도 유지   
명시적 삭제 필요 | 윈도우나 브라우저 탭을 닫을 경우 삭제됨 | 쿠키 저장시 설정(설정 없을 시에는 브라우저 종료시 만료) | 브라우저 종료 시 만료기간에 상관없이 삭제됨  
생성단위 | Origin별로 생성  
다른 오리진의 로컬 스토리지에는 접근 불가  
서로 다른 브라우저 탭이라도 동일한 오리진이라면 동일한 로컬 스토리지를 사용함  
| Origin별마다 탭/윈도우 단위로 생성->탭/윈도우를 닫을 시 데이터가 삭제됨 | 브라우저에 여러개 생성가능 | 브라우저당 하나의 세션SessionID이 생성  
주 사용처 | 지속적으로 필요한 정보를 저장할때  
e.g.자동 로그인 등 | 잠시 동안 필요한 정보를 저장할 때  
e.g.입력 폼 저장, 일회성 로그인 등 | 로그인유지, 자동완성, 일주일간 다시 보지 않기, 최근 검색한 상품들을 광고에서 추천, 쇼핑몰 장바구니 기능 | 로그인유지  
  
  
  
  

# 캐시(Cache)는 또 뭘까?

쿠키와 세션을 이야기하다보면 자연스럽게 캐시가 나온다.  
어떤 차이가 있을까?

  * 캐시: 웹 페이지 요소(e.g.img,css,js등 리소스파일)를 저장하기 위한 임시 저장소 for 빠른 웹페이지 랜더링
  * 쿠키,세션: 정보 저장소 for 사용자인증

  
  
  

# 참고

  * <https://developer.mozilla.org/ko/docs/Web/API/Window/sessionStorage>
  * [IT엘도라도 - 쿠키, 웹 스토리지(로컬 스토리지, 세션 스토리지)](https://it-eldorado.tistory.com/90)
  * [푸고배님 - 쿠키 vs 세션 vs 웹 스토리지(로컬 스토리지, 세션 스토리지)](https://doqtqu.tistory.com/m/306)
  * <https://sowon-dev.github.io/2020/06/30/200701jspi/>
