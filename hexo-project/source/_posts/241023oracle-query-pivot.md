---
title: "[오라클]GROUP BY쿼리를 PIVOT쿼리로 바꿔보자"
date: 2024-10-22 16:10:17
tags:
  - "TIL"
  - "Oracle"
categories:
  - Database
  - Oracle
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">동적 또는 유동적인 코드로 인해 GROUP BY로 해결하기 어려운 다중 컬럼 집계 문제를 오라클 PIVOT 함수로 해결하는 방법이다.
    ROW_NUMBER 또는 RANK 윈도우 함수로 순번을 부여한 뒤 PIVOT을 적용하여 행 데이터를 유연하게 열로 전환할 수 있다.</p>
</div>

<!-- more -->

GORUP BY로 해결하려고 노력했지만 잘 되지않아서 PIVOT 쿼리를 처음 사용하게 되었다.

# PIVOT VS GROUP BY

| | GROUP BY | PIVOT  
---|---|---  
목적 | 특정 열을 기준으로 그룹화하여 각 그룹에 대해 집계(합계, 평균, 최대값 등)된 결과를 계산 | 데이터를 열로 변환하여 요약된 데이터를 테이블 형태로 표현  
결과 | 각 그룹별로 집계된 값이 행 단위로 출력 | 행 데이터를 열로 변환하여 각 카테고리(예: 부서, 제품 종류 등)에 대한 요약 정보를 한눈에 출력  
사용 용도 | 열로 변환하는 것이 아니라, 그룹별로 집계한 데이터를 행으로 출력할때 사용 | 특정 컬럼 값을 기준으로 데이터를 회전(pivot) 시켜 집계한 값을 여러 열로 표현할때 사용  
  
  
  
  

# 내 코드: GROUP BY 사용

요구사항은 학생별로 과목코드100,200,300의 점수와 세 과목의 점수합계를 보고싶었다.  
그래서 먼저 그룹핑을 떠올렸다.

```sql
SELECT 
	A.YR     
	, A.USERNO   
	, A.USERNM                                     
	, SUBSTR(A.IDENTITY_NO, 1, 6) AS BRDT	/*생년월일*/     
	, NVL(MAX(CASE WHEN C.TEST_CD = '100' THEN C.SCR END),0) AS SCORE1 /* TEST_CD가 100인 점수 */
	, NVL(MAX(CASE WHEN C.TEST_CD = '200' THEN C.SCR END),0) AS SCORE2 /* TEST_CD가 200인 점수 */
	, NVL(MAX(CASE WHEN C.TEST_CD = '300' THEN C.SCR END),0) AS SCORE3 /* TEST_CD가 300인 점수 */
	, D.TOTAL_SCR 	/*산출점수*/
FROM EE_USER_INFO A  
JOIN EE_TEST_SCORE C    
ON A.YR = C.YR   
AND A.USERNO = C.USERNO
JOIN EE_TEST_RESLUT D
ON A.YR = D.YR
AND A.USERNO = D.USERNO
GROUP BY A.YR, A.USERNO, A.USERNM, SUBSTR(A.IDENTITY_NO), 1, 6), D.TOTAL_SCR
```

여기서 문제는 TEST_CD가 100,200,300으로 고정되지 않았다는 것이다.  
TEST_CD가 공통코드로 이루어져있어서 연도에 따라 특정연도에는 400,500,600을 쓸 수도 있었다.  
연도별 과목코드 3개만 추출하면 되는데… 난감한 상황!  
이럴때는 어떻게 해야할까? 

팀장님은 PIVOT을 사용해보라고 조언해주셨다.

  
  
  

# 잠깐) GROUP BY 절에 집계함수를 안 넣어도 되는지?

`GROUP BY` 절에는 집계 함수에 포함되지 않은 모든 필드 또는 표현식을 포함해야한다.  
CASE WHEN과 MAX 함수는 그룹화된 데이터에 대해 집계를 수행하는 부분이므로 `GROUP BY` 절에 포함되지 않아도 된다.  
집계되지 않는 필드들은 각 그룹에 대해 고유한 값을 가져야 하므로, 그룹핑 조건으로 추가되어야 한다. 

  
  
  

# 팀장님 코드 : PIVOT 사용

팀장님 수정해주신 쿼리는 아래와 같다.

```sql
SELECT 
    A.YR,
    A.USERNO,
    A.USERNM,
    SUBSTR(A.IDENTITY_NO, 1, 6) AS BRDT,    /* 생년월일 */
    A.SCR1,          
    A.SCR2,          
    A.SCR3,          
    D.TOTAL_SCR  /*산출점수*/
FROM (
    SELECT 
        A.YR,
        A.USERNO,
        TO_CHAR(RANK_1) AS SCR1,
        TO_CHAR(RANK_2) AS SCR2, 
        TO_CHAR(RANK_3) AS SCR3
	FROM (
		SELECT 
            A.YR
            , A.USERNO           
            , A.SCR            
            , 'RANK' || RANK() OVER (PARTITION BY A.YR, A.USERNO ORDER BY A.TEST_CD) AS RANK_CD
        FROM 
            EE_TEST_SCORE A
        WHERE 
            A.YR = #{YR}
        ORDER BY 
            A.USERNO
	)
	 PIVOT (
    	SUM(SCR) 
    	FOR RANK_CD IN (
            'RANK1' AS RANK_1,
            'RANK2' AS RANK_2,
            'RANK3' AS RANK_3
        )
	)
) A
JOIN EE_TEST_RESLUT D
ON A.YR = D.YR
AND A.USERNO = D.USERNO
```

PIVOT을 사용하여 각 과목 점수를 가로로 변환하고, 최종적으로 합계 점수는 다른 테이블(EE_TEST_RESLUT)에서 가져와 출력했다.

쿼리결과 예시는 아래와 같다.

```plain
YR	USERNO	USERNM	BRDT	SCORE1	SCORE2	SCORE3	TOTAL_SCR1
2024	101	John	900101	90	85	70	245
2024	102	Alice	920202	95	80	60	235
2024	103	Bob	880303	88	78	65	231
```

두 쿼리는 동일한 데이터를 출력하지만,  
PIVOT 쿼리는 데이터 피봇팅을 사용해 TEST_CD 값에 따라 자동으로 점수를 열로 변환하므로 코드가 훨씬 간결하고 명확하다.

아는 것만 보인다고…  
PIVOT과도 친해지자.

  
  
  

# 출처

  * 팀장님 지식

#[TIL](/tags/TIL/)[Oracle](/tags/Oracle/)
