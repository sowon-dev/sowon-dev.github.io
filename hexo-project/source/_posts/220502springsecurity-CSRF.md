---
title: "전자정부프레임워크3.8에 CSRF 설정하기"
date: 2022-05-02 05:23:27
tags:
  - "CSRF"
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">전자정부프레임워크3.8에 CSRF 설정하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    스프링부트로는 CORS 설정을 한 적이 있는데 이번 프로젝트는 전자정부프레임워크를 사용해야해서 조금 새로웠다.</p>
</div>

<!-- more -->

CSRF란 Cross Site Request Forgery로 보안 이슈이기때문에 꼭 해결해야한다.

스프링부트로는 CORS 설정을 한 적이 있는데 이번 프로젝트는 전자정부프레임워크를 사용해야해서 조금 새로웠다.  
전자정부프레임워크 공식문서[(링크)](https://www.egovframe.go.kr/wiki/doku.php?id=egovframework:rte3:fdl:server_security:xmlschema_v3_8)에 spring security CSRF 간편설정이 있지만 왜인지 설정이 잘 되지않아 그냥 spring security를 pom.xml에 추가했다.

## pom.xml 에 의존성 추가

프로젝트에 spring security를 추가한다.

```xml
<properties>
	<spring.maven.artifact.version>4.3.16.RELEASE</spring.maven.artifact.version>
	<egovframework.rte.version>3.8.0</egovframework.rte.version>
	<security.version>4.2.13.RELEASE</security.version>
</properties>

(중략)
	<!-- spring security -->
	<dependency>
		<groupId>org.springframework.security</groupId>
		<artifactId>spring-security-core</artifactId>
		<version>${security.version}</version>
	</dependency>
	<dependency>
		<groupId>org.springframework.security</groupId>
		<artifactId>spring-security-web</artifactId>
		<version>${security.version}</version>
	</dependency>
	<dependency>
		<groupId>org.springframework.security</groupId>
		<artifactId>spring-security-config</artifactId>
		<version>${security.version}</version>
	</dependency>
	<dependency>
		<groupId>org.springframework.security</groupId>
		<artifactId>spring-security-taglibs</artifactId>
		<version>${security.version}</version>
	</dependency>
(생략)
```

  
  
  

## web.xml 추가

아래 필터를 추가한다.

```xml
<!-- spring security -->
<filter>
	<filter-name>springSecurityFilterChain</filter-name>
	<filter-class>org.springframework.web.filter.DelegatingFilterProxy</filter-class>
</filter>
<filter-mapping>
	<filter-name>springSecurityFilterChain</filter-name>
	<url-pattern>/*</url-pattern>
</filter-mapping>
```

  
  
  

## context-security.xml 생성

context 설정에 따라 이름에 맞는 시큐리티 config xml파일을 생성한다.

```xml
<?xml version="1.0" encoding="UTF-8"?>

<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:sec="http://www.springframework.org/schema/security" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans 
	http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/security 
	http://www.springframework.org/schema/security/spring-security.xsd">

	<sec:authentication-manager alias="authenticationManager" /> 

	<!-- 인증예외처리 -->
	<sec:http pattern="/admin/**" security="none" />
	<sec:http pattern="/css/**" security="none" />
	<sec:http pattern="/img/**" security="none" />
	<sec:http pattern="/js/**" security="none" />
	<sec:http pattern="/uploads/**" security="none" />
	<sec:http pattern="/file/**" security="none" />

	<!-- 접근경로 권한처리 -->
	<sec:http use-expressions="true">
	
		<!-- 로그인 페이지 정보 -->
 		<sec:form-login  />
		<sec:csrf disabled="false" />
	</sec:http>
</beans>
```

form-login 로그인 페이지를 연결하면 CSRF를 방어할 수 있다.  
커스텀한 로그인 로직을 사용하기때문에 `<sec:form-login />`해당 부분을 빼고 싶었는데 해당 코드를 빼면 서버 에러가 나서 입력만 하고 연결하지 않았다.  
참고로 disabled=”false”가 CSRF를 사용하겠다는 의미이다.

  
  
  

## 토큰을 jsp화면에 넣기

form태그 아래에 넣어주면 된다!

```html
<sec:csrfToken>
```

#[CSRF](/tags/CSRF/)
