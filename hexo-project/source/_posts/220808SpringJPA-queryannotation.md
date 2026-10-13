---
title: "[JPA] 쿼리 어노테이션(Query Annotation) 에러(expression or DISTINCT expected, got)해결"
date: 2022-08-08 00:57:57
tags: []
categories:
  - Backend
  - JPA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">친구가 인텔리제이로 공부하던 중에 JPA 쿼리어노테이션 에러가 떠서 나한테 물어봤는데 나도 정확히 잘 몰라서 이참에 함께 공부해봤다.
    오류가 해결되었다!을 통해 문제를 해결할 수 있다.</p>
</div>

<!-- more -->

인텔리제이를 사용하면 Spring 프레임워크를 사용하는데 많은 도움을 받을 수 있다.  
친구가 인텔리제이로 공부하던 중에 JPA 쿼리어노테이션 에러가 떠서 나한테 물어봤는데 나도 정확히 잘 몰라서 이참에 함께 공부해봤다.

## 에러

친구는 Todo테이블에서 userId에 일치되는 행을 가져오는 쿼리를 짜고 싶었다고 한다.

![](/img/220808jpaqueryannotation.png)

```java
@Query("SELECT * FROM Todo WHERE t.userId = ?1")
```

위 쿼리에서 오류가 있어 인텔리제이가 인텔리저이의 아래 error 메시지를 보여줬다.

```plain
<expression> or DISTINCT expected, got '*'
```

에러를 해석해보면, `표현식 또는 구별자가 있어야한다`라고 한다.  
어떤 오류일까?

  
  
  

## 오류 해결

where절에서 t.userId를 불러오는데 쿼리상에 t가 정의되지 않았다.  
즉 Todo 테이블의 별칭을 t로 정의해줘야한다.

```java
@Query("SELECT * FROM Todo t WHERE t.userId = ?1")
```

오류가 해결되었다!  
사실 아주 간단한 문제였다.  
하지만 JPA Query Annotation을 잘 알지못하니 5초만에 턱 해결할 수가 없었다.  
JPA Query Annotation은 뭘까?  
간단하게라도 공부해봤다.

  
  
  

## JPA Query Annotation 간단 설명

```java
@Query("SELECT * FROM Todo t WHERE t.userId = ?1")
```

여기서 물음표의 의미는 파라미터갯수이다.  
물음표 뒤의 숫자 1의 의미는 무엇일까?  
물음표에 들어올 파라미터의 위치이다. 즉 첫번째 파라미터는 `?1`여기에 위치하게된다.  
만약 파라미터가 두개라면?

```java
@Query("SELECT * FROM Todo t WHERE t.userId = ?1 AND t.userName = ?2")
```

간단하다!  
더 깊은 설명은 아래 글을 참고하면 된다.

  * [Spring Data JPA Custom Queries using @Query Annotation](https://attacomsian.com/blog/spring-data-jpa-query-annotation)
