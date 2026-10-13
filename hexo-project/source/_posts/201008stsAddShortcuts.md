---
title: "[스프링SPRING]STS 단축키 추가하기(스프링 이클립스 단축키), System.out.printf()단축키"
date: 2020-10-07 17:47:32
tags:
  - "TIL"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">STS 단축키 추가하기(스프링 이클립스 단축키), System.out.printf()단축키의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * Context : Java statements 설정을 적용할 수 있다.</p>
</div>

<!-- more -->

## STS 단축키 추가하기

Spring Tool Suite 4(STS)는 이클립스환경이다. 이클립스와 동일하게 단축키도 이용가능한 줄 알았다.  
`sout` \+ Ctrl + Space를 통해서 `System.out.println()`을 이용하려고 했는데 단축키가 적용되지않았다.  
`sysout` 매번 입력하기는 너~~~~무 귀찮기때문에 구글링하여 직접 단축키를 추가해보았다.

이클립스도 STS와 별반 다르지않게 단축키를 추가할 수 있다.

![](/img/201008stsAddShortcuts.PNG)

  
  
  

## 1\. Window > Preferences 클릭 > Templates검색

## 2\. Java-Editor하위의 Templates 클릭(사진 속 1번 참조)

  * 여기서 내장되어있는 단축키를 확인할 수 있다.
  * 기존 단축키 수정도 가능하고 새로운 단축키 추가도 가능하다

## 3\. New버튼클릭(사진 속 2번 참조)

## 4\. Edit Template에 단축키 추가(사진 속 3번 참조)

  * Name : 원하는 단축키
  * Context : Java statements 설정
  * Description : 단축키 설명 입력
  * Pattern : 단축키 입력시 원하는 동작 추가

```java
//Pattern예시
System.out.println(${word_selection}${});${cursor}
```

나는 두가지를 단축키로 추가하였다.

  * `System.out.println()`를 `sout`으로 단축키 추가 지정
  * `System.out.printf()`를 `souf`로 단축키 추가 지정

```java
//`System.out.println()`를 `sout`으로 단축키 추가 지정시 Pattern예시
System.out.println(${word_selection}${});${cursor}

//`System.out.printf()`를 `souf`로 단축키 추가 지정시 Pattern예시
System.out.printf(${word_selection}${});${cursor}
```

## 5\. OK클릭 > Apply and Close 클릭(사진 속 4번 참조)

  * 단축키가 잘 되는 지 확인한다.
  * 완-벽!

#[TIL](/tags/TIL/)
