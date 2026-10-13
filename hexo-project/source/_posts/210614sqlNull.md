---
title: "[MySQL] SQL에서 컬럼값이 NULL처리는 어떻게 하면 좋을까?"
date: 2021-06-13 20:47:04
tags:
  - "MySQL"
categories:
  - Database
  - General
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">SQL에서 컬럼값이 NULL처리는 어떻게 하면 좋을까?의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    핵심 설정과 구현 코드를 단계별로 파악하여 상황에 맞게 유연하게 활용할 수 있다.</p>
</div>

<!-- more -->

SQL에서 컬럼값이 NULL이 출력되었을 경우 default값이나 원하는 값으로 치환해주고싶을때가 있다.  
이럴때 어떻게 하면 좋을까?

  * 컬럼값이 Null인 경우를 처리해주는 함수들
    1. MySQL: IFNULL, CASE
    2. Orcale: NVL()
    3. 모든 DBMS : COALESCE

  
  
  

### ISNULL()

  * 기본

```sql
// 기본
SELECT IFNULL(컬럼명, "Null일 경우 대체 값") FROM 테이블명;
```

  * 예시: 학부모연락처가 NULL인 경우 “학부모없음”을 출력, NULL이 아닌 경우 학부모tel을 출력

```sql
SELECT IFNULL(학부모tel, "학부모연락처없음")
FROM user
```

  
  
  

### CASE문

  * 기본

```sql
// 기본
CASE 
    WHEN 조건식1 THEN 식1
    WHEN 조건식2 THEN 식2
    ...
    ELSE 조건에 맞는경우가 없는 경우 실행할 식
END
```

  * 예시

```sql
SELECT 
 CASE
   WHEN 학부모tel IS NULL THEN "학부모연락처없음"
   ELSE 학부모tel
 END
FROM user
```

  
  
  

## COALESCE()

  * 기본  
컬럼1이 null인경우 컬럼2를 출력하고 컬럼2도 null인 경우 컬럼3을 출력한다.  
컬럼3도 null이면 컬럼4를 출력하고, 마지막 컬럼까지 null인 경우 그냥 null을 출력한다.

```sql
SELECT COALESCE(컬럼1, 컬럼2, 컬럼3, 컬럼4, ...)
FROM 테이블명
```

  * 예시

```sql
SELECT COALESCE(학부모tel, 학부모tel2, "비상연락처도없음")
FROM user
```

#[MySQL](/tags/MySQL/)
