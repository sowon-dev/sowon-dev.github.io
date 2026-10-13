---
title: "[자바JAVA]문자열 내 p와 y의 개수 프로그래머스"
date: 2021-02-27 21:59:33
tags:
  - "Programmers"
categories:
  - Reflections
  - Algorithm
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'문자열 내 p와 y의 개수 프로그래머스' 알고리즘 문제의 요구사항을 분석하고 최적의 자료구조와 연산 방식을 적용해 구현한 풀이다.
    시간 복잡도와 메모리 사용량을 고려한 효율적인 구현 코드로 문제를 통과할 수 있다.</p>
</div>

<!-- more -->

## 문자열 내 p와 y의 개수

대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 ‘p’의 개수와 ‘y’의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. ‘p’, ‘y’ 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.  
예를 들어 s가 “pPoooyY”면 true를 return하고 “Pyy”라면 false를 return합니다.

  * 제한사항  
문자열 s의 길이 : 50 이하의 자연수  
문자열 s는 알파벳으로만 이루어져 있습니다.

  * 입출력 예시1

```plain
//입력
pPoooyY

//출력
true
```

  * 입출력 예시2

```plain
//입력
Pyy

//출력
false
```

  
  
  

## 코드1

제일 처음 생각했던 방법이다.

```java
static boolean solution(String s) {
//sol1. score 1004, 평균 통과 (0.02ms, 51.8MB)

int cntP = 0;
int cntY = 0;
for(char c : s.toCharArray()){
  if(c == 'p' || c =='P'){
	cntP ++;
  }
  if(c == 'y' || c == 'Y'){
	cntY ++;
  }
}

return cntP == cntY;
}
```

  
  
  

## 코드2

int cnt를 하나로 가져가면서 toUpperCase 사용하는 방법이다.  
평균 통과 (0.04ms, 53.9MB)

```java
static boolean solution(String s) {
int cnt = 0;
    for(char c : s.toUpperCase().toCharArray()){
      if(c == 'P'){
        cnt ++;
      }
      if(c == 'Y'){
        cnt --;
      }
    }
 
    return cnt == 0 ? true : false;
}
```

  
  
  

## 코드3 : 람다식 사용

평균 통과 (3.37ms, 53.3MB)

```java
static boolean solution(String s) {
    s = s.toUpperCase();
    return s.chars().filter( e -> 'P'== e).count() == s.chars().filter( e -> 'Y'== e).count();
}
```

#[Programmers](/tags/Programmers/)
