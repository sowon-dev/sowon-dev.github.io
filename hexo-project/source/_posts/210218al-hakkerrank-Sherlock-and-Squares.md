---
title: "[자바JAVA]Sherlock and Squares 해커랭크"
date: 2021-02-18 04:29:16
tags:
  - "Hackerrank"
categories:
  - Reflections
  - Algorithm
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'Sherlock and Squares 해커랭크' 알고리즘 문제의 요구사항을 분석하고 최적의 자료구조와 연산 방식을 적용해 구현한 풀이다.
    Math 적절히 사용하면 한 줄 코드로 문제 해결아 가능하다.</p>
</div>

<!-- more -->

## Sherlock and Squares

주어진 수의 범위 안의 제곱근(square integer)의 갯수를 구하는 문제이다.  
Watson likes to challenge Sherlock’s math ability. He will provide a starting and ending value that describe a range of integers, inclusive of the endpoints. Sherlock must determine the number of square integers within that range.  
Note: A square integer is an integer which is the square of an integer, e.g. 1,4,9.16,25

  * 입출력예시1

```java
//입력
3 9

//출력
2
```

  * 입출력예시2

```java
//입력
17 24

//출력
0
```

  
  
  

## 풀이

```java
public class SherlockandSquares {
	static int squares(int a, int b) {
		//sol1
		int start = (int) Math.sqrt(a);
		int end = (int) Math.sqrt(b);
		
		start = (Math.pow(start, 2) >= a) ? start-1 : start;

		return end - start;	}

	public static void main(String[] args) {
		System.out.println(squares(24, 49) + ", ans: 3");
		System.out.println(squares(3, 9) + ", ans: 2");
		System.out.println(squares(17, 24) + ", ans: 0");
		System.out.println(squares(100, 1000) + ", ans: 22");
		System.out.println(squares(9, 16) + ", ans: 2");
		System.out.println(squares(11, 734) + ", ans: 24");
		System.out.println(squares(228, 919) + ", ans: 15");
		System.out.println(squares(71, 188) + ", ans: 5"); //9 10 11 12 13
		System.out.println(squares(4, 4) + ", ans: 1");
	}

}
```

  
  
  

## 한 줄 풀이

Math 적절히 사용하면 한 줄 코드로 문제 해결아 가능하다.

```java
public class SherlockandSquares {
	static int squares(int a, int b) {		
		//sol2. one line code
		return (int) Math.floor(Math.sqrt(b)) - (int) Math.ceil(Math.sqrt(a)) + 1;
	}

	public static void main(String[] args) {
		System.out.println(squares(24, 49) + ", ans: 3");
		System.out.println(squares(3, 9) + ", ans: 2");
		System.out.println(squares(17, 24) + ", ans: 0");
		System.out.println(squares(100, 1000) + ", ans: 22");
		System.out.println(squares(9, 16) + ", ans: 2");
		System.out.println(squares(11, 734) + ", ans: 24");
	}

}
```

  
  
  

## 해커랭크의 다른 문제 풀이가 보고싶다면?

  * [해커랭크(HackerRank) Easy Level java 풀이 모음](https://github.com/sowon-dev/AlgorithmStudy_Java/tree/master/src/hackerrank)

#[Hackerrank](/tags/Hackerrank/)
