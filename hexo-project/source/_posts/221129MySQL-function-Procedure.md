---
title: "[MySQL/MariaDB] 함수(function) vs 프로시저(Procedure) 차이"
date: 2022-11-28 21:03:57
tags: []
categories:
  - Database
  - MySQL
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'함수(function) vs 프로시저(Procedure) 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    이번에 진행중인 프로젝트는 프로시저보다 함수가 더 많이 사용되었다. 지난번 담당했던 프로젝트는 오직 프로시저만 썼었다. 둘의 차이가 뭘까? 언뜻 생각해봤을땐 return유무정도인데 깊이있게 알고싶어졌다.</p>
</div>

<!-- more -->

이번에 진행중인 프로젝트는 프로시저보다 함수가 더 많이 사용되었다. 지난번 담당했던 프로젝트는 오직 프로시저만 썼었다. 둘의 차이가 뭘까? 언뜻 생각해봤을땐 return유무정도인데 깊이있게 알고싶어졌다.

  
  
  

# 함수

  1. 정의: 항상 리턴값을 가짐
  2. 특징
     * 리턴값은 필수이고 오직 하나
     * try catch 사용 불가
  3. 단점
     * 클라이언트실행으로 프로시저보다 속도가 느리다.
  4. 선언 

```sql
CREATE FUNCTION function_name(
	param1,
	param2,…
)
RETURNS datatype
[NOT] DETERMINISTIC
BEGIN
 -- statements
END
```

  5. 선언예시 

```sql
create function MultiplyNumbers(@int1 as int,@int2 as int)
As
BEGIN
Return (@int1 * @int2)
end
```

  6. 호출 

```sql
MultiplyNumbers(2,2) 
// RETURN: 4
```

# 프로시저

  1. 정의: 특정 작업을 수행. 여러 SQL문을 한 번에 실행 가능
  2. 특징
     * 개발업무와 DB처리를 구분하여 개발할 수 있음
     * 보수성 뛰어남
     * 서버 실행이라 속도가 함수보다 상대적으로 빠름
     * 리턴값 없거나 여러개도 가능 -> 유연성
     * try catch 사용가능 -> 에러처리가능
  3. 단점
     * 재사용성이 좋지 않음
  4. 선언 

```sql
Create Procedure [Procedure Name] ([Parameter 1], [Parameter 2], [Parameter 3] )
Begin
-- SQL Queries..
End
```

  5. 선언 예시 

```sql
CREATE PROCEDURE GetAllProducts()
BEGIN
SELECT *  FROM products;
END
```

  6. 호출 

```sql
CALL GetAllProducts()
```

  
  
  

# 차이

| | 함수(Function) | 프로시저(Procedure)  
---|---|---  
처리주체 | 클라이언트에서 처리 | 서버로 보내서 처리  
리턴값 유무 | 필수 | 선택  
리턴값 갯수 | 하나만 반환가능 | 여러개 반환가능  
호출방법 | select문장안에서 함수호출 | call 프로시저명()  
주사용처 | 로직 처리 도와주는 용도 | 로직 처리를 직접하는 용도 why? DML문 사용가능해서  
  
  
  
  

# 참고

  * <https://www.geeksforgeeks.org/difference-between-function-and-procedure/>
  * <https://www.mysqltutorial.org/getting-started-with-mysql-stored-procedures.aspx>
  * <https://velog.io/@devjooj/Mysql-Function%EA%B3%BC-Procedure-%EC%B0%A8%EC%9D%B4>
  * <https://spiderwebcoding.tistory.com/7>
