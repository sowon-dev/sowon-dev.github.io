---
title: "REST API 컨트롤러 Mapping을 어떻게 하지?"
date: 2021-05-25 15:00:00
tags:
  - "SpringBoot"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">REST API 컨트롤러 Mapping을 어떻게 하지?의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    스프링부트로 RestAPI를 구현하고 있다. Mapping 어노테이션에서 URI를 지정시 어떤 규칙으로 적용해야할까?을 적용할 수 있다.</p>
</div>

<!-- more -->

스프링부트로 RestAPI를 구현하고 있다. Mapping 어노테이션에서 URI를 지정시 어떤 규칙으로 적용해야할까?

## web api규칙

이를 잘 정리해 둔 블로그가 있다. 이 블로그를 통해 감을 잡을 수 있었다.

  * <https://www.mimul.com/blog/web-api-design-from-apigee/?fbclid=IwAR1Q5QmdYTLpgc9c5w9IKQM2i49JBsNuEwyJHntYjWytEYQK89m2fJUMPAE>

모든 내용들이 다 좋았지만 그 중에서도 직관적으로 바로 이해가는 세가지는 아래와 같다.

  1. Nouns are good; verbs are bad.
  2. Plural nouns and concrete names. 복수명사를 사용하고 구체적인 이름을 사용하기.
  3. Simplify associations - sweep complexity under the ‘?’. 자원간의 관계, 매개 변수 및 속성과 같은 복잡한 것은 HTTP 물음표 뒤에 가지고 가자.

위 규칙은 [Web API Design - Crafting Interfaces that Developers Love](https://pages.apigee.com/rs/apigee/images/api-design-ebook-2012-03.pdf)과 위 블로그에서 발췌했다.

  
  
  

## OData (Open Data Protocol)

번역하면 공공 데이터 규약 즉, 데이터를 주고 받는데 있어 지켜야하는 규약을 의미한다.  
OPEN API들은 보통 이 규약을 준수한다.

  * <https://docs.microsoft.com/en-us/graph/use-the-api?view=graph-rest-1.0>

마이크로소프트사의 페이지를 가보면 Access data and methods, Paging등에 관한 API예시가 있다.  
이를 참조하여 오픈 API 틀을 잡는데 도움이 된다.

  
  
  

## 참고

  * <https://www.odata.org/getting-started/basic-tutorial/>
  * <https://www.ibm.com/docs/ko/license-metric-tool?topic=api-rest-resources-http-methods>

#[SpringBoot](/tags/SpringBoot/)
