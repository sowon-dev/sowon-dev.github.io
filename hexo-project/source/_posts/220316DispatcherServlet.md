---
title: "DispatcherSerlvet 씹어먹기"
date: 2022-03-16 05:34:04
tags: []
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">DispatcherSerlvet 씹어먹기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    Spring 프레임워크는 개발을 지원하기 위해 다양한 clas를 제공하는데 그 중 아래 3가지를 이번 글에서 다룰 것이다.</p>
</div>

<!-- more -->

SpringMVC에선 DispatcherSerlvet가 아주 중요한 역할을 한다.  
잠깐 SpringMVC란 무엇일까?  
Spring프레임워크에 Model, View, Controller를 븐리한 디자인 패턴을 말한다.

Spring 프레임워크는 개발을 지원하기 위해 다양한 clas를 제공하는데 그 중 아래 3가지를 이번 글에서 다룰 것이다.

  1. DispatcherServlet
  2. HandlerMapping
  3. ViewResolver

용어 | 역할 | 예시  
---|---|---  
DispatcherServlet | 클라이언트의 요청을 받아서 HandlerMapping에 넘긴다 |   
HandlerMapping | Key-Value구조로 URL-메서드를 저장한 table에서 클라이언트의 요청을 처리할 Controller를 찾는 역할 | @RequestMapping(“/url”) annotaion사용하면 Controller URL Mapping한다.  
ViewResolver | Controller가 리턴한 View Name에 prefix와 suffix를 적용하여 반환한다. |   
  
  
  
  

## SpringMVC 요청 처리 과정

![https://docs.spring.io/spring-framework/docs/2.0.8/reference/mvc.html](https://docs.spring.io/spring-framework/docs/2.0.8/reference/images/mvc.png)

  1. 클라이언트가 요청을 한다. 
     * ex) /admin/post/add
  2. DispatcherServlet는 어떤 메서드가 좋은지 HandlerMapping에게 물어본다.
  3. HandlerMapping는 URL매칭테이블에서 뒤져서 해당 url과 일치하는 메서드를 반환한다. 
     * ex) add()
  4. DispatcherServlet는 받은 메서드를 가지고 어떤 HandlerAdapter가 처리할 수 있는 지 확인후 특정 HandlerAdapter에 넘겨준다.
  5. HandlerAdapter가 받은 정보로 Controller에게 전달한다. 
     * ex) @RequestMapping(“/admin/post/add”) public String add(){ return “addForm” }
     * 스프링의 큰 특징은 관심사의 분리이다. DispatcherServlet이 직접 Controller를 호출하는 것보다 HandlerAdapter를 통함으로써 느슨한 연결이 된다.
     * 느슨한 연결은 어떤 변경에서든지 유리하게 대처할 수 있다. => 즉, 변경의 유리한 설계
  6. Controller 반환값을 HandlerAdapter에게 넘겨준다.
     * ex) addForm
  7. HandlerAdapter는 그 값을 DispatcherServlet에게 전달한다.
     * ex) addForm
  8. DispatcherServlet는 ViewResolver에게 전달한다. 
     * ex) addForm
  9. ViewResolver는 prefix와 suffix를 적용한 뒤 실제 화면을 알아내서 DispatcherServlet에게 반환한다.
     * ex) /WEB-INF/views/addForm.jsp
  10. DispatcherServlet은 해당 뷰를 호출하면서 Model도 함께 전달한다.
  11. 화면은 Model객체를 가져와서 응답결과를 만들고 클라이언트에게 응답결과를 전달한다.
