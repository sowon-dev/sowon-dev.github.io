---
title: "이벤트루프(Event loop)와 메인스레드(Main thread)"
date: 2022-01-04 05:31:30
tags:
  - "Node.js"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">이벤트루프(Event loop)와 메인스레드(Main thread)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    이벤트 루프 모델은 여러 스레드를 사용한다.</p>
</div>

<!-- more -->

탄탄한 자바스크립트 기본기를 다지기 위해 이벤트 루프에 대해 알아보자.

## 이벤트루프모델

이벤트 루프 모델은 여러 스레드를 사용한다.  
Node.js 프로세스에서 메인 스레드는 1개이며, 한 순간에 한 줄씩만 실행하지만 워커스레드(Worker thread)는 여러개이다.  
이벤트 루프는 앞에 있는 콜백이 전부 처리가 끝나야 다음 콜백을 처리할 수 있다.

## 용어정리

  * 메인스레드: 자바스크립트 코드가 실행되는 스레드
  * 워커스레드: 파일입출력스레드, 네트워크스레드등 메인스레드 외의 일을 하는 스레드
  * 콜스택: 현재까지 불린 함수들의 스택
  * 스택: 스택자료구조로 후입선출의 특성을 가진다.

![출처: 위키백과](https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Data_stack.svg/1280px-Data_stack.svg.png)

#[Node.js](/tags/Node-js/)
