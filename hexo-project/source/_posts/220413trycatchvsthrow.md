---
title: "try catch와 throws, throw의 차이"
date: 2022-04-13 04:52:33
tags: []
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'try catch와 throws, throw의 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    이 중 try catch와 throw의 차이는 무엇일까?의 차이를 고려하여 상황에 맞게 적용해야 한다.</p>
</div>

<!-- more -->

예외처리기법은 크게 3가지가 있다.

  1. try catch를 통한 예외처리
  2. throw로 그냥 예외발생시키기
  3. throws 키워드를 통한 예외처리 위임

이 중 try catch와 throw의 차이는 무엇일까?

## try catch와 throws의 차이

throws의 예외를 던지는 것, 즉 위임이다. 이는 처리와는 다르다.  
try catch는 예외를 받아서 처리하는 것이다. 이는 처리이다. catch구문에서 사용자가 흐름을 능동적으로 제어할 수 있다.

  
  
  

## throws

throws는 메서드에서 처리해야 할 하나 이상의 예외를 메서드를 호출한 곳으로 던져버린다.  
이러한 위임은 처리와는 다르다.  
try catch사용시 catch블록에서 예외를 처리해서 없애버린다.  
BUT 위임은 예외를 없애지 못하고 그냥 호출한 곳으로 예외를 전달만 한다.  
예외를 전달받은 메서드는 다시 예외 처리 책임이 발생한다.

throws를 쓰면 예외처리를 해줘야하는 번거로움이 있는데 왜 사용할까?  
주로 개발자가 직접 정의하는 예외를 발생시키고 싶은 경우 사용한다.

```java
public class Main {

	public static void customThrowExample() throws Exception {
		// 다시 예외처리해줘야한다.
		throw new Exception();
	}
	public static void main(String[] args) {
		try {
			customThrowExample();
		} catch (Exception e){
			System.out.println("catch구문은 잡히지않는다. try에서 customThrowExample으로 직접 예외를 발생시킴");
		}
	}
}
```

  
  
  

## 참고

  * [자바 Error와 Exception](https://sowon-dev.github.io/2020/07/21/200722javai/)
