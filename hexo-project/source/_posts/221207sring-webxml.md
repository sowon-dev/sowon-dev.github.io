---
title: "[Java] web.xml이 뭐길래"
date: 2022-12-06 19:19:12
tags:
  - "WEB"
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">web.xml이 뭐길래의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    자바 웹 애플리케이션은 배포 설명자 파일을 사용하여 URL이 서블릿에 매핑되는 방법, 인증이 필요한 URL 등의 정보를 확인한다.</p>
</div>

<!-- more -->

자바로 웹어플리케이션을 만드면 필수로 만나게 되는 파일 중 `web.xml`이 있다.

# web.xml이란

단어로는 Deployment Descriptor로 배포설명자이다.  
자바 웹 애플리케이션은 배포 설명자 파일을 사용하여 URL이 서블릿에 매핑되는 방법, 인증이 필요한 URL 등의 정보를 확인한다.  
자바 웹 애플리케이션이면 반드시 하나씩 존재해야하는 파일이며 프로그램에 필요한 전반적인 설정을 지정할 수 있다.  
프로젝트 실행시 가장 먼저 실행되는 파일로서 메모리에 로딩된다.  
위치는 WEBCONTENT하위의 WEB-INF폴더 하위에 있으며 가장 많이 사용되는 곳은 에러코드별 페이지처리이다.

> In a java web application a file named web.xml is known as deployment descriptor. It is a xml file and  is the root element for it. When a request comes web server uses web.xml file to map the URL of the request to the specific code that handle the request.  
> 출처: [w3schools](https://www.w3schools.blog/deployment-descriptor-web-xml-file)

  
  
  

# 무엇을 설정할수있을까?

  1. ServletContext의 초기 파라미터
  2. Session의 유효시간 설정
  3. Servlet/JSP에 대한 정의
  4. Servlet/JSP 매핑: URL 패턴 및 URL이 해당 패턴과 일치하는 요청에 사용할 선언된 서블릿의 이름을 지정. 

```html
<servlet-mapping>
     <servlet-name>redteam</servlet-name>
     <url-pattern>/red/*</url-pattern>
   </servlet-mapping>

   <servlet-mapping>
     <servlet-name>blueteam</servlet-name>
  <url-pattern>/blue/*</url-pattern>
   </servlet-mapping>
```

  5. Mime Type 매핑
  6. Welcome File list
  7. Error Pages 처리 

```html
<!-- 존재하지 않는 페이지, 404에러시 처리 페이지를 error.jsp로 설정함 -->
<error-page>
  <error-code>404</error-code>
  <location>/error.jsp</location>
</error-page>
```

  8. 리스너: 어떠한 이벤트가 발생하면 호출되어 처리하는 객체 

```html
<listener>
  <listener-class>TestListener</listener-class>
</listener>
```

  9. 필터: [Spring-Filter 포스팅참조](https://sowon-dev.github.io/2021/08/06/210807Spring-filter/)
  10. 보안: 패턴과 일치하는 URL에 대한 보안 제약조건을 정의할 수 있다. 제약조건에서 사용자 역할을 admin으로 지정하면 등록된 애플리케이션 개발자만 URL에 액세스하도록 만들수있다. 

```html
<security-constraint>
  <web-resource-collection>
       <web-resource-name>admin</web-resource-name>
       <url-pattern>/admin/*</url-pattern>
     </web-resource-collection>
    <auth-constraint>
	  <role-name>admin</role-name>
       </auth-constraint>
   </security-constraint>
```

  
  
  

# 참고

  * <https://www.w3schools.blog/deployment-descriptor-web-xml-file>
  * [http://wiki.gurubee.net/pages/viewpage.action?pageId=26740333&](http://wiki.gurubee.net/pages/viewpage.action?pageId=26740333&)
  * <https://cloud.google.com/appengine/docs/standard/java/config/webxml?hl=ko>

#[WEB](/tags/WEB/)
