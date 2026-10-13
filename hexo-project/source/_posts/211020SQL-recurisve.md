---
title: "[MySQL/MariaDB] WITH RECURSIVE 초간단 설명"
date: 2021-10-19 15:00:00
tags:
  - "MariaDB"
categories:
  - Database
  - MySQL
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">WITH RECURSIVE 초간단 설명의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    MySQL에서 재귀쿼리를 사용해야한다면? with recursive문을 사용할 수 있다.</p>
</div>

<!-- more -->

MySQL에서 재귀쿼리를 사용해야한다면? with recursive문을 사용할 수 있다.  
with recursive는 UNION ALL과 함께 사용하며 UNION ALL은 관련 포스팅인 [Union all 사용법](https://sowon-dev.github.io/2021/10/18/211019SQL-unionall/)을 참조하면 된다. 

## 기본 쿼리

```xml
with recursive 테이블명 as (
	select 초기값 as 별명1
	
	union all
	
	select 별명1 반복_할_계산식 from 테이블명 where 반복을_멈출_제어문
)
select * from 테이블명
```

  
  
  

## 코드

예시코드를 보자.  
menu테이블이 있고 menu테이블은 계층형구조로 이루어져있다.  
상위 메뉴ID와 하위 메뉴ID를 동일한 menu테이블에서 가져오는 재귀쿼리로 활용할 수 있다.

```xml
with recursive cte as (
	SELECT	MENU_ID
			, UPPER_MENU_ID
			, MENU_NM
	FROM 	menu

	UNION ALL

	SELECT	m.MENU_ID
			, m.UPPER_MENU_ID
			, m.MENU_NM
	FROM	cte
	INNER JOIN 
			menu m
	ON 		cte.MENU_ID = m.UPPER_MENU_ID
)
SELECT	*
FROM	menu M
```

#[MariaDB](/tags/MariaDB/)
