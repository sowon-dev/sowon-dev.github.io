---
title: "[오류일지]React에러 Warning: Failed prop type: The prop `open` is marked"
date: 2021-03-24 15:52:27
tags:
  - "SpringBoot"
  - "오류일지"
categories:
  - Frontend
  - React
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">리액트 작업 도중 Warning: Failed prop type: The prop open is marked as required in ForwarRef(Menu), but its value is undefined 에러가 계속 발생했다.
    관련 환경 설정과 코드를 알맞게 수정하여 정상적으로 동작하도록 해결할 수 있다.</p>
</div>

<!-- more -->

## 상황

스프링부트와 리액트 MySQL를 사용하여 학사프로그램을 만들고 있다.  
리액트 작업 도중 Warning: Failed prop type: The prop `open` is marked as required in `ForwarRef(Menu)`, but its value is `undefined` 에러가 계속 발생했다.  
Menu인 부분이 뭐있을까 검색하면서 찾아보니 정말 어이없는 실수를 발견했다.

![에러발생](/img/210324ReactErr.PNG)

  
  
  

## 원인 및 해결

import시 @material-ui/icons/Menu를 해야했는데 @material-ui/core/Menu를 해놓은 것을 발견했다.  
core가 아닌 icons로 하니 에러가 더이상 발생하지 않았다.

![에러해결](/img/210324ReactErr2.PNG)

#[SpringBoot](/tags/SpringBoot/)[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)
