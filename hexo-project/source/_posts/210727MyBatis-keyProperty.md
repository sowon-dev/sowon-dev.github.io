---
title: "[MyBatis] insert할때 자동으로 키 생성하기(useGeneratedKeys과 selectKey방식 차이점)"
date: 2021-07-26 15:00:00
tags:
  - "MyBatis"
categories:
  - Database
  - General
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'insert할때 자동으로 키 생성하기(useGeneratedKeys과 selectKey방식 차이점)'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    결과가 같은데 왜 방식이 두개일까? 사용방향에 따라 차이점이 존재하기때문이다.</p>
</div>

<!-- more -->

## 😎 insert할때 자동으로 번호를 올리고 싶어

방금 insert한 autoincrement가 걸린 PK값을 바로 사용하고싶다면 어떻게 해야할까?  
두가지방식이 있다. 

  1. useGeneratedKeys와 keyProperty 사용하기
  2. selectKey 사용하기  
이름을 어떻게 부르는 지 몰라서 그냥 내가 지어보았다.

  
  
  

## 방법1: useGeneratedKeys와 keyProperty

항상 useGeneratedKeys와 keyProperty는 함께 사용하면 된다.

  * useGeneratedKeys : insert나 update됨가 동시에 자동생성된 키를 가져올 수 있는 속성으로 true로 설정 (default: false)
  * keyProperty : 리턴 될 key property 설정. 즉 values나 set 다음에 오는 컬럼명과 동일하게 설정하면 됨. 여러개를 사용한다면 ,(콤마)를 구분자로 설정

```java
public exampleVO {
  int userCode;
  String name;
  String email;
}
```

```xml
<insert id="insertExample" useGeneratedKeys="true" keyProperty="userCode" parameterType="exampleVO"> 
	INSERT INTO example 
		   (name, email ) 
	VALUES 
		   (#{name}, #{email} ) 
</insert>
```

userCode가 자동 증감되어 DB에 등록된다.  
따로 set해주지 않더라도 exampleVO.getUserCode()를 하면 autoIncrement된 값을 get할 수 있다!  
세상 간편하다!  
insert 나 update return받을 때 주로 사용할 수 있다.

  
  
  

## 방법2: selectKey

마이바티스는 자동생성키 칼럼을 지원하지 않는 다른 데이터베이스를 위해 다른 방법 또한 제공한다.  
바로 selectKey를 이용하는 것이다.  
아래 예제에서 selectKey구문이 먼저 실행되고 userCode 최대값에서 1씩 증가되게끔 셋팅된다. 그리고 나서 insert 구문이 실행된다. 이건 복잡한 자바코드 없이도 데이터베이스에 자동생성키의 행위와 비슷한 효과를 가지도록 해준다.

```xml
<insert id="insertExample">
  <selectKey keyProperty="userCode" resultType="int" order="BEFORE">
    SELECT IFNULL(MAX(userCode+1),1) FROM example
  </selectKey>
  INSERT INTO example
  		 (userCode, email)
  VALUES
    	 (#{userCode}, #{email})
</insert>
```

selectKey에 대한 추가설명은 아래 포스팅을 참고하면 된다.

  * [select한 값을 바로 insert할 수 있을까?](https://sowon-dev.github.io/2021/06/03/210604MyBatis-selectKey/)

  
  
  

## 방법1과 방법2의 차이

위의 두 예시는 최근 userCode에서 `+1`을 해주는 결과를 나타낸다.  
결과가 같은데 왜 방식이 두개일까? 사용방향에 따라 차이점이 존재하기때문이다.

방법 1은 DBMS의 도움이 필요하다. 즉 auto increment가 되는 DBMS만 사용가능하다.  
만약 사용하는 DBMS는 AUTO INCREMENT를 지원해주지 않는다면 방법 2를 써야한다.

auto increment를 지원해주는 DBMS라 하더라도 단순히 `+1` 증감이 아닌 뭔가 커스텀하게 증가시키고싶다면 2번을 사용해야한다.  
커스텀하게 증가시키는 게 무엇일까?  
아래 예시처럼 항상 5자리로 userCode를 등록할 수 있다.

```xml
<insert id="insertExample">
	<selectKey resultType="int" keyProperty="userCode" order="BEFORE">
		SELECT lpad(cast((IFNULL(MAX(userCode), 0) + 1) as char),5,'0') 
		  FROM example
    </selectKey> 
  INSERT INTO example
  		 (userCode, email)
  VALUES
    	 (#{userCode}, #{email})
</insert>
```

만약 현재 userCode의 최대값이 12라면 다음 userCode는 selectKey 실행에 의해 `00013`으로 DB에 등록된다.

  
  

### 요약

  * 방법1: DBMS가 auto increment를 지원하고 특정 컬럼에 `+1`하는 로직인 경우 사용
  * 방법2: 
    * DBMS가 auto increment를 지원하지 않는 경우 사용
    * DBMS가 auto increment를 지원하지만 특정 규칙으로 컬럼값을 증가시키는 로직인 경우 사용

  
  
  

## 참고

  * <https://mybatis.org/mybatis-3/sqlmap-xml.html>

#[MyBatis](/tags/MyBatis/)
