---
title: "괄호가 &#41;로 자동으로 바뀌어버릴때 해결법(ft.EscapeHtml)"
date: 2022-05-05 22:02:04
tags:
  - "오류일지"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">이는 브라우저에서 자동으로 문자열 escape를 하기 때문이다.
    따라서 unescape를 해주면 해결된다.</p>
</div>

<!-- more -->

jsp페이지에서 검색을 하는데 자동으도 괄호가 escape되어 쿼리에서 where 조건절이 검색되지않았다.

## 🥨 문제 상황

아래 예시를 보자. option의 value값에 괄호가 들어가있다. 그결과 브라우저가 자동으로 

  * jsp페이지

```jsp
(코드 생략)
<form name="searchFrm" method="get" action="/example">
  <select name="calType">
	<option value="">:: 전체 ::</option>
	<option value="달력(움력)" <c:if test="${searchInfo.calType eq '달력(움력)'}">selected</c:if>>달력(움력)</option>
	<option value="달력(양력)" <c:if test="${searchInfo.calType eq '달력(양력)'}">selected</c:if>>달력(양력)</option>
  </select>
</form>
(코드 생략)
```

  * sql쿼리

```sql
SELECT
   *
FROM
   tb_example
WHERE
	1 = 1
AND	USE_AT = 1
AND	CAL_TYPE = #{calType}
```

실행결과 CAL_TYPE 조건이 `달력(음력)`이 아닌 `달력&#40;음력&#41;`으로 where 조건절이 들어갔기에 원하는 데이터가 나오지않았다.

```console
SELECT
   *
FROM
   tb_example
WHERE
	1 = 1
AND	USE_AT = 1
AND	CAL_TYPE = '달력&#40;음력&#41;'
```

  
  
  

## 🥨 원인

이는 브라우저에서 자동으로 문자열 escape를 하기 때문이다.

  * 문자열 escape란? 브라우저에서 get방식 전송시 브라우저 자체적으로 UTF-8문자를 escape한다.

  
  
  

## 🥨 해결방법

따라서 unescape를 해주면 해결된다.  
크게 3가지 방법이 있다.

  1. org.springframework.web.util.HtmlUtils.htmlUnescape
  2. org.apache.commons.lang.StringEscapeUtils.escapeHtml
  3. replace메서드 사용

  
  
  

### 1 HtmlUtils.htmlUnescape 사용

컨트롤러에서 받은 파라미터를 unescape한다.

```java
(중략)
param.setCalType(HtmlUtils.htmlUnescape(param.getCalType()));
(생략)
```

  
  
  

### 2 StringEscapeUtils.escapeHtml 사용

컨트롤러에서 받은 파라미터를 unescape한다.

```java
(중략)
param.setCalType(StringEscapeUtils.escapeHtml(param.getCalType());
(생략)
```

  
  
  

### 3 replace() 사용

컨트롤러에서 받은 특정 파라미터를 replace메서드를 이용해 바꿔준다.

```java
(중략)
param.getCalType().replace("&#40;", "(");
param.getCalType().replace("&#41;", ")");
(생략)
```

  
  
  

## 🥨 선택

현재 전자정부프레임워크3.8환경이므로 스프링프레임워크에서 제공하는 htmlUnescape메서드를 사용했다.  
내 상황에서는 escape가 1번했는데도 정상출력이 되지않아 찾아보니 escape가 2번 되어있었다. 왜일까…?  
암튼 unescape를 2번해서 해결했다.

  * Controller.java

```java
(중략)
String calTypeUnescape = HtmlUtils.htmlUnescape(param.getCalType());
param.setCalType(HtmlUtils.htmlUnescape(calTypeUnescape));
(생략)
```

적용한 뒤 콘솔을 보니 아래처럼 쿼리가 원하는대로 정상출력됐다.

```console
SELECT
   *
FROM
   tb_example
WHERE
	1 = 1
AND	USE_AT = 1
AND	CAL_TYPE = '달력(음력)'
```

해결!

#[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)
