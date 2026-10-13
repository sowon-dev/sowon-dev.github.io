---
title: "제네릭(Generic) 타입파라미터(T) vs 와일드카드(?) 차이"
date: 2022-07-14 21:47:59
tags:
  - "차이"
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'제네릭(Generic) 타입파라미터(T) vs 와일드카드(?) 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    제네릭의 장점은 컴파일시 데이터타입을 체크해줘서 타입이 안정적이고 타입체크와 형변환을 생략할 수 있어 코드가 간결해진다.</p>
</div>

<!-- more -->

제네릭(Generic)의 사전적 의미는 일반화이다.  
제네릭의 장점은 컴파일시 데이터타입을 체크해줘서 타입이 안정적이고 타입체크와 형변환을 생략할 수 있어 코드가 간결해진다.

## 와일드카드(<?>)

  1. 하나의 참조 변수로 대입된 타입이 다른 객체를 참조 가능하다.

분류 | 설명  
---|---  
<? extneds T> | 와일드 카드의 상한 제한. T와 그 자손들만 가능.실무에서 가장 많이 사용함  
<? super T> | 와일드 카드의 하한 제한. T와 그 조상들만 가능  
<?> | 제한 없으므르 모든 타입 가능. <? extneds Object>와 동일  
  

```java
ArrayList<? extneds Fruit> list = new ArrayList<apple>(); // OK
ArrayList<? extneds Fruit> list = new ArrayList<orange>(); // OK

ArrayList<apple> list = new ArrayList<orange>(); // 에러발생
```

  2. 메서드의 매개변수에 와일드 카드를 사용할 수 있다.

```java
class Payment {
	static Payment buyFruit(FruitBox<? extends Fruit> box){
		// 매개변수에 와일드카드를 사용했다.
	}
}
```

  
  
  

## 타입 매개변수(<T>)

타입 매개변수는 총 3곳에서 사용할 수 있다.

명 | 사용 위치  
---|---  
제네릭 인터페이스 | 인터페이스에 타입 매개변수를 사용  
제네릭 클래스 | 클래스에 타입 매개변수를 사용  
제네릭 메서드 | 메서드에 타입 매개변수를 사용  
  
이 중에서 오늘 다룰 내용은 제네릭 클래스이다.  
제네릭 클래스의 인스턴스를 생성할 때 타입 매개변수로 전달받은 타입으로 데이터타입이 정해진다.

```java
// 제니릭 클래스 선언
class 클래스명<타입 매개변수>{
}

// 제네릭 클래스 생성
new 클래스명<타입 인자>(new 타입매개변수());

// 제네릭 클래스 생성 - JDK7이후부터는 타입인자 생략 가능
new 클래스명<타입 인자>();
```

과일로 예시를 들어보자.

```java
class FruitBox<T>{
	T fruit;
	public FruitBox
}

// 제네릭 클래스 생성
new FruitBox<Grape>(new Grape());
new FruitBox<Pear>(new Pear());

// 제네릭 클래스 생성 - JDK7이후부터는 타입인자 생략 가능
new FruitBox<>(new Grape());
new FruitBox<>(new Pear());
```

  
  
  

## 와일카드 vs 정규타입 매개변수 T차이

> The difference is that if you have a type parameter U, you can use that type inside the method;  
> if you use a wildcard, you don’t have access to the actual type inside the method (you only know that it is some unknown type that extends Number).  
> If you need to know the actual type for whatever reason inside the method, then you cannot use the wildcard version.  
> 출처: [coderanch 블로그](https://coderanch.com/t/688561/java/difference-Bounded-Type-Parameters-Upper)

  * 와일드카드는 Object를 받기때문에 get메서드를 사용할 수 있지만 set, put메서드는 사용할 수 없다.
  * 타입 매개변수는 get, set, put메서드는 사용가능하다.

  
  
  

## 참고

  * [기본클래스 이외에 자바 구성요소3 : annotation, generic](https://sowon-dev.github.io/2020/07/19/200720javai2/)
  * 추천영상: 자바의 정석 기초편 와일드카드, 지네릭 메서드 by 남궁성의 정석코딩 유튜브채널

#[차이](/tags/%EC%B0%A8%EC%9D%B4/)
