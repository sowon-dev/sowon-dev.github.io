---
title: "[Java] TimeUnit의 sleep() 사용하기"
date: 2022-12-12 15:39:23
tags: []
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">TimeUnit의 sleep() 사용하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    js에서는 setTimeout()이나 setInterval()을 자주 사용했는데 자바에서는 어떻게 사용할까?을 적용할 수 있다.</p>
</div>

<!-- more -->

js에서는 [setTimeout()이나 setInterval()](https://sowon-dev.github.io/2019/09/21/190922/)을 자주 사용했는데 자바에서는 어떻게 사용할까?  
바로 TimeUnit의 static메서드인 sleep()이 있다.

# TimeUnit

TimeUnit는 자바가 제공하는 Enum타입클래스이다.  
시간에 관한 열거형 클래스로 두날짜의 차이를 구하기, sleep()걸기 등에 유용하게 쓰인다.

  * DAYS 
  * HOURS 
  * MICROSECONDS 
  * MILLISECONDS 
  * MINUTES 
  * NANOSECONDS 
  * SECONDS 

  
  
  

# sleep()

TimeUnit.class에 sleep()이 선언되어있다.  
파라미터에 따라 Thread.sleep()을 쉽게 걸어준다.  
열거형이기때문에 직관적이고 static 메서드라 바로 사용할 수 있다는 것이 장점이다.

```java
 /**
 * Performs a {@link Thread#sleep(long, int) Thread.sleep} using
 * this time unit.
 * This is a convenience method that converts time arguments into the
 * form required by the {@code Thread.sleep} method.
 *
 * @param timeout the minimum time to sleep. If less than
 * or equal to zero, do not sleep at all.
 * @throws InterruptedException if interrupted while sleeping
 */
public void sleep(long timeout) throws InterruptedException {
	if (timeout > 0) {
		long ms = toMillis(timeout);
		int ns = excessNanos(timeout, ms);
		Thread.sleep(ms, ns);
	}
}
```

  
  
  

# 예시

다양하게 사용할 수 있다.

```java
// 5분 지연시키기
TimeUnit.MINUTES.Sleep(5);

// 10초 지연시키기
TimeUnit.SECONDS.sleep(10);
```

  
  
  

# 참고

  * <https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/TimeUnit.html>
