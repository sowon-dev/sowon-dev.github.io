---
title: "[Moment.js] moment String을 Controller에서 LocalDateTime으로 받기"
date: 2023-10-18 20:57:25
tags:
  - "Moment.js"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">moment String을 Controller에서 LocalDateTime으로 받기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    핵심 설정과 구현 코드를 단계별로 파악하여 상황에 맞게 유연하게 활용할 수 있다.</p>
</div>

<!-- more -->

moment으로 startDate를 포맷하여 `startDate.format("YYYY-MM-DDTHH:mm:ss")` ajax를 이용해 컨트롤러로 보냈다.  
LocalDateTime 데이터타입이 당연히 받을 수 있을 줄 알았는데 typeMismatch.java.time.LocalDateTime 에러가 발생했다. 

# 문제

```js
// request body
calendarParam(idx=10, startDate=2023-10-01T00:00:00, endDate=2023-10-31T23:59:59)
```

클라이언트에서 보내는 데이터는 위와 같다

```
Field error in object 'calendarParam' on field 'startDate': rejected value [2023-10-01&amp;#39;T&amp;#39;00:00:00.000]; codes [typeMismatch.calendarParam.startDate,typeMismatch.startDate,typeMismatch.java.time.LocalDateTime,typeMismatch]; arguments [org.springframework.context.support.DefaultMessageSourceResolvable: codes [calendarParam.startDate,startDate]; arguments []; default message [startDate]]; default message [Failed to convert property value of type 'java.lang.String' to required type 'java.time.LocalDateTime' for property 'startDate'; nested exception is org.springframework.core.convert.ConversionFailedException: Failed to convert from type [java.lang.String] to type [@org.springframework.format.annotation.DateTimeFormat java.time.LocalDateTime] for value '2023-10-01&amp;#39;T&amp;#39;00:00:00.000'; nested exception is java.lang.IllegalArgumentException: Parse attempt failed for value [2023-10-01&amp;#39;T&amp;#39;00:00:00.000]]
Field error in object 'calendarParam' on field 'end': rejected value [2023-10-31&amp;#39;T&amp;#39;23:59:59.999];
```

typeMismatch 에러가 발생했다.  
혹시 데이터포맷상 `startDate.format("YYYY-MM-DDTHH:mm:ss")`의 `T` 때문인가 싶어(그럴리없겠지만) 여러가지를 시도했다.

```js
startDate.format("YYYY-MM-DD'T'HH:mm:ss") //작은따옴표로 감싸보기
startDate.format("YYYY-MM-DD[T]HH:mm:ss") //대괄호로 감싸보기
startDate.format("YYYY-MM-DD HH:mm:ss") //T없애보기
```

결과는 여전히 typeMismatch에러였다.

  
  
  

# 해결: String

LocalDateTime을 쓰고 싶었던 이유는 mybatis에서 시작일과 종료일 날짜연산을 하기위해서였다.  
LocalDateTime을 String으로 변경하고 나서야 정상 작동했다. String이라도 형식이 맞기때문인지 날짜연산도 잘되었다.  
해결!

#[Moment.js](/tags/Moment-js/)
