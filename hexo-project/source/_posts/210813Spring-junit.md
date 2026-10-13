---
title: "[Spring]Junit"
date: 2021-08-12 15:00:00
tags:
  - "패스트캠퍼스(초격차Java/Spring)"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Junit의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    Mock이란 실제 사용되어야하는 객체의 대체객체로 실제 객체를 만들어서 하기엔 시간이 부족하고 비용이 높은 경우, 구현이 까다로울 경우에 가짜 객체를 만들어서 사용하는데 그중 하나가 Mock객체이다.</p>
</div>

<!-- more -->

Junit 사용법을 예시와 함께 확인해보자

## Junit

  * java 기반의 단위 테스트를 위한 프레임워크
  * 어노테이션기반으로 테스트 지원
  * Assert를 통해서 예상과 실제를 비교하여 검증

  
  
  

## Mock

Mock이란 실제 사용되어야하는 객체의 대체객체로 실제 객체를 만들어서 하기엔 시간이 부족하고 비용이 높은 경우, 구현이 까다로울 경우에 가짜 객체를 만들어서 사용하는데 그중 하나가 Mock객체이다.

  * 행위를 검증하기 위해 사용되는 객체
  * 직접 만들거나 스프링프레임워크를 통해서 간단하게 만들수 있음
  * @Mock
    * Mockito 라이브러리에 위치
    * 주로 @injectMocks 조합으로 사용
    * give, when, then으로 Mock객체의 행위 정의함
  * @MockBean
    * Springboot 테스트 패키지 내에 위치
    * 테스트를 하려는 객체 내에서 기존에 등록된 Bean이 아닌, MockBean을 주입함.
    * 주로 @SpringbootTest, @WebMVCTest와 함께 사용
    * give, when, then으로 Mock객체의 행위 정의함

  
  
  

## Jacoco

자바코드의 코드 커버리지를 체크하는 라이브러리로 결과를 html로 확인 가능하다.

플러그인 id에 `jacoco`를 추가하기만하면 끝!

  * build.gradle

```java
plugins {

	(중략)
	id 'jacoco'
}
```

#[패스트캠퍼스(초격차Java/Spring)](/tags/%ED%8C%A8%EC%8A%A4%ED%8A%B8%EC%BA%A0%ED%8D%BC%EC%8A%A4-%EC%B4%88%EA%B2%A9%EC%B0%A8Java-Spring/)
