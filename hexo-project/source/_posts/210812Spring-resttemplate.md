---
title: "[Spring]RestTemplate 활용"
date: 2021-08-11 15:00:00
tags:
  - "패스트캠퍼스(초격차Java/Spring)"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">RestTemplate 활용의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    클라이언트와 서버끼리 RestTemplate객체를 사용하여 JSON을 주고받을 수 있다.</p>
</div>

<!-- more -->

클라이언트와 서버끼리 RestTemplate객체를 사용하여 JSON을 주고받을 수 있다.

## 클라이언트

클라이언트에서 GET방식, POST방식으로 서버에 응답을 요청해보자.

  
  
  

### ClientApiController.java

```java
@Slf4j
@RestController
@RequestMapping("/api/client")
public class ClientApiController {
	
	@Autowired
	private RestTemplateService service;
	
	@GetMapping("")
	public UserResponse getHello() {
		log.info("get메서드 호출");
		return service.hello();
	}
	
	@PostMapping("")
	public void post() {
		log.info("post메서드 호출");
		service.post();
	}

	@GetMapping("/exchange")
	public UserResponse exchange() {
		log.info("exchange메서드 호출");
		return service.exchange();
	}
	
	@GetMapping("/genericExchange")
	public Req<UserResponse> genericExchange() {
		log.info("genericExchange메서드 호출");
		return service.genericExchange();
	}
}
```

  
  
  

### RestTemplateService.java

  * UriComponentsBuilder: 원하는 uri를 만들 수 있는 객체

```java
@Service
public class RestTemplateService {
	
	public UserResponse hello() {
		//클라이언트이므로 주소를 만들어서 리턴해야한다 -> 이때 URI컴포넌트를 주로 사용함.
		URI uri = UriComponentsBuilder
				.fromUriString("http://localhost:9090")
				.path("/api/server")
				//쿼리파람을 사용할 수 있다.
				.queryParam("name", "신경숙")
				.queryParam("age", 22)
				.encode()
				.build()
				.toUri();
		System.out.println("@ uri.toString(): " + uri.toString());
		
		/* =====================================================================
		 * getForObject()와 getForEntity()의 차이
		 * 여기서 get은 가져온다의 get이 아니라 HTTP GET 메서드의 get이다.
		 * getForObject(): Object형태
		 * getForEntity(): Entity형태로 getStatusCode(), getBody()를 확인할 수 있어 유용
		 * 
		 * =====================================================================
		 * 두 방식 다 동일한 결과를 나타냄
		 * 1. String으로 테스트
		 * 호출: http://localhost:8083/api/client
		 * 결과: 안녕 나는 클라이언트야, 내가 사라져볼께 얍! 안녕 나는 서버야
		 * 
		 * 2. UserResponse로 json 받기
		 * 호출: http://localhost:8083/api/client
		 * 결과: {
		 *		    "name": "신경숙",
		 *		    "age": 22
		 *		}
		 */
		
		// 상세정보를 알기 위해서 ResponseEntity를 받는 것을 추천
		RestTemplate rt = new RestTemplate();
		
//		String result1 = rt.getForObject(uri, String.class);
		UserResponse result1 = rt.getForObject(uri, UserResponse.class);
		System.out.println("@ result1: "+result1.toString());

		
//		ResponseEntity<String> result2 = rt.getForEntity(uri, String.class);
		ResponseEntity<UserResponse> result2 = rt.getForEntity(uri, UserResponse.class);
		System.out.println("@ HTTP CODE확인: "+result2.getStatusCode());
		System.out.println("@ BODY 확인: "+result2.getBody());
		
		return result2.getBody();
	}
	
	public void post() {
		
		URI uri = UriComponentsBuilder
				.fromUriString("http://localhost:9090")
				.path("/api/server/user/{userId}/name/{userName}")
				.encode()
				.build()
				//위 PathVariable과 expand()안 콤마로 순서대로 매칭
				.expand("wony", "choi")
				.toUri();
		
		System.out.println("@ uri.toString(): " + uri.toString());
		
		UserRequest req = new UserRequest();
		req.setAge(44);
		req.setName("최정원");
		
		RestTemplate rt = new RestTemplate();
		ResponseEntity<UserResponse> res = rt.postForEntity(uri, req, UserResponse.class);
		System.out.println("@ HTTP CODE확인: "+res.getStatusCode());
		System.out.println("@ HTTP Header확인: "+res.getHeaders());
		System.out.println("@ BODY 확인: "+res.getBody());
	}

	public UserResponse exchange() {
		
		URI uri = UriComponentsBuilder
				.fromUriString("http://localhost:9090")
				.path("/api/server/user/{userId}/name/{userName}")
				.encode()
				.build()
				//위 PathVariable과 expand()안 콤마로 순서대로 매칭
				.expand("wony", "choi")
				.toUri();
		
		System.out.println("@ uri.toString(): " + uri.toString());
		
		UserRequest userReq = new UserRequest();
		userReq.setAge(44);
		userReq.setName("최정원");
		
		// requestEntity로 header에 원하는 데이터를 넣어서 보낼 수 있다.
		RequestEntity<UserRequest> reqEntity = RequestEntity
				.post(uri)
				.contentType(MediaType.APPLICATION_JSON)
				.header("x-authorization", "abc")
				.header("custom-header", "ABC")
				.body(userReq);
				
		RestTemplate resTemplate = new RestTemplate();
		ResponseEntity<UserResponse> res = resTemplate.exchange(reqEntity, UserResponse.class);
		return res.getBody();
		
	}
	
	// 내가 원하는 Req<UserResponse> 타입의 JSON형태 주고 받기
	/*{
	    "header": {
	        "resCode": null
	    },
	    "responseBody": {
	        "name": "가나다",
	        "age": 55
	    }
	}*/
	public Req<UserResponse> genericExchange() {
		
		URI uri = UriComponentsBuilder
				.fromUriString("http://localhost:9090")
				.path("/api/server/user/{userId}/name/{userName}")
				.encode()
				.build()
				//위 PathVariable과 expand()안 콤마로 순서대로 매칭
				.expand("wony", "choi")
				.toUri();
		
		System.out.println("@ uri.toString(): " + uri.toString());
		
		UserRequest userReq = new UserRequest();
		userReq.setAge(55);
		userReq.setName("가나다");
		
		Req<UserRequest> req = new Req<>();
		req.setHeader(new Req.Header());
		req.setResponseBody(userReq);
		
		// requestEntity로 header에 원하는 데이터를 넣어서 보낼 수 있다.
		RequestEntity<Req<UserRequest>> reqEntity = RequestEntity
				.post(uri)
				.contentType(MediaType.APPLICATION_JSON)
				.header("x-authorization", "abc")
				.header("custom-header", "ABC")
				.body(req);
		
		RestTemplate resTemplate = new RestTemplate();
		// 제네릭에는 class를 사용할 수 없다 즉, Req<UserResponse>.class -> 오류발생 -> 따라서 RestTemplate의 ParameterizedTypeReference를 사용해야한다. 
		// ResponseEntity<Req<UserResponse>> res = resTemplate.exchange(reqEntity, Req<UserResponse>.class);
		ResponseEntity<Req<UserResponse>> res = resTemplate.exchange(reqEntity, new ParameterizedTypeReference<Req<UserResponse>>(){});
		return res.getBody();
		
	}
	
	
}
```

  
  
  

