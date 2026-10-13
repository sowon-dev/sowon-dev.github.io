---
title: "[자바JAVA]Picking Numbers 해커랭크"
date: 2021-02-17 03:54:51
tags:
  - "Hackerrank"
categories:
  - Reflections
  - Algorithm
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'Picking Numbers 해커랭크' 알고리즘 문제의 요구사항을 분석하고 최적의 자료구조와 연산 방식을 적용해 구현한 풀이다.
    0부터 99까지의 숫자배열 temp를 만든 뒤 a의 요소값과 동일한 temp인덱스에 1씩 카운트를 증가시킨다.</p>
</div>

<!-- more -->

## Picking Numbers

list의 모든 요소들의 절대편차(absolute difference) <= 1 인 가장 긴 list의 길이를 출력하는 문제이다  
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

  * 입출력예시1

```java
//입력
4 6 5 3 3 1

//출력
3
```

  * 입출력예시2

```java
//입력
1 2 2 3 1 2

//출력
5
```

  
  
  

## 풀이

문제의 조건에서 0 < a[i] < 100이므로 maxIndex는 100이다.  
0부터 99까지의 숫자배열 temp를 만든 뒤 a의 요소값과 동일한 temp인덱스에 1씩 카운트를 증가시킨다.  
예를 들어, a=[1,1,2,2,4,4,5,5,5]인 경우 temp[0]=0, temp[1]=2, temp[2]=2, temp[3]=0, temp[4]=2, temp[5]=3, temp[6]=0, temp[7]=0, … , temp[99]=0이다.

temp[i]와 temp[i+1]의 합은 항상 절대편차가 <= 1이다. 따라서 배열 전체를 반복문으로 돌려서 두 요소의 합의 최대값을 리턴하면 되는 문제이다.  
예를 들어, 0번1번 인덱스를 더하면 2가 되고, 1번2번 인덱스를 더하면 4, 2번3번인덱스의 합은 2, 3번4번 인덱스를 더하면 2, 4번5번 인덱스 합은 5, 5번6번 인덱스합은 3, 6번7번 인덱스합은 0, 7번8번인덱스합은 0, …, 98번99번 인덱스합은 0 처럼 바로 옆 인덱스의 값을 합해서 99까지 반복한다.

```java
public class PickingNumbers {
	public static int pickingNumbers(List<Integer> a) {
		// 문제의 조건에서 0< a[i] <100이므로 maxIndex는 100이다.
        int maxIndex = 100;
        int[] temp = new int[maxIndex];
 
        //0부터 99까지의 숫자배열에 a의 요소와 동일한 숫자가 있으면 1씩 카운트룰 증가시킨다.
        //예를 들어 a = [1,2,1]인경우 temp[1]=2이고 temp[2]=1이다.
        for (int number : a) {
        	temp[number]++;
        }

        int result = 0;
 
        for (int i = 0; i < maxIndex - 1; i++) {
            result = Math.max(result, temp[i] + temp[i + 1]);
        }
        return result;
	}
	public static void main(String[] args) {
		System.out.println(pickingNumbers(new ArrayList<>(Arrays.asList(1, 1, 2, 2, 4, 4, 5, 5, 5)))+", ans: 5");
		System.out.println(pickingNumbers(new ArrayList<>(Arrays.asList(4, 6, 5, 3, 3, 1)))+", ans: 3");
		System.out.println(pickingNumbers(new ArrayList<>(Arrays.asList(1, 2, 2, 3, 1, 2)))+", ans: 5");
		System.out.println(pickingNumbers(Arrays.asList(98, 3, 99, 1, 97, 2)) == 2);
        System.out.println(pickingNumbers(Arrays.asList(1, 1, 1)) == 3);

	}
}
```

  
  
  

## 해커랭크의 다른 문제 풀이가 보고싶다면?

  * [해커랭크(HackerRank) Easy Level java 풀이 모음](https://github.com/sowon-dev/AlgorithmStudy_Java/tree/master/src/hackerrank)

#[Hackerrank](/tags/Hackerrank/)
