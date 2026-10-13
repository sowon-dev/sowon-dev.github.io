---
title: "[MySQL] selet 컬럼명을 조건에 따라 다르게 출력할 수 있을까?"
date: 2021-06-13 19:57:15
tags:
  - "MySQL"
categories:
  - Database
  - MySQL
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">selet 컬럼명을 조건에 따라 다르게 출력할 수 있을까?의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    먼저 if나 case절을 생각했는데 아무래도 select값이 변경되어야하기때문에 사용하기가 힘들었다.</p>
</div>

<!-- more -->

오늘 쿼리를 작성하다가 궁금증이 생겼다.  
예를 들어 학교 교직원 및 학생 정보를 user테이블에 다 있다고 생각해보자.  
relation테이블을 이용하여 학생의 담임교사와 학부모정보를 출력하고 싶었다.  
user테이블에서 자기 자신을 계속 join하는 상황에서 상황별 학생정보를 출력하려면 어떻게 해야할까?

## 첫 시도와 문제점 ☝️

```sql
// 모든 정보가 다 있는 경우
select u1.name, u1.tel, --학생정보 
   u2.name, u2.tel, --학부모정보
   u3.name, u3.tel --담임교사정보
FROM user u1
join user_relation ur
on u1.tel = ur.학생tel
JOIN user u2
ON ur.학부모tel = u2.tel
JOIN user u3
ON ur.교사tel = u3.tel
WHERE u1.tel = #{학생tel}
```

위 쿼리의 문제점은 크게 2가지이다.

  1. 학부모정보가 없는 경우 학생정보가 아예 출력 안됨.
  2. 담임교사 정보가 없는 경우 학생정보가 아예 출력 안됨.

학무보정보나 담임교사정보가 없는 상황에서도 학생정보를 출력하고 싶다면 어떻게 해야할까?

  
  
  

## 모든 쿼리를 다 만들면 어때? 🤔

먼저 if나 case절을 생각했는데 아무래도 select값이 변경되어야하기때문에 사용하기가 힘들었다.  
그렇다면 모든 경우의 수별로 쿼리를 다 만들어보는 방법이 있다.  
예를 들면 아래와 같다.

  1. 모든 정보가 다 있는 경우

```sql
// 모든 정보가 다 있는 경우
select u1.name, u1.tel, --학생정보 
   u2.name, u2.tel, --학부모정보
   u3.name, u3.tel --담임교사정보
FROM user u1
join user_relation ur
on u1.tel = ur.학생tel
JOIN user u2
ON ur.학부모tel = u2.tel
JOIN user u3
ON ur.교사tel = u3.tel
WHERE u1.tel = #{학생tel}
```

  2. 담임정보가 없는 경우

```sql
// 담임정보가 없는 경우
select u1.name, u1.tel, --학생정보 
   u2.name, u2.tel, --학부모정보
FROM user u1
join user_relation ur
on u1.tel = ur.학생tel
JOIN user u2
ON ur.학부모tel = u2.tel
WHERE u1.tel = #{학생tel}
```

  3. 학부모정보가 없는 경우

```sql
// 학부모정보가 없는 경우
select u1.name, u1.tel, --학생정보 
   u3.name, u3.tel --담임교사정보
FROM user u1
join user_relation ur
on u1.tel = ur.학생tel
JOIN user u3
ON ur.교사tel = u3.tel
WHERE u1.tel = #{학생tel}
```

  4. 담임정보도 없고 학부모정도 없는 경우

```sql
// 담임정보도 없고 학부모정도 없는 경우
select u1.name, u1.tel
FROM user u1
WHERE u1.tel = #{학생tel}
```

보시다시피 너무 비효율적이다.  
한 쿼리로 해결하는 방법이 없을까? 구글링하다가 도저히 모르겠어서 팀장님께 조심스럽게 물어봤는데 바로 해결방법을 알려주셨다!

  
  
  

## 한 쿼리로 해결 😎

해결책은 바로 left outer join이었다!

```sql
select u1.name, u1.tel, --학생정보 
   u2.name, u2.tel, --학부모정보
   u3.name, u3.tel --담임교사정보
FROM user u1
left outer join user_relation ur
on u1.tel = ur.학생tel
left outer JOIN user u2
ON ur.학부모tel = u2.tel
left outer JOIN user u3
ON ur.교사tel = u3.tel
WHERE u1.tel = #{학생tel}
```

위에서 내가 작성한 join 앞에 아무것도 적지않았으므로 기본적으로 inner조인이 된다. 즉 교집합만 보여주는 쿼리가 된다.  
outer조인에는 크게 3가지가 있고 그 중 left outer join을 실무에서 가장 많이 사용한다고 한다.  
아무리 쉬워보이는 거라도 용기내서 물어보길 잘했다! 덕분에 확실히 개념이 잡혔다. 룰루!

  
  
  

## outer join이란?

아래 그림을 보면 이해하기가 쉽다.

  * join = inner join : 교집합
  * outer join 종류
    * left outer join : 실무에서 가장 많이 사용
    * right outer join
    * full outer join

![https://blog.edit.kr/m/entry/Oracle-%EC%BF%BC%EB%A6%AC%EC%A4%91%EC%97%90-%EC%9D%98-%EC%9D%98%EB%AF%B8?category=290081](https://blog.kakaocdn.net/dn/3qpye/btq14YgdCQB/18ZMl4d3sROOblZn4i6kYk/img.jpg)

  
  
  

## SQL NULL 처리하기

팀장님께서 추가로 null값이 들때 default값을 설정할 수 있는 COALESCE()도 함께 알려주셨다.

  * [바로가기: SQL에서 컬럼값이 NULL처리는 어떻게 하면 좋을까?]()

  
  
  

## 참고

  * [더 많은 join](https://sowon-dev.github.io/2020/07/09/200710dbi2/)

#[MySQL](/tags/MySQL/)
