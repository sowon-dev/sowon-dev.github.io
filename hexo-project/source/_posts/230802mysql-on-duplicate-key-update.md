---
title: "[MySQL/MariaDB] ON DUPLICATE KEY UPDATE"
date: 2023-08-01 20:41:32
tags:
  - "MariaDB"
categories:
  - Database
  - MySQL
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">ON DUPLICATE KEY UPDATE의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    SQL 쿼리 작성시 PK키가 중복되는 경우 지정한 데이터만 INSERT가 아닌 UPDATE 시킬 수는 없을까?을 적용할 수 있다.</p>
</div>

<!-- more -->

SQL 쿼리 작성시 PK키가 중복되는 경우 지정한 데이터만 INSERT가 아닌 UPDATE 시킬 수는 없을까?  
ON DUPLICATE KEY UPDATE를 사용하면 된다.

# ON DUPLICATE KEY UPDATE

INSERT시 PK나 UNIQUE KEY가 중복인 경우 원하는 컬럼만 UPDATE하고 중복되지 않은 경우에는 INSERT된다.

  
  
  

# 예시코드

```sql
-- 테이블생성
 CREATE TABLE tb_user (
 	user_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY
    , name VARCHAR(20) NOT NULL
    , mobile VARCHAR(20) NOT NULL
    , address VARCHAR(50) DEFAULT NULL
    , reg_dt DATE()
	, update_dt DATE()
  ) ENGINE=INNODB DEFAULT CHARSET=utf8 

-- 제약조건
 ALTER TABLE tb_user ADD UNIQUE (name, mobile);
```

테이블 tb_user에서 pk는 user_id이고 AUTO_INCREMENT이고 mobile이 UNIQUE KEY인 경우를 예시로 해보자.  
이름과 휴대전화번호가 쌍으로 없는 경우 INSERT하고, 존재하는 경우 주소만 UPDATE하는 쿼리는 아래와 같다.

```sql
INSERT INTO tb_user
(
	name,
	mobile,
	address,
	reg_dt
) VALUES (
	'김테스트', 
	'010-1234-1234,
	'서울 강남구',
	now()
) ON DUPLICATE KEY UPDATE 
  address = #{address},
  update_dt = now()
```

#[MariaDB](/tags/MariaDB/)
