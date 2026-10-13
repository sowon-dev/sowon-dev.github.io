---
title: "[JPA] 리턴타입이 옵셔널(Optional)인 이유는?"
date: 2022-07-10 22:19:54
tags: []
categories:
  - Backend
  - JPA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">리턴타입이 옵셔널(Optional)인 이유는?의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    Optional은 Java 8에 추가되었다. 이전 자바버전에서는 사용 불가능하다.</p>
</div>

<!-- more -->

JPA를 사용 중 아래 코드를 만났고 의문이 생겼다.

```java
final Optional<TodoEntity> original = repository.findById(entity.getId());
```

왜 꼭 Optional로 리턴타입을 감싸줘야하는걸까?  
그냥 리턴타입만 쓰면 안될까?

```java
final TodoEntity original = repository.findById(entity.getId());
```

이런식으로 말이다.  
위처럼 옵셔널(Optional)을 빼버리니 바로 IDE가 에러를 알려주었다.

```plain
Type mismatch: cannot convert from Optional<TodoEntity> to TodoEntity
```

왜 이런 에러가 발생하는 걸까?  
원인은 바로 CrudRepository 인터페이스였다.

  
  
  

## 갑자기 CrudRepository라고?

Repository 인터페이스를 만들때 JPA를 쓰기 위해서 JpaRepository를 상속받는다.  
JpaRepository인터페이스에서 find와 관련된 메서드를 알기위해서는 CrudRepository를 확인하라고 적혀있다.

  * JpaRepository 인터페이스

```java
/**
 * JPA specific extension of {@link org.springframework.data.repository.Repository}.
 *
 * @author Oliver Gierke
 * @author Christoph Strobl
 * @author Mark Paluch
 * @author Sander Krabbenborg
 * @author Jesse Wouters
 * @author Greg Turnquist
 */
@NoRepositoryBean
public interface JpaRepository<T, ID> extends PagingAndSortingRepository<T, ID>, QueryByExampleExecutor<T> {

	/*
	 * (non-Javadoc)
	 * @see org.springframework.data.repository.CrudRepository#findAll()
	 */
	@Override
	List<T> findAll();

	/*
	 * (non-Javadoc)
	 * @see org.springframework.data.repository.PagingAndSortingRepository#findAll(org.springframework.data.domain.Sort)
	 */
	@Override
	List<T> findAll(Sort sort);

	/*
	 * (non-Javadoc)
	 * @see org.springframework.data.repository.CrudRepository#findAll(java.lang.Iterable)
	 */
	@Override
	List<T> findAllById(Iterable<ID> ids);

	// (중략)
}
```

  
  
  

## CrudRepository 인터페이스

CrudRepository 인터페이스에서 findById 메서드를 확인해보면 리턴값이 Optional 타입으로 고정되어있다.  
그래서 바로 IDE가 에러를 알려주었다. 그렇다면 Optional를 쓰면 좋은 점이 뭘까?

```java
/**
 * Interface for generic CRUD operations on a repository for a specific type.
 *
 * @author Oliver Gierke
 * @author Eberhard Wolff
 * @author Jens Schauder
 */
@NoRepositoryBean
public interface CrudRepository<T, ID> extends Repository<T, ID> {

	/**
	 * Retrieves an entity by its id.
	 *
	 * @param id must not be {@literal null}.
	 * @return the entity with the given id or {@literal Optional#empty()} if none found.
	 * @throws IllegalArgumentException if {@literal id} is {@literal null}.
	 */
	Optional<T> findById(ID id);
 
	// (생략)
}
```

  
  
  

## Optional 쓰면 좋은 점?

Optional은 Java 8에 추가되었다. 이전 자바버전에서는 사용 불가능하다.  
Optional은 고통스러운 null 처리를 도와주는 Wrapper 클래스이다.

코드 예시를 보자.

```java
class Person {
	String name;
    
	String getName(){
    	if(name != null) {
        	return name;
        }
        return "name is null";
 	}
}
```

또는 try catch문을 이용해서 null을 처리할 수 있도 있고 다양한 NPE 처리 방법이 있다. 

  * [참고: 특별한 거 추가 없이 기본 메서드로 NPE처리하는 방법](https://sowon-dev.github.io/2021/06/27/210627Memoir6months/#4-%EC%BB%A4%EC%8A%A4%ED%85%80-%EC%98%88%EC%99%B8-%ED%81%B4%EB%9E%98%EC%8A%A4%EB%A1%9C-%EC%98%88%EC%99%B8%EC%B2%98%EB%A6%AC-%EA%B0%80%EB%8A%A5)

그런데 만약 필드가 많다면? 모든 필드를 NULL처리를 해줘야한다.

이때 Optional 클래스와 해당 클래스가 제공하는 orElse 메서드 또는 orElseGet 메서드를 이용하면 쉽게 NPE 처리가 가능하다.

메서드명 | 특징  
---|---  
orElseThrow(NullPointerException::new) | null이라면 함수형 파라미터로 생성한 예외(NullPointerException)를 발생시킨다.  
orElse(person) | null이면 파라미터(person)를 반환한다. 이때 파라미터(person)은 해당 값이 null이든지 말든지 항상 미리 생성된다.  
orElseGet | null이면 파라미터(person)를 반환한다. 이때 파라미터(person)은 해당 값이 null 일때만 생성된다. 즉 미리 생성되지 않는다.  
  
  
  

## 참고

  * <https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html?is-external=true>
