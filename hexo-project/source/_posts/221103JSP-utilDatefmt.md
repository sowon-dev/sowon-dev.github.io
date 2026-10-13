---
title: "[JSTL] java.util.Date 현재날짜의 시간을 0으로 설정하기"
date: 2022-11-02 16:15:38
tags:
  - "JSTL"
categories:
  - Backend
  - JSP
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">java.util.Date 현재날짜의 시간을 0으로 설정하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    구글링하면 가장 많이 사용하는 방법으로 포스팅 - 날짜 차이 계산하기을 작성했다.</p>
</div>

<!-- more -->

JSTL로 현재날짜와 DB에서 가져오는 날짜 차이를 계산했었다.  
잘 되는 줄 알았던 코드가 특정 시간을 기점으로 버그가 발생한다는 것을 알게되었다.

  
  
  

# 기존코드와 문제점

구글링하면 가장 많이 사용하는 방법으로 [포스팅 - 날짜 차이 계산하기](https://sowon-dev.github.io/2022/08/18/220818JSTL-date/)을 작성했다.  
날짜차이 계산은 모든 날짜를 시간으로 바꾼 뒤 뺄셈을 통해 날짜가 얼마나 남았는지 계산할 수 있다. 

```java
<jsp:useBean id="now" class="java.util.Date" />
<fmt:parseNumber var="nowfmtTime" value="${now.time / (1000*60*60*24)}" integerOnly="true" scope="request"/>
<fmt:parseNumber var="dbDtParse" value="${list.dbDt.time / (1000*60*60*24)}" integerOnly="true" scope="request"/>

${nowfmtTime }
```

코드상의 문제는 전혀없으나 요구사항이 하루전에는 예약할 수 없는 예약프로그램을 구현하는 것이라서 수정이 필요했다.  
현재시간을 time로 변경하는데 HH:mm:ss가 00:00:00이 아니라서 위 방식으로 시간계산시 미세하게 차이가 발생했다.  
이를 해결하기 위해 현재날짜의 시간을 0으로 설정해야했다.

  
  
  

# 해결코드

```java
<jsp:useBean id="now" class="java.util.Date" />
<fmt:formatDate var="today" value="${now}" pattern="yyyyMMdd000000" />
<fmt:parseDate var="nowfmt" value="${today}" pattern="yyyyMMddHHmmss"/>
<fmt:parseNumber var="nowfmtTime" value="${nowfmt.time / (1000*60*60*24)}" integerOnly="true" scope="request"/>

${nowfmtTime }
```

`fmt:formatDate`의 pattern속성으로 시간을 0으로 설정한다.  
그리고 `fmt:parseDate`로 Date 타입으로 파싱해준 뒤 바로 날짜를 이용할 수 있고 나처럼 날짜계산을 위해 다시 `fmt:parseNumber` 숫자타입으로 변경해서 이용할수도 있다.

  
  
  

# 참고

  * [JSTL과 EL : fmt 라이브러리(formatDate, formatNumber)](https://sowon-dev.github.io/2020/08/11/200812jspi2/)

#[JSTL](/tags/JSTL/)
