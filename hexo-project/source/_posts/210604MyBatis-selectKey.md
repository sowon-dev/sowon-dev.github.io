---
title: "[MyBatis] select한 값을 바로 insert할 수 있을까?"
date: 2021-06-03 15:00:00
tags:
  - "MyBatis"
categories:
  - Database
  - General
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">select한 값을 바로 insert할 수 있을까?의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    그렇다면 가장 쉽게 생각나는 방법은 dept_code를 찾는 쿼리와 insert하는 쿼리로 2가지 쿼리 만드는 방법이다.</p>
</div>

<!-- more -->

DB Mapper를 코딩하면서 일회성으로 쓸 쿼리를 계속 만들어야하는가에 대한 의문이 생겼다.  
예를 들어 아래와 같은 UserDTO가 있다고하자.  
user테이블에 idx, name, dept_code만 넣고 싶다. dept_code는 department테이블에서 user_id로 알아낼 수 있다.

그렇다면 가장 쉽게 생각나는 방법은 dept_code를 찾는 쿼리와 insert하는 쿼리로 2가지 쿼리 만드는 방법이다.  
하지만 dept_code를 찾는 쿼리는 insert하는 쿼리하기위해 한번만 사용되는 일회성 쿼리라면 굳이 쿼리를 나눠서 작성할 필요가 있을까?  
여기서 내 궁금증은 커져만 갔고 한 개의 쿼리를 만들고 싶다는 마음이 강해졌다.

  
  
  

## 공통코드

```java
@Data
  public class UserDTO{
    private int idx;
	private String name;
    @NotBlank @Size(min=13, max=14)
    private String user_id;
	private String dept_code;
  }
```

  
  
  

## 기존코드

UserDTO를 선언하고 findDeptCode 쿼리 실행하여 나온 result값을 dept_code에 넣어주고 난 뒤 insertUser쿼리를 실행하면 된다.

```xml
<!-- dept_code를 찾는 쿼리  -->
<select id="findDeptCode" parameterType="String" resultType="String">
	SELECT dept_code from department
	WHERE user_id = #{user_id}
</select> 

<!-- insert 쿼리  -->
<insert id="insertUser" parameterType="UserDTO">
	insert into user
	(idx, name, dept_code)
	values ( #{idx}, #{name}, #{dept_code} )
</insert>
```

직관적인 쿼리들이지만 나는 하나의 쿼리로 만들고 싶었다.  
한 기능에서만 딱 한 번 그리고 세트로 실행되는데 여러 개 쿼리를 나눈 것이 비효율적이라고 느껴졌기때문이다.  
findDeptCode 쿼리와 insertUser 쿼리는 세트이기때문에 유지보수를 위해서도 한 쿼리로 관리하고 싶었다.

다른 방법이 없을까 구글링하던 끝에 주임님께 조심스럽게 내 생각을 전해보았다.  
주임님은 바로 이해하시고는 selectkey를 알려주셨다.  
주임님은 겸손하면서 다정하게 잘 알려주신다.  
다 가졌어.  
겸손까지…  
그저 완벽.

  
  
  

## selectkey사용한 코드

짜잔! 한 쿼리로 다 관리할 수 있다. 이를 조금 고급스럽게 표현하면 Mybatis 동적쿼리라고 부른다.

```xml
<insert id="insertUser" parameterType="UserDTO">
	<selectKey id="findDeptCode" resultType="String" keyProperty="dept_code" order="BEFORE">
		SELECT dept_code from department
		WHERE user_id = #{user_id}
	</selectKey> 
	insert into user
	(idx, name, dept_code)
	values ( #{idx}, #{name}, #{dept_code} )
</insert>
```

  
  
  

## selectkey 사용법

  * `keyProperty` : 컬럼명이므로 DTO에 있는 동일한 명을 입력하면 된다.
  * `order="BEFORE"` : insert전에 selectKey문이 실행된다.
  * `order="AFTER"` : insert후에 selectKey문이 실행된다.

  
  
  

## 여담

주임님 덕분에 오늘 난 한 걸음 더 성장했다!  
될지 안 될지 알 수 없는 상황에서 구글링해도 안 나오니까 그냥 안 되나보다하고 포기하지않고 끝까지 물어보길 잘했다.  
아 스트레스도 많이 받지만 이럴땐 정말 재밌다 코딩  
하나하나 알게 되는 기쁨이 이루 말할수없다.  
앞으로도 이렇게 성장해나가야지!  
그나저나 주임님 정말 천재!!

  
  
  

## 참고

  * <https://yookeun.github.io/java/2014/07/11/mybatis-selectkey/>

#[MyBatis](/tags/MyBatis/)
