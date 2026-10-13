---
title: "[@Autowired에러]no qualifying bean of type available: expected at least 1 bean which qualifies as autowire candidate 오류해결"
date: 2023-03-12 23:29:17
tags:
  - "오류일지"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">스트레스를 주는(?) 생성자주입에러! 나는 분명 모든 스프링빈등록을 어노테이션으로 제대로 걸었다고 생각했는데 자꾸 빈등록할 것이 없단다.
    추가해주니 정상적으로 빈생성이 되고 server run이 성공했다.</p>
</div>

<!-- more -->

스트레스를 주는(?) 생성자주입에러! 나는 분명 모든 스프링빈등록을 어노테이션으로 제대로 걸었다고 생각했는데 자꾸 빈등록할 것이 없단다.

# 1\. @Controller, @Service, @Repository 누락 어노테이션 찾기

구글링해보니 @Controller, @Service, @Repository 어노테이션을 누락된 부분을 찾으라는 글이 많았다.  
하지만 아무리 찾아도 보이지않았다.  
프로세스 흐름대로 흘러가도 보이지 않는 누락 어노테이션.

  
  
  

# 2\. component-scan에 패키지가 누락되었는지 확인하기

`root-context.xml` 과 `servlet-context.xml`에서 해당 패키지가 누락되진않았는지 체크해보자.  
나의 경우 패키지 `com.test.api`가 누락되서 발생된 에러였다.  
추가해주니 정상적으로 빈생성이 되고 server run이 성공했다.

```xml
<bean>
  <context:component-scan base-package="com.test.dao" />
  <context:component-scan base-package="com.test.service" />
  <context:component-scan base-package="com.test.util" />
  <context:component-scan base-package="com.test.api" /> <!-- 추가 -->
</bean>
```

#[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)
