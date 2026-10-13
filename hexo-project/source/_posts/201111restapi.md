---
title: "[REST API]ResponseEntity 타입클래스"
date: 2020-11-10 20:05:39
tags:
  - "ITWILL(JAVA)"
  - "RESTfulAPI"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">ResponseEntity 타입클래스의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    @RestController는 결과로 view를 제공하지 않기때문에 에러 발생유무를 확인할 수 없다.</p>
</div>

<!-- more -->

## `@RestController`의 한계

@RestController는 결과로 view를 제공하지 않기때문에 에러 발생유무를 확인할 수 없다.  
이때 사용할 수 있는 것이 `웹 HTTP 상태 코드`이다.

  
  
  

## HTTP 상태코드

  * [HTTP 상태코드 MDN](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)
  * [에러처리하는 방법](https://sowon-dev.github.io/2020/07/15/200715jspi/)

![https://slidesplayer.org/slide/14780959/](https://player.slidesplayer.org/90/14780959/slides/slide_18.jpg)

구분 | 코드 | 설명  
---|---|---  
100번대 |  | 현재 데이터의 처리중인 상태  
| 100 | 데이터의 일부만 서버가 받은 경우  
200번대 |  | 정상적인 응답상태  
| 200 | 에러가 없이 정상처리된 경우  
| 204 | 정상처리가 되었으나 서버에 전달할 값이 없는 경우  
300번대 |  | 다른 URL을 처리하는 상태  
| 301 | 요청된 페이지가 새 URL로 변경된 경우  
| 304 | 이미 기존의 데이터와 변경이 없는 경우  
400번대 |  | 서버에서 인식불가한 상태  
| 400 | 전송된 Request객체에 문제가 있어 서버가 인지하지 못하는 경우  
| 403 | 서버에서 허락되지 않는 경우(서버에 접근권한이 없는 경우)  
| 404 | URL에 해당하는 자원을 찾을 수 없는 경우  
| 406 | 전송방식의 오류 발생한 경우(주로 REST작동시 발생)  
500번대 |  | 서버 내부의 문제가 발생한 상태  
| 500 | 서버에서 처리시 문제가 발생한 경우  
| 502 | 게이트웨이, 프록시에 문제가 발생한 경우(=과부화, 개발자의 영역이 아니라 엔지니어의 영역임)  
| 503 | 일시적인 과부화 상태인 경우, 서비스 중단상태인 경우(개발자의 영역이 아니라 엔지니어의 영역임)  
| 504 | 지정된 처리시간이 지나서 처리를 못하는 경우  
  
  
  
  

## ResponseEntity 타입클래스

  * HTTP 상태코드를 활용하여 상태처리를 할 수 있다.
  * @RestController사용하지 않고 일반컨트롤러에서도 @ResponseBody을 통해서 rest로 처리가능하다.
  * ResponseEntity를 사용하면 단순한 객체 정보도 JSON형태로 전달가능하지만, HTML 정보와 JS정보까지 전달할 수 있다.(예를 들어 Header정보)
    * 이를 통해 결과확인 및 오류메세지 체크가 가능해진다.

```java
@RestController
@RequestMapping(value = "/test/*")
public class TestController {

	//ResponseEntity를 사용하면 단순한 객체 정보도 JSON형태로 전달가능하지만,
	//HTML 정보와 JS정보까지 전달할 수 있다.(예를 들어 Header정보)
	//이를 통해 결과확인 및 오류메세지 체크가 가능해진다.
	@RequestMapping(value = "res2")
	public ResponseEntity res2() {
		System.out.println("res2 메서드 호출");
		
		//응답정보 중에 header에 데이터를 add해서 보낸다.
		HttpHeaders responseHeaders = new HttpHeaders();
		responseHeaders.add("Content-type", "text/html; charset=UTF-8");
		String msg = "<script>";
		msg += "alert('얼럿창테스트');";
		msg += "location.href='/res1';";
		msg += "</script>";
		
		return new ResponseEntity(msg,responseHeaders, HttpStatus.INTERNAL_SERVER_ERROR);
	}
}
```

#[ITWILL(JAVA)](/tags/ITWILL-JAVA/)[RESTfulAPI](/tags/RESTfulAPI/)
