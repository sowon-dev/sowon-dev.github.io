---
title: "[JS] URL 파라미터(쿼리파라미터Query Parameter)가져오기(ft.EL표현식)"
date: 2024-01-07 17:20:47
tags: []
categories:
  - Backend
  - JSP
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">URL 파라미터(쿼리파라미터Query Parameter)가져오기(ft.EL표현식)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    정말 초간단한 Query Parameter 가져오는 방법은 param 객체를 사용하는 것이다.</p>
</div>

<!-- more -->

정말 초간단한 Query Parameter 가져오는 방법은 param 객체를 사용하는 것이다.

네이버 검색을 예로 들어보자.  
아래와 같은 URL에서 `query=가나다`만 가져오고 싶다면 어떻게 해야할까?

```console
https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=가나다
```

  
  
  

# 1\. EL표현식 사용!

```jsp
${param.query}

//output : 가나다
```

해결!

  
  
  

# 2\. request사용!

```jsp
<%= request.getAttribute("query") %>

//output : 가나다
```

이 방법을 활용하면 String뿐만 아니라 객체도 가져올 수 있다.  
객체 파라미터를 가져오는 방법은 아래 포스팅 참고하면 된다.

  * [참고: 스프링SPRING에서 페이지이동하기, 파라미터가지고 페이지이동하기](https://sowon-dev.github.io/2020/10/12/201013spring/)

  
  
  

# 참고

  * [js에서 URL 파라미터(쿼리파라미터Query Parameter)가져오기](https://sowon-dev.github.io/2023/10/19/231020URLsearchparams/)
  * [jsp에서 URL 파라미터(쿼리파라미터Query Parameter)가져오기(ft.EL표현식)](https://sowon-dev.github.io/2024/01/07/240108jsp-el-queryparam/)
