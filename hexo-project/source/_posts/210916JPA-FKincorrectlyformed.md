---
title: "[JPA/MariaDB]errno: 150 Foreign key constraint is incorrectly formed 해결방법"
date: 2021-09-15 21:16:32
tags:
  - "오류일지"
categories:
  - Backend
  - JPA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">MariaDB와 JPA로 복합키이면서 그 중 하나는 FK인 테이블을 만들고 싶었는데 계속해서 FK 에러가 발생했다.
    2. 조합이 UTF-8 한쪽만 설정되어 있음을 통해 문제를 해결할 수 있다.</p>
</div>

<!-- more -->

MariaDB와 JPA로 복합키이면서 그 중 하나는 FK인 테이블을 만들고 싶었는데 계속해서 FK 에러가 발생했다.

![](/img/210915commoncodegrup3.PNG)

위 ERD와 같이 symptom테이블을 만들고 싶었다.  
모든 키가 복합키이면서 review_id키는 FK 제약조건을 걸고싶었다.  
create해서 테이블은 잘 생성되지만 FK를 걸다가 에러를 발생했다.

  * 에러코드

```java
Hibernate: alter table symptom add constraint FKct400cemwq2cjh9mdfusfieko foreign key (review_id) references review (id)
GenerationTarget encountered exception accepting command : Error executing DDL "alter table symptom add constraint FKct400cemwq2cjh9mdfusfieko foreign key (review_id) references review (id)" via JDBC Statement
org.hibernate.tool.schema.spi.CommandAcceptanceException: Error executing DDL "alter table symptom add constraint FKct400cemwq2cjh9mdfusfieko foreign key (review_id) references review (id)" via JDBC Statement

(중략)

Caused by: java.sql.SQLTransientConnectionException: (conn=115300) Can't create table `boostshot`.`symptom` (errno: 150 "Foreign key constraint is incorrectly formed")
```

  
  
  

## 에러 150을 해결하는 방법 4가지

아래 4가지 조건에 부합해야한다.

  1. 데이터 타입이 일치해야 함
  2. NOT NULL or NULL 여부가 동일해야 함
  3. 참조받는 데이터가 unique key / primary key 이어야함
  4. 두 테이블의 charset 이 같아야함

참고 포스팅 : [박스님 - errno: 150 “Foreign key constraint is incorrectly formed](https://box0830.tistory.com/211)

  
  
  

## 기존 테이블

![](/img/210916jpafkerror1.PNG)

위 4가지 조건에서 1번과 4번조건이 부합하지않는다.

  1. 데이터 타입이 BIGINT와 VARCHAR임
  2. 조합이 UTF-8 한쪽만 설정되어 있음

  
  
  

## 해결

복합키를 위해 생성한 클래스에서 데이터 타입이 잘못 지정되어있었다.  
String타입을 Long타입으로 변경하여 일치 시켜주니 정상 작동했다!

```java
@NoArgsConstructor @AllArgsConstructor
@EqualsAndHashCode
public class SymptomId implements Serializable {
	// 기존 
	// private String reviewId; 
	// 변경: String -> Long
	private Long reviewId;
	private String symptomCode;
}
```

  * 정상작동한 테이블 모습

![](/img/210916jpafkerror2.PNG)

여담이지만 이 별것도 아닌 에러를 가지고 2시간이나쓰고 그것도 모자라서 과장님께 한번만 도와달라고 부탁까지했다.  
과장님은 단 5분만에 데이터 타입이 다른 것을 찾아주셨다…그저 빛🌞  
역시 물어보길 잘했다. 완벽하게 이해했기때문에 이 에러는 다시는 만나지 않을 것 같다.

  
  
  

## 참고

에러부분 말고 전체 코드는 [JPA: Entity에 복합키와 FK 제약조건 넣기](https://sowon-dev.github.io/2021/09/15/210916Jpa-entityPKFK/) 포스팅에서 확인할 수 있다.

#[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)
