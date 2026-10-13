---
title: "[스프링Spring]에러 커스텀하기"
date: 2021-08-03 21:35:42
tags:
  - "패스트캠퍼스(초격차Java/Spring)"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Exceprion이 발생했을 때 어떤 부분의 예외인지 그 이름을 알고 싶을때 Exception클래스 내 e.getClass().getName()메서드를 사용할 수 있다.
    * @ControllerAdvice: 글로벌 예외처리을 통해 문제를 해결할 수 있다.</p>
</div>

<!-- more -->

## 예외처리 어노테이션

  * `@ControllerAdvice`: 글로벌 예외처리
    * 속성 basePackageClasses
  * `@ControllerAdvice(특정패키지명)`: 괄호안에 특정 package명을 기재하면 해당 package만 예외처리함
    * @ControllerAdvice(“com.test.springeprjt”): excom.test.springeprjt를 라는 특정 package 예외처리
  * `@ExceptionHandler`: 특정 controller예외처리

Exceprion이 발생했을 때 어떤 부분의 예외인지 그 이름을 알고 싶을때 Exception클래스 내 `e.getClass().getName()`메서드를 사용할 수 있다.

  
  
  

## 다른 개발자가 봐도 알기쉽도록 메시지를 꾸며보자

  * ErrorResponse.java  
한 파라미터에 조건이 여러 개가 있을 수 있으므로 List로 에러필드와 에러메시지를 받을 필요가 있다.

```java
@Data
public class ErrorResponse {
	String statusCode;
    String requestUrl;
    String code;
    String message;
    String resultCode;

    List<Error> errorList;
}
```

  * Error.java

```java
@Data
public class Error {
	private String field; //파라미터명
	private String message; //오류메시지
	private String invalidValue; //입력한 값
}
```

이제 제일 중요한 컨트롤러 부분을 보자.

  * ApiControllerAdvice.java  
String으로 각각 에러값을 받은 다음 위에서 선언한 Error클래스에 set해준 뒤 list에 add해준다.  
각 예외클래스마다 사용할 수 있는 것들이 다르니 디버그나 공식문서를 통해서 원하는 내용을 찾으면 된다!

아래 예시는 가장 기본이 되는 방식

```java
// 다른 컨트롤러들말고 오로지 ApiController에서만 사용하고싶을때 basePackageClasses속성을 사용한다
@RestControllerAdvice(basePackageClasses = ApiController.class)
public class ApiControllerAdvice {
	 @ExceptionHandler(value = MethodArgumentNotValidException.class)
    public ResponseEntity methodArgumentNotValidException(MethodArgumentNotValidException e, HttpServletRequest httpServletRequest){

        List<Error> errorList = new ArrayList<>();

        BindingResult bindingResult = e.getBindingResult();
        bindingResult.getAllErrors().forEach(error -> {
            FieldError field = (FieldError) error;

            String fieldName = field.getField();
            String message = field.getDefaultMessage();
            String value = field.getRejectedValue().toString();
            
            Error errorMessage = new Error();
            errorMessage.setField(fieldName);
            errorMessage.setMessage(message);
            errorMessage.setInvalidValue(value);

            errorList.add(errorMessage);
        });

        ErrorResponse errorResponse = new ErrorResponse();
        errorResponse.setErrorList(errorList);
        errorResponse.setMessage("");
        errorResponse.setRequestUrl(httpServletRequest.getRequestURI()); //현재 api주소 
        errorResponse.setStatusCode(HttpStatus.BAD_REQUEST.toString());
        errorResponse.setResultCode("FAIL");

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
    }

    @ExceptionHandler(value = ConstraintViolationException.class)
    public ResponseEntity constraintViolationException(ConstraintViolationException e, HttpServletRequest httpServletRequest){

        List<Error> errorList = new ArrayList<>();

        e.getConstraintViolations().forEach(error ->{
            Stream<Path.Node> stream = StreamSupport.stream(error.getPropertyPath().spliterator(), false);
            List<Path.Node> list = stream.collect(Collectors.toList());

            String field = list.get(list.size() -1).getName();
            String message = error.getMessage();
            String invalidValue = error.getInvalidValue().toString();

            Error errorMessage = new Error();
            errorMessage.setField(field);
            errorMessage.setMessage(message);
            errorMessage.setInvalidValue(invalidValue);

            errorList.add(errorMessage);

        });

        ErrorResponse errorResponse = new ErrorResponse();
        errorResponse.setErrorList(errorList);
        errorResponse.setMessage("");
        errorResponse.setRequestUrl(httpServletRequest.getRequestURI()); //현재 api주소 
        errorResponse.setStatusCode(HttpStatus.BAD_REQUEST.toString());
        errorResponse.setResultCode("FAIL");

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
    }

    @ExceptionHandler(value = MissingServletRequestParameterException.class)
    public ResponseEntity missingServletRequestParameterException(MissingServletRequestParameterException e, HttpServletRequest httpServletRequest){

        List<Error> errorList = new ArrayList<>();

        String fieldName = e.getParameterName();
        String invalidValue = e.getMessage();

        Error errorMessage = new Error();
        errorMessage.setField(fieldName);
        errorMessage.setMessage(e.getMessage());

        ErrorResponse errorResponse = new ErrorResponse();
        errorResponse.setErrorList(errorList);
        errorResponse.setMessage("");
        errorResponse.setRequestUrl(httpServletRequest.getRequestURI());
        errorResponse.setStatusCode(HttpStatus.BAD_REQUEST.toString());
        errorResponse.setResultCode("FAIL");

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
    }
}
```

  
  
  

## 결과

만약 valid 설정을 아래와 같이 했다면 예외 메시지는 어떻게 나올까?

  * User.java

```java
@Data
public class User {

	@NotEmpty @Size(min=1, max=10)
	private String name;
	
	@Min(1) @NotNull
	private Integer age;
}
```

  * ApiController.java

```java
@RestController
@RequestMapping("/api/user")
@Validated 
public class ApiController {
	
	@PostMapping("")
	public User post(@Valid @RequestBody User user) {
		System.out.println("@ post call");
		return user;
	}
}
```

위처럼 유효성체크를 설정한 뒤 POST맨을 통한 결과를 알아보자.  
name에 빈값을 넣었고, age에는 0을 넣었다.

![](/img/210805SpringbootError.PNG)

사진처럼 다른 개발자가 보아도 이해하기 쉬운 에러메시지를 확인할 수 있다.

  
  
  

## 출처

  * <https://github.com/steve-developer/fastcampus-springboot-introduction/tree/master/06.%20%EC%8A%A4%ED%94%84%EB%A7%81%EC%9D%98%20%EA%B8%B0%EB%8A%A5%EC%9D%84%20%ED%99%9C%EC%9A%A9%ED%95%B4%EB%B3%B4%EC%9E%90/SourceCode/exception>

#[패스트캠퍼스(초격차Java/Spring)](/tags/%ED%8C%A8%EC%8A%A4%ED%8A%B8%EC%BA%A0%ED%8D%BC%EC%8A%A4-%EC%B4%88%EA%B2%A9%EC%B0%A8Java-Spring/)
