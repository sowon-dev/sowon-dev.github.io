---
title: "[SQL]변수 @사용법, 사용자 정의 변수 직접 사용해보기"
date: 2022-08-11 15:13:20
tags:
  - "MySQL"
categories:
  - Database
  - MySQL
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">변수 @사용법, 사용자 정의 변수 직접 사용해보기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    SQL에서도 변수를 사용할 수 있다! 알고는 있었지만 잘 사용한 적이 없는데 이번에 select로 가져온 값을 서브쿼리에서 사용하고 싶어서 찾아보다가 변수를 사용하게 되었다.</p>
</div>

<!-- more -->

SQL에서도 변수를 사용할 수 있다! 알고는 있었지만 잘 사용한 적이 없는데 이번에 select로 가져온 값을 서브쿼리에서 사용하고 싶어서 찾아보다가 변수를 사용하게 되었다.  
이밖에도 row갯수를 셀때에도 단독으로 많이 사용한다.

## 사용자 정의 변수

변수란? 특정 값을 담아두는 곳이다.  
사용자 정의변수란? 명칭 그대로 사용자가 임의로 사용하려고 만든 변수이다.

  
  
  

### 1\. 선언 및 초기화

사용자 정의 변수를 선언 및 초기화하는 방법은 간단하다.

```sql
SET @변수명 = 대입값;
SET @변수명 := 대입값;
SELECT @변수명 := 대입값;
```

SET 명령문에서는 `=`과 `:=`를 둘 다 사용할 수 있지만 SET 이외의 명령문에서는 `=`가 비교연산자이기때문에 변수를 선언할땐 `:=`만 쓸 수 있다.  
기본값은 NULL이다.

  
  
  

### 2\. 사용

변수를 사용하는 방법은 더 간단하다.  
원하는 곳에 

```sql
SET @변수명 = 대입값;
SET @변수명 := 대입값;
SELECT @변수명 := 대입값;
```

  
  
  

## 예시코드

내가 하고 싶었던 것: select에서 가져온 TPOT.WEEK_CODE의 값을 별칭 roundRowNo를 가져올 서브쿼리에 사용하기.  
그래서 아래와 같은 코드를 짰다.

```xml
<select id="getDetail" parameterType="int" resultType="Movie">
	/* query id: getDetail */
	SELECT
		DATE_FORMAT(TPR.RESERVE_DT, '%Y-%m-%d') as reserveDt
		, @weekcode := TPOT.WEEK_CODE 
		, (SELECT roundRowNo 
			FROM (
					SELECT 
						OPEN_TIME_ID
						, (@row_number := @row_number + 1) AS roundRowNo 
					FROM tb_open_time
					JOIN (SELECT @row_number := 0) r
					WHERE IS_USE = 1 
					AND   WEEK_CODE = @weekcode
				) totalRowCnt
		  WHERE totalRowCnt.OPEN_TIME_ID = TPR.OPEN_TIME_ID
		  ) AS roundRowNo
		, -- 중략
	FROM TB_RESERVE TPR 
	JOIN TB_USER TU 
	ON	 TPR.RESERVE_USER_NO = TU.USER_NO
	JOIN TB_OPEN_TIME TPOT 
	ON 	 TPR.OPEN_TIME_ID = TPOT.OPEN_TIME_ID 
	WHERE TPR.RESERVE_ID = #{reserveId}
</select>
```

  
  
  

### 1\. `@weekcode := TPOT.WEEK_CODE`의 의미

SELECT문에서 `weekcode`라는 변수를 선언 한 뒤(= `@weekcode`) TPOT.WEEK_CODE 값으로 초기화 했다.  
이때 SET 명령문이 아닌 SELECT문이기에 `:=`를 사용했다.

  
  
  

### 2\. row_number

실무에서 사용자 정의 변수를 가장 많이 사용할 때는 바로 row 개수를 구할때이다.

  1. `@row_number := 0` : 변수 `@row_number`를 0으로 선언 및 초기화를 한다.
  2. `@row_number := @row_number + 1` : 출력되는 행의 갯수만큼 +1 더해주면 되므로 누적합을 한다.
  3. 이를 행마다 출력해주면 row 개수를 구하는 쿼리 끝!

#[MySQL](/tags/MySQL/)
