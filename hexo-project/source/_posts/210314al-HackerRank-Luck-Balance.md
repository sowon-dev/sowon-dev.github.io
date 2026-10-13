---
title: "[자바JAVA]Luck Balance 해커랭크"
date: 2021-03-13 17:57:18
tags:
  - "Hackerrank"
categories:
  - Reflections
  - Algorithm
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'Luck Balance 해커랭크' 알고리즘 문제의 요구사항을 분석하고 최적의 자료구조와 연산 방식을 적용해 구현한 풀이다.
    * 해커랭크(HackerRank) Easy Level java 풀이 모음을 확인했다.</p>
</div>

<!-- more -->

## 문제 : Luck Balance

contests에서 각 대회가 중요하면 1이고 중요하지 않으면 0이다.  
k는 중요한 대회에서 질 수 있는 횟수이다.  
contests에서 지면 행운이 높아지고 이기면 행운이 낮아진다.  
최대 행운이 얼마인지 구하는 문제이다.  
Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. Initially, her luck balance is 0. She believes in “saving luck”, and wants to check her theory. Each contest is described by two integers, L[i] and T[i]:

  * L[i] is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by L[i]; if she loses it, her luck balance will increase by L[i].

  * T[i] denotes the contest’s importance rating. It’s equal to 1 if the contest is important, and it’s equal to 0 if it’s unimportant.  
If Lena loses no more than K important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? This value may be negative.

  * 입출력예시

```java
//입력
K=2
L = [5,1,4]
T = [1,2,0]

//출력
10
```

  
  
  

## 코드

```java
static int luckBalance(int k, int[][] contests) {

  int maxLuck = 0;
  int important = 0;

  List<Integer> luckList = new ArrayList<>();
  for (int i = 0; i < contests.length; i++) {
    if (contests[i][1] == 1) { //중요한 대회면 luckList에 담기
      important++;
      luckList.add(contests[i][0]);
    } else { //중요하지 않은 대회들은 바로 maxLuck에 누적합
      maxLuck += contests[i][0];
    }
  }

  //중요한대회만 luckList 오름차순으로 정렬
  Collections.sort(luckList);

  //가장 낮은 행운을 가진 대회 maxLuck에서 빼준다.
  int ableToLose = important - k;
  for (int i = 0; i < ableToLose; i++) {
    maxLuck -= luckList.remove(0); //가장 낮은 행운 빼기
  }

  //가장 높은 행운을 가진 대회를 maxLuck에 더해준다.
  for (int i = 0; i < luckList.size(); i++) {
    maxLuck += luckList.get(i);
  }

  return maxLuck;
}

public static void main(String[] args) {
  int[][] contests1 = {{5, 1}, {1, 1}, {4, 0}};
  int[][] contests2 = {{5, 1}, {2, 1}, {1, 1}, {8, 1}, {10, 0}, {5, 0}};
  System.out.println(luckBalance(2, contests1) + ", ans: 10");
  System.out.println(luckBalance(1, contests1) + ", ans: 8");
  System.out.println(luckBalance(3, contests2) + ", ans: 29");
}
```

  
  
  

## 해커랭크의 다른 문제 풀이가 보고싶다면?

  * [해커랭크(HackerRank) Easy Level java 풀이 모음](https://github.com/sowon-dev/AlgorithmStudy_Java/tree/master/src/hackerrank)

#[Hackerrank](/tags/Hackerrank/)
