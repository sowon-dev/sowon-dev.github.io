---
title: "[Spring]validation라이브러리, 커스텀 validation annotation만들기"
date: 2021-08-01 15:00:00
tags:
  - "패스트캠퍼스(초격차Java/Spring)"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">validation라이브러리, 커스텀 validation annotation만들기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    2. 구현에 따라 Service Logic과 분리가 필요할 수 있음을 적용할 수 있다.</p>
</div>

<!-- more -->

일반적으로 validation을 진행할 때 아래와 같이 서비스단에서 null값을 체크해준다.  
파라미터가 3개이상인 경우나 여러 상황에서 한계점이 존재한다.

```java
public void example(String 파람1, String 파람2, int 파람3){
	if(파람1 == null || 파람2 == null){
	 return 
	}

	if(파람3 == 0){
	 return 
	}
	
	// 비즈니스 로직시작
}
```

  
  
  

## 예상할 수 있는 한계점

  1. 검증해야 할 파라미터가 많은 경우 코드가 길어짐
  2. 구현에 따라 Service Logic과 분리가 필요할 수 있음
  3. 흩어져 있는 경우 어디에서 검증하는 지 알기 어려움
  4. 재사용의 한계 존재

이럴때는 spring-boot-starter-validation 라이브러리를 사용할 수 있다.  
![출처: https://prinha.tistory.com/entry/%EC%9E%90%EB%B0%94-%EC%8A%A4%ED%94%84%EB%A7%81-%EC%96%B4%EB%85%B8%ED%85%8C%EC%9D%B4%EC%85%98-annotation%EC%9D%98-%EC%A0%95%EC%9D%98%EC%99%80-%EC%A2%85%EB%A5%98](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbiYEHh%2FbtqHscMte8C%2FZhCLLxW0FrI5rUYnrVfK7K%2Fimg.png)

[끄적끄적님의 어노테이션 포스팅](https://prinha.tistory.com/entry/%EC%9E%90%EB%B0%94-%EC%8A%A4%ED%94%84%EB%A7%81-%EC%96%B4%EB%85%B8%ED%85%8C%EC%9D%B4%EC%85%98-annotation%EC%9D%98-%EC%A0%95%EC%9D%98%EC%99%80-%EC%A2%85%EB%A5%98)에 자세한 설명과 예시가 나와있다.

  
  
  

## BindingResult객체

해당 객체를 통해 예외처리 가능하다.

  * 참고: <https://jhparkkk.tistory.com/12>

  
  
  

## validation 커스텀 어노테이션 만들기

YearMonth형태가 yyyyMM형태인 어노테이션을 만들어보자.

  
1\. Annotation 클래스 생성하기 new Annotation을 생성하고 아래처럼 작성하면 된다. 

```java
@Documented
@Constraint(validatedBy ={ YearMonthValidator.class }) // 어떠한 클래스를 가지고 유효성 검사를 할 것인지 작성해야함
@Target({METHOD, FIELD, ANNOTATION_TYPE, CONSTRUCTOR, PARAMETER, TYPE_USE})
@Retention(RetentionPolicy.RUNTIME)
public @interface YearMonth {

  String message() default "yyyyMM 형식에 맞지 않습니다.";

  Class<?>[] groups() default {};

  Class<? extends Payload>[] payload() default {};
  
  String pattern() default "yyyyMMdd"; //기본패턴이 yyyyMM이지만 validator에서 Datetime으로 받기 때문에 yyyyMMdd를 넣어줘야함.
}
```

  
2\. Validator 로직 작성하기 위에서 만든 어노테이션을 활용하여 유효성체크를 하는 클래스를 만들어야한다. new Java Class를 생성하고 아래처럼 작성하면 된다. 

```java
public class YearMonthValidator implements ConstraintValidator<YearMonth, String>{

  private String pattern;

  @Override
  public void initialize(YearMonth constratintAnnotation) {
  	this.pattern = constratintAnnotation.pattern();

  }

  @Override
  public boolean isValid(String value, ConstraintValidatorContext cxt) {

    LocalDate l = LocalDate.parse(value+"01", DateTimeFormatter.ofPattern(this.pattern));
	
    return true;
  }

}
```

  
3\. 사용하기 

그리고 사용법은 VO에서 패턴을 걸어주면된다.

```java
// VO 일부

@YearMonth
private String reqDate;
```

#[패스트캠퍼스(초격차Java/Spring)](/tags/%ED%8C%A8%EC%8A%A4%ED%8A%B8%EC%BA%A0%ED%8D%BC%EC%8A%A4-%EC%B4%88%EA%B2%A9%EC%B0%A8Java-Spring/)
