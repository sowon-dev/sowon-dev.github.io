---
title: "[자바JAVA]Two Characters 해커랭크"
date: 2021-02-27 18:53:14
tags:
  - "Hackerrank"
categories:
  - Reflections
  - Algorithm
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'Two Characters 해커랭크' 알고리즘 문제의 요구사항을 분석하고 최적의 자료구조와 연산 방식을 적용해 구현한 풀이다.
    2차원 배열로 접근할 수 있다.</p>
</div>

<!-- more -->

## 문제 : Two Characters

주어진 String의 요소 2가지만을 추출하여 String을 만들때 가장 길이가 긴 String의 길이값을 리턴하는 문제이다.  
Given a string, remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Determine the longest string possible that contains just two alternating letters

  * 입출력예시1

```java
//입력
beabeefeab

//출력
5
```

  
  
  

## 코드

2차원 배열로 접근할 수 있다.

```java
public class TwoCharacters {

  public static final int NUM_LETTERS = 26;

  static int alternate(int length, String s) {
    int maxPattern = 0;

    if(s.length() == 1)//Edge case where length is 1
    {
      return maxPattern;
    }

    /* Create arrays representing the 26^2 subproblems */
    int[][] pair = new int[NUM_LETTERS][NUM_LETTERS];
    int[][] count = new int[NUM_LETTERS][NUM_LETTERS];

    for (int i = 0; i < length; i++) {
      char letter = s.charAt(i);
      int letterNum = letter - 'a';

      /* Update row */
      for (int col = 0; col < NUM_LETTERS; col++) {
        if (pair[letterNum][col] == letter) {
          count[letterNum][col] = -1;
        }
        if (count[letterNum][col] != -1) {
          pair[letterNum][col] = letter;
          count[letterNum][col]++;
        }
      }

      /* Update column */
      for (int row = 0; row < NUM_LETTERS; row++) {
        if (pair[row][letterNum] == letter) {
          count[row][letterNum] = -1;
        }
        if (count[row][letterNum] != -1) {
          pair[row][letterNum] = letter;
          count[row][letterNum]++;
        }
      }
    }

    /* Find max in "count" array */
    for (int row = 0; row < NUM_LETTERS; row++) {
      for (int col = 0; col < NUM_LETTERS; col++) {
        maxPattern = Math.max(maxPattern, count[row][col]);
      }
    }

    return maxPattern;
  }

  public static void main(String[] args) {
    System.out.println(alternate(10, "beabeefeab")+", ans: 5");
  }
}
```

  * 참고 : <https://studyalgorithms.com/string/hackerrank-two-characters/>

  
  
  

## 해커랭크의 다른 문제 풀이가 보고싶다면?

  * [해커랭크(HackerRank) Easy Level java 풀이 모음](https://github.com/sowon-dev/AlgorithmStudy_Java/tree/master/src/hackerrank)

#[Hackerrank](/tags/Hackerrank/)
