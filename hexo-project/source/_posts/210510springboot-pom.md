---
title: "[스프링부트]Springboot + Spring Security + JWT 기본 dependencies 추천"
date: 2021-05-09 23:19:02
tags:
  - "SpringBoot"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Springboot + Spring Security + JWT 기본 dependencies 추천의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    프로젝트 구조와 사용하는 의존성에는 완벽이란 없다. 자신의 프로젝트에 맞게 알아서 골라서 사용하면 된다.</p>
</div>

<!-- more -->

스프링부트 + 스프링시큐리티 + JWT + MyBatis + MariaDB로 진행하는 API프로젝트에서 참고하면 좋은 프로젝트 구조와 `pom.xml`을 공유하고자한다.  
프로젝트 구조와 사용하는 의존성에는 완벽이란 없다. 자신의 프로젝트에 맞게 알아서 골라서 사용하면 된다.

## 프로젝트구조

![]()

src/main/java

  * config: 시큐리티설정파일, DB연결설정파일
  * controller
  * dao
  * dto
  * exception
  * payload: 성공이나 실패등이 일어났을때 내가 챙겨 보고 싶은 message를 뜻한다. [추천 참고링크 - JSON과 Payload](https://minieetea.com/2017/03/archives/5001)
  * security
  * service
  * mapper: mapper interface파일

src/main/resources

  * mappers: mapper xml파일

  
  

## pom.xml 의 dependencies

```xml
<dependencies>
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-actuator</artifactId>
	</dependency>
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-security</artifactId>
	</dependency>
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-web</artifactId>
	</dependency>
	<dependency>
		<groupId>org.mybatis.spring.boot</groupId>
		<artifactId>mybatis-spring-boot-starter</artifactId>
		<version>2.1.4</version>
	</dependency>
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-devtools</artifactId>
		<scope>runtime</scope>
		<optional>true</optional>
	</dependency>
	<dependency>
		<groupId>org.mariadb.jdbc</groupId>
		<artifactId>mariadb-java-client</artifactId>
		<scope>runtime</scope>
	</dependency>
	<dependency>
		<groupId>org.projectlombok</groupId>
		<artifactId>lombok</artifactId>
		<optional>true</optional>
	</dependency>
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-test</artifactId>
		<scope>test</scope>
	</dependency>
	<dependency>
		<groupId>org.springframework.security</groupId>
		<artifactId>spring-security-test</artifactId>
		<scope>test</scope>
	</dependency>
	<!-- add -->
	<dependency>
		<groupId>org.apache.commons</groupId>
		<artifactId>commons-lang3</artifactId>
	</dependency>
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-validation</artifactId>
	</dependency>
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-tomcat</artifactId>
		<scope>provided</scope>
	</dependency>	
</dependencies>
```

의존성 명칭 | 기능 | 주요 사용 | 추천 참고링크  
---|---|---|---  
spring-boot-starter-actuator | Spring Boot Application의 상태 관리 | CORS설정 | [링크](https://supawer0728.github.io/2018/05/12/spring-actuator/)  
spring-boot-devtools | 스프링 부트에서 제공하는 개발 편의를 위한 모듈 | 자동재시작, liveLoad |   
commons-lang3 | 문자열 효율적인 처리 |  | [링크](https://m.blog.naver.com/PostView.nhn?blogId=racoon_z&logNo=220770377702&proxyReferer=https:%2F%2Fwww.google.com%2F)  
spring-boot-starter-validation | 효과적인 유효성 검사 | @NotNull @NotBlank @NotEmpty @AssertTrue @Min @Max | [링크](https://gaemi606.tistory.com/entry/Spring-Boot-ResponseBody-%EA%B0%81-%ED%95%AD%EB%AA%A9%EC%97%90-%ED%81%AC%EA%B8%B0-%ED%95%84%EC%88%98-%EA%B0%92-%EC%84%A4%EC%A0%95-spring-boot-starter-validation)  
  
  
  
  

#### 여담

난 인복이 좀 타고난 편이다. 주변에 좋은 지인들이 참 많고, 일터에서도 좋은 사람들을 더 많이 만났다. 참 감사한 삶이다.  
이번 팀장님도 역시나 최고다…👍  
이번에 내가 맡은 프로젝트는 내가 처음 해보는 것 투성이었다.  
내가 해본게 몇개있겠냐만은 정말 어려운 개념들이라 주말을 불사하고 이해하려고 노력했다.  
시간이 갈수록 조급해지고 얼마나 답답하던지…

프로젝트 셋팅을 하는 입장에서 프로젝트 구조와 의존성 추가하는 부분이 가장 어려웠다.  
특히 어디에 어떤 폴더를 생성하고 그 폴더에는 무슨 파일을 넣으면 좋을지 난감했다.  
팀장님이 내 마음을 어떻게 아시고 갑자기 자리로 부르셨다.  
그리고 내 프로젝트 상황에 맞게 프로젝트구조부터 코드리팩토링할 수 있도록 하나부터 열까지 설명해주셨다.  
물론 설명을 알아듣진 못했지만… 못 알아들은 부분들은 열심히 필기했다.  
길을 알려주셨으니 이제 열심히 걸어가기만 하면 된다.

이 자리를 빌어(?) 배움의 길잡이를 해주신 팀장님 다시한번 감사드립니다! 최고최고👍

#[SpringBoot](/tags/SpringBoot/)
