---
title: "[SQLD] 슈퍼타입과 서브타입"
date: 2022-10-31 21:31:02
tags:
  - "SQLD"
categories:
  - Database
  - General
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">슈퍼타입과 서브타입의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    if 10만건도 되지 않는 데이터 or 시스템을 운영하는 도중에도 데이터가 증가하지 않는다, 트랜잭션의 성격을 고려하지않고 전체를 하나의 테이블로 묶는 것도 괜찮은 방법이다.</p>
</div>

<!-- more -->

슈퍼/서브타입 데이터 모델은 Extended ER모델이라고도 불린다.

  * 슈퍼타입: 공통의 부분
  * 서브타입: 공통으로부터 상속받아 서

if 10만건도 되지 않는 데이터 or 시스템을 운영하는 도중에도 데이터가 증가하지 않는다, 트랜잭션의 성격을 고려하지않고 전체를 하나의 테이블로 묶는 것도 괜찮은 방법이다.  
하지만 데이터 양이 이미 많고 지속적으로 증가한다면 슈퍼/서브타입 물리적 데이터 모델로 변환하는 세 가지 유형을 고려해야한다.

  
  
  

# 성능을 고려한 슈퍼/서브타입 데이터 모델 변환

![https://hec-ker.tistory.com/68](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FdIB9Iq%2FbtqCbgT9pcy%2FxrapasEiGw1KvgUTjG4k31%2Fimg.jpg)

![https://hec-ker.tistory.com/68](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FFLEnX%2FbtqCbhrWGzj%2FJk1PxKYOQNEXq8zkDbqGz0%2Fimg.jpg)

논리모델 | One to One Type(1:1 타입) | Plus Type(슈퍼+서브 타입) | Single Type(All in One 타입)  
---|---|---|---  
정의 | if 슈퍼타입과 서브타입 각각 트랜잭션이 발생, 개별 테이블로 구성(1:1 관계) | if 슈퍼타입과 서브타입 함께 트랜잭션이 발생, 슈퍼타입의 PK와 각 서브타입의 속성을 묶어 N개의 테이블을 구성 | if 슈퍼타입과 서브타입 정확히 지정x상황, 하나의 테이블로 통합  
예시 | 고객엔티티 하위에 개인고객, 법인고객으로 구분 | 개인고객엔티티, 법인고객엔티티 | 고객엔티티  
물리모델 결정기준 | 개별로 발생되는 경우가 많은 서비스는 Identity로 | 슈퍼타입+서브타입에 대해 발생되는 서비스는 RollDown 으로! | 전체를 하나로 묶어 트랜잭션이 발생할 때는 RollUp 으로!  
  
  
  
  

# 출처

  * [마띠의블로그 - 데이터베이스 구조와 성능](https://hec-ker.tistory.com/68)
  * [데이터온에어 - ‘6개의 열쇠’로 데이터 모델링의 고수가 되자](https://dataonair.or.kr/db-tech-reference/d-lounge/expert-column/?mod=document&uid=54034)
  * [공부하는 개발자 핑구 - 슈퍼-서브타입 모델의 물리모델 결정기준](https://developer-ping9.tistory.com/293)

#[SQLD](/tags/SQLD/)
