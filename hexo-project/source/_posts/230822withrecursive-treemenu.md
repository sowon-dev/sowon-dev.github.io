---
title: "[MySQL/MariaDB] 트리메뉴 WITH RECURSIVE로 정렬하기"
date: 2023-08-21 22:31:43
tags:
  - "MariaDB"
categories:
  - Database
  - MySQL
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">트리메뉴 WITH RECURSIVE로 정렬하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    핵심 설정과 구현 코드를 단계별로 파악하여 상황에 맞게 유연하게 활용할 수 있다.</p>
</div>

<!-- more -->

트리구조의 메뉴를 select하는 과정에서 1뎁스가 10개가 넘어가니 문제가 발생했다.

# 문제

  * 기존코드

```sql
SELECT SITEMENUID, PARENTID, SEQ, FULLSEQ
FROM (
	 SELECT '1' AS DEPTH
	 , '00_00_00' AS FULLSEQ
	 , A1.PARENTID
	 , A1.SITEMENUID
	 , A1.SEQ
	FROM tb_site_menu A1
	UNION ALL   
	SELECT '2' AS DEPTH
	 , CONCAT(A2.SEQ,'_',A1.SEQ) AS FULLSEQ
	 , A2.PARENTID
	 , A2.SITEMENUID
	 , A2.SEQ
	FROM tb_site_menu A1
	INNER JOIN tb_site_menu A2
	ON A1.SITEMENUID = A2.PARENTID
    UNION ALL 
	SELECT '3' AS DEPTH
	, CONCAT(A2.SEQ,'_',A1.SEQ,'_',A3.SEQ) AS FULLSEQ
	, A3.PARENTID
	, A3.SITEMENUID
	, A3.SEQ
	FROM tb_site_menu A1
	INNER JOIN tb_site_menu A2
	ON A1.SITEMENUID = A2.PARENTID
	INNER JOIN tb_site_menu A3
	ON A2.SITEMENUID = A3.PARENTID
	)  TBL
ORDER BY FULLSEQ;
```

1번 다음에 2번이 와야하는데 VARCHAR라서 1다음에 10이 와버렸다.

  * 콘솔

```plain
<1뎁스-2뎁스-3뎁스>
00_00_00
1_01
1_02_01
1_02_02
1_03
10_01
10_02
2_01_01
2_01_02
2_02
```

  
  
  

# LPAD로 해결

팀장님이 자리수를 맞추면 해결되는 문제라고 알려주셨다.

  * LPAD추가된 코드

```sql
SELECT SITEMENUID, PARENTID, SEQ, FULLSEQ
FROM (
	 SELECT '1' AS DEPTH
	 , '00_00_00' AS FULLSEQ
	 , A1.PARENTID
	 , A1.SITEMENUID
	 , A1.SEQ
	FROM tb_site_menu A1
	UNION ALL   
	SELECT '2' AS DEPTH
	 -- , CONCAT(A2.SEQ,'_',A1.SEQ) AS FULLSEQ
	 , CONCAT(LPAD(A2.SEQ, 2 , '0'),'_',LPAD(A1.SEQ, 2 , '0')) AS FULLSEQ
	 , A2.PARENTID
	 , A2.SITEMENUID
	 , A2.SEQ
	FROM tb_site_menu A1
	INNER JOIN tb_site_menu A2
	ON A1.SITEMENUID = A2.PARENTID
    UNION ALL 
	SELECT '3' AS DEPTH
	-- , CONCAT(A2.SEQ,'_',A1.SEQ,'_',A3.SEQ) AS FULLSEQ
	, CONCAT(LPAD(A2.SEQ, 2 , '0'),'_',LPAD(A1.SEQ, 2 , '0'),'_',LPAD(A3.SEQ, 2 , '0')) AS FULLSEQ
	, A3.PARENTID
	, A3.SITEMENUID
	, A3.SEQ
	FROM tb_site_menu A1
	INNER JOIN tb_site_menu A2
	ON A1.SITEMENUID = A2.PARENTID
	INNER JOIN tb_site_menu A3
	ON A2.SITEMENUID = A3.PARENTID
	)  TBL
ORDER BY FULLSEQ;
```

  * 콘솔

```plain
<1뎁스-2뎁스-3뎁스>
00_00_00
01_01
01_02_01
01_02_02
01_03
02_01_01
02_01_02
02_02
10_01
10_02
```

원하는대로 잘 출력!!!

  
  
  

# 더나은 방법: with recursive

팀장님께서 LPAD 대신 with recursive를 써서 쿼리를 더 간단하게 만들수있다고 알려주셨다.

```sql
with recursive menuTree as (
	SELECT 1 AS DEPTH
	, cast('00' as VARCHAR(256)) AS FULLSEQ
	, A1.PARENTID
	, A1.SITEMENUID
	, A1.SEQ
	FROM tb_site_menu A1
	UNION ALL
	SELECT parent.DEPTH + 1 AS DEPTH
	, CONCAT(parent.SEQ, '-', LPAD(child.SEQ, 2, '0')) AS FULLSEQ
	, child.PARENTID
	, child.SITEMENUID
	, child.SEQ
	FROM menuTree parent
	JOIN tb_site_menu child
	ON parent.SITEMENUID = child.PARENTID
)
SELECT * FROM menuTree ORDER BY FULLSEQ;
```

와 역시 팀장님 최고다…

  
  
  

# 참고

  * 팀장님 지식
  * [WITH RECURSIVE 초간단 설명](https://sowon-dev.github.io/2021/10/19/211020SQL-recurisve/)

#[MariaDB](/tags/MariaDB/)
