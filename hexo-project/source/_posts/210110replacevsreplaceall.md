---
title: "[자바JAVA]125. Valid Palindrome"
date: 2021-01-09 19:20:04
tags:
  - "Leetcode"
categories:
  - Reflections
  - Algorithm
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'125. Valid Palindrome'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    코드1과 비교해보니 성능면에서 좋지않았다. 하지만 한 줄로 풀이할 수 있음에 엄청난 재미를 느꼈다! 생각 해 낸 개발자는 엄청난 희열을 느꼈겠지?의 차이를 고려하여 상황에 맞게 적용해야 한다.</p>
</div>

<!-- more -->

## 문제 125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.  
Note: For the purpose of this problem, we define empty string as valid palindrome.

  * 입출력예시

```java
//예시1
Input: "A man, a plan, a canal: Panama"
Output: true

//예시2
Input: "race a car"
Output: false
```

  
  
  

## Palindrome(팰린드롬)이란?

해당 문제는 팰린드롬이라고 불린다.  
한국에서 쉽게 찾아볼 수 있는 예로는 옛날옛적 <슈퍼주니어의 로꾸꺼>가 있다.  
그 가사를 보면

```plain
아많다많다많다많아
다이뿐이뿐이뿐이다
여보게저기저게보여
여보안경안보여
통술집술통 소주만병만주소
다이심전심이다 뽀뽀뽀
아좋다좋아 수박이박수
다시합창합시다
```

  
  
  

## 문제 접근법

`아좋다좋아`는 앞에서부터 뒤로 읽거나 뒤에서 앞으로 읽어도 `아좋다좋아`가 된다.  
문제에서 원하는 것은 알파벳과 숫자만 체크를 해서 boolean형태로 리턴하는 것이다.  
즉, `아 좋 다 좋 아`, `아, 좋다. 좋아!` 등등 아무리 많은 공백과 특수기호가 있더라도 true가 반환되어야한다.

그렇다면 String에서 어떻게 알파벳과 숫자만 남겨두고 나머지는 잘라버릴 수 있을까?

  1. split()을 사용할까?  
처음에는 split()을 생각해봤는데 특수문자와 기호가 너무 많기 때문에 다 처리하는 것은 불가능했다.
  2. 그럼 replace로 대체해버릴까?  
replace(char oldChar, char newChar)의 형태로 파라미터로 character가 들어간다.  
특수문자와 기호등이 너무 많아 char로 처리가 불가능하다.
  3. replaceAll로 정규식을 이용하자!  
replaceAll(String regex, String replacement)의 형태로 파라미터로 regex(정규식)을 넣을 수 있다.

  
  
  

## 코드

  * Runtime 24ms Memory 40MB 

```java
public static boolean isPalindrome(String s) {
    //sol1. => Runtime 24ms Memory 40MB
    //정규식으로 알파벳이 아닌 것들을 없앤다
    String s1 = s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
    System.out.println(s1);

    //반으로 나눈뒤 글자가 일치하는 지 확인한다.
    for(int i=0; i<s1.length()/2; i++){
      if(s1.charAt(i) != s1.charAt(s1.length()-i-1)){
        return false;
      }
    }
    return true;
}
```

  
  
  

## 한 줄 코드

구글링을 하다보니 한 줄로 풀이를 한 코드가 눈에 띄었다.

  * [Frankenstein’s-Function-One-Line-Java-Solution](https://leetcode.com/problems/valid-palindrome/discuss/1008365/Frankenstein's-Function-One-Line-Java-Solution)
  * Runtime 39 ms Memory 40.4 MB

코드1과 비교해보니 성능면에서 좋지않았다. 하지만 한 줄로 풀이할 수 있음에 엄청난 재미를 느꼈다! 생각 해 낸 개발자는 엄청난 희열을 느꼈겠지?

```java
public static boolean isPalindrome(String s) {
    //sol2 => Runtime 39 ms Memory 40.4 MB
    return new StringBuilder().append(s).reverse().toString()
        .replaceAll("[^a-zA-Z0-9]", "").toLowerCase()
        .equals(s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase()) ? true: false;
}
```

  
  
  

## 배운내용 : 정규표현식

자주 사용하는 정규식은 암기해두면 좋다.

위에서 사용한 정규식 `[^a-zA-Z0-9]`을 설명하자면,

  * `[]` : 문자열을 뜻한다.
  * `^` : 문자열안에 들어가면 not의 의미한다.
  * `a-z` : 소문자 전체를 의미한다.
  * `A-Z` : 대문자 전체를 의미한다.
  * `0-9` : 숫자 전체를 의미한다.

즉 대소문자와 숫자를 포함하지 않는 문자열 전체를 뜻하는 정규식이다.  
참고로

  * 한글은 `가-힣`이다.

  * `^`는 두가지 의미가 있다. 위에서는 2번으로 사용되었다.

    1. `^`, `\A`: (위치) 문자열의 시작
    2. `[^문자열]` : 문자열의 문자를 제외한 문자에 매핑
  * [참고 링크 : 정규표현식, 자주 사용하는 정규식](https://sowon-dev.github.io/2020/08/10/200810javai2/)

  
  
  

## 배운내용 : replace() VS replaceAll()

차이점 | replace() | replaceAll()  
---|---|---  
형태 | replace(char oldChar, char newChar) | replaceAll(String regex, String replacement)  
Parameters | character | regular expression  
Returns | replaced string | replaced string  
  

```java
String s = "안녕하세요! 행복하세요~"

//예시 : replace()
System.out.println(s.replace("하","ha")); // 안녕ha세요! 행복ha세요~

//예시 : replaceAll()
System.out.println(s.replaceAll("요","yo")); // 안녕하세yo! 행복하세yo~
System.out.println(s.replaceAll("[^가-힣]","")); // 안녕하세요행복하세요
```

  * [Java String replace()](https://www.javatpoint.com/java-string-replace)

  
  
  

## 다른 문제 풀이가 보고싶다면?

  * [모든 릿코드(LeetCode)(leetcode) java 풀이](https://github.com/sowon-dev/AlgorithmStudy_Java/tree/master/src/leetcodeEasyLevel)

#[Leetcode](/tags/Leetcode/)
