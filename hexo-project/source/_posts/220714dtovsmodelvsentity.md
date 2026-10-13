---
title: "DTO vs Model vs Entity"
date: 2022-07-14 05:34:26
tags: []
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'DTO vs Model vs Entity'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    스프링프레임워크를 공부하면서 DTO와 Entity의 역할 차이는 확실한데 Model의 개념과 셋의 차이점이 궁금해 추가로 공부해봤다.</p>
</div>

<!-- more -->

스프링프레임워크를 공부하면서 DTO와 Entity의 역할 차이는 확실한데 Model의 개념과 셋의 차이점이 궁금해 추가로 공부해봤다.  
닷넷프레임워크를 사용할땐 대부분의 클래스를 Model라고 칭했기 때문에 더 혼란스러웠다.  
언어별로 부르는 명칭이 다른 듯하다. 사실 명칭보다 더 중요한 것은 각 클래스가 어떤 역할을 하는지 정확히 아는 것이다.

명칭 | 역할  
---|---  
DTO | 클라이언트의 데이터를 받는 역할. 클라이언트에서 사용하는 것이므로 노출되도 상관없다.  
Model | 비즈니스 데이터를 담는 역할  
Entity | 데이터베이스의 테이블과 스키마를 표현하는 역할. DB컬럼과 연결되기때문에 필드명이 노출되서는 안된다.  
  
  * [참고: Entity VS DTO 차이점, 컨트롤러에서는 뭘 받아야할까?](https://sowon-dev.github.io/2021/09/06/210907Jpa-entityVSDto/)

  
  
  

## 예시

공부하면서 내가 생각해 본 예시이다.  
결제프로그램을 예로 들어 DTO, Model, Entity를 비교한다면 아래와 같을 것이다.

명칭 | 예시  
---|---  
DTO | 클라이언트가 입력한 카드정보, 쿠폰정보, 결정정보 파라미터로 전달한 걸 컨트롤러에서 받음  
Model | 유저별 결제 혜택, 포인트 차감, 통신사할인등 중간에 연산이나 외부시스템연동할때 쓸 필드들을 model에 담아서 처리함  
Entity | 연산되고 DB에 기록되어야 할 데이터(유저ID, 연산 후 포인트등)를 담아서 update시킴  
  
  
  
  

## 참고

  * [Entity, domain model and DTO – why so many?](https://itzone.com.vn/en/article/entity-domain-model-and-dto-why-so-many/)
