---
title: "[Spring] 컨트롤러에서 json을 리턴하고 싶을때"
date: 2023-01-08 21:44:25
tags: []
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">컨트롤러에서 json을 리턴하고 싶을때의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    컨트롤러에서 json형식으로 반환해주는 방법은 크게 두가지이다.</p>
</div>

<!-- more -->

컨트롤러에서 json형식으로 반환해주는 방법은 크게 두가지이다.

  1. String으로 반환: Controller return type을 String으로 리턴한 뒤 클라이언트에서 파싱하기.
  2. MappingJackson2JsonView 사용: ModelAndView를 json 형식으로 반환해 준다.

스프링프레임워크에서는 주로 MappingJackson2JsonView을 bean으로 등록해서 이용한다.

  
  
  

# MappingJackson2JsonView

`servlet-context.xml`에서 아래 코드를 추가한다.

```xml
<bean id="jsonView" class="org.springframework.web.servlet.view.json.MappingJacksonJsonView">
    <property name="contentType" value="application/json;charset=UTF-8"> </property>
</bean>

<!-- BeanNameViewResolver 우선순위 지정 -->
<bean id="beanNameResolver" class="org.springframework.web.servlet.view.BeanNameViewResolver">
	<property name="order" value="0"/>
</bean>
```

> BeanNameViewResolver우선순위 지정: beanNameResolver는 우선순위를 0으로 해서 ViewPage를 찾을 때 우선 탐색한다. 만약 BeanNameViewResolver에서 없으면 viewResolver에서 탐색한다.  
> 출처: [Classic!님의 블로그 글 BeanNameViewResolver](https://icefree.tistory.com/entry/Spring-BeanNameViewResolver)