### UserResponse.java

응답 DTO이다.

```java
@Data
public class UserResponse {
	private String name;
	private int age;
}
```

  
  
  

### UserRequest.java

요청 DTO이다.

```java
@Data
public class UserRequest {
	private String name;
	private int age;
}
```

  
  
  

### Req.java

DTO이다. 제네릭타입으로 원하는 JSON형태를 만들 수 있다.

```java
@Data
public class Req<T> {

	private Header header;
	private T responseBody;
	
	@Data
	public static class Header{
		private String resCode;
	}
```

  
  
  

## 서버

클라이언트의 요청에 적절한 응답을 할 수 있다.

  
  
  

### ServerApiComtroller.java

  * 순수한 HttpEntity을 파라미터 변수로 받으면 디버깅 등에 유용하다

```java
@Slf4j
@RestController
@RequestMapping("/api/server")
public class ServerApiComtroller {

	@GetMapping("")
	public User hello(@RequestParam String name, @RequestParam int age) {
		User u = new User();
		u.setName(name);
		u.setAge(age);
		return u;
	}
	
//	@PostMapping("/user/{userId}/name/{userName}")
	public User post(@RequestBody User user, 
					 @PathVariable String userId, 
					 @PathVariable String userName) {
		log.info("client req: {}", user);
		log.info("userId: {}, userName: {}", userId, userName);
		return user;
	}
	
//	@PostMapping("/user/{userId}/name/{userName}")
	public User exchange(@RequestBody User user, 
						 @PathVariable String userId,
						 @PathVariable String userName,
						 @RequestHeader("x-authorization") String xAuthorization,
						 @RequestHeader("custom-header") String customHeader
						 ) {
		log.info("client req: {}", user);
		log.info("userId: {}, userName: {}", userId, userName);
		log.info("xAuthorization: {}, customHeader: {}", xAuthorization, customHeader);
		return user;
	}

	// 순수한 HttpEntity<String>을 파라미터 변수로 받으면 디버깅 등에 유용하다
	@PostMapping("/user/{userId}/name/{userName}")
	public Req<User> genericExchange(
//							HttpEntity<String> entity, 
							@RequestBody Req<User> user, 
							@PathVariable String userId,
							@PathVariable String userName,
							@RequestHeader("x-authorization") String xAuthorization,
							@RequestHeader("custom-header") String customHeader
		) {
//		log.info("entity 순수한 : {}", entity);
		log.info("HttpEntity<String> 디버깅 등에 유용: {}", user);
		log.info("userId: {}, userName: {}", userId, userName);
		log.info("xAuthorization: {}, customHeader: {}", xAuthorization, customHeader);
		
		// 원하는 json형태로 응답하기
		/*{
		    "header": {
		        "resCode": null
		    },
		    "responseBody": {
		        "name": "가나다",
		        "age": 55
		    }
		}*/
		Req<User> response = new Req<>();
		response.setHeader(new Req.Header());
		response.setResponseBody(user.getResponseBody());
		
		return response;
	}
}
```

  
  
  

### User.java

  * @Data: @ToString, @EqualsAndHashCode, @Getter(모든 필드), @Setter(정적 필드가 아닌 모든 필드), @RequiredArgsConstructor
  * @NoArgsConstructor: 파라미터가 없는 기본 생성자 생성
  * @AllArgsConstructor: 모든 필드 값을 파라미터로 받는 생성자 생성

```java
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
	private String name;
	private int age;
}
```

  
  
  

### Req.java

DTO이다. 제네릭타입으로 원하는 JSON형태를 만들 수 있다.

```java
@Data
public class Req<T> {

	private Header header;
	private T responseBody;
	
	@Data
	public static class Header{
		private String resCode;
	}
}
```

#[패스트캠퍼스(초격차Java/Spring)](/tags/%ED%8C%A8%EC%8A%A4%ED%8A%B8%EC%BA%A0%ED%8D%BC%EC%8A%A4-%EC%B4%88%EA%B2%A9%EC%B0%A8Java-Spring/)
