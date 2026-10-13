---
title: "Oracle SQL"
date: 2020-12-28 15:26:15
tags:
  - "TIL"
  - "Oracle"
categories:
  - Database
  - Oracle
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Oracle SQL의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    쿼리 마지막라인에 --주석문을 사용하면 그 뒤의 내부적으로 추가되는 sql구문에 주석이 인식되어질 수 있어 에러가 발생할 수 있다.</p>
</div>

<!-- more -->

## 주석

두 가지 방법이 있다.  
쿼리 마지막라인에 `--주석문`을 사용하면 그 뒤의 내부적으로 추가되는 sql구문에 주석이 인식되어질 수 있어 에러가 발생할 수 있다.  
따라서 `--주석문`보다 `/* 주석문 */`을 사용하는 습관을 들이는 것이 좋다.

  * `--주석문` : 한 줄 주석처리

```plain
insert into test(
	ppl_name, -- 사원이름
	ppl_dept -- 사원부서
) values (
	#{name},
	#{dept}
)
```

  * `/* 주석문 */` : 범위를 주석처리

```plain
select member from dual
union all /* member테이블과 dept테이블을 합침*/
select dept from dual
```

  
  
  

## ||(쌍 파이프)

문자열이나 컬럼을 합쳐주는 역할을 한다.

```plain
// 예시
select rpad('010-', 8, '*'),  lpad('1234', 5, '-') from dual;

// 출력값
rpad : 010-****
lpad : -1234

// 콤마대신 ||(쌍파이프 사용)
select rpad('010-', 8, '*') || '(개인정보보호)' || lpad('1234', 5, '-') from dual;
010-****(개인정보보호)-1234
```

  
  
  

## UNION

![UNION과 INNER JOIN차이](https://cdn.sqlservertutorial.net/wp-content/uploads/SQL-Server-UNION-vs-JOIN.png)

위의 사진에서 왼쪽테이블을 table1, 오른쪽테이블은 table2라고 해보자.

```plain
//union
select * from table1
union
select * from table2

//출력값
id컬럼안에 1,2,3,4

//union all
select * from table1
union all
select * from table2

//출력값
id컬럼안에 1,2,3,2,3,4
```

  
  
  

## CASE WHEN THEN ELSE END

JAVA에서 IF ELSE구문같은 역할을 한다.

  * 규칙
    1. CASE문은 반드시 END로 끝나야한다.
    2. ELSE 뒷 부분에 NULL이 와선 안된다.

```plain
case when x = y then a else b end
: 조건 x = y 가 true 일 경우 a 이고 그렇지 않으면 b

case when x < y then a when x = y then b else c end
: 조건 x<y가 true 일 경우 a 로, 조건 x = y 일 경우엔 b 로 그렇지 않으면 c 로 변경

case XYZ when 'foo' then 'moo' else 'bar' end
:  XYZ 가 foo일 경우  moo로 변경,  그렇지 않으면  bar로 변경

출처: https://joke00.tistory.com/103 [Smile virus]
```

  
  
  

## 참고

  * <https://mazekb.tistory.com/424>
  * <https://sesok808.tistory.com/510>
  * <https://www.sqlservertutorial.net/sql-server-basics/sql-server-union/>
  * <https://joke00.tistory.com/103>

#[TIL](/tags/TIL/)[Oracle](/tags/Oracle/)
