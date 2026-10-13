---
title: "[JSTL] 날짜 차이 계산하기"
date: 2022-08-18 04:00:10
tags:
  - "JSTL"
categories:
  - Backend
  - JSP
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'날짜 차이 계산하기'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    현재날짜와 db에서 가져오는 날짜 차이를 계산하고 싶었다.</p>
</div>

<!-- more -->

현재날짜와 db에서 가져오는 날짜 차이를 계산하고 싶었다.

# 코드

구글링끝에 드디어 성공~!!  
now는 오늘날짜이고 list.dbDt는 db에서 가져온 날짜값이다.  
여기서 중요한 점은 parseNumber할때 `.time`을 해줘야지 제대로 계산된다는 점이다. 

```html
<jsp:useBean id="now" class="java.util.Date" />
<fmt:parseNumber value="${now.time / (1000*60*60*24)}" integerOnly="true" var="nowfmtTime" scope="request"/>
<fmt:parseNumber value="${list.dbDt.time / (1000*60*60*24)}" integerOnly="true" var="dbDtParse" scope="request"/>

${dbDtParse - nowfmtTime }
```

예를 들어 now가 2022-08-18이고 list.dbDt가 2022-08-19이면 `${dbDtParse - nowfmtTime }`값은 0이다.  
테스트해보면 아래와 같이 값을 계산할 수 있다.

now | list.dbDt | ${dbDtParse - nowfmtTime }  
---|---|---  
2022-08-18 | 2022-08-18 | -1  
2022-08-18 | 2022-08-18 | 0  
2022-08-18 | 2022-08-20 | 1  
2022-08-18 | 2022-08-23 | 4  
  
# 관련

  * [java.util.Date 현재날짜의 시간을 0으로 설정하기]()

#[JSTL](/tags/JSTL/)
