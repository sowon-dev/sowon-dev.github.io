---
title: "[스프링SPRING] 프레임워크란, Spring 특징과 기능, 컨테이너란"
date: 2020-10-04 20:06:41
tags:
  - "TIL"
  - "ITWILL(JAVA)"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">프레임워크란, Spring 특징과 기능, 컨테이너란의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * 사용될 기능을 클래스/인터페이스로 만들어놓고 제공해주는 형태을 적용할 수 있다.</p>
</div>

<!-- more -->

## Framework란?

  * 어떤것을 구성하는 구조/뼈대/틀
  * 사용될 기능을 클래스/인터페이스로 만들어놓고 제공해주는 형태
  * 직접적인 구현X, 활용O
  * 프레임워크 등장배경 : 기존 언어의 불편함을 개선하기 위해서
    * 개발생산성 향상됨
  * [spring beans DTD](http://ldg.pe.kr/framework_reference/spring/ver1.2.2/html/springbeansdtd.html) : 해당 문서의 저장되는 데이터를지정한다.

  
  
  

## 컨테이너 Container

> Container 는 Spring 의 핵심입니다. Container 는 개발자를 대신하여, Bean 을 생성 / 관리 / 제거합니다. Container 가 Bean 을 관리해주기 때문에, 개발자는 모듈 간에 의존 및 결합으로 인해 발생하는 문제로부터 자유로워 졌습니다. 아래와 같이 독립적인 코드를 작성해서 Annotaion 만 남겨주면 Container 가 개발자가 원하는 상황에 코드를 실행합니다. 따라서 개발자는 메서드가 언제, 어디서 호출되어야 하는지 그리고 메서드를 호출하기 위해 필요한 매개 변수를 준비해서 전달하지 않습니다. Container 가 개발자 대신 알아서 호출합니다.  
> 이렇게 Container 가 개발자를 대신하여 메서드가 호출될 때와 메서드가 필요한 자원을 전달하는 설계 구조를 Inversion of Control (IOC) 이라 합니다.  
> IOC 는 메서드가 필요로 하는 자원을 코드가 실행되는 타임에 전달하는데, 이를 Dependency Injection (DI) 이라 합니다. 예를 들어 Container가 알아서 greeting 메서드가 필요로 하는 name 매개변수를 전달하는 과정과 run 메서드가 필요로 하는 RestTemplate 매개변수를 전달하는 과정 모두 Dependency Injection (DI) 입니다.  
> 출처: <https://ibocon.tistory.com/122>

  
  
  

## Spring

  * 자바 웹 애플리케이션을 생성하기위한 오픈소스
  * 스프링은 경량 프레임워크이면서 경량 컨테이너이다.
    * 컨테이너란 무엇일까? ex) 톰캣
    * EJB(Enterprise Java Beans)프레임워크 : 굉장히 무거움. 스프링 이전에 사용됨.

  
  
  

### 스프링의 특징

스프링의 특징 | 추가설명  
---|---  
[제어의 역행(IoC, Inversion of Control)](https://sowon-dev.github.io/2020/10/03/201003spring-1/#제어의-역행-IoC-Inversion-of-Control) | 서블릿/빈 개발자가 코드로 작성X, 프레임워크로 수행  
[의존성 주입(DI, Dependency Injection)](https://sowon-dev.github.io/2020/10/03/201003spring-1/#%EC%9D%98%EC%A1%B4%EC%84%B1-%EC%A3%BC%EC%9E%85-DI-Dependency-Injection) | 클래스를 사용한 객체를 개발자가 코드로 생성X, 프레임워크가 생성해서 사용  
[관점 지향 (AOP, Aspect-Oriented Programming)]() | 핵심기능(주요기능) 제외한 부수적인 기능을 프레임워크가 생성해서 제공  
영속성-(DB) | -  
라이브러리 연동 제공 | -  
POJO(Plain Old Java Object)방식 프레임워크 | ![https://yunjigo92.github.io/2020/02/18/java_pojo.html](https://yunjigo92.github.io/img/study/POJO.png)  
  
  
  
  

## 스프링의 주요 기능

스프링의 주요 기능 | 설명  
---|---  
SPRING Core | 다른 기능과 설정값을 분리하기위한 IoC 기능을 제공한다.  
SPRING Context | 스프링의 기본 기능으로 각각의 애플리케이션을 작동하는 Bean(=객체)에 대한 접근을 처리한다.  
SPRING DAO | 모델2보다 향상된 JDBC기능 활용할 수 있다.  
SPRING ORM | MyBatis(마이바티스)와 같은 영속성 프레임워크 연동기능을 제공한다.  
SPRING AOP | 관점지향 프로그래밍를 제공한다.  
SPRING Web | 웹 개발에 필요한 기능을 제공한다.  
SPRING WebMVC | 스프링에서 MVC구현에 관한 기능을 제공한다.  
  
  
  
  

## Tomcat은 컨테이너다?

  * 톰캣은 서블릿컨테이너다.
  * 서블릿 생성,초기화,서비스 실행, 서비스 소멸등 모든 서블릿에 관한 권한을 가지고 있다.

#[TIL](/tags/TIL/)[ITWILL(JAVA)](/tags/ITWILL-JAVA/)
