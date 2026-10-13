---
title: "[자바JAVA] Maximum Perimeter Triangle 해커랭크"
date: 2021-03-13 20:24:40
tags:
  - "Hackerrank"
categories:
  - Reflections
  - Algorithm
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'Maximum Perimeter Triangle 해커랭크' 알고리즘 문제의 요구사항을 분석하고 최적의 자료구조와 연산 방식을 적용해 구현한 풀이다.
    * 해커랭크(HackerRank) Easy Level java 풀이 모음을 확인했다.</p>
</div>

<!-- more -->

## 문제 : Maximum Perimeter Triangle

a non-degenerate triangle이 되는 가장 긴 둘레를 구하는 문제이다.  
a non-degenerate triangle란 무엇일까? 구글링해보니 아래 3가지 조건을 충족하는 삼각형이라고 한다. 한국어로 부르는 명칭은 찾을 수 없었다. 분명 있을텐데…

  1. a+b>c
  2. a+c>b
  3. b+c>a

Given an array of stick lengths, use 3 of them to construct a non-degenerate triangle with the maximum possible perimeter.  
Return an array of the lengths of its sides as 3 integers in non-decreasing order.

If there are several valid triangles having the maximum perimeter:

  1. Choose the one with the longest maximum side.
  2. If more than one has that maximum, choose from them the one with the longest minimum side.
  3. If more than one has that maximum as well, print any one them.  
If no non-degenerate triangle exists, return [-1].

  * 입출력예시1

```java
//입력
[1, 2, 3, 4, 5, 10]

//출력
[3,4,5]
```

  * 입출력예시2

```java
//입력
[1, 1, 1, 3, 3]

//출력
[1,3,3]
```

  * 입출력예시3

```java
//입력
[1,1,1,2,3,5]

//출력
[1,1,1]
```

  
  
  

## 코드

```java
static int[] maximumPerimeterTriangle(int[] sticks) {

    int answerArr[] = new int[3];
    Arrays.sort(sticks);

    // non-degenerate triangle의 조건 만족하는 지 확인하기
    // 반복문을 통해서 answerArr요소는 조건에 부합하는 가장 큰 숫자가 된다. 따라서 가장 긴 둘레 조건 충족된다.
    boolean isNonDegenerateTriangle = false;
    for (int i = 0; i < sticks.length - 2; i++) {
      int a = sticks[i];
      int b = sticks[i + 1];
      int c = sticks[i + 2];

      if ((a + b) > c && (a + c) > b && (b + c) > a) {
        answerArr[0] = (int) a;
        answerArr[1] = (int) b;
        answerArr[2] = (int) c;
        isNonDegenerateTriangle = true;
      }
    }

	//a non-degenerate triangle 조건을 충족하지 못했으므로 -1 arr를 리턴한다.
    if (!isNonDegenerateTriangle) {
      return new int[]{-1};
    }

    System.out.print(Arrays.toString(answerArr));
    return answerArr;
  }

  public static void main(String[] args) {
    System.out.println(maximumPerimeterTriangle(new int[]{1, 2, 3, 4, 5, 10}) + ", ans: [3,4,5]");
    System.out.println(maximumPerimeterTriangle(new int[]{1, 1, 1, 3, 3}) + ", ans: [1,3,3]");
    System.out.println(maximumPerimeterTriangle(new int[]{1,1,1,2,3,5}) + ", ans: [1,1,1]");
  }
```

  
  
  

## 해커랭크의 다른 문제 풀이가 보고싶다면?

  * [해커랭크(HackerRank) Easy Level java 풀이 모음](https://github.com/sowon-dev/AlgorithmStudy_Java/tree/master/src/hackerrank)

#[Hackerrank](/tags/Hackerrank/)
