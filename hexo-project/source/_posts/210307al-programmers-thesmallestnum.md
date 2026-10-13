---
title: "[자바JAVA]제일 작은 수 제거하기 프로그래머스"
date: 2021-03-07 04:13:38
tags:
  - "Programmers"
categories:
  - Reflections
  - Algorithm
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'제일 작은 수 제거하기 프로그래머스' 알고리즘 문제의 요구사항을 분석하고 최적의 자료구조와 연산 방식을 적용해 구현한 풀이다.
    정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.</p>
</div>

<!-- more -->

## 문제 : 제일 작은 수 제거하기

정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

  * 입출력예시1

```java
//입력
[4,3,2,1]

//출력
[4,3,2]
```

  * 입출력예시2

```java
//입력
[10]

//출력
[-1]
```

  
  
  

## 첫번째 시도 코드

아래 코드는 프로그래머스에 `코드실행` (테스트케이스)는 정상 실행되나 `제출 후 채점하기`에서 실패가 되었다.  
어떤 점이 문제인지 한참을 고민했다.

```java
public class quizprogrammersthesmallestnum {
  static int[] solution(int[] arr) {
    // 제일 작은 수 제거한 배열을 리턴하는 문제
    if (arr.length <= 1) {
      System.out.println(Arrays.toString(new int[] {-1}));
      return new int[] {-1};
    }

    // 배열에서 가장 작은 수 찾기
    int min = arr[0];
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] < min) {
        min = arr[i];
      }
    }

    // 찾은 가장 작은 수만 빼고 정답배열에 넣기
    int[] answer = new int[arr.length - 1];
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] != min) {
        answer[i] = arr[i]; 
      }
    }

    System.out.println(Arrays.toString(answer));
    return answer;
  }

  public static void main(String[] args) {
    System.out.println(solution(new int[] {4, 3, 2, 1}) + ", ans: [4,3,2]");
    System.out.println(solution(new int[] {10}) + ", ans: [-1]");
  }
}
```

answer 배열의 index문제였다.

```java
(전략)
    // 찾은 가장 작은 수만 빼고 정답배열에 넣기
    int[] answer = new int[arr.length - 1];
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] != min) {
        answer[i] = arr[i]; //여기가 수상하다.
      }
    }
(하략)
```

제시된 두 테스트케이스는 제일 작은 수가 마지막에 위치해있기때문에 아무런 문제가 없으나 제일 작은 수가 배열의 중간에 위치한다면 answer의 index가 띄엄띄엄 되어버리는 문제가 발생하기때문이다.  
예를 들어 입력값이 [4, 1, 2, 3]인 경우 출력값은 가장 작은 숫자 1을 뺀 [4,2,3]이다.

위의 코드로 실행시켜보면 아래와 같이 ArrayIndexOutOfBoundsException가 발생한다. 

```java
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 3
```

그 이유는 코드에서 answer[1]이 1이기때문에 if문에 false가 되면서 다음 인덱스인 2로 넘어간다.  
answer[2]는 2이기때문에 min값과 달라서 if문이 true라 실행이되면서 `answer[2] = arr[2]`가 된다.  
그럼 answer 배열은 answer[1]이 없고 answer[3]가 생기면서 answer의 길이보다 1 많아지게 되면서 ArrayIndexOutOfBoundsException가 발생하게 되는 것이다.

이를 해결하기 위해서는 answer만의 index가 필요하다. 

  
  
  

## 완성된 코드

```java
public class quizprogrammersthesmallestnum {
  static int[] solution(int[] arr) {
    // 제일 작은 수 제거한 배열을 리턴하는 문제
    if (arr.length <= 1) {
      System.out.println(Arrays.toString(new int[] {-1}));
      return new int[] {-1};
    }

    // 배열에서 가장 작은 수 찾기
    int min = arr[0];
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] < min) {
        min = arr[i];
      }
    }

    // 찾은 가장 작은 수만 빼고 정답배열에 넣기
    int idx = 0; //answer전용 index를 선언했다.
    int[] answer = new int[arr.length - 1];
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] != min) {
        answer[idx] = arr[i]; //answer전용 index를 사용
        idx++;
      }
    }

    System.out.println(Arrays.toString(answer));
    return answer;
  }
}
```

  
  
  

## 향상된 코드 : Arrays.stream() 사용

프로그래머스는 다른 사람의 풀이를 볼 수 있다.  
이는 아주 큰 장점인데 세상에 얼마나 많은 천재가 있는지 보여준다!  
그들의 풀이를 보면서 정말 많이 배운다!

```java
class Solution {
  public int[] solution(int[] arr) {
      if (arr.length <= 1) return new int[]{ -1 };
      int min = Arrays.stream(arr).min().getAsInt();
      return Arrays.stream(arr).filter(i -> i != min).toArray();
  }
}
```

Arrays.stream()를 사용한 풀이는 정말 간결해서 놀라웠다.

  
  
  

## Arrays.stream() 개념과 예제

Arrays.stream()란 자바 8부터 Arrays.stream()를 사용할 수 있는 메서드로 배열이나 컬렉션에서 for 또는 foreach 문 도는 것을 대신하여 사용할 수 있다.  
foreach문처럼 요소를 하나씩 참조하여 람다식으로 처리할 수 있다.

```java
// 기본 배열과 리스트
String[] strArr = {"aaa", "bbb", "ccc"};

// 스트림 생성
Stream<String> strStream1 = Arrays.stream(strArr);

// 스트림 출력
strStream1.sorted().forEach(System.out::println);

//출력값
aaa
bbb
ccc
```

  * filter(): 주어진 조건(Predicate)에 맞지 않는 요소를 걸러낸다.

아래는 스트림으로 1부터 10까지를 만든 뒤 `filter()`를 이용하여 짝수만 찾아내는 예제이다.

```java
// filter()
IntStream example2Stream = IntStream.rangeClosed(1, 10);
example2Stream.filter(i -> i%2 ==0).forEach(System.out::print); // 246810
```

  
  
  

## 참고

  * <https://ryan-han.com/post/java/java-stream/>

#[Programmers](/tags/Programmers/)
