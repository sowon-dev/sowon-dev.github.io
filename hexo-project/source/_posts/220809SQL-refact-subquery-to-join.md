---
title: "[MySQL] 서브쿼리(Subquery)보다 조인(Join)을 써야하는 이유(코드비교)"
date: 2022-08-09 04:09:53
tags: []
categories:
  - Database
  - MySQL
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'서브쿼리(Subquery)보다 조인(Join)을 써야하는 이유(코드비교)'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    MySQL버전마다 성능이 다르지만 MySQL5.5에서 MySQL5.6으로 버전업되면서 서브쿼리 성능이 개선되었다고 한다.</p>
</div>

<!-- more -->

회차별로 예약할 수 있는 영화 프로그램을 만들어야 한다고 생각해보자.  
여기서 회차는 요일별로 동일하다. 즉, 이번주 월요일에 총 3회차 영화상영이, 화요일에는 2회차 영화상영이 있었다면 다음주 월요일도 총 3회차, 화요일에는 2회차 영화상영이 예정되어 있는 것이다.  
사용자가 선택한 날짜의 회차별로 이미 예약된 내역정보뿐만 아니라 예약 가능한 좌석수를 가져오는 쿼리를 만들어야한다.

쿼리를 이해하기 위한 정보는 아래와 같다.

구분 | 명칭 | 설명  
---|---|---  
테이블 | TB_TIME | 회차 테이블  
테이블 | TB_RESERVE | 예약 내역테이블  
파라미터 | dt | 조회 날짜  
파라미터 | id | 회차 ID  
컬럼 | ALL_SEAT | 해당 회차의 전체 좌석수  
컬럼 | RESERVE_DT | 상영일  
별칭 | openSeat | 예약가능한 좌석수  
  
## 내쿼리

select구문에 subquery를 넣어서 해당 날짜에서 선택된 회차의 잔여 예약좌석수를 구했다.

```sql
SELECT
	TPOT.ID
	, -- 여러 정보 컬럼 (중략) 
	, IFNULL(TPOT.ALL_SEAT,0) - IFNULL((SELECT sum(IFNULL(TPR.RESERVED_SEAT, 0)) FROM TB_RESERVE TPR WHERE TPR.ID = #{id} AND TPR.RESERVE_DT = DATE(#{dt}) GROUP BY TPR.ID),0) as openSeat
FROM TB_TIME TPOT 
WHERE TPOT.ID = #{id}
```

팀장님이 이 쿼리를 보시곤 join을 써보는게 어떻냐며 알려주셨다.

  
  
  

## subquery를 제거한 쿼리

```sql
SELECT
	TPOT.ID
	, -- 여러 정보 컬럼 (중략) 
	, IFNULL(TPOT.ALL_SEAT, 0) - IFNULL(a.totalReservedSeat, 0) as openSeat
FROM TB_TIME TPOT 
LEFT JOIN (
		SELECT 
			RESERVE_DT	
		,	DATE_FORMAT(RESERVE_DT, '%a') as WEEK_CODE
		,	TIME_ID 
		,	SUM(RESERVED_SEAT) totalReservedSeat 
		FROM  TB_RESERVE
		WHERE DATE(RESERVE_DT) = DATE(#{dt})
		GROUP BY 
			RESERVE_DT
		,	DATE_FORMAT(RESERVE_DT, '%a')
		,	TIME_ID
	) a
	ON TPOT.WEEK_CODE = a.WEEK_CODE
	AND TPOT.TIME_ID = a.TIME_ID
WHERE TPOT.ID = #{id}
AND   DATE_FORMAT(#{dt}, '%a') = TPOT.WEEK_CODE
```

팀장님이 도와주셔서 다시 작성한 쿼리이다.이 쿼리를 보면 요일 구분이 확실히 들어가있어 요구사항이 제대로 반영되어있다는 걸 알 수 있다.  
자칫 길어보이는 쿼리인데 왜 subquery보다 join을 쓰면 좋을까?

  
  
  

## subquery보다 join을 써야하는 이유

MySQL버전마다 성능이 다르지만 MySQL5.5에서 MySQL5.6으로 버전업되면서 서브쿼리 성능이 개선되었다고 한다.  
MySQL5.5에서는 서브퀴리 최적화에 많은 문제가 있어왔다. 의도한대로 서브쿼리가 제대로 실행되지 않거나 속도가 느리다.  
[jojoldu님이 블로그 글 MySQL where in (서브쿼리) vs 조인 조회 성능 비교 (5.5 vs 5.6)](https://jojoldu.tistory.com/520)을 참고하면 얼마나 속도차이가 나는지까지 확인 할 수 있다.  
버전과 조건 관계없이 좋은 성능을 내려면 최대한 join을 이용하는 것이 좋다.  
만약 서브 쿼리를 사용해 필터링을 하면 이는 크게 성능이 저하된다. 이럴땐 LEFT [OUTER] JOIN을 써서 옵티마이저(Optimizer)가 최적화 하기 쉽도록 하여 성능을 개선할 수 있다.

오늘도 또 하나 배웠다! 뿌듯~
