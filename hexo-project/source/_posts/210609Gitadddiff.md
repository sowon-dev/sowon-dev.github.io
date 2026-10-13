---
title: "[GIT]git add의 차이"
date: 2021-06-08 22:09:39
tags:
  - "GIT"
categories:
  - Reflections
  - Version control
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'git add의 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    동작 원리와 장단점을 비교 파악하여 프로젝트 개발 상황에 적합한 방식을 선택할 수 있다.</p>
</div>

<!-- more -->

GIT명령어 비슷한 것들도 많고 여간 헷갈리는 것이 아니다. 헷갈리는 김에 정리해보았다.

## `git add .` 와 `git add *` 차이

  * `git add .`: .gitignore에 기재된 것 고려하여 모두 추가
  * `git add *`: .gitignore에 기재된 것 상관없이 모두 추가

따라서 그냥 `git add .`를 사용하자

#[GIT](/tags/GIT/)
