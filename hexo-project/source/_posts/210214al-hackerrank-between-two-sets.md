---
title: "[자바JAVA]Between Two Sets 해커랭크"
date: 2021-02-14 06:48:35
tags:
  - "Hackerrank"
categories:
  - Reflections
  - Algorithm
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'Between Two Sets 해커랭크' 알고리즘 문제의 요구사항을 분석하고 최적의 자료구조와 연산 방식을 적용해 구현한 풀이다.
    배열a와 배열b가 주어지고 a요소가 약수이면서 b요소가 배수인 숫자 X가 몇 개인 지 찾는 문제이다.</p>
</div>

<!-- more -->

## Between Two Sets

배열a와 배열b가 주어지고 a요소가 약수이면서 b요소가 배수인 숫자 X가 몇 개인 지 찾는 문제이다.

There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

  1. The elements of the first array are all factors of the integer being considered
  2. The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

  * 입출력예시1

```java
//입력
a = [2, 6]
b = [24, 36]

//출력
2
```

  * 입출력예시2

```java
//입력
a = [2, 4]
b = [16, 32, 96]

//출력
3
```

  
  
  

## 풀이

  * `int flag;` : a의 요소가 current의 약수가 아니거나 b의 요소가 current의 배수가 아닌 경우 flag 1 대입 후 break -> current를 1 더해준 뒤 다시 while문 반복 실행한다.

```java
public class BetweenTwoSets {

  public static int getTotalX(List<Integer> a, List<Integer> b) {
    int cnt = 0;
    int current = a.get(a.size() - 1);
    int flag;

    while (current <= b.get(0)) {
      flag = 0;

      //a 요소가 current의 약수면 flag=0 유지
      for (int i : a) {
        if (current % i != 0) {
          flag = 1;
          break;
        }
      }

      //b 요소가 current의 배수면 flag=0 유지
      if (flag == 0) {
        for (int i : b) {
          if (i % current != 0) {
            flag = 1;
            break;
          }
        }
      }

      //위의 두 for문이 참이면 cnt 1씩 증가
      if (flag == 0) {
        cnt++;
      }

      System.out.printf("cnt: %d, current: %d, flag: %d%n", cnt, current, flag);
      current++;
    }
    return cnt;
  }

  //테스트케이스
  public static void main(String[] args) {
    //test case 1
	System.out.println(getTotalX(
		new ArrayList<>(Arrays.asList(2, 6)), 
		new ArrayList<>(Arrays.asList(24, 36))) + ", ans: 2");
	//test case 2
    System.out.println(getTotalX(
		new ArrayList<>(Arrays.asList(2, 4)), 
		new ArrayList<>(Arrays.asList(16, 32, 96))) + ", ans: 3");
  }
}
```

  * test case 1번의 콘솔  
이 문제는 배열a와 배열b가 주어지고 a요소가 약수이면서 b요소가 배수인 숫자 X가 몇 개인 지 찾는 문제이다.  
flag가 0일때의 current값이 내가 찾던 x의 값이다.  
x는 6, 12 총 2개이다. 따라서 2를 리턴한다.

```plain
//test case 1번의 콘솔
cnt: 1, current: 6, flag: 0
cnt: 1, current: 7, flag: 1
cnt: 1, current: 8, flag: 1
cnt: 1, current: 9, flag: 1
cnt: 1, current: 10, flag: 1
cnt: 1, current: 11, flag: 1
cnt: 2, current: 12, flag: 0
cnt: 2, current: 13, flag: 1
cnt: 2, current: 14, flag: 1
cnt: 2, current: 15, flag: 1
cnt: 2, current: 16, flag: 1
cnt: 2, current: 17, flag: 1
cnt: 2, current: 18, flag: 1
cnt: 2, current: 19, flag: 1
cnt: 2, current: 20, flag: 1
cnt: 2, current: 21, flag: 1
cnt: 2, current: 22, flag: 1
cnt: 2, current: 23, flag: 1
cnt: 2, current: 24, flag: 1
2, ans: 2
```

  * test case 2번의 콘솔  
위의 설명과 동일하게 flag가 0일때의 current값이 내가 찾던 x의 값이다.  
x는 4, 8, 16으로 총 3개이다. 따라서 3를 리턴한다.

```plain
//test case 2번의 콘솔
cnt: 1, current: 4, flag: 0
cnt: 1, current: 5, flag: 1
cnt: 1, current: 6, flag: 1
cnt: 1, current: 7, flag: 1
cnt: 2, current: 8, flag: 0
cnt: 2, current: 9, flag: 1
cnt: 2, current: 10, flag: 1
cnt: 2, current: 11, flag: 1
cnt: 2, current: 12, flag: 1
cnt: 2, current: 13, flag: 1
cnt: 2, current: 14, flag: 1
cnt: 2, current: 15, flag: 1
cnt: 3, current: 16, flag: 0
3, ans: 3
```

  
  
  

## 해커랭크의 다른 문제 풀이가 보고싶다면?

  * [해커랭크(HackerRank) Easy Level java 풀이 모음](https://github.com/sowon-dev/AlgorithmStudy_Java/tree/master/src/hackerrank)

  
  
  

## 참고

  * <https://www.youtube.com/watch?v=gtvE0vxuvy8>

#[Hackerrank](/tags/Hackerrank/)
