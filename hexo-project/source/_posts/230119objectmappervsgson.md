---
title: "Jackson ObjectMapper VS Gson 차이"
date: 2023-01-18 15:51:35
tags:
  - "차이"
  - "Gson"
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'Jackson ObjectMapper VS Gson 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    Object Mapper만 사용하다가 Gson을 알게되면서 둘의 차이점이 궁금해졌다.</p>
</div>

<!-- more -->

Object Mapper만 사용하다가 Gson을 알게되면서 둘의 차이점이 궁금해졌다.

# 개념

Jackson ObjectMapper와 Gson은 뭐하는 애들일까? 자바에서 JSON data-binding 지원해주는 라이브러리이다.

  
  
  

# 사용법

HashMap을 Json으로 변환한뒤 콘솔에 출력하는 예시이다.

```java
HashMap<String, Obejct> map = new HashMap<>();
map.put("name", "나혜석");
map.put("age", 77);

// 1. ObjectMapper 사용 + throws Exception 필수
String serializedMap1 = new ObjectMapper().writeValueAsString(map);
system.out.println(serializedMap1);
// output: {"name":"나혜석","age":77}

// 2. Gson 사용
String serializedMap2 = new GsonBuilder().create().toJson(map)
system.out.println(serializedMap2);
// output: {"name":"나혜석","age":77}
```

사용하다보면 큰 차이점 하나를 발견할 수 있는데 ObjectMapper는 Exceptionc처리가 필수이다.

  
  
  

# 각 장점

Jackson | Gson  
---|---  
스프링프레임워크에 이미 속해있어 따로 설치안해도 됨 | 가장 간단한 toJson/fromJson방식  
다양한 어노테이션 활용가능 | 역직렬화시 자바 엔티티에 접근할 필요가 없음  
  
  * Jackson:
    * Built into all JAX-RS (Jersey, Apache CXF, RESTEasy, Restlet), and Spring framework
    * Extensive annotation support
  * Gson:
    * Simplicity of toJson/fromJson in the simple cases
    * For deserialization, do not need access to the Java entities

출처: [baeldung의 jackson-vs-gson 글](https://www.baeldung.com/jackson-vs-gson)

#[차이](/tags/%EC%B0%A8%EC%9D%B4/)[Gson](/tags/Gson/)
