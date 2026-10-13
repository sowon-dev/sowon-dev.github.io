---
title: "Springboot validation annotation parttern 정규식 오류 해결"
date: 2021-08-01 17:48:46
tags:
  - "오류일지"
  - "정규표현식"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Spring Validation의 @NotNull, @NotBlank 어노테이션으로 해결하기 어려운 NULL 허용 및 공백 차단 조건을 @Pattern 정규표현식으로 구현한 사례다.
    정규식 선언 시 글자수 범위({0,64})를 명시해야 단일 문자가 아닌 전체 문자열에 대해 유효성 검사가 정상적으로 통과된다.</p>
</div>

<!-- more -->

Spring 프로젝트에서 서비스단에서 처리하는 유효성체크를 VO에서 처리하고 싶었다.  
내가 원하는 바는 String depart컬럼에 null은 허용하지만 빈값과 white space는 허용하지 않는 유효성체크를 하고 싶었다.  
만약 빈값과 white space가 들어온다면 null로 변경해서 DB에 저장해야하는 로직이었다.

## 기본 어노테이션들

NULL체크를 위해 기본으로 제공되는 어노테이션들이 있다.

| | NULL | 빈칸(“”) | White Space(“ “)  
---|---|---|---  
`@NotNull` | 허용X | 허용O | 허용O  
`@NotEmpty` | 허용X | 허용X | 허용O  
`@NotBlank` | 허용X | 허용X | 허용X  
  
내 경우는 NULL은 허용해주어야했기에 위의 어노테이션들을 전부 사용할 수 없었다.

  
  
  

## 기존코드

  * VO코드

```java
public class exampleVO{
	String depart;
}
```

  * SERVICE 클래스의 checkVal메서드  
서비스에서 null은 허용되면서도 isBlank가 참인 조건으로 만들었다. 정상작동하지만 마음에 들지 않았다.

```java
public boolean checkVal(String depart){
	if(exampleVO.getDepart() != null && exampleVO.getDepart().isBlank()) {
  		exampleVO.setDepart(null);
	}

  	//비즈니스 로직
}
```

  
  
  

## 정규표현식 코드

[정규식 테스트 사이트](https://regexr.com/)를 이용하여 원하는 정규식인 `[0-9a-zA-Z가-힣]`를 만들었다.  
혹시 정규표현식이 처음이라면 [정규표현식 기초 포스팅](https://sowon-dev.github.io/2021/03/16/210317pythonRegularExpression/)을 참고하자

내가 만든 정규식 `[0-9a-zA-Z가-힣]`은 아래와 같이 처리한다.

  * 허용: 숫자와 영대소문자, 한글, NULL
  * 허용하지않음: 빈칸, 공백 

  
  
  

### 첫시도 => 실패

```java
public class exampleVO{

	@Pattern(groups = {ValidationGroups.insert.class, ValidationGroups.update.class}
				, regexp = "[0-9a-zA-Z가-힣]", message = "빈값이나 공백이 들어갈 수 없습니다.")
	String depart;
}
```

포스트맨을 통해서 아래와 같이 테스트를 해봤는데 문자열을 입력할때 `"빈값이나 공백이 들어갈 수 없습니다."`가 응답되면서 에러가 발생했다.

파라미터 | 정상작동여부 | 설명  
---|---|---  
null | O | DB에 null값이 정상적으로 insert, update됨  
빈값(“”) | O | @Pattern message속성에 걸어둔 메시지가 출력됨  
white space(“ “) | O | @Pattern message속성에 걸어둔 메시지가 출력됨  
숫자,영대소문자,한글이 포함된 문자열 | X | @Pattern message속성에 걸어둔 메시지가 출력됨  
  
도대체 왜일까? 에러를 이해하지못해서 삽질하고 있었는데 과장님이 간단하게 해결해주셨다.  
과장님 감사합니다.🙏

  
  
  

### 성공코드

글자수`{0,64}`만 추가하면 된다!!

```java
public class exampleVO{

	@Pattern(groups = {ValidationGroups.insert.class, ValidationGroups.update.class}
				, regexp = "[0-9a-zA-Z가-힣]{0,64}", message = "빈값이나 공백이 들어갈 수 없습니다.")
	String depart;
}
```

파라미터 | 정상작동여부 | 설명  
---|---|---  
null | O | DB에 null값이 정상적으로 DB에 insert, update됨  
빈값(“”) | O | @Pattern message속성에 걸어둔 메시지가 출력됨  
white space(“ “) | O | @Pattern message속성에 걸어둔 메시지가 출력됨  
숫자,영대소문자,한글이 포함된 문자열 | O | 문자열값이 정상적으로 DB에 insert, update됨  
  
세상 간단한 에러였는데 내 눈에는 보이지 않는 것이 참 이상했다.  
앞으로는 절대 빼먹을 일 없겠다! 과장님 다시한번 감사합니다!

여담이지만 사실 이렇게 사소한 오류일지를 적어야할지 고민이 많았다.  
하지만 사소한 것일수록 남겨놔야 나중에 시간을 단축시킬 수 있고, 또 누군가는 나처럼 삽질할 수 도 있으니 단 한 명에게라도 도움을 줄수있다면 아주 사소한 오류일지라도 적여야겠다는 생각이 들었다.  
주니어개발자 여러분 우리 모두 화이팅합시다.

#[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)[정규표현식](/tags/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D/)
