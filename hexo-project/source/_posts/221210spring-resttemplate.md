---
title: "[Spring]RestTemplate과 HttpEntity가 뭐길래(제네릭과 ParameterizedTypeReference)"
date: 2022-12-09 19:32:44
tags:
  - "RestTemplate"
  - "HttpEntity"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">RestTemplate과 HttpEntity가 뭐길래(제네릭과 ParameterizedTypeReference)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    스프링어플리케이션에서 HTTP요청할때 사용하며 주로 외부API와 연동할때 RestTemplate와 함께 MultiValueMap, HttpEntity도 사용한다.</p>
</div>

<!-- more -->

프로젝트를 하다보면 화면이 아닌 서비스단에서 외부 API와 호출해야할 일들이 생긴다.  
이때 주로 사용되는 것이 RestTemplate이다.

이번 프로젝트에서 백엔드 업무를 도맡았다. 첫 작업으로 맡게 된 건 외부 프로그램과 API로 연동하는 작업이었다.  
Http통신을 화면에서 수도없이 날렸지만 서비스단에서 하는 건 업무로썬 처음이었다. 결론 너무 재밌다!  
역시 난 프론트보단 백이 더 재밌어.

# ✍ RestTemplate 이란?

스프링 3.0에서부터 지원하는 객체로 REST방식으로 API를 호출할 수 있는 내장 클래스이다.  
스프링어플리케이션에서 HTTP요청할때 사용하며 주로 외부API와 연동할때 RestTemplate와 함께 MultiValueMap, HttpEntity도 사용한다.  
다만, 스프링프레임워크5부터는 [WebClient](https://www.baeldung.com/spring-5-webclient)사용을 권장하고 있기에 조만간 RestTemplate은 deprecated 될지도 모른다.

  * 특징

    * RESTful 원칙을 지킴
    * 멀티쓰레드 방식 사용
    * [Blocking(동기) 방식 사용](https://sowon-dev.github.io/2019/09/23/190924/#2-%EB%8F%99%EA%B8%B0%EC%99%80-%EB%B9%84%EB%8F%99%EA%B8%B0-%EA%B0%9C%EB%85%90%EC%84%A4%EB%AA%85-Blocking-VS-non-blocking)
  * 함수

    * ![출처: https://velog.io/@soosungp33/%EC%8A%A4%ED%94%84%EB%A7%81-RestTemplate-%EC%A0%95%EB%A6%AC%EC%9A%94%EC%B2%AD-%ED%95%A8](https://velog.velcdn.com/images%2Fsoosungp33%2Fpost%2Fd02efacc-56e6-4abc-a390-12ecbb565c6b%2Fimage.png)
    * 가장 많이 사용하는 메서드는 당연 exchage()이다.
    * exchage() : 모든 HTTP 요청 메소드를 지원하며 원하는 서버에 요청시켜주는 메소드

```plain
ResponseEntity<원하는클래스타입> resultMap = restTemplate.exchange(uri.toString(), HttpMethod.원하는통신, entity, 원하는클래스타입.class);
```

  
  
  

# ✍ 사용방법

  
  
  

## 1 의존성 설정

스프링부트를 사용하면 이미 포함되어있으므로 의존성 설정을 따로 해줄 필요가 없다.

```java
implementation 'org.springframework.boot:spring-boot-starter-web'
```

  
  
  

## 2 RestTemplate의 생성

  1. Header 생성: HTTP요청을 보낼때 Body를 설명해주는 Header도 같이 보내야한다.
  2. Body 생성: key-value 형식인 MultiValueMap 타입을 사용해서 만든다.
  3. HttpEntity생성: HTTP통신을 하려면 Header와 Body가 하나여야하는데 HttpEntity클래스가 Header와 Body를 합쳐준다. 

```java
public class RestTemplateClientService {

public String test() {
        // 1. Header생성
		HttpHeaders headers = new HttpHeaders();
		headers.add("content-type", "application/json");
		
		// 2. Body생성
		MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
		params.add("name", "sowon-dev");
		
		// 3. HttpEntity생성
		HttpEntity<MultiValueMap<String, String>> entity = new HttpEntity<>(params, headers);
		
		// 4. HTTP 통신
		RestTemplate rt = new RestTemplate();
		ResponseEntity<Map> response = rt.exchange(
                "http://localhost:3000/", //요청할 서버주소
                HttpMethod.POST, //요청방식
                entity, //요청데이터
                String.class //반환되는 데이터타입
		);
		
		// 5. Map데이터타입을 메서드리턴타입인 String형태로 파싱
		ObjectMapper mapper = new ObjectMapper();
		jsonInString = mapper.writeValueAsString(response.getBody());
		
		return jsonInString;
    }
}
```

  
  
  

# ✍ 만약 exchange 메서드에서 Generic 클래스를 사용하고싶다면?

위의 4번에서 exchange()할때 반환되는 데이터타입이 제네릭클래스라면 어떻게 처리할까?  
하루종일 구글링한 방법을 정리하고자한다.

  
  
  

## 1 현재 상황

아래처럼 `ResponseVO<T>클래스`와 `TestVO 클래스`가 선언되어있다.

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

exchange()를 실행하고자한다.

```java
ResponseEntity<ResponseVO<TestVO>> response = rt.exchange(
                "http://localhost:3000/",
                HttpMethod.POST,
                testJson,
                ResponseVO<TestVO>.class //반환되는 데이터타입
		);
```

당연히 잘 될꺼라고 생각했던 코드에 빨간 밑줄이 생기면서 에러가 발생했다.

```plain
// 에러메시지
ResponseVO cannot be resolved to a variable
TestVO cannot be resolved to a variable
```

제네릭클래스인 경우 인스턴스를 어떻게 생성해야할까?

  
  
  

## 2 ParameterizedTypeReference로 해결

  * 정의: [ParameterizedTypeReference](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/core/ParameterizedTypeReference.html)는 제네릭형식을 

```java
ResponseEntity<ResponseVO<TestVO>> response = rt.exchange(
	"http://localhost:3000/",
	HttpMethod.POST,
	testJson,
	new ParameterizedtypeReference<ResponseVO<TestVO>>(){} //반환되는 데이터타입
);
```

잘해결되었지만 어떤 문제가 있었던걸까? 원인을 알아봤다.

## 3 문제 원인

  * 제네릭은 데이터타입을 클래스 내부에서 지정하는 것이 아닌 외부에서 사용자가 지정한다. 
  * 자바는 컴파일시에 제네릭 타입 정보들을 제거 한다.런타임시에는 실제로 타입정보는 존재 하지 않고 강제 캐스팅 된다.

> 이런 제네릭 정보가 지워지는 문제 때문에 Super type token 기법이 생겨났다.  
> Super type token은 수퍼(상위)타입을 토큰으로 사용하겠다는 의미이다. 무슨말인가?  
> 제네릭 정보가 컴파일시 런타임시 다 지워지지만 제네릭 정보를 런타임시 가져올 방법이 존재한다. 제네릭 클래스를 정의한 후에 그 제네릭 클래스를 상속받으면 런타임시에는 제네릭 정보를 가져올 수 있다.  
> Class의 메소드의 public Type getGenericSuperclass() 메소드를 통해 구할수 있다. getGenericSuperclass() 이용하여 바로 위의 슈퍼 클래스의 타입을 반환한다. 상위타입은 제네릭의 타입토큰 정보가 존재한다.  
> 슈퍼(상위)타입의 제네릭 파라미터정보인 Type을 통해 제네릭 파라미터 클래스 정보를 가져온다.  
> 출처: <https://ka0oll.tistory.com/m/6>

제네릭 정보가 지워지는 문제때문에 제네릭타입은 인스턴스를 생성할 수 없는게 흥미로웠다. 구글링할수록 자바를 깊이있게 알 수 있어서 재밌었고 좋은 글 써주신 분들 덕분에 한결 쉽게 이해할 수 있었다.

  
  
  

# 참고

  * <https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/client/RestTemplate.html>
  * <https://sowon-dev.github.io/2021/08/11/210812Spring-resttemplate/>
  * <https://jung-story.tistory.com/132>
  * <https://www.baeldung.com/rest-template>
  * <https://tecoble.techcourse.co.kr/post/2021-07-25-resttemplate-webclient/>
  * <https://vmpo.tistory.com/27>
  * <https://www.skyer9.pe.kr/wordpress/?p=1476>
  * <https://countryxide.tistory.com/148>
  * <https://ka0oll.tistory.com/m/6>

#[RestTemplate](/tags/RestTemplate/)[HttpEntity](/tags/HttpEntity/)
