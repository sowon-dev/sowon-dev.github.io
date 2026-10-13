---
title: "[Spring]Filter"
date: 2021-08-06 15:00:00
tags:
  - "패스트캠퍼스(초격차Java/Spring)"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Filter의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * 보통 실무에선 logging용도로 사용되고 intercepter가 인증단계로 사용됨을 적용할 수 있다.</p>
</div>

<!-- more -->

스프링에서 필터에 대해 알아보자.

## Filter

  * Filter란 웹 어플리케이션에서 관리되는 영역
  * 스프링부트 프레임워크에서 요청/응답의 최초와 최종단계에 위치
  * 필터를 통해 요청/응답 정보 변경 가능
  * **유일하게 ServletRequest, ServletResponse 객체를 변환할 수 있음**
  * 주로 인증로직과 logging용도로 활용
    * 보통 실무에선 logging용도로 사용되고 [intercepter](https://sowon-dev.github.io/2021/08/09/210809Spring-interceptor/)가 인증단계로 사용됨

  
  
  
전역 Filter설정방법과 특정 컨트롤러에만 Filter를 설정하는 방법을 예제 코드와 함께 보자.  
차이점으로는 특정 컨트롤러 필터사용시 아래 두 어노테이션을 사용한다는 점이다.

  * `@ServletComponentScan`
  * `@WebFilter("/api2/user/*")`

  
  

## Filter 공통 코드

  * User.java

```java
@Slf4j
@Data
public class User {
  private String name;
  private int age;
}
```

  
  
  

## 전역 Filter 코드 예제

  * FilterApplication.java

```java
@Slf4j
@SpringBootApplication
public class FilterApplication {

	public static void main(String[] args) {
		SpringApplication.run(FilterApplication.class, args);
	}

}
```

  * controller1.java

```java
@Slf4j
@RestController
@RequestMapping("/api")
public class ApiController {

  @PostMapping("/user")
  public User user(@RequestBody User user){
    log.info("user1: {}", user);
    return user;
  }
}
```

  * GlobalFilter1.java

```java
@Slf4j
@Component
public class GlobalFilter implements Filter {

  @Override
  public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
      throws IOException, ServletException {

    //전처리
    ContentCachingRequestWrapper req = new ContentCachingRequestWrapper((HttpServletRequest) request);
    ContentCachingResponseWrapper res = new ContentCachingResponseWrapper((HttpServletResponse) response);

    chain.doFilter(req, res);
    String url = req.getRequestURI();

    //후처리
    String reqContent = new String(req.getContentAsByteArray()); //default가 UTF-8
    log.info("respone url: {}, reqBody: {}", url, reqContent);

    String resContent = new String(res.getContentAsByteArray()); //default가 UTF-8
    log.info("respone resBody: {}", resContent);
    // 필수: 한 번 읽었기때문에 원래대로 copy 돌려놓아야한다.
    res.copyBodyToResponse();
  }
}
```

  
  
  

## 특정 컨트롤러 Filter 코드 예제

  * FilterApplication.java

```java
@Slf4j
@SpringBootApplication
@ServletComponentScan //2번방법용
public class FilterApplication {

	public static void main(String[] args) {
		SpringApplication.run(FilterApplication.class, args);
	}

}
```

  * controller2.java

```java
// 이 컨트롤러에만 필터적용
@Slf4j
@RestController
@RequestMapping("/api2")
public class Api2Controller {

  @PostMapping("/user")
  public User user(@RequestBody User user){
    log.info("Api2Controller 컨트롤러에만 GlobalFilter2 필터 적용");
    log.info("user2: {}", user);
    return user;
  }
}
```

  * GlobalFilter2.java

```java
@Slf4j
@WebFilter("/api2/user/*") //특정 컨트롤러에만 사용 가능하도록 설정
public class GlobalFilter2 implements Filter {

  @Override
  public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
      throws IOException, ServletException {

    //전처리
    ContentCachingRequestWrapper req = new ContentCachingRequestWrapper((HttpServletRequest) request);
    ContentCachingResponseWrapper res = new ContentCachingResponseWrapper((HttpServletResponse) response);

    chain.doFilter(req, res);
    String url = req.getRequestURI();

    //후처리
    String reqContent = new String(req.getContentAsByteArray()); //default가 UTF-8
    log.info("respone url: {}, reqBody: {}", url, reqContent);

    String resContent = new String(res.getContentAsByteArray()); //default가 UTF-8
    log.info("respone resBody: {}", resContent);
    // 필수: 한 번 읽었기때문에 원래대로 copy 돌려놓아야한다.
    res.copyBodyToResponse();
  }
}
```

#[패스트캠퍼스(초격차Java/Spring)](/tags/%ED%8C%A8%EC%8A%A4%ED%8A%B8%EC%BA%A0%ED%8D%BC%EC%8A%A4-%EC%B4%88%EA%B2%A9%EC%B0%A8Java-Spring/)
