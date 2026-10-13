---
title: "[자바JAVA]Missing Numbers 해커랭크"
date: 2021-03-07 04:05:52
tags:
  - "Hackerrank"
categories:
  - Reflections
  - Algorithm
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'Missing Numbers 해커랭크' 알고리즘 문제의 요구사항을 분석하고 최적의 자료구조와 연산 방식을 적용해 구현한 풀이다.
    arr과 brr을 비교하여 brr에는 있지만 arr에는 없는 숫자(Missing Numbers)를 배열로 나타내는 문제.을 적용해 성능을 최적화했다.</p>
</div>

<!-- more -->

## 문제

arr과 brr을 비교하여 brr에는 있지만 arr에는 없는 숫자(Missing Numbers)를 배열로 나타내는 문제.

Given two arrays of integers, find which elements in the second array are missing from the first array.

Function Description : Complete the missingNumbers function in the editor below. It should return a sorted array of missing numbers.  
missingNumbers has the following parameter(s):

  * int arr[n]: the array with missing numbers
  * int brr[m]: the original array of numbers

Returns : int[]: an array of integers

  * 입출력예시

```java
//입력
10
203 204 205 206 207 208 203 204 205 206
13
203 204 204 205 206 207 205 208 203 206 205 206 204

//출력
204 205 206
```

  
  
  

## 코드

두 배열을 각각 HashMap에 담은 뒤 (brr 해쉬맵 - arr 해쉬맵)을 통해 빠진 숫자를 효율적으로 찾을 수 있다.

```java
public class MissingNumbers {

  static int[] missingNumbers(int[] arr, int[] brr) {

    HashMap<Integer, Integer> hashmapA = new HashMap<Integer, Integer>();
    HashMap<Integer, Integer> hashmapB = new HashMap<Integer, Integer>();

    //arr을 HashMap으로 만든 뒤 반복되는 숫자가 있으면 value값을 1 누적합한다.
    for (int i : arr) {
      if (hashmapA.containsKey(i)) {
        hashmapA.put(i, hashmapA.get(i) + 1);
      } else {
        hashmapA.put(i, 1);
      }
    }

    //brr을 HashMap으로 만든 뒤 반복되는 숫자가 있으면 value값을 1 누적합한다.
    for (int j : brr) {
      if (hashmapB.containsKey(j)) {
        hashmapB.put(j, hashmapB.get(j) + 1);
      } else {
        hashmapB.put(j, 1);
      }
    }

    //HashMapB - HashMapA한 값을 리스트 diff에 담는다.
    ArrayList<Integer> diff = new ArrayList<Integer>();
    for (Integer i : hashmapB.keySet()) {
      if (hashmapA.get(i) == null || hashmapA.get(i) < hashmapB.get(i)) {
        diff.add(i);
      }
    }

    //리스트를 배열로 만든다.
    int[] result = new int[diff.size()];
    for (int i = 0; i < diff.size(); i++) {
      result[i] = diff.get(i);
    }

    System.out.println(Arrays.toString(result));
    return result;
  }

  public static void main(String[] args) {
    System.out.println(missingNumbers(new int[]{203, 204, 205, 206, 207, 208, 203, 204, 205, 206},
        new int[]{203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204})
        + ", ans: [204 205 206]");
  }
}
```

  
  
  

## 참고

  
  
  

## 해커랭크의 다른 문제 풀이가 보고싶다면?

  * [해커랭크(HackerRank) Easy Level java 풀이 모음](https://github.com/sowon-dev/AlgorithmStudy_Java/tree/master/src/hackerrank)

#[Hackerrank](/tags/Hackerrank/)
