---
title: "[자바JAVA] 전위연산(a++)과 후위연산(++a) 차이점"
date: 2020-10-04 17:37:15
tags:
  - "TIL"
  - "ITWILL(JAVA)"
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'전위연산(a++)과 후위연산(++a) 차이점'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    아래 문제를 통해 차이점을 알아보자의 차이를 고려하여 상황에 맞게 적용해야 한다.</p>
</div>

<!-- more -->

## [전위 증감 연산자(prefix) VS 후위 증감 연산자(postfix)](https://sowon-dev.github.io/2020/06/08/200609jspi/#%EC%A0%84%EC%9C%84%EC%97%B0%EC%82%B0-VS-%ED%9B%84%EC%9C%84%EC%97%B0%EC%82%B0)

  * 전위 증감 연산자(++a,–a) : 연산 후 대입
  * 후위 증감 연산자(a++,a–) : 대입 후 연산

## 예시

아래 문제를 통해 차이점을 알아보자

```java
int a, b;
a = b = 10;

boolean c = ++a > b++ || a++ >= ++b;
System.out.println(a+","+b);
System.out.println("변수 c의 값 :"+c);
```

## 답

```java
11, 11
true
```

## 풀이

  * `++a > b++`의 값은 11 > 10 이라서 true
  * `a++ >= ++b`의 값은 11 >= 12 라서 false
  * 그렇다면 출력할때 왜 12,12가 아닌 11,11이 나올까?
    * 컴파일러는 앞부분이 true인 경우 굳이 `||` 연산자 뒤를 연산 할 필요가 없다.
    * 따라서 12,12가 아닌 11,11이고 이것이 논리연산자의 특징이다.

  
  
  

## 참고

  * [추가학습 : 코딩 도장](https://dojang.io/mod/page/view.php?id=96)

#[TIL](/tags/TIL/)[ITWILL(JAVA)](/tags/ITWILL-JAVA/)
