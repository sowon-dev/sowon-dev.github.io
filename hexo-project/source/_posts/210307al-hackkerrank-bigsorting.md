---
title: "[자바JAVA]Big Sorting 해커랭크"
date: 2021-03-07 05:14:22
tags:
  - "Hackerrank"
categories:
  - Reflections
  - Algorithm
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'Big Sorting 해커랭크' 알고리즘 문제의 요구사항을 분석하고 최적의 자료구조와 연산 방식을 적용해 구현한 풀이다.
    String 타입의 정렬안된 배열을 숫자오름차순으로 숫자를 정렬하는 문제이다.</p>
</div>

<!-- more -->

## 문제

String 타입의 정렬안된 배열을 숫자오름차순으로 숫자를 정렬하는 문제이다.

Consider an array of numeric strings where each string is a positive number with anywhere from to digits. Sort the array’s elements in non-decreasing, or ascending order of their integer values and return the sorted array.

  * 입출력예시1

```java
//입력
[1 200 150 3]

//출력
[1 3 150 200]
```

  * 입출력예시2

```java
//입력
6 <-길이
31415926535897932384626433832795
1
3
10
3
5

//출력
1
3
3
5
10
31415926535897932384626433832795
```

  * 입출력예시3

```java
//입력
8 <-길이
1
2
100
12303479849857341718340192371
3084193741082937
3084193741082938
111
200

//출력
1
2
100
111
200
3084193741082937
3084193741082938
12303479849857341718340192371
```

  
  
  

## 첫 시도: NumberFormatException

처음에는 String[]을 long[]로 바꾼 뒤 오름차순 정렬 후 다시 String[]로 만들어서 출력하고자했다.  
하지만 숫자가 long보다 더 커서 NumberFormatException이 발생했다.

```java
public class BigSorting {

  static String[] bigSorting(String[] unsorted) {
	//String arr를 long arr로 바꾼다.
    long[] arr = new long[unsorted.length];
    for (int i = 0; i < unsorted.length; i++) {
      arr[i] = Long.parseLong(unsorted[i]);
    }
	
	//long 배열을 오름차순정렬한다.
    Arrays.sort(arr);

	//정렬한 long배열을 String 배열로 바꾼 뒤 리턴한다.
    String[] result = new String[unsorted.length];
    for (int i = 0; i < unsorted.length; i++) {
      result[i] = Long.toString(arr[i]);
    }
    System.out.println(Arrays.toString(result));
    return result;
  }

  public static void main(String[] args) {
    System.out.println(bigSorting(new String[]{"1", "200", "150", "3"}) + ", ans: [1 3 150 200]");
    System.out.println(
        bigSorting(new String[]{"31415926535897932384626433832795", "1", "3", "10", "3", "5"})
            + ", ans: [1 3 3 5 10 31415926535897932384626433832795]");
  }
}
```

  
  
  

## 성공한 코드

람다식을 활용하여 unsorted 배열을 정렬했다.  
`x.compareTo(y)`는 int를 리턴한다. 

  * x == y면 0을 출력, 
  * x > y 면 1을 출력,
  * x < y 면 -1을 출력한다

리턴한 값을 기준으로 sort한다.

```java
public class BigSorting {

  static String[] bigSorting(String[] unsorted) {
    Arrays.sort(unsorted, (x, y) -> {
      System.out.print("시작 arr: "+Arrays.toString(unsorted) + "   x: "+x+"   y:"+y);
      if (x.length() == y.length()) {
        System.out.print("    x.compareTo(y): "+x.compareTo(y)+"\n");
        return x.compareTo(y); //자리수에 상관없이 첫째자리만 보고 오름차순 정렬
      }else {
        System.out.print("     x.length() - y.length(): "+ (x.length() - y.length()) +"\n");
        return x.length() - y.length(); //자리수에 상관한 오름차순 정렬
      }
    });

    return unsorted;
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    String[] arr = new String[n];
    for (int i = 0; i < n; i++) {
      arr[i] = sc.next();

    }
    arr = bigSorting(arr);
    for (int i = 0; i < arr.length; i++) {
      System.out.println(arr[i]);
    }
    sc.close();
  }
}
```

arr, x, y를 출력하면 아래와 같다.  
근데 `x.compareTo(y): 2`가 어떻게 나왔는지 구글링을 해도 모르겠다… 왜 2가 나왔지?  
그래서 그냥 암기하기로했다…..

```js
시작 arr: [31415926535897932384626433832795, 1, 3, 10, 3, 5]   x: 1   y:31415926535897932384626433832795     x.length() - y.length(): -31
시작 arr: [31415926535897932384626433832795, 1, 3, 10, 3, 5]   x: 3   y:1    x.compareTo(y): 2
시작 arr: [1, 31415926535897932384626433832795, 3, 10, 3, 5]   x: 3   y:31415926535897932384626433832795     x.length() - y.length(): -31
시작 arr: [1, 31415926535897932384626433832795, 3, 10, 3, 5]   x: 3   y:1    x.compareTo(y): 2
시작 arr: [1, 3, 31415926535897932384626433832795, 10, 3, 5]   x: 10   y:3     x.length() - y.length(): 1
시작 arr: [1, 3, 31415926535897932384626433832795, 10, 3, 5]   x: 10   y:31415926535897932384626433832795     x.length() - y.length(): -30
시작 arr: [1, 3, 10, 31415926535897932384626433832795, 3, 5]   x: 3   y:10     x.length() - y.length(): -1
시작 arr: [1, 3, 10, 31415926535897932384626433832795, 3, 5]   x: 3   y:3    x.compareTo(y): 0
시작 arr: [1, 3, 3, 10, 31415926535897932384626433832795, 5]   x: 5   y:3    x.compareTo(y): 2
시작 arr: [1, 3, 3, 10, 31415926535897932384626433832795, 5]   x: 5   y:31415926535897932384626433832795     x.length() - y.length(): -31
시작 arr: [1, 3, 3, 10, 31415926535897932384626433832795, 5]   x: 5   y:10     x.length() - y.length(): -1
```

  
  
  

## 참고

  * 람다식 : <https://codeman77.tistory.com/40>
  * compareTo() : <https://www.tutorialspoint.com/java/number_compareto.htm>

  
  
  

## 해커랭크의 다른 문제 풀이가 보고싶다면?

  * [해커랭크(HackerRank) Easy Level java 풀이 모음](https://github.com/sowon-dev/AlgorithmStudy_Java/tree/master/src/hackerrank)

#[Hackerrank](/tags/Hackerrank/)
