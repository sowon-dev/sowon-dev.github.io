---
title: "[Gson]한글이 ?로 깨져보일때"
date: 2023-01-05 21:07:31
tags:
  - "Gson"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">한글이 ?로 깨져보일때의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    구글에서 만든 Gson을 사용해서 객체를 json으로 혹은 그 반대로 변환하는데 사용하고 있다. 이때 한글이 ?로 깨지는 현상이 나타났다.</p>
</div>

<!-- more -->

구글에서 만든 [Gson](https://github.com/google/gson)을 사용해서 객체를 json으로 혹은 그 반대로 변환하는데 사용하고 있다. 이때 한글이 ?로 깨지는 현상이 나타났다.

# 한글깨질때 `produces="text/plain;charset=UTF-8"` 추가하기

컨트롤러 RequestMapping 에 추가하면 된다.

```java
@RequestMapping(value="/test", method=RequestMethod.GET, produces="text/plain;charset=UTF-8")
```

  
  
  

# 그래도 안될때

produces를 설정하고 나니까 http통신이 안된다. 그래서 `produces = "application/json;charset=utf-8"`로 바꿔주니 통신이 되었다.

```java
@RequestMapping(value="/test", method=RequestMethod.GET, produces="application/json;charset=UTF-8")
```

  
  
  

# 그래도 또 안될때

하지만 여전히 한글이 깨졌다. 그래서 다시 구글링해서 찾은 내용인 `produces = "MediaType.APPLICATION_JSON_UTF8_VALUE"`로 바꿔적용했다.

```java
@RequestMapping(value="/test", method=RequestMethod.GET, produces="MediaType.APPLICATION_JSON_UTF8_VALUE")
```

해결!

#[Gson](/tags/Gson/)
