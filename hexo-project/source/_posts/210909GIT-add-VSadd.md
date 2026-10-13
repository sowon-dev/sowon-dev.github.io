---
title: "[GIT]`git add .` 와 `git add *` 차이"
date: 2021-09-08 14:14:28
tags:
  - "GIT"
categories:
  - Reflections
  - Version control
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'`git add .` 와 `git add *` 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    동작 원리와 장단점을 비교 파악하여 프로젝트 개발 상황에 적합한 방식을 선택할 수 있다.</p>
</div>

<!-- more -->

간단한 내용이지만 적어두지않으면 잊어버리기 쉽다.

## `git add .` 와 `git add *` 차이

  * `git add .`: .gitignore에 기재된 것 고려하여 모두 추가
  * `git add *`: .gitignore에 기재된 것 상관없이 모두 추가

따라서 `git add .`를 사용하자.

#[GIT](/tags/GIT/)
