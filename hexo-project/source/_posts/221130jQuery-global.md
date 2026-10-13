---
title: "[jQuery] Ajax 글로벌 이벤트(Global Event)가 뭐길래"
date: 2022-11-29 21:10:59
tags:
  - "jQuery"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Ajax 글로벌 이벤트(Global Event)가 뭐길래의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    셋팅 | global속성을 false(default)설정 | global속성을 true설정을 적용할 수 있다.</p>
</div>

<!-- more -->

레거시 소스코드를 분석하면서 jQuery.ajaxSetup()에 대해 알아볼 기회가 생겼다.

jQuery Ajax는 지역 이벤트(Local Event)와 전역 이벤트(Global Event)로 나뉜다. 둘이 가지고 있는 이벤트가 매우 비슷하다.

# 지역 이벤트(Local Event) vs 전역 이벤트(Global Event)

| | 로컬 이벤트 | 글로벌 이벤트  
---|---|---  
셋팅 | global속성을 false(default)설정 | global속성을 true설정  
시행시기 | ajax수행의 특정시점에 함수가 호출되는 callback형태로 이벤트 발생 | 개별 혹은 전체 ajax전송에 이벤트 발생  
전송시 | beforeSend | ajaxSend()  
성공시(응답코드 200 일때) | success | ajaxSuccess()  
에러발생시(응답코드 오류일때) | error | ajaxError()  
완료시 | complete | ajaxComplete()  
시작시 정의 |  | ajaxStart()  
정지시 |  | ajaxStop()  
  
  * 특징
    * 지역과 전역에 둘다 존재하는 send, success, error, complete와 관련된 이벤트들은 지역이벤트 callback이 실행 후 전역이벤트가 실행된다.

  
  
  

# 참고

  * <https://api.jquery.com/jquery.ajaxsetup/>
  * <https://www.nextree.co.kr/p10308/>

#[jQuery](/tags/jQuery/)
