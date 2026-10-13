---
title: "[JS] 자바스크립트 파일 문서화해주는 유용한 라이브러리 JSDoc"
date: 2022-09-27 20:11:55
tags: []
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">자바스크립트 파일 문서화해주는 유용한 라이브러리 JSDoc의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    REST API 문서화할때 자주 사용되는 Swagger 라이브러리처럼 자바스크립트 파일을 문서화해주는 라이브러리가 있다.</p>
</div>

<!-- more -->

REST API 문서화할때 자주 사용되는 [Swagger 라이브러리](https://sowon-dev.github.io/2020/09/21/200921opemsource/#%EC%8A%A4%EC%9B%A8%EA%B1%B0)처럼 자바스크립트 파일을 문서화해주는 라이브러리가 있다.

개발뿐만아니라 프로젝트 산출물시에도 활용할 수 있어 유용한 라이브러이이다.

# JSDoc

JavaScript용 API 문서 생성기이다. 공식사이트에 정말 자세히 잘 나와있다!

  * [공식 사이트](https://jsdoc.app/)
  * [공식 깃헙 리포지토리](https://github.com/jsdoc/jsdoc)

  
  
  

# 설치

```plain
npm install -g jsdoc
```

  
  
  

# 사용 예시

애노테이션(@)을 가지고 정말 쉽게 사용할 수 있다.  
문서확인은 `http://localhost/docs/` 로 가면 확인할 수 있다!

```plain
/**
 * 이 메서드는 유저서비스에 사용합니다
 * 
 * @module UserHelper
 * @author sowon-dev
 * @example 
 * // require에 모듈을 등록하고 사용합니다.
 * require([..., 'UserHelper'], function (..., UserHelper) 
 */
```
