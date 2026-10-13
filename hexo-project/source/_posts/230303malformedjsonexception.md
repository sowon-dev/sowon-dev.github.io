---
title: "[Gson]MalformedJsonException 에러해결"
date: 2023-03-02 19:12:09
tags:
  - "Gson"
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">백단 테스트 중 json을 받을 일이 있어서 그냥 작성했더니 아래와 같은 오류가 발생했다.
    jsp코드와 컨트롤러 코드를 수정했다.</p>
</div>

<!-- more -->

백단 테스트 중 json을 받을 일이 있어서 그냥 작성했더니 아래와 같은 오류가 발생했다.

# 문제

  * jsp코드

```js
let param = {};
param.userid = 'testuser';
param.json = '{\"title\":\"테스트제목\", \"detail\":\"테스트1의 설명입니다.\"}';

$.ajax({
	url: "/test/json",
	method: "POST",
	data: param,
	callback: function(data){
		alert(JSON.stringify(data));
	}
})
```

  * testVO코드

```java
@Data
public class TestVO {
	private String title;
	private String detail;
}
```

  * 컨트롤러코드

```java
@RequestMapping(value="/test/json", method= RequestMethod.POST)
@ResponseBody
public TestVO testControl(@ResquestParam HashMap<String, String> param) throws Exception{
	TestVO test = new TestVO();
	test = new Gson().fromJson(param.get("json"), TestVO.class);
	
	return test;
}
```

  * 에러메시지

```plain
com.google.gson.stream.MalformedJsonException: Expected ':' at line 1 column 8 path $.&quot
```

언제나 에러메시지 안에 답이 있다.

  
  
  

# 해결1: 공백, 특수문자 제거

[com.google.gson.stream.MalformedJsonException - juno.log](https://everydayidid.tistory.com/69)을 참고하면 특수문자를 제거하는 방법이 있다.  
내 상황에선 json형태가 깨지기에 사용할 수 없었다. 

  
  
  

# 해결2: setter 사용

jsp코드와 컨트롤러 코드를 수정했다.

  * jsp코드

```js
let param = {};
param.userid = "testuser";
param.title = "테스트제목";
param.detail = "테스트1의 설명입니다";

$.ajax({
	url: "/test/json",
	method: "POST",
	data: param,
	callback: function(data){
		alert(JSON.stringify(data));
	}
})
```

  * 컨트롤러코드

```java
@RequestMapping(value="/test/json", method= RequestMethod.POST)
@ResponseBody
public TestVO testControl(@ResquestParam HashMap<String, String> param) throws Exception{
	TestVO test = new TestVO();
	test.setTitle(param.get("title"));
	test.setDetail(param.get("detail"));
	
	return test;
}
```

그냥 받았다… 더 좋은 방법이 있다면 댓글로 알려주시면 감사하겠습니다. 

#[Gson](/tags/Gson/)
