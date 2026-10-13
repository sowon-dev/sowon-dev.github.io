---
title: "[JSP] jsp파일을 수정하면 서버를 재시작해야할까?"
date: 2022-08-15 20:16:34
tags: []
categories:
  - Backend
  - JSP
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">jsp파일을 수정하면 서버를 재시작해야할까?의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    Deployment Assembly 설정이 제대로 되어 있는지 확인해야한다.</p>
</div>

<!-- more -->

개발을 하다보면 알겠지만 jsp 파일을 수정한 뒤 서버를 재시작하지않아도 반영이 된다. 어떨땐 즉시 반영되는데 또 어떨땐 반영이 느릴때도 있다.  
jsp에는 java코드도 있는데 어떻게 컴파일없이 바로 반영이 될까? 그리고 즉시반영이 안 될때 혹 반영이 느릴때는 어떻게 해야할까?

  
  
  

## JSP 특징

  * 동적 웹어플리케이션 컴포넌트
  * 응답형식 html

  
  
  

## 페이지 실행 순서

  * 최초 호출: jsp -> 서블릿 java 변환 -> .class로 컴파일(컴파일 일시를 기록) -> 클래스파일을 메모리에 로딩 -> html 전송 -> 브라우저에서 html이 보여짐
  * jsp 파일 수정없이 호출한 경우: 단순히 publishing
  * jsp 파일 수정후 호출한 경우: 컴파일일시가 변경되었다면, 서블릿 java로 변환 -> .class컴파일 후 재로딩

  
  
  

## jsp 수정사항 즉시 반영이 안될때?

  1. 서버세팅에서 자동 컴파일 되는 지 체크
     * 톰캣 context.xml 파일에서 `<Context reloadable="true">` 리로더블이 true인지 확인할 것
  2. 이클립스에서 publish to the server 버튼을 클릭(단축키 : Ctrl + Alt + P) 
     * [참고글: Eclipse HTML 수정 즉시 반영](https://gocoder.tistory.com/387)

  
  

### 만약 서버 재시작해도 반영이 안된다면?

  * 기본위치: C:\workspace.metadata.plugins\org.eclipse.wst.server.core\tmp1\work\Catalina\localhost\ROOT\org\apache\jsp\WEB_002dINF\views

위 위치에서 `파일명_jsp.java`과 `파일명_jsp.class`을 찾아 삭제하면 된다.  
주의할 점은 jsp파일을 삭제하는 것이 아니라 컴파일된 `파일명_jsp.java`과 `파일명_jsp.class`을 삭제하는 것이다!  
삭제한 뒤 브라우저에서 해당 페이지 다시 호출하면 컴파일 파일이 자동 생성된다.  
이때 새로 생성된 `파일명_jsp.java`과 `파일명_jsp.class`의 수정된 날짜가 현재 날짜로 되어있다면 반영이 잘 된 것이다.

  
  

### 만약 그래도 반영이 안된다면?

Deployment Assembly 설정이 제대로 되어 있는지 확인해야한다.

  * 프로젝트 우클릭 > Deployment Assembly 에서 Source에 target/m2e-wtp/web-resources가 제대로 설정되어있는지 확인하기.

![](/img/20230110stssetting.png)
