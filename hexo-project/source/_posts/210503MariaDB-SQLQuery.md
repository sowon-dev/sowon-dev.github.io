---
title: "[MariaDB/MySQL]SQL Query"
date: 2021-05-02 15:00:00
tags:
  - "MySQL"
  - "MariaDB"
categories:
  - Database
  - MySQL
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">SQL Query의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    핵심 설정과 구현 코드를 단계별로 파악하여 상황에 맞게 유연하게 활용할 수 있다.</p>
</div>

<!-- more -->

# 📣 테이블

## 테이블 생성

```xml
create table [테이블명] 
(id int, name varchar(20), isDeleted boolean not null default 0);
```

## 테이블명 수정

```sql
alter table [테이블명] rename [변경할_테이블명];
```

## 테이블삭제

```sql
drop table [테이블명];
```

  
  
  

# 📣 컬럼

## 테이블에 컬럼추가

여러 개 추가시 컴마로 구분하기

```sql
alter table [테이블명] 
add [컬럼명] varchar(20) not null default 'N/A',
add [컬럼명] boolean not null default 0;
```

## 컬럼명 및 컬럼타입 변경

```sql
alter table [테이블명] 
change [컬럼명] [변경할_컬럼명] int;
```

## 컬럼삭제

```sql
alter table [테이블명] drop [컬럼명];
```

## 컬럼순서변경

```sql
alter table [테이블명]
modify [컬럼명] INT
after [앞에_위치시키고싶은_컬럼명]
```

  
  
  

# 📣 제약조건

## 제약조건확인

```sql
select * from information_schema.table_constraints 
where TABLE_SCHEMA = [스키마명];
```

## 제약조건 추가(PK)

```sql
alter table [테이블명] 
add constraint primary key [컬럼명];
```

## 제약조건 추가(FK)

```sql
alter table [테이블명] 
add constraint [제약조건이름] foreign key [컬럼명] 
references [부모테이블명] [pk컬럼명] on delete cascade / on update cascade;
```

## 제약조건 삭제

```sql
alter table [테이블명] drop constraint [제약조건명];
```

  
  
  

# 📣 데이터

## insert

  * 필드순서와 데이터값의 순서가 일치할때

```sql
INSERT INTO 테이블이름
VALUES (데이터값1, 데이터값2, 데이터값3, ...)
```

  * 필드순서와 데이터값의 순서가 불일치할때

```sql
INSERT INTO [테이블이름] (필드이름1, 필드이름2, 필드이름3, ...)
VALUES (데이터값1, 데이터값2, 데이터값3, ...)
```

## update

```sql
UPDATE [테이블이름]
SET [필드이름1]=[데이터값1], [필드이름2]=[데이터값2], ...
WHERE [필드이름=데이터값];
```

## delete

```sql
DELETE FROM [테이블이름]
WHERE [필드이름]=[데이터값];
```

#[MySQL](/tags/MySQL/)[MariaDB](/tags/MariaDB/)
