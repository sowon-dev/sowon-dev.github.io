---
title: "[Spring]RestTemplate response 한글깨짐 UTF-8적용하기"
date: 2023-01-12 15:46:57
tags: []
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">RestTemplate response 한글깨짐 UTF-8적용하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    RestTemplate 선언하는 방법은 블로그 글 RestTemplate과 HttpEntity가 뭐길래(제네릭과 ParameterizedTypeReference)를 참조하면 된다.</p>
</div>

<!-- more -->

최근에 Gson 한글 깨지는 현상을 해결한 블로그 글 [Gson 한글이 ?로 깨져보일때](https://sowon-dev.github.io/2023/01/05/230106gson-korean-encoding/)을 포스팅했었다.  
성공메시지는 한글이라 몰랐는데 에러메시지가 엉망진창으로 인코딩되서 출력되었다.  
나는 한글을 정말 사랑하는데… 한글 인코딩이 나를 힘들게 한다. 한글아 그만 깨져😠

# 문제 현상

이번에는 어디서 한글이 깨졌는지부터 찾아야했다. log를 뒤진 결과 `RestTemplateLoggingInterceptor`의 로그까지는 한글이 깨지지않고 출력하나 그 뒤 RestTemplate response를 받는 부분에서 한글이 깨지는 것을 확인했다.  
RestTemplate 선언하는 방법은 블로그 글 [RestTemplate과 HttpEntity가 뭐길래(제네릭과 ParameterizedTypeReference)](https://sowon-dev.github.io/2022/12/09/221210spring-resttemplate/)를 참조하면 된다.

  
  
  

# 수정한 코드

StringHttpMessageConverter의 default Charset이 ISO-8859-1이라고 한다. 이를 UTF-8로 변경하면 한글이 깨짐없이 잘 출력된다! 

```java
RestTemplate restTemplate = new RestTemplate(new BufferingClientHttpRequestFactory(new HttpComponentsClientHttpRequestFactory()));
restTemplate.getMessageConverters().add(0, new StringHttpMessageConverter(StandardCharsets.UTF_8)); // 추가한 부분
restTemplate.exchange(apiUrl, HttpMethod.POST, entity, String.class);
```

StringHttpMessageConverter가 어떤 역할을 하는 지 좀 더 깊게 궁금했는데 잘 정리된 글이 이미 있었다. 자세한 내용은 [깡냉쓰님의 RestTemplate 한글 깨짐관련(StringHttpMessageConverter)](https://cornswrold.tistory.com/402)을 참고하면 된다.

해결!😎
