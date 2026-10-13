---
title: "ClassCastException발생 Java.lang.Integer cannot be case to Java.lang.String 해결방법(ft. ChatGPT)"
date: 2023-02-13 23:37:19
tags:
  - "ChatGPT"
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">String을 int로 변환하는 과정에서 cast 에러가 발생했다.
    일단 해결부터! 아래로 캐스팅하니 바로 해결되었다.</p>
</div>

<!-- more -->

String을 int로 변환하는 과정에서 cast 에러가 발생했다.

# 문제상황

내가 원했던 건 DB에서 가져온 balance정보를 int로 바꿔주고싶었다. 쿼리가 아주 길지만 간략하게 요약해보면 아래와 같다.

  * 컬럼 정의
    * balance int(11) 잔액

```xml
<select id="getBalance" resultType="HashMap">
	select balance from User
</select>
```

```java
HashMap<String, String> map = dao.getBalance();

int curBalance = Integer.parseInt(map.get("balance"));

// 결과
// ClassCastException발생 Java.lang.Integer cannot be case to Java.lang.String
```

컴파일 에러는 안나지만 ClassCastException이 발생했다.  
이상했다.  
HashMap 데이터타입을 String으로 정의했는데 왜 Integer to String으로 캐스팅을 하는걸까? 

  
  
  

# 해결

일단 해결부터! 아래로 캐스팅하니 바로 해결되었다.

```java
int curBalance = Integer.valueOf(String.valueOf(map.get("balance")));
```

해결 방법은 금방 찾았으나 원인이 너무 궁금했다.  
다시 질문으로 돌아가보자. HashMap 데이터타입을 String으로 정의했는데 왜 Integer to String으로 캐스팅을 하는걸까? 

  
  
  

# 원인찾기

데이터타입이 무엇인지 정확히 알기위해 `getClass()`를 하니 Integer가 나왔다.

```java
map.get("balance").getClass();
// 결과 Java.lang.Integer
```

이게 말이 되는 건가?  
HashMap의 데이터타입을 String으로 정의했는데 어떻게 Integer가 들어간걸까?  
구글링해도 도저히 찾지 못하겠어서 팀장님께 질문드리니 팀장님이 아래와 같은 예제 코드를 주셨다. 

```java
HashMap test = new HashMap<>();
test.put("test", 123);
HashMap<String, String> test2 = test;

System.out.println(test2.get("test").getClass());
// 결과값 jva.lang.Integer
```

컴파일 에러없이 서버런해도 정상 작동해버리는 코드! 뭐야?  
팀장님께서는 자바8 제네릭에 대해 찾아보라는 조언을 주셨다. 역시 팀장님은 천재야…!

  
  
  

# 제네릭 타입소거 (ft.ChatGPT)

요즘 유행인 ChatGPT에게 물어봤다.

> This code will result in a compilation error because test is declared as a HashMap with a key of type String and a value of type Integer, while test2 is declared as a HashMap with a key and value of type String. Therefore, you cannot assign test to test2 as the two types are not compatible.  
> Assuming that test2 is declared correctly with the same key and value types as test, and test.put(“test”, 123) has been fixed to use a String value, the output of System.out.println(test2.get(“test”).getClass()) would be java.lang.Integer, since the value associated with the key “test” is an Integer. The getClass() method returns the runtime class of an object, which in this case is Integer since that’s the type of the value associated with the “test” key in the HashMap.

하지만 이 케이스는 컴파일에러가 발생하지 않기에 다시 물어봤다.

> Me: But there is no compilation error in java 8. how can you explain this?  
> ChatGPT: You are correct that in Java 8, the code you provided will compile without error.  
> In Java 8 and earlier versions, the generic types of a variable were not enforced by the compiler in all situations. This is known as type erasure, where the generic type information is removed during compilation and is not available at runtime. As a result, it was possible to assign a variable of type HashMap to a variable of type HashMap<String, String> or vice versa, even if the generic types were not the same.  
> However, this type of assignment is not recommended as it can result in runtime errors if the wrong types of data are inserted or retrieved from the map. Starting from Java 9, the compiler will issue a warning for this kind of unchecked conversion, and it is recommended to use generics correctly to avoid any potential issues.  
> So, while the code you provided will compile in Java 8, it is not considered good programming practice and may result in unexpected behavior if the wrong data types are used with the map.

