---
title: "Double/Float 변환시 ClassCastException오류 NaN 해결"
date: 2023-05-09 00:57:24
tags: []
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">화면에서 컨트롤러로 파라미터 HashMap map를 받아 double값을 형변환하려고 하는데 ClassCastException이 발생했다.
    관련 환경 설정과 코드를 알맞게 수정하여 정상적으로 동작하도록 해결할 수 있다.</p>
</div>

<!-- more -->

화면에서 컨트롤러로 파라미터 `HashMap<String, String> map`를 받아 double값을 형변환하려고 하는데 ClassCastException이 발생했다.  
Java.lang.Integer cannot be case to Java.lang.String 이었고 원인을 찾아보니 NaN가 문제였다.

# 기존코드와 원인분석

```java
Double fee = Double.valueOf(map.get("fee"));
```

원인은 바로바로 `NaN`이다!  
화면에서 map.get(“fee”)의 값이 없어서 `NaN`으로 파라미터가 컨트롤러로 넘어왔다.  
내 의도는 화면에서 주는 값이 없으면 서비스단에서 `null`을 넣는 거였는데 NaN이라 이를 Double로 형변환하려니까 ClassCastException이 발생한 것이었다. 

  
  
  

# 해결

Double에서는 isNaN을 제공해준다. 이를 이용하면 된다.

```java
//해결코드
if(Double.isNaN(Double.valueOf(map.get("fee")))){
	fee = null;
} else{
	fee = Double.Double.valueOf(map.get("fee"));
}
```

오늘도 해결!

# 참고

  * <https://www.javatpoint.com/java-double-isnan-method>
