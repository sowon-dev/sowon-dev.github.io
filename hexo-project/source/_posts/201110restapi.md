---
title: "[REST API]REST란? RESTful이란? REST API란?"
date: 2020-11-09 15:10:34
tags:
  - "RESTfulAPI"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">REST란? RESTful이란? REST API란?의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * REST가 필요한 이유 : 모바일 기기가 다양해지면서 REST를 통해 다양한 기기로 공통의 데이터를 처리할 수 있다.</p>
</div>

<!-- more -->

## REST(Representational State Transfer)

  * 개념 : 하나의 URI는 하나의 고유한 리소스를 가진다.
  * REST가 필요한 이유 : 모바일 기기가 다양해지면서 REST를 통해 다양한 기기로 공통의 데이터를 처리할 수 있다.
  * REST API : REST방식을 사용한 API으로 핵심데이터, 콘텐츠, 기능등을 외부 페이지에서 가져와 사용할 수 있게 만들어 놓은 인터페이스이다.
    * 외부 페이지를 어떻게 가져올까? URI 주소를 통해서!
  * `RESTful` 의미 : REST방식의 서비스 제공이 가능한 형태. 
  * [필수 지침 : 마이크로 소프트 웹 API 디자인 DOCUMENT](https://docs.microsoft.com/ko-kr/azure/architecture/best-practices/api-design)

![URI](https://media.vlpt.us/images/jch9537/post/51dcc312-8ecb-4048-80df-cbde40865e7a/image.png)

  * 이해에 도움이 되는 유튜브영상! 이해하기 쉽게 설명해주신다.

  
  
  

## REST 개발을 위한 제약조건

  * Client - Server : 요청 또는 제공 진영으로 표준 인터페이스를 사용해서 구분하며 상호 독립적이어야한다.
    * 리소스(html, json등)를 관리하는 서버가 존재하고 다수의 클라이언트가 리소스를 소비하려고 네트워크를 통해 서버에 접근하는 구조여야한다.
  * stateless(상태없음) : 클라이언트의 컨텍스트가 서버에 저장되지 않고 클라이언트에 저장되어야한다.
    * 컨텍스트는 간단히 내 프로젝트 데이터라고 할 수 있다. 그리고 이 컨텍스트를 **서버에 저장하지않아야한다** 는 의미이다. 즉, 서버는 이전 정보를 모른다 -> 그럼 로그인 상태유지는 how? 클라이언트가 정보를 가지고 요청해야 한다.
    * 상태없음이란? 클라이언트가 서버에 요청을 보낼 때 서버는 이전 요청의 영향을 받지 않음을 의미. 
    * HTTP는 기본적으로 상태가 없는 프로토콜임. 따라서 HTTP를 사용하는 웹 애플리케이션은 기본적으로 상태가 없는 구조를 따른다.
  * [cashe](https://sowon-dev.github.io/2020/10/04/201005jspSessionVSCookie/) : 서버의 응답은 캐싱될 수 있어야하고 이를 사용하여 확장성, 개발 성능을 개선할 수 있다.
    * 서버에서 리소스를 리턴할 때 캐시가 가능한지 아닌지 명시할 수 있어야 한다.
  * uniform interface : 표준 인터페이스가 존재. 각각 서버/클라이언트를 발전가능 =>[아키텍쳐 디커플링](https://lipcoder.tistory.com/entry/13%EC%9E%A5-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8-%ED%8C%A8%ED%84%B4-Component-Pattern)
    * 리소스 접근할때 인터페이스가 일관적 + URI의 일관성있어야 한다.
  * layered system : 클라이언트와 서버사이의 부하분산을 의미허며 캐싱과 같은 중개서버 사용 가능하다.
    * 클라이언트는 서버 레이어 존재 유무를 알지 못해야한다.
    * 계층을 만들어서 클라이언트와 1:1이 아닌, 중간 서버가 필요하다는 의미
  * code-on-demand : Java Applet/Script를 통해 클라이언트가 사용가능한 코드를 제공한다.
    * 필수는 아니고 선택사항으로 클라이언트는 서버에 코드를 요청할 수 있고 서버가 리턴한 코드를 실행할 수 있어야한다.

![https://velog.io/@leobit/RESTful-API](https://media.vlpt.us/images/leobit/post/61d6d16f-318b-4179-ac1b-cc9e0b60c317/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7,%202020-09-27%2019-05-28.png)

  
  
  

## SOAP

REST API와 상반된 개념  
xml데이터를 사용해서 header와 body를 생성 후 text/xml형태로 정보를 전달한다.

![https://www.thistechnologylife.com/soap-vs-rest/](https://i2.wp.com/www.thistechnologylife.com/wp-content/uploads/2019/04/SOAP-vs-REST-1.png?resize=1200%2C469&ssl=1)

![https://www.geeksforgeeks.org/difference-between-rest-api-and-soap-api/](https://media.geeksforgeeks.org/wp-content/uploads/20190418141401/diag1.jpg)

  
  
  

## uniform interface

uniform interface는 정해진 룰이 존재한다.

  1. 리소스는 URI로 구분되어야한다.
  2. 리소스를 생성/추가/삭제할때는 HTTP메세지의 상태정보를 사용해서 전달해야한다.
  3. 메세지는 스스로 설명가능해야한다. 즉 메세지 자체에 바로 이해할 수 있는 의미가 있어야한다.
  4. 프로그램 상태는 하이퍼링크로 전달 가능해야한다.

  
  
  

## @ResponseBody와 @RestController

| | @ResponseBody | @RestController  
---|---|---  
사용가능버전 | 스프링3버전부터 | 스프링4버전부터  
개념 | 객체를 json으로 만들어주는 어노테이션 | jsp뷰를 찾아가는게 아니라 데이터를 생성하는 것(REST방식)  
사용특징 | 메서드/리턴타입에 사용가능 | 클래스에만 사용  
특징 | MessageConverter에 의해서 처리되는 정보가 브라우저로 전달되는 처리방식 | 하위의 메서드는 @ResponseBody가 없어도 동일하게 처리된다(@ResponseBody생략됨)  
  
![https://mangkyu.tistory.com/49](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F7bceC%2Fbtqx8K6BbxE%2FLVs4KK74mUj9CZ70uHTsjK%2Fimg.png)

  
  
  

## 예시

  * [jackson-databind 라이브러리 추가](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind/2.8.4)
  * [jQuery 3.x snippet 뷰페이지에 복붙](https://developers.google.com/speed/libraries#jquery)

### 어노테이션특징

  * @PathVariable : 요청URL에 있는 매개변수를 json형태로 가져옴
    * 주소의 {num}값을 저장하여 사용가능
  * @RequestBody : JSON형태로 전달된 데이터를 해당 파라미터 타입에 자동으로 저장하겠다는 의미

### 소스코드

  * `TestController.java` 소스코드
    * @RestController를 활용하여 String, int, List, Map, JSON객체까지 데이터처리를 할 수 있다.

```java
package com.itwillbs.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.itwillbs.domain.SampleVO;

@RestController
@RequestMapping(value = "/test/*")
public class TestController {
	//@ResponseBody : 객체를 json으로 만들어주는 어노테이션
	//@RestController : 스프링4부터, 하위의 메서드는 @ResponseBody가 없어도 동일하게 처리된다(@ResponseBody생략됨)

	//http://localhost:8088/test/hello
	@RequestMapping(value= "hello", method= RequestMethod.GET)
	public String hello() {
		//문자열리턴의 목적은 : jsp페이지로 가는 것이 아니라 문자열타입의 데이터를 리턴하거나 생성하는 목적으로 사용된다.
		return "Hello ITWILL!"; //text형태로 보여짐
	}
	
	//http://localhost:8088/test/sendVO
	@RequestMapping(value= "sendVO")
	public @ResponseBody SampleVO sendVO() {
		SampleVO svo = new SampleVO(1, "나혜석", "010-123-4567" );
		return svo;
	}
	
	//컬렉션객체활용 1.List(리스트)
	//http://localhost:8088/test/sendList
	@RequestMapping(value = "sendList")
	public List<SampleVO> sendList(){
		List<SampleVO> voList = new ArrayList<SampleVO>();
		
		for(int i=0;i<10;i++) {
			SampleVO vo = new SampleVO(i, "나혜석", "0"+i+"0-123-4567" );
			voList.add(vo);
		}
		return voList;
	}
	
	//컬렉션객체활용 2.Map
	//http://localhost:8088/test/sendMap
	@RequestMapping(value = "sendMap")
	public Map<Integer, SampleVO> sendMap(){
		Map<Integer, SampleVO> voMap = new HashMap<Integer, SampleVO>();
		for(int i=0;i<10;i++) {
			SampleVO vo = new SampleVO(i, "나혜석", "0"+i+"0-123-4567" );
			
			voMap.put(i, vo);
		}
		return voMap;
	}
 	
	//파라미터들을 json데이터로 꺼내올 수 있음
	//http://localhost:8088/test/board2/1234
	//@RequestMapping(value = "board/{num}")
	public int board(@PathVariable("num") int num) {
		return num; //숫자리턴은 json형태가 된다.
	}
	
	//String타입 매개변수도 사용가능하다 
	@RequestMapping(value = "board/{num}")
	public int board(@PathVariable("num") String num) {
		System.out.println(num);
		return 0; //숫자리턴은 json형태가 된다.
	}
	
	//String타입 매개변수도 사용가능하다 
	@RequestMapping(value = "board2/{num}")
	public SampleVO board2(@PathVariable("num") int num) {
		SampleVO vo = new SampleVO(num, "나혜석", "0"+num+"0-123-4567" );
		return vo; //숫자리턴은 json형태가 된다.
	}
	
	//ajax로 데이터전달받기
	@RequestMapping(value = "info", method = RequestMethod.POST)
	public void checkVO(@RequestBody SampleVO vo) {
		//@RequestBody : JSON형태로 전달된 데이터를 해당타입(여기서는 SampleVO)에 자동으로 저장함
		System.out.println("REST컨트롤러 checkVO메서드 호출"+vo);
	}	
}
```

  * `SampleVO.java` 소스코드

```java
package com.itwillbs.domain;

public class SampleVO {
	private Integer num;
	private String name;
	private String tel;
	
	public SampleVO() {};
	public SampleVO(Integer num, String name, String tel) {
		super();
		this.num = num;
		this.name = name;
		this.tel = tel;
	}
	public Integer getNum() {
		return num;
	}
	public void setNum(Integer num) {
		this.num = num;
	}
	(이하생략)
}
```

  * `JSONTest.jsp` 소스코드
    * [JSON.stringify(member)](https://www.w3schools.com/js/js_json_stringify.asp) : member변수로 만든 객체를 문자열로 바꾼다.

```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<!-- 제이쿼리 라이브러리추가 -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script type="text/javascript">
$(function(){
	//alert("제이쿼리 테스트")

	//뷰에서 버튼 클릭시, 전달한 데이터를 JSON형태로 생성 후 전송 -> ajax 비동기방식사용하여 RestController로 이동 -> RestController안에서 정보를 전달받아서 표시
	$('#checkJsonBtn').click(function(){
		//1.JSON형태로 데이터 생성
		let member = {num: "777", name: "사용자1", tel: "010-777-7777"};
		//2.데이터를 ajax 비동기방식으로 전송
		$.ajax({
			type:"post",
			url:"${contextPath}/test/info", //contextPath는  컨크롤러의 시작지점(/)을 의미
			contentType: "application/json",
			data: JSON.stringify(member), //member변수로 만든 객체를 문자열로 바꿔서 보낸다는 의미
			success:function(){
				 alert("ajax 이동 성공")
				},
			error:function(){
				 alert("ajax 이동 실패")
				},
			complete:function(){
				alert("ajax complete 항상 실행(이건 성공/실패 유무와 상관없이 항상 실행됨)")
				}
			});
	});
});
</script>
</head>
<body>
<h1>JSONtest.jsp</h1>
일반컨트롤러(HomeController)로 접속 후 input태그 사용<br>
<input type="button" id="checkJsonBtn" value="회원정보전송">
</body>
</html>
```

  
  
  

## REST API를 RESTful API로!

[이상학 - RESTful API 설계 가이드](https://sanghaklee.tistory.com/57)를 참고하니 좋은 내용이 정말 많았다. 꼭 읽어봐야하는 글이다!

정리

분류 | 설명 | 추가설명  
---|---|---  
URL Rules 1 | 마지막에 / 포함하지 않는다. |   
URL Rules 2 | `_(underbar)` 대신 `-(dash)`를 사용한다. |   
URL Rules 3 | 소문자를 사용한다. |   
URL Rules 4 | 행위(method)는 URL에 포함하지 않는다. |   
URL Rules 5 | 컨트롤 자원을 의미하는 URL 예외적으로 동사를 허용한다. |   
Set HTTP Headers 1 | Content-Location |   
Set HTTP Headers 2 | Content-Type |   
Set HTTP Headers 3 | Retry-After | 인증, 자원 요청  
Set HTTP Headers 4 | Link |   
Use HTTP methods 1 | POST, GET, PUT, DELETE 4가지 methods는 반드시 제공한다. |   
Use HTTP methods 2 | OPTIONS, HEAD, PATCH를 사용하여 완성도 높은 API를 만든다. | OPTIONS, HEAD, PATCH  
Use HTTP status 1 | 의미에 맞는 HTTP status를 리턴한다. |   
Use HTTP status 2 | HTTP status만으로 상태 에러를 나타낸다. |   
Use the correct HTTP status code 1 | 성공 응답은 2XX로 응답한다. |   
Use the correct HTTP status code 2 | 실패 응답은 4XX로 응답한다. |   
Use the correct HTTP status code 3 | 5XX 에러는 절대 사용자에게 나타내지 마라! |   
Use HATEOAS | 구성 요소 |   
Paging | Paging Key | HTTP Header의 Link 속성을 이용하고 HATEOAS로 응답한다.  
Ordering | Ordering |   
Filtering |  |   
Field-Selecting |  |   
Versioning | 예외적으로 서비스의 기본 도메인이 3차인 경우 path level에 모두 명시한다. |   
  
  
  
  

### Use HTTP status

RESTful API를 설계하기 위해선 HTTP status를 정확하게 사용해야한다.  
서버API를 개발하다보면 흔하게(?) 받는 요청사항이 모든 응답을 200으로 처리하고 body 내용으로 성공|실패를 판단하게끔 해달라는 것이었다. 이는 사실 잘못된 설계이다.  
그와 관련해서 [이상학 - REST API 관점에서 바라보는 HTTP 상태 코드(HTTP status code)](https://sanghaklee.tistory.com/61)글이 정말 좋다. 강력추천!

#[RESTfulAPI](/tags/RESTfulAPI/)
