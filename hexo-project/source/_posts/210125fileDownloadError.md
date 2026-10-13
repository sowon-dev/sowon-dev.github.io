---
title: "[오류일지]PatternSyntaxException 오류 해결"
date: 2021-01-25 00:51:04
tags:
  - "Eclipse"
  - "오류일지"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">파일 다운로드 클릭시 아래와 같은 콘솔에러가 발생했다.
    위 방법으로 해결안된다면 파일 경로 자체의 문제일 수 있다.</p>
</div>

<!-- more -->

## 문제상황

파일 다운로드 클릭시 아래와 같은 콘솔에러가 발생했다.

```xml
java.util.regex.PatternSyntaxException: Unexpected internal error near index 1
\
```

  
  
  

## 해결순서

### 파일을 업로드한 위치에 파일이 있는지 확인하기

나는 아래의 파일에 다운로드 할 파일 원본이 있는지 확인해본다.

```xml
D:\\workspace\\프로젝트명\\webapp\\upload
```

  
  
  

### `FileController.java`로 가서 해당 Mapping부분을 확인하기

아래처럼 Mapping 부분을 체크해본다

```java
@RequestMapping(value = "/downloadn", method = RequestMethod.GET)
@AuthMapping
public void downloadDo(){
	if(savename != null && !"".equals(savename)) {
	savename = savename.replaceAll("/", "");
	savename = savename.replaceAll("\\", "");
	}
	if(realname != null && !"".equals(realname)) {
		realname = realname.replaceAll("/", "");
		realname = realname.replaceAll("\\", "");
	}
	//코드 생략
}
```

  
  
  

### 이스케이프 문자 사용하기

문자열을 다루는 메서드를 사용할 때는 `\`를 주의해야한다.  
split이나 replace메서드의 인자로 들어가는 String 토큰이 regex 정규식이기 때문에 이스케이프 문자를 사용해야한다.

  * `\`이라면 `\\`로 사용해야한다.  
자세한 내용은 [여기 split 메서드 사용시 실수하기 쉬운 것](https://mytory.net/archives/285)를 참고하자.

```java
//수정전
if(savename != null && !"".equals(savename)) {
	savename = savename.replaceAll("/", "");
	savename = savename.replaceAll("\\", "");
}
if(realname != null && !"".equals(realname)) {
	realname = realname.replaceAll("/", "");
	realname = realname.replaceAll("\\", "");
}

//수정후
if(savename != null && !"".equals(savename)) {
	savename = savename.replaceAll("/", "");
	savename = savename.replaceAll("\\\\", "\\");
}
if(realname != null && !"".equals(realname)) {
	realname = realname.replaceAll("/", "");
	realname = realname.replaceAll("\\\\", "\\");
}
```

  
  
  

### 파일 경로 자체의 문제

위 방법으로 해결안된다면 파일 경로 자체의 문제일 수 있다.  
`local.properties`에서 `file.base.path`를 확인해본다.  
파일이 저장된 곳이랑 일치하는 지 확인한다.  
나의 경우 달랐기때문에 1번의 경로와 일치시켜주었다.

```xml
file.base.path=D:\\workspace\\프로젝트명\\webapp\\upload
```

오류 해결!!  
문자열을 다루는 메서드를 사용할 때는 `\`를 꼭 주의하자!

#[Eclipse](/tags/Eclipse/)[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)
