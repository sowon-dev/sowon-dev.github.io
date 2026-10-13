---
title: "[Spring]@Transactional 속성 총정리"
date: 2022-12-22 20:35:29
tags: []
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'@Transactional 속성 총정리' 알고리즘 문제의 요구사항을 분석하고 최적의 자료구조와 연산 방식을 적용해 구현한 풀이다.
    레거시 코드를 분석하면서 다양한 @Transactional 속성을 만났다.</p>
</div>

<!-- more -->

레거시 코드를 분석하면서 다양한 @Transactional 속성을 만났다.  
평소에 디폴트로만 썼었기에 이참에 정리해보았다.

# @Transactional 이란?

먼저 Transaction을 살펴보자. 트랜젝션은 데이터베이스의 상태를 변화시키기 위한 작업 수행의 논리적 단위를 의미한다.  
테스트를 위해 서비스에서 SQL쿼리를 호출한 후 롤백을 해야하는 경우라든지 전체 실행 중 특정 수행이 오류가 나면 이전에 완료했던 SQL쿼리들을 다 롤백해야할 경우에 @Transactional을 사용한다.

자세한 내용은 포스팅 [@Transactional 쓰는 이유](https://sowon-dev.github.io/2021/08/04/210805Spring-Transactional/)를 참고하면 된다.

  
  
  

# @Transactional 에 우선순위가 있다?

@Transactional은 우선순위를 가지고 있다.

  1. 클래스 메서드
  2. 클래스
  3. 인터페이스 메서드
  4. 인터페이스

클래스 메서드에 선언된 트랜잭션의 우선순위가 가장 높다.  
가장 구체적으로 구현된 것부터 트랜잭션순위가 높다고 생각하면 된다.

  
  
  

# 속성

속성명 | 특징 | 옵션  
---|---|---  
isolation | 일관성없는 데이터 허용 수준을 설정 | DEFAULT, READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE  
noRollbackFor, rollbackFor | 특정 예외발생시 rollback하지않음 or rollback함으로 설정 |   
noRollbackForClassName, rollbackForClassName | 특정 클래스이름인 경우 rollback하지않음 or rollback함으로 설정 | (e.g)rollbackForClassName=”Exception”  
propagation(전파속성) | 트랜잭션 동작 도중 다른 트랜잭션을 호출할 때, 어떻게 할 것인지 설정 | REQUIRED(Defualt), REQUIRES_NEW, SUPPORT, NOT_SUPPORT, MANDATORY, NEVER, NESTED  
readOnly | 트랜잭션을 읽기 전용으로 설정. true면 insert, update, delete 실행 시 예외 발생 | true, false(Defualt)  
timeout, timeoutString | 지정한 시간내에 메서드수행이 완료되지 않으면 rollback함으로설정(단위 : 초,seconds) |   
transactionManager | 특정 Transaction의 qualifier value를 설정 |   
value | transactionManager의 alias(별칭)을 설정한다. |   
  
  * <https://nesoy.github.io/articles/2019-05/Database-Transaction-isolation>
  * <https://n1tjrgns.tistory.com/266>

  
  
  

# isolation 레벨

  1. DEFAULT : 기본 격리 수준
  2. READ_UNCOMMITED (level 0): 트랜잭션의 동시 액세스 허용, 커밋되지 않는 데이터에 대한 읽기를 허용
  3. READ_COMMITED (level 1) : 커밋된 데이터에 대해 읽기 허용, Dirty read 방지
  4. REPEATEABLE_READ (level 2) : 동시 액세스를 허용하지 않음, 동일 필드에 대해 다중 접근 시 모두 동일한 결과를 보장, Dirty read, Nonrepeatable read 방지
  5. SERIALIZABLE (level 3) : 가장 높은 격리, 성능 저하의 우려가 있음, 모든 부작용을 방지

  
  
  

## isolation 문제점

[feco님 블로그 글 - 트랜잭션, 트랜잭션 격리수준(Isolation Level)](https://feco.tistory.com/45)에 예시까지 잘 설명되어있다! 꼭 읽어보길!  
아래는 feco님 블로그글의 격리성 문제점부분만 발췌했다.

  1. Dirty Read: 한 트랜잭션(T1)이 데이타에 접근하여 값을 ‘A’에서 ‘B’로 변경했고 아직 커밋을 하지 않았을때, 다른 트랜잭션(T2)이 해당 데이타를 Read 하면? T2가 읽은 데이타는 B가 될 것이다. 하지만 T1이 최종 커밋을 하지 않고 종료된다면, T2가 가진 데이타는 꼬이게 된다.
  2. Non-Repeatable Read: 한 트랜잭션(T1)이 데이타를 Read 하고 있다. 이때 다른 트랜잭션(T2)가 데이타에 접근하여 값을 변경 또는, 데이타를 삭제하고 커밋을 때려버리면? 그 후 T1이 다시 해당 데이타를 Read하고자 하면 변경된 데이타 혹은 사라진 데이타를 찾게 된다.
  3. Phantom Read: 트랜잭션(T1) 중에 특정 조건으로 데이타를 검색하여 결과를 얻었다. 이때 다른 트랜잭션(T2)가 접근해 해당 조건의 데이타 일부를 삭제 또는 추가 했을때, 아직 끝나지 않은 T1이 다시 한번 해당 조건으로 데이타를 조회 하면 T2에서 추가/삭제된 데이타가 함께 조회/누락 된다. 그리고 T2가 롤백을 하면? 데이타가 꼬인다

  
  
  

# propagation(전파속성) 레벨

트랜잭션 동작 도중 다른 트랜잭션을 호출할 때, 어떻게 할 것인지 전파속성을 선택할 수 있다. 총 7가지 속성이 있다.

  1. REQUIRED(Defualt): 이미 진행중인 트랜잭션이 있다면 해당 트랜잭션 속성을 따르고, 진행중이 아니라면 새로운 트랜잭션을 생성한다.
  2. REQUIRES_NEW: 항상 새로운 트랜잭션을 생성한다. 이미 진행중인 트랜잭션이 있다면 잠깐 보류하고 해당 트랜잭션 작업을 먼저 진행한다.
  3. SUPPORT: 이미 진행 중인 트랜잭션이 있다면 해당 트랜잭션 속성을 따르고, 없다면 트랜잭션을 설정하지 않는다.
  4. NOT_SUPPORT: 이미 진행중인 트랜잭션이 있다면 보류하고, 트랜잭션 없이 작업을 수행한다.
  5. MANDATORY: 이미 진행중인 트랜잭션이 있어야만, 작업을 수행한다. 없다면 Exception을 발생시킨다.
  6. NEVER: 트랜잭션이 진행중이지 않을 때 작업을 수행한다. 트랜잭션이 있다면 Exception을 발생시킨다.
  7. NESTED: 진행중인 트랜잭션이 있다면 중첩된 트랜잭션이 실행되며, 존재하지 않으면 REQUIRED와 동일하게 실행된다.

  
  
  

# 참고

  * <https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/transaction/annotation/Transactional.html>
  * <https://nesoy.github.io/articles/2019-05/Database-Transaction-isolation>
  * <https://velog.io/@kdhyo/JavaTransactional-Annotation-%EC%95%8C%EA%B3%A0-%EC%93%B0%EC%9E%90-26her30h>
