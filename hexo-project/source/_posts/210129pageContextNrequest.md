---
title: "request.getParameter()시 null이 뜰때 해결방법, ModelAndView 넘겨받는 방법"
date: 2021-01-29 01:30:42
tags:
  - "오류일지"
categories:
  - Backend
  - JSP
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">컨트롤러에서 request.setAttribute()을 하지 않으면 null값이 출력되기때문에 컨트롤러에서 set해줘야한다.
    관련 환경 설정과 코드를 알맞게 수정하여 정상적으로 동작하도록 해결할 수 있다.</p>
</div>

<!-- more -->

## 문제상황

[pdf.js](https://mozilla.github.io/pdf.js/examples/)  
DB에서 param으로 page정보를 받아서 PDF파일의 특정 페이지로 바로 출력하고싶었다.  
request객체를 시도했는데 계속 null을 가져왔다.  
왜 실패했을까? 

## 공통코드

  * Controller.java 코드

```java
@RequestMapping(value = "/content/{path}", method = {RequestMethod.GET, RequestMethod.POST})
    public ModelAndView homeMain(HttpServletRequest request, HttpServletResponse response, @PathVariable String path) {
    	ModelAndView model = new ModelAndView();
        SiteMenuContent siteMenuContent = siteMenuContentService.getSiteMenuContent(path);
        model.addObject("siteMenuContent", siteMenuContent);
        model.setViewName("/html");
        return model;
}
```

  * 입력값  
DB의 param컬럼에는 `page=4`가 들어있다.

```html
<input id="param" name="param" value="">
```

  
  
  

## 시도1 : request.getParameter() 사용

`request.getParameter()` 를 사용했지만 null값이 나타났다.  
왜일까? 아직도 답을 모르겠다.

```xml
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%
String pageParam = "2";
if(request.getParameter("param") != null){
	pageParam = request.getParameter("param");
}
%>

<div class="pdf-box">
     <iframe id="docIframe" src="/resources/js/jquery/pdfjs-dist/web/viewer.html?file=/upload/down/파일명.pdf#page=<%=pageParam %>" width="100%" height="860"></iframe>
</div>
```

  
  
  

## 헤결방법1 : request.getAttribute() 이용

request.getParameter() 대신 request.getAttribute()를 사용했다.  
컨트롤러에서 request.setAttribute()을 하지 않으면 null값이 출력되기때문에 컨트롤러에서 set해줘야한다.  
하지만 컨트롤러의 소스코드를 바꾸고 싶지 않았으므로 이 방법을 사용하지않았다.

  * Controller.java 코드

```java
@RequestMapping(value = "/content/{path}", method = {RequestMethod.GET, RequestMethod.POST})
    public ModelAndView homeMain(HttpServletRequest request, HttpServletResponse response, @PathVariable String path) {
    	ModelAndView model = new ModelAndView();
        SiteMenuContent siteMenuContent = siteMenuContentService.getSiteMenuContent(path);
        model.addObject("siteMenuContent", siteMenuContent);
        model.setViewName("/html");
		
		//set해준다.
		request.setAttribute("paramAttri", siteMenuContent.getParam());
		
        return model;
}
```

  * jsp코드

```xml
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%
String pageParam = "2";
String paramFormC = (String) request.getAttribute("paramAttri");
if(paramFormC != null){
	pageParam = paramFormC.split("=")[1];
}
%>

<div class="pdf-box">
     <iframe id="docIframe" src="/resources/js/jquery/pdfjs-dist/web/viewer.html?file=/upload/down/파일명.pdf#page=<%=pageParam %>" width="100%" height="860"></iframe>
</div>
```

  
  
  

## getParameter()와 getAttribute()의 차이점

| | getParameter() | getAttribute()  
---|---|---  
가져오는 값 | 웹브라우저에서 전송받은 request영역 | setAttribute()  
리턴타입 | String | Object  
  
  * [참고 : JSP - getParameter()와 getAttribute()의 차이점](http://hsprnote.blogspot.com/2017/03/jsp-getparameter-getattribute.html)

  
  
  

## 시도2 : el태그 ${} 이용

el태그를 사용할 경우 console에는 정상출력되지만 iframe안에서는 정상 출력이 되지않는다.  
왜일까…? 

```
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<div class="pdf-box">
     <iframe id="docIframe" src="/resources/js/jquery/pdfjs-dist/web/viewer.html?file=/upload/down/파일명.pdf#page=${siteMenuContent.param }" width="100%" height="860"></iframe>
</div>

<script type="text/javascript">
var $param = ${siteMenuContent.param }
console.log($param )
</script>
```

  
  
  

## 해결방법2 : pageContext.getAttribute(); 이용

따라서 jstl로 el태그를 스크립틀릿안으로 pageContext를 이용하여 불러왔다.

```xml
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:set value="${siteMenuContent.param }" var="paramFormC" />
<%
String pageParam = "2";
String paramFormC = (String) pageContext.getAttribute("paramFormC");
if(paramFormC != null){
	pageParam = paramFormC.split("=")[1];
}
%>

<div class="pdf-box">
     <iframe id="docIframe" src="/resources/js/jquery/pdfjs-dist/web/viewer.html?file=/upload/down/파일명.pdf#page=<%=pageParam %>" width="100%" height="860"></iframe>
</div>
```

성공!!

  
  
  

## 참고

  * <https://stackoverflow.com/questions/19183747/modelandview-addobject-vs-model-addattribute>

#[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)
