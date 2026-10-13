---
title: "[Spring]ResponseEntity 코드리뷰"
date: 2022-12-20 15:31:41
tags:
  - "차이"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">ResponseEntity 코드리뷰의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    RestTemplate을 통해서 외부 API와 통신하는 메서드를 구현하고 있었다.</p>
</div>

<!-- more -->

RestTemplate을 통해서 외부 API와 통신하는 메서드를 구현하고 있었다.  
팀장님이 내 코드를 보시더니 코드리뷰를 해주셨다. (바쁘신 와중에도 코드봐주셔서 감사합니다🙂)

# 내코드

```java
// ResponseVO<T> 클래스
public class ResponseVO<T> {
	private int code;
	private T payload;
}

// testVO 클래스
public class TestVO {
	private int id;
	private String message;
}
```

아래처럼 exchange()를 실행하는 코드였다. RestTemplate과 HttpEntity가 궁금한 사람은 [RestTemplate과 HttpEntity가 뭐길래](https://sowon-dev.github.io/2022/12/09/221210spring-resttemplate/)글을 참고하면 된다.

```java
ResponseEntity<ResponseVO<TestVO>> response = rt.exchange(
	"http://localhost:3000/",
	HttpMethod.POST,
	testJson,
	new ParameterizedtypeReference<ResponseVO<TestVO>>(){} //반환되는 데이터타입
);
```

여기서 좀 더 나은 코드가 있다고 말씀해주셨다.

  
  
  

# 코드리뷰

OOP(객체지향프로그램)를 설명해주시면서 java lang reflect으로 데이터타입을 유연하게 가져갈 수 있다고 말씀해주셨다.

```java
ResponseEntity<String> responseEntity = rt.exchange(
	"http://localhost:3000/", 
	HttpMethod.POST, 
	httpEntity, 
	string.class
);
String bodyofResponseEntity = responseEntity.getBody();
Gson gson= new Gson();
Type gType = TypeToken.getparameterized(ResponseVO.class, TestVO.class).getType():
ResponseVO<TestVO> responsevo = gson.fromJson(responseentity.getBody(), gType);
```

기존 코드와 가장 큰 차이점은 ResponseEntity반환데이터 타입을 String으로 설정했다는 점이다.  
그 이유는 무엇일까?  
만약 특정한 데이터타입을 지정해놓으면 exchange()한 뒤 반환데이터타입 형식이 안 맞는 경우 exchage()를 성공적으로 수행했음에도 타입변환에러가 발생한다.  
이를 예방하기 위해 String으로 반환데이터를 받으면된다!

  
  
  

## 반환데이터타입을 왜 굳이 String을 쓸까?

반환타입을 String으로 쓰면 좋은 점은 크게 3가지가 있다.

  1. exchage()하는 도중에 에러가 발생한건지, 캐스팅중에 에러가 발생한건지 명확하게 파악가능
  2. String변수`bodyofResponseEntity`에 값을 대입함으로서 데이터 유실을 예방가능

  
  
  

## String데이터를 원하는 데이터로 캐스팅하려면?

[구글에서 만든 Gson](https://sites.google.com/site/gson/gson-user-guide#TOC-Using-Gson)을 이용하면 된다.  
String데이터를 Gson으로 원하는 `ResponseVO<TestVO>`로 변환하면 해결!

```java
Gson gson= new Gson();
Type gType = TypeToken.getparameterized(ResponseVO.class, TestVO.class).getType():
ResponseVO<TestVO> responsevo = gson.fromJson(responseentity.getBody(), gType);
```

#[차이](/tags/%EC%B0%A8%EC%9D%B4/)
