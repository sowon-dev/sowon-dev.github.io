---
title: "[자바JAVA]Grid Challenge 해커랭크"
date: 2021-03-13 15:46:40
tags:
  - "Hackerrank"
categories:
  - Reflections
  - Algorithm
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'Grid Challenge 해커랭크' 알고리즘 문제의 요구사항을 분석하고 최적의 자료구조와 연산 방식을 적용해 구현한 풀이다.
    전체코드는 아래와 같다.</p>
</div>

<!-- more -->

## 문제: Grid Challenge

주어진 그리드의 열이 사전순 정렬이면 YES를 출력하는 문제로 그리드의 행은 순서를 변경할 수 있다.  
Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

  * 입출력예시1

```java
//입력
["abc", "ade", "efg"]

//출력
YES
```

  
  
  

## 코드

행을 사전순으로 정렬하는 것은 쉬웠지만 열이 사전순 정렬인지 확인하는 부분이 어려웠다.

```java
(생략)
for (int i = 0; i < grid[0].length(); i++) {
  for (int j = 0; j < grid.length - 1; j++) {
	if (grid[j].charAt(i) > grid[j + 1].charAt(i)) {
	  return "NO";
	}
  }
}
(후략)
```

위의 부분에서 입출력예시를 가지고 설명한다면, `grid[j].charAt(i) > grid[j + 1].charAt(i)`이 부분은 먼저 grid[0].charAt(1) > grid[1].charAt(1) 을 비교한다. 둘다 a 이기때문에 사전순을 만족한다. 이 부분을 반복하면 아래와 같다.

```xml
1. grid[0].charAt(0) > grid[1].charAt(0) 을 비교
a  a => 사전순 맞음

2. grid[1].charAt(0) > grid[2].charAt(0) 을 비교
a  e => 사전순 맞음

// 여기까지 첫번째 열 비교 완료
// 두번째 열 비교 시작

3. grid[0].charAt(1) > grid[1].charAt(1) 을 비교
b  d => 사전순 맞음

4. grid[1].charAt(1) > grid[2].charAt(1) 을 비교
d  f => 사전순 맞음

// 여기까지 두번째 열 비교 완료
// 세번째 열 비교 시작

5. grid[0].charAt(2) > grid[1].charAt(2) 을 비교
c  e => 사전순 맞음

6. grid[1].charAt(2) > grid[2].charAt(2) 을 비교
e  g => 사전순 맞음
```

전체코드는 아래와 같다.

```java
static String gridChallenge(String[] grid) {
  // 1. 행을 사전순 정렬하기
  // String을 char로 변환하여 사전순으로 sort한 후 다시 grid[i]번째에 넣는다.
  for (int i = 0; i < grid.length; i++) {
    char[] chars = grid[i].toCharArray();
    Arrays.sort(chars);
    grid[i] = String.valueOf(chars);
  }

  // 2. 열이 사전순 정렬인지 확인하기
  // 지금 열과 다음 열의 i번째를 비교하여 사전순이 아니면 NO를 출력
  for (int i = 0; i < grid[0].length(); i++) {
    for (int j = 0; j < grid.length - 1; j++) {
      if (grid[j].charAt(i) > grid[j + 1].charAt(i)) {
        return "NO";
      }
    }
  }

  return "YES";
}

public static void main(String[] args) {
  System.out.println(gridChallenge(new String[]{"abc", "ade", "efg"}) + ", ans:YES");
  System.out.println(gridChallenge(new String[]{"ebacd", "fghij", "olmkn", "trpqs", "xywuv"}) + ", ans:YES");
  System.out.println(gridChallenge(new String[]{"kc", "iu"}) + ", ans:YES");
  System.out.println(gridChallenge(new String[]{"uxf", "vof", "hmp"}) + ", ans:NO");
}
```

  
  
  

## 해커랭크의 다른 문제 풀이가 보고싶다면?

  * [해커랭크(HackerRank) Easy Level java 풀이 모음](https://github.com/sowon-dev/AlgorithmStudy_Java/tree/master/src/hackerrank)

#[Hackerrank](/tags/Hackerrank/)
