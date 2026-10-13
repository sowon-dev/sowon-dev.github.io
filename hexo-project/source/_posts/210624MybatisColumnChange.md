---
title: "[MyBatis] update할때 컬럼명 바꿀 수 없을까?"
date: 2021-06-23 19:14:50
tags:
  - "MyBatis"
categories:
  - Database
  - General
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">update할때 컬럼명 바꿀 수 없을까?의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    그래서 단순하게 아래 쿼리를 작성한 뒤 String값 2개 name과 수정할이름을 넘겨주었다.</p>
</div>

<!-- more -->

## 😫 너무 비효율적이야!

동일한 테이블에서 컬럼명에 따라 값이 달라지는 update 구문을 만들고 싶었다.  
물론 컬럼명마다 update구문을 만들 수 있지만 동일테이블인데 그건 너무 비효율적이다.  
그래서 단순하게 아래 쿼리를 작성한 뒤 String값 2개 name과 `수정할이름`을 넘겨주었다.

```xml
<update id="updateUserOneByOne" parameterType="String">
	update user
	set #{column_name} = #{value}
</update>
```

그 결과는 아래처럼 오류가 발생했다. name을 컬럼이 아닌 String으로 받아들여졌기때문에 생긴 오류였다.

```xml
java.sql.SQLSyntaxErrorException: (conn=9442) You have an error in your SQL syntax; 
check the manual that corresponds to your MariaDB server version for the right syntax to use near ''name' = '수정할이름'
```

이를 어떻게 해결할 수 있을까?

  
  
  

## 😎Mybatis 컬럼명 동적쿼리

이를 조금 고급스럽게 표현하면 Mybatis 동적쿼리라고 부른다.  
`#`에서 `$`로 바꿔줬을뿐인데 정상작동한다! 

```
<update id="updateUserOneByOne" parameterType="String">
	update user
	set ${column_name} = #{value}
</update>
```

## 정리

  1. `${}`: 파라미터값 그대로 입력
  2. `#{}`: 파라미터값이 ‘ ‘으로 감싸져서 문자열로 입력

#[MyBatis](/tags/MyBatis/)
