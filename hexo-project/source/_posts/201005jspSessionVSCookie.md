---
title: "세션(Session)와 쿠키(Cookie)의 차이 그리고 캐시(Cache)"
date: 2020-10-04 15:02:53
tags:
  - "차이"
categories:
  - Backend
  - CS
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'세션(Session)와 쿠키(Cookie)의 차이 그리고 캐시(Cache)'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    동작 원리와 장단점을 비교 파악하여 프로젝트 개발 상황에 적합한 방식을 선택할 수 있다.</p>
</div>

<!-- more -->

## 세션 vs 쿠키

  * 공통점 : 데이터 저장
  * 차이점 
    * [세션](https://sowon-dev.github.io/2020/06/28/200629jspi/) : 정보를 서버에 저장
      * 서버가 종료되면 사라짐
      * 브라우저별로 하나씩 생성
      * 정확한 데이터를 사용
    * [쿠키](https://sowon-dev.github.io/2020/06/30/200701jspi/) : 정보를 클라이언트에 저장(사용자PC의 하드디스크에 저장)
      * 서버가 종료되면 안 살아짐
      * 쿠기 사용기간이후 사라짐
      * 쿠기 삭제할 수 있음
      * 사용자의 PC가 바이러스로 인해서 파일이 손상될 가능성이 큼

  
  

## 세션과 쿠키 vs 캐시

  * state(상태가 있는): 세션과 쿠키
    * 목적: 상태를 잃어버리면 안될 때 사용 ex)사용자 자동로그인
  * Stateless(상태가 없는): 캐시
    * 목적: 빠르게 로딩하기위해서 사용

#[차이](/tags/%EC%B0%A8%EC%9D%B4/)
