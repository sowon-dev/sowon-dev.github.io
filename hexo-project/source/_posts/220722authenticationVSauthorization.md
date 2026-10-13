---
title: "[도서]인증과 인가"
date: 2022-07-22 01:38:14
tags:
  - "Book"
  - "WEB"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'인증과 인가'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    인증종류 3가지 | 설명 | 장점 | 단점의 차이를 고려하여 상황에 맞게 적용해야 한다.</p>
</div>

<!-- more -->

책 `React.js, 스프링 부트, AWS로 배우는 웹 개발 101` 를 읽고 공부한 내용을 정리한 글입니다.

![](http://image.kyobobook.co.kr/images/book/xlarge/656/x9791161755656.jpg)

  * [도서 공식 링크](http://www.acornpub.co.kr/book/reactjs-springboot#toc)
  * [도서 정오표](http://www.acornpub.co.kr/book/reactjs-springboot#errata)
  * [공식 레포지토리 링크](https://github.com/fsoftwareengineer/todo-application)

  
  

# 인증과 인가

  * 인증: 내 집에 들어올 수 있는 사용자
  * 인가: 인증받고 들어온 사용자가 내 집에서 할 수 있는 것들
    * 화장실 사용, 주방사용, 거실사용 등등

인증에는 여러 방법이 있다.  
책에서는 3가지 방법에 대해 이야기한다.

인증종류 3가지 | 설명 | 장점 | 단점  
---|---|---|---  
Basic 인증 | 클라이언트는 매 요청시 아이디와 비번을 전달하여 자신이 인증된 사용자임을 증명한다 |  | 인코딩헤도 아이디와 비번 노출됨.사용자를 로그아웃시킬수없음.인증서버에 요청이 많아져 단일 장애점이 되버림.  
토근기반인증(Bearer 인증) | 토큰은 최초 로그인시 서버가 만들어 줌. 서버가 자기만 아는 시크릿코드로 토큰을 만들어 반환하면 클라이언트는 이후 요청에 아이디와 비번 대신 토큰을 넘겨 자신이 인증된 사용자임을 증명한다. | 아디랑 비번이 노출되지 않으므로 보안측면에서 Basic인증방식보다 안전함.서버가 토큰을 생성하므로 유효시간, 인가관리가능. | 토큰 이름만 바꾸면 새로운 사용자가 되버리므로 스케일문제 해결못함  
JSON 웹 토큰(JWT) | [JWT](https://jwt.io/)는 JSON Web Token의 약자. | 전자서명된 토큰을 이용항 스케일 문제를 해결함. | 인증서버에 토큰유효성을 물어보지않으므로 단일 장애점문제해결  
  
  
  
  
  

# 인코딩을 했는데 왜 문제가 될까?

Basic Auth에서는 아이디와 비밀번호를 인코딩한다. 이 솔루션은 아이디와 비밀번호를 노출한다.  
인코딩을 했는데 왜 문제가 될까? 인코딩은 보안을 목적으로 하는 것이 아니기때문!  
인간이 아이디와 비밀번호를 바로 알아내기 어렵지만 디코더만 있으면 누구나 원래의 아이디와 비번을 알아낼수 있다.  
이렇게 가로채는 것을 [MITM(Man in the middle attack)](https://blog.larapulse.com/security/prevent-mitm-attacks)라고한다.

![https://blog.larapulse.com/security/prevent-mitm-attacks](https://blog.larapulse.com/files/original/images/3e/8c/3e8c78810e53dec80d2a5b2933b564a20c0e0295.png)

  
  
  
  

# JWT 설명 및 각 필드 뜻

JWT는 JSON 형태로 된 토큰이면서 토큰 기반 인증방식이다.  
JSON 웹 토큰방식과 토큰 기반 인증방식의 차이점은 무엇일까?  
JWT는 서버가 헤더와 페이로드를 생성한 후 전자 서명을 한다는 점이 기존 토큰 기반 인증방식과 다르다.  
JWT에게 전자사명이란 {헤더}.{페이로드}와 시크릿키를 이용해 해시 함수에 돌린 암호화한 결과값이다.

  * HEADER
    * typ: Type의 약자. 토큰타입을 의미.
    * alg: Algorithm의 약자. 토큰 서명을 발행하는 데 사용된 해시 알고리즘의 종류를 의미
  * Payload
    * sub: Subject의 약자. 토큰의 주인을 의미 ex)사용자이메일, 사용자아이디
    * iss: Issuer의 약자. 토큰을 발행한 주체를 의미 ex) 내가만든애플리케이션이름, facebook
    * iat: issued at의 약자. 토큰이 발행된 날짜와 시간을 의미.
    * exp: expiration의 약자. 토큰 만료 시간을 의미.
  * Signature
    * 토큰을 발행한 주체 Issuer가 발행한 서명으로 토큰의 유효성 검사에 사용된다.

  
  
  

## JWT 인증 방식

  1. 최초 로그인: 서버는 사용자 아디와 비번을 서버에 저장딘 아디와 비번에 비교해 인증
  2. 일치하면 사용자의 정보를 이용해 `{헤더}.{페이로드}` 작성한 뒤 자신의 시크릿키로 `{헤더}.{페이로드}`부분을 전자서명함.
  3. 전자 서명의 결과로 나온 값을 `{헤더}.{페이로드}.{서명}`으로 이어붙이고 Base64로 인코딩한 후 반환.

  
  
  

## 만약 누군가가 이 토큰으로 리소스 접근을 요청한다면?

  1. 서버:토큰을 Base64로 디코딩
  2. 디코딩한 JSON을 `{헤더}.{페이로드}`과 `{서명}`으로 나눈다.
  3. 서버는 위에서 나눴던 `{헤더}.{페이로드}`와 자신이 갖고있는 시크릿키로 전자서명을 만든 후 잘라놨던 `{서명}`부분과 일치하는 비교

이렇게 처리하면 좋은 점은 인증서버에 토큰 유효성에 대해 물어볼 필요가 없기에 단일 장애점 문제가 발생하지 않는다.

  
  
  

## 만약 누군가가 토큰을 훔쳐간다면?

당연히 해당 계정 리소스에 접근이 가능하다.  
따라서 반드시 HTTPS로 통신해야만 한다.

> 그래서 Postman 인증 테스트시 HTTP로 하면 안되었던 거구나. 유레카!

  
  
  

# 스프링 시큐리티가 필요한 이유?

API 실행시마다 사용자 인증을 해주는 부분을 스프링 시큐리티가 대신해줄수있다.

  * 스프링 시큐리티란? 서블릿 필터의 집합
  * 서블릿 필터이란? 서블릿 실행 전 에 실행되는 클래스들로 디스패처 서블릿 실행되기 전에 항상 실행됨.
  * 스프링 시큐리티에서 서블릿 펄터를 사용하려면 2가지를 해야함
    1. 서블릿 필터 구현하는 작업
    2. 서블릿 컨테이너에 구현한 필터를 사용하도록 설정해주는 작업
  * 여기서 개발자가 할 일은?  
서블릿 필터를 구현하고 서블릿 필터를 서블릿 컨테이너가 실행하도록 설정해주기!
  * 서블릿필터는 꼭 한 개여야할까?  
서블릿 필터가 1개일 필요는 없다. 하나의 클래스에 모든 필터를 다 담으면 크기가 어마어마해질 것이다. 따라서 기능에 따라 서블릿 필터 여러 개를 작성하는 것이 좋다.  
생성한 서블릿 필터들을 FilterChain을 통해 연쇄적으로 순서대로 실행시킬수 있음.

  
  
  

## HttpSecurity란?

  * WebSecurityConfig.java 파일을 생성해서 스프링시큐리티 설정해야 함
  * 시큐리티 설정을 위한 오브젝트임. 
  * 이 오브젝트를 통해 web.xml 대신 HttpSecurity를 이용해 시큐리티 관련 설정함.
  * 스프링시큐리티에 JwtAuthenticationFilter를 사용하라고 알려줘야함
  * [코드 출처 및 원본 바로가기](https://github.com/fsoftwareengineer/todo-application/blob/main/4.3-Spring_Security_Integration/demo/src/main/java/com/example/demo/config/WebSecurityConfig.java)

```java
@EnableWebSecurity
@Slf4j
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {

	@Autowired
	private JwtAuthenticationFilter jwtAuthenticationFilter;

	@Override
	protected void configure(HttpSecurity http) throws Exception {
		// http 시큐리티 빌더
		http.cors() // WebMvcConfig에서 이미 설정했으므로 기본 cors 설정.
				.and()
				.csrf()// csrf는 현재 사용하지 않으므로 disable
					.disable()
				.httpBasic()// token을 사용하므로 basic 인증 disable
					.disable()
				.sessionManagement()  // session 기반이 아님을 선언
					.sessionCreationPolicy(SessionCreationPolicy.STATELESS)
				.and()
				.authorizeRequests() // /와 /auth/** 경로는 인증 안해도 됨.
					.antMatchers("/", "/auth/**").permitAll()
				.anyRequest() // /와 /auth/**이외의 모든 경로는 인증 해야됨.
					.authenticated();

		// filter 등록.
		// 매 리퀘스트마다
		// CorsFilter 실행한 후에
		// jwtAuthenticationFilter 실행한다.
		http.addFilterAfter(
						jwtAuthenticationFilter,
						CorsFilter.class
		);
	}
}
```

addFilterAfter()메서드는 JwtAuthenticationFilter를 CorsFilter 이후에 실행하라고 설정하는 것임. 즉, 실행순서는 `CorsFilter -> JwtAuthenticationFilter` 이 된다. 반드시 이 순서로 실행해야하는 것은 아니다. 저자가 보기에 적당해보여서 그렇게 설정한 것이다.

#[Book](/tags/Book/)[WEB](/tags/WEB/)
