---
title: "[Spring]@Transactional 쓰는 이유"
date: 2021-08-04 20:05:51
tags: []
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">@Transactional 쓰는 이유의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    핵심 설정과 구현 코드를 단계별로 파악하여 상황에 맞게 유연하게 활용할 수 있다.</p>
</div>

<!-- more -->

세상에 이렇게 재밌는 일이 또 있을까?  
습관처럼 쓰던 것들이 왜 써야하는 지 알게될 때의 그 재미.  
정말 겪어 본 사람만 안다.

## 이럴때 있으시죠?

Service에서 mapper로 여러 SQL쿼리를 처리할 때 그 중 하나가 오류가 난 경우 그 전에 실행되었던 SQL 쿼리들이 다 롤백되어야한다.  
이를 트랜잭션 처리라고 부른다.  
트랜잭션 처리는 SQL에서 할 수도 있고 Spring에서 할수도 있다.

  
  
  

## Spring에서 트랜잭션을 설정하는 2가지 방법

  1. xml파일에서 AOP + tx:advice 태그 활용
  2. 어노테이션 @Transactional

트랜잭션처리를 하면 transaction begin, commit을 자동 수행해준다. 만약 예외가 생겼다면 rollback 처리를 자동 수행해준다.  
정말 간편!

  
  
  

## Springboot에서 @Transactional 설정

어노테이션은 클래스뿐만 아니라 인터페이스, 클래스 내 메서드위에도 붙일 수 있다.  
세상 간편!

주로 아래 에시코드처럼 서비스 클래스 위에 붙여준다.  
이걸로 설정 끝!

```java
@Service
@Transactional(rollbackFor = Exception.class)
public class UserServiceImpl implements UserService {
 
  @Override
  public void insertUser(UserDTO user) throws Exception{
    	// 비즈니스 로직
	}

  // 기타 메서드
}
```

위 예시 코드의 rollbackFor속성외에도 @Transactional에는 다양한 속성이 있다. [하누모카님의 @Transactional 포스팅](https://www.hanumoka.net/2018/09/11/spring-20180911-spring-Transactional/)에 알기 쉽게 적혀있다. 꼭 읽어보자!

그리고 rollbackFor 속성을 꼭 붙여줘야하는 이유는 [kdhyo님의 @Transactional Annotation 알고 쓰자 포스팅](https://velog.io/@kdhyo/JavaTransactional-Annotation-%EC%95%8C%EA%B3%A0-%EC%93%B0%EC%9E%90-26her30h)에 정말 자세하게 나와있으니 꼭 읽어보자. 정말 좋은 글이다.

  
  
  

## 요약

요약하자면 @Transactional은 기본적으로 Unchecked Exception, Error를 rollback한다.  
try catch로 명시해준 에러인 경우 Checked Exception이기 때문에 트랜잭션이 일어나지 않을 수 있다.  
따라서 `rollbackFor = Exception.class`속성을 통해서 Unchecked Exception, Error뿐만 아니라 checked Exception도 트랜잭션 처리를 가능하게할 수 있다!
