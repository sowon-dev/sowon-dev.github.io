---
title: "[JPA] @Autowired보다 생성자 주입을 사용해야하는 이유"
date: 2021-09-09 16:25:47
tags: []
categories:
  - Backend
  - JPA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'@Autowired보다 생성자 주입을 사용해야하는 이유'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    하지만 JPA를 사용하는 경우 @Autowired 필드 주입보다는 생성자 주입 사용을 권장한다.</p>
</div>

<!-- more -->

MVC패턴 스프링프로젝트에서 Controller에서 Service를 의존성 주입할때 대부분 @Autowired로 필드주입을 한다.  
하지만 JPA를 사용하는 경우 @Autowired 필드 주입보다는 생성자 주입 사용을 권장한다.  
그 이유가 무엇인지 알아보자.

## 필드 주입(Field Injection)이란?

사용법이 매우 간단하여 많은 개발자들이 사용한다. 필드에 @Autowired만 붙여주면 끝!  
해당 필드에 자동으로 의존성이 주입된다.

  * ApiController.java

```java
@RestController
public class ApiController {
	@Autowired 
	NoticeService noticeService;
}
```

  
  
  

## 생성자 주입(Constructor Injection)이란?

생성자로 의존성을 주입한다. 방법은 총 두가지이다.

### 첫번째 방법: 정석

  * ApiController.java

```java
@RestController
public class ApiController {
	NoticeRepository noticeRepository;
	
	public ApiController(NoticeRepository noticeRepository) {
		this.noticeRepository = noticeRepository;
	}
}
```

  
  
  

### 두번째 방법: @RequiredArgsConstructor + final사용

위의 방법을 쉽게 할 수 있는 스프링프레임워크의 어노테이션이 있다!  
바로 @RequiredArgsConstructor를 넣은 뒤 필드를 final로 선언해주면 된다.

  * ApiController.java

```java
@RestController
@RequiredArgsConstructor
public class ApiController {

	private final NoticeRepository noticeRepository;
}
```

  
  
  

## 스프링팀에서 쉬운 필드 주입보다 생성자 주입은 권장하는 이유는?

  1. 순환참조 방지해서 애플리케이션이 뻗어버리는 걸 방지
  2. final선언이 가능해서 불변성 확보
