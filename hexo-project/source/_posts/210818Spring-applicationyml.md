---
title: "application.properties과 application.yml 차이"
date: 2021-08-17 15:00:00
tags:
  - "SpringBoot"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'application.properties과 application.yml 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    이 둘은 외부 속성을 설정하는 파일이다. 그럼 둘의 차이점은 무엇일까?의 차이를 고려하여 상황에 맞게 적용해야 한다.</p>
</div>

<!-- more -->

스프링부트 프로젝트를 설정하다보면 application.properties 또는 application.yml 혹은 둘 다 만날때가 있다.  
이 둘은 외부 속성을 설정하는 파일이다. 그럼 둘의 차이점은 무엇일까?

## application.properties

키-밸류형식을 사용하여 외부 구성의 속성을 설정할 수 있다.

```xml
spring.datasource.url=jdbc:h2:DB이름
spring.datasource.username=유저이름
spring.datasource.password=비밀번호
```

  
  
  

## application.yml

YAML기반으로 외부 구성의 속성을 설정할 수 있다.  
반복되는 접두사가 없어 가독성이 좋다.

```xml
spring:
    datasource:
        url: jdbc:h2:DB이름
        username: 유저이름
		password: 비밀번호
```

  
  
  

## 결론

application.yml이 계층적으로 잘 표현할 수 있어 편리하다.

#[SpringBoot](/tags/SpringBoot/)
