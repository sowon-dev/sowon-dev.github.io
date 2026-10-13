---
title: "[JAVA] float, double 소수점 오류(부동소수점) 해결하기"
date: 2023-05-21 21:42:19
tags: []
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">컴퓨터의 메모리는 한정적이라 실수의 소숫점 표현에 제한이 있을 수 밖에 없고 이로인해 소수점이하 계산 오차가 발생한다.
    이를 해결하기 위해서는 2가지 방법이 있다.</p>
</div>

<!-- more -->

사용자가 기입한 확률을 DB에 넣고 싶었다.  
자세히 말하자면 사용자가 2라고 입력하면 백분율로 환산하여 DB에는 0.02로 넣고싶었다.  
그런데 입력된 DB 값을 보니 0.02가 아닌 0.019999999999999999…로 되어있었다.  
난 정확히 0.02를 넣고싶었는데 무엇이 잘못된걸까?

# 상황

마리아DB를 사용하고 있고 Data Type은 float이다.  
VO는 Double형을 선언했다.

  * 기존코드

```java
@Data
class Testvo{
  Double rate;
}
```

  
  
  

# 문제 원인

컴퓨터의 메모리는 한정적이라 실수의 소숫점 표현에 제한이 있을 수 밖에 없고 이로인해 소수점이하 계산 오차가 발생한다.  
이를 해결하기 위해서는 2가지 방법이 있다.

  1. int, long 정수형타입 치환
  2. BigDecimal 클래스 사용

계속 소수점을 이용해야했기에 2번방법을 사용했다.

  
  
  

# BigDecimal 클래스 사용한 사칙연산 간단 예시

```java
BigDecimal a = new BigDecimal("7");
BigDecimal a = new BigDecimal("3");

a.add(b);
= 10

a.subtract(b)
= 4

a.multiply(b);
= 21

a.divide(b);
= 2.3333...
```

다른 사칙연산과 달리 나눗셈을 하기 위해서는 `setScale()`을 사용해야 정확한 소수점 연산이 가능하다.

```java
BigDecimal setScale(int newScale);
BigDecimal setScale(int newScale, int roundingMode);
BigDecimal setScale(int newScale, RoundingMode mode);
```

첫번째 파라미터는 표시하고자하는 소수점의 자릿수이고  
두번째 파라미터는 라운딩모드이고 라운딩모드 상수값은 아래와 같다.

RoudingMode의 상수 | 설명  
---|---  
CELING | 올림  
FLOOR | 내림  
UP | 양수일 때는 올림, 음수일 때는 내림  
DOWN | 양수일 때는 내림, 음수일 때는 올림  
HALF_UP | 5기준으로 반올림(5이상 올림, 5미만 버림)  
HALF_EVEN | 반올림 자리의 값이 짝수면 HALF_DOWN, 홀수면 HALF_UP  
HALF_DOWN | 6기준으로 반올림(6이상 올림, 6미만 버림)  
UNNECESSARY | 나눗셈의 결과가 딱 떨어지는 수가 아니면, ArithmeticException발생  
  
  
  
  

# 해결코드

  * Service 코드

```java
BigDecimal feeRate = new BigDecimal(vo.getRate());
r.setSacle(6, RoudingMode.HALE_UP);
```

해결!

  
  
  

# 참고

  * [Inpa Dev - 소수 정확히 계산하는 방법](https://inpa.tistory.com/entry/JAVA-%E2%98%95-%EC%8B%A4%EC%88%98-%ED%91%9C%ED%98%84%EB%B6%80%EB%8F%99-%EC%86%8C%EC%88%98%EC%A0%90-%EC%9B%90%EB%A6%AC-%ED%95%9C%EB%88%88%EC%97%90-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0#:~:text=double%EA%B3%BC%20float%EC%9D%98%20%EB%B9%84%EA%B5%90%EC%97%B0%EC%82%B0%20%EB%AC%B8%EC%A0%9C,-%EC%8B%A4%EC%88%98%EB%A5%BC%20%EB%8D%94%ED%95%98%EA%B1%B0%EB%82%98&text=%EC%9E%90%EB%B0%94%EC%9D%98%20float%EB%8A%94%204,%EA%B0%80%20%EB%B0%9C%EC%83%9D%ED%95%9C%EB%8B%A4%EB%8A%94%20%EC%A0%90%EC%9D%B4%EB%8B%A4.)
  * [작은거인 - 부동소수점의 문제점과 해결책 (BigDecimal의 필요성)](https://blog.naver.com/passionisall/222139065323)
