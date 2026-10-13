---
title: "String.valueOf() vs toString() 차이 알고쓰자"
date: 2023-02-06 16:41:56
tags:
  - "차이"
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'String.valueOf() vs toString() 차이 알고쓰자'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    비슷한 역할을 하지만 결과는 다른 두 메서드 String.valueOf()와 Object.toString()의 차이에 대해 알아보자.</p>
</div>

<!-- more -->

비슷한 역할을 하지만 결과는 다른 두 메서드 String.valueOf()와 Object.toString()의 차이에 대해 알아보자.

# 차이점: Null처리

가장 큰 차이점은 null처리이다. null처리때문에 보통 Object.toString()을 많이 쓴다. 클라이언트는 null을 볼 필요가 없기때문이다.

```java
Object testObj = null; 

System.out.println(String.valueOf(testObj)); 
// 결과: null

System.out.println(testObj.toString()); 
// 결과: NullPointerException 오류 발생
```

  * String.valueOf(): null인 경우 문자열null을 만들어서 출력
    * null체크: “null”.equals(string) 확인 필수
  * Object.toString(): null인 경우 NPE 발생
    * Onject의 값이 String타입이 아니어도 출력한다.

  
  
  

# 결론

NPE를 방지하고 싶다면 String.valueOf()를 사용하고 널체크를 꼭 해줘야한다. 

#[차이](/tags/%EC%B0%A8%EC%9D%B4/)