요약해보자면, Java 8에서 제네릭타입은 컴파일 중 타입 소거(Type Erasure)되어 HashMap 타입의 변수를 `HashMap<String, String>` 타입의 변수에 할당하거나 그 반대의 경우에도 할당할 수 있게 된 것 이다.  
너무 신기하잖아😲  
ChatGPT에게 자바8 타입 소거(Type Erasure)에 대해 지금 예시로 알려달라고 요청했다.

> Me: Can you explain more about Type Erasure in this case?  
> ChatGPT: Sure, I’d be happy to explain type erasure in this case.  
> In Java, generic types were introduced in order to provide stronger type checking and to avoid class cast exceptions. A generic type is a type that can be parameterized with other types. For example, `List<T>` is a generic type that can be parameterized with another type, such as `List<String>`.  
> However, at runtime, Java’s virtual machine (JVM) doesn’t have access to the generic type information. This is where type erasure comes in. Type erasure is the process by which the JVM replaces the generic type parameters with their upper bounds or with Object, depending on the type’s use.  
> For example, in the code you provided, the HashMap is declared with a generic type of HashMap<String, Integer>. However, at runtime, the JVM replaces the type parameters with their upper bounds, which means that the HashMap object will be treated as if it were of type HashMap<Object, Object>. This is why, in Java 8 and earlier versions, it is possible to assign a variable of type HashMap to a variable of type HashMap<String, String> or vice versa, as the generic type information is not used to enforce the type compatibility between the two variables.  
> In summary, type erasure is a process by which the JVM removes the generic type information from a class or method, and replaces it with its upper bounds or with Object. This can lead to unchecked type conversions and potential runtime errors, which is why it is recommended to use generics correctly and to avoid unchecked conversions.

요약해보자면 아래와 같다.

  
  
  

## 타입 소거(Type Erasure)란?

Type Erasure(타입 소거)란 제네릭 타입에 사용된 타입 정보를 컴파일 타임에만 사용하고 런타임에는 소거하는 것을 말한다.  
자바 컴파일러는 모든 타입 파라미터를 Object 타입으로 교체한다. 제네릭 타입을 제거한 후 타입이 일치하지 않으면 타입 캐스팅을 추가한다. 

  
  
  

### 왜 Object 타입으로 바꿀까?

런타임시 Java 가상 머신(JVM)은 제네릭 타입 정보에 접근할 수 없다. 그래서 타입 소거(Type Erasure)가 필요하다.  
즉, 타입 소거는 JVM이 제네릭 타입 매개변수를 상한값으로 또는 Object로 대체하는 과정이다.  
런타임에서 JVM은 상한값으로 타입 매개변수를 대체하므로 HashMap 객체는 HashMap<Object, Object> 타입인 것처럼 처리된다. 그래서 Java 8 이전 버전에서 HashMap 타입의 변수를 HashMap<String, String> 타입의 변수에 할당할 수 있게 된 것이다.  
즉, 제네릭 타입 정보가 두 변수 간의 타입 호환성을 강제하기 위해 사용되지 않기 때문입니다.

  
  
  

### 결론

타입 소거는 JVM이 클래스 또는 메서드에서 제네릭 타입 정보를 제거하고 상한값으로 또는 Object로 대체하는 과정이다. 이는 검사되지 않은 타입 변환 및 잠재적인 런타임 오류를 발생시킬 수 있기 때문에 올바른 제네릭 사용을 권장하고 검사되지 않은 변환을 피해야 한다.

ChatGPT 진짜 천재다.😲

  
  
  

# 참고

  * 김팀장님 지식
  * ChatGPT
  * <https://wisdom-and-record.tistory.com/134>

#[ChatGPT](/tags/ChatGPT/)
