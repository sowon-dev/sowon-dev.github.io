---
title: "[Spring]Interceptor"
date: 2021-08-08 15:00:00
tags:
  - "패스트캠퍼스(초격차Java/Spring)"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Interceptor의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * 주로 인증 단계를 처리하는데 사용 (조직에 따라 Logging용도로 사용)을 적용할 수 있다.</p>
</div>

<!-- more -->

스프링에서 인터셉터에 대해 알아보자.

## Interceptor

  * [Filter](https://sowon-dev.github.io/2021/08/06/210807Spring-filter/)와 매우 유사한 형태지만 차이점은 Spring Context에 등록됨.
  * Controller 영역 안에 존재
  * AOP와 유사한 기능 제공 가능
  * 주로 `인증 단계`를 처리하는데 사용 (조직에 따라 Logging용도로 사용)
  * 인터셉터를 선/후처리함으로써, 서비스 비즈니스 로직과 분리시킴.
  * `@RequiredArgsConstructor`: final로 선언된 객체들을 생성자에서 주입받을 수 있도록 해줌

#[패스트캠퍼스(초격차Java/Spring)](/tags/%ED%8C%A8%EC%8A%A4%ED%8A%B8%EC%BA%A0%ED%8D%BC%EC%8A%A4-%EC%B4%88%EA%B2%A9%EC%B0%A8Java-Spring/)
