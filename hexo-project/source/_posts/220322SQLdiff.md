---
title: "예약가능여부 SQL쿼리로 알아보는 주니어 개발자와 시니어 개발자의 차이"
date: 2022-03-22 05:26:26
tags:
  - "MySQL"
categories:
  - Database
  - MySQL
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'예약가능여부 SQL쿼리로 알아보는 주니어 개발자와 시니어 개발자의 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    동작 원리와 장단점을 비교 파악하여 프로젝트 개발 상황에 적합한 방식을 선택할 수 있다.</p>
</div>

<!-- more -->

예약시간표를 만들고싶었다.  
예악가능한 시간대는 10시와 13시, 15시가 총 3가지이고 예약상태가 예약승인, 예약취소 총 3가지가 있다.  
예약이 한 번도 없거나, 예약취소가 된 경우 예약이 가능하며 예약승인인 경우 예약이 불가능하다.  
이때 특정 날짜를 달력에서 선택했을때 시간대별로 예약가능한지 불가능한지를 알고싶었다.

예를 들어 달력에서 3월 22일 클릭했을때 예약상태가 null이거나 예약취소이면 예약이 가능하고 예약상태가 예약승인경우에 예약이 불가능하다. 예약시간대와 예약상태는 DB 데이터로 존재하므로 쿼리를 잘 짜서 예약가능여부를 출력하고 싶었다.

선택한날짜(searchDate) | 예약시간대 | 예약상태 | 예약가능여부  
---|---|---|---  
2022-03-22 | 10시 | 예약승인 | X  
2022-03-22 | 13시 | null | O  
2022-03-22 | 15시 | 예약취소 | O  
  
  
  
  

## 내 쿼리

예약상태 값이 있든 없든 출력되어야하므로 먼저 left join을 생각했었다. 하지만 기준테이블을 뭘로 잡으면 좋을지 고민해봤지만 주니어의 머리속엔 아무것도 떠오르지 않았다.  
그래서 고민하다가 union이 떠올랐다. union에 관해서는 2번적도 포스팅을 한 적이 있었는데 언젠가 내 머리속에서 버로 떠올랐으면 했었는데 드디어 떠올랐다. 짜릿해😆  
배운 지식이 머리속에서 떠오르는 건 짜릿한 경험이다.

```java
select date
	, ifnull(예약시간대, '10:00')
	, ifnull(count(예약상태), 0)
from exampletable
where 예약시간대 = '10:00'
and date = #{searchDate}
and 예약상태 = '예약승인'

union 

select date 
	, ifnull(예약시간대, '13:00')
	, ifnull(count(예약상태), 0)
from exampletable
where 예약시간대 = '13:00'
and date = #{searchDate}
and 예약상태 = '예약승인'

union 

select date
	, ifnull(예약시간대, '15:00')
	, ifnull(count(예약상태), 0)
from exampletable
where 예약시간대 = '15:00'
and date = #{searchDate}
and 예약상태 = '예약승인'
```

ifnull을 이용하여 예약이 한 번도 되지 않은 날짜인 경우 0이 출력되도록 했다.  
해당 일자에 예약이 있었던 경우에는 ‘예약승인’상태가 몇 개인지 count했다.  
즉 count로 1이상 나오는 경우 예약이 불가능하다. 0이면 예약가능하다.

union이 머리속에 나온건 좋았지만 중복이 너무 많은 쿼리이다.  
아쉽고도 아쉬웠다.  
중복을 없앨 수 있지 않을까? 더 좋은 쿼리가 있을건데! 분명히!  
구글링을 통해 여러 방법을 따라하면서 고민해보다가 결국 팀장님께 여쭤봤다.

  
  
  

## 중복을 제거한 쿼리

팀장님이 union쿼리도 이해하기 쉽게 잘 짰다고 칭찬해주셨다.  
난 참 운도 좋아! 매일 칭찬해주시는 팀장님 그저 빛… 칭찬은 주니어를 춤추게 해🕺  
“음 중복을 없애고 싶다면 이렇게는 어때요?” 하면서 1분만에 중복이 제거된 쿼리를 짜주셨다.😯  
솔직히 1분도 안 걸린듯하다. 팀장님. 천재. 그저 빛….  
바쁘신 와중에 도와주셔서 정말 감사했다.

```sql
SELECT a.v_dt,
	   a.v_tm
	   b.cnt
FROM   (SELECT # {searchDate} v_dt,
               '10:00'         v_tm
        UNION
        SELECT # {searchDate},
               '13:00'
        UNION
        SELECT # {searchDate},
               '15:00') a
       LEFT JOIN (SELECT date,
                         예약시간대,
                         Count(*) cnt
                  FROM   exampletable
                  WHERE  예약상태 = '예약승인'
                  GROUP  BY date, 예약시간대) b
              ON a.v_dt = b.date
                 AND a.v_tm = b.예약시간대;
```

from절에 서브쿼리를 사용했는데 서브쿼리안에 `from 테이블`이 없다. 이는 무조건 출력하겠다는 의미이다.  
선택한 날짜와 예약시간대 3가지는 항상 출력되야하므로 union을 사용했다.  
특정 시간대에 아무런 예약상태가 없어 null이 나올 수 있도록 left join을 걸었고 이때 where조건인 예약승인을 넣는다.

서브쿼리가 들어가고 그 안에 join절이 나오면 어떻게 SQL formatting해야 가독성이 좋아지는지 잘모르겠다. Javascript 코드 포맷터인 Pretieer처럼 SQL도 다수가 사용하는 format형식같은 게 있었으면 좋겠다. 

#[MySQL](/tags/MySQL/)
