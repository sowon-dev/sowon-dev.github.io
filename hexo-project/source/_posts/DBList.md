---
title: "[ITWILL : DB] DB전체목록List"
date: 2020-10-29 15:00:00
tags:
  - "ITWILL(JAVA)"
  - "Oracle"
  - "List"
categories:
  - Database
  - Oracle
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">DB전체목록List의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    1. 간단 리눅스명령어(복붙포함), Oracle 명령어, DB작동방법, 접속순서을 적용할 수 있다.</p>
</div>

<!-- more -->

## 🌱리눅스와 SQL

  1. [간단 리눅스명령어(복붙포함), Oracle 명령어, DB작동방법, 접속순서](https://sowon-dev.github.io/2020/06/01/200602dbi/)
  2. [virtualBox로 가상컴퓨터만들어서 리눅스Linux 설치하기](https://sowon-dev.github.io/2020/06/15/200616dbi/)
  3. [CUI환경 VS GUI환경, 리눅스명령어자세히, vi단축키](https://sowon-dev.github.io/2020/06/18/200619dbi/)
  4. [SQL DEVELOPER사용방법](https://sowon-dev.github.io/2020/07/09/200710dbi/)

## 🌱DB와 SQL개념

  1. [DB기초이론, DBMS](https://sowon-dev.github.io/2020/05/28/200529dbi/)
  2. [데이터베이스기초활용](https://sowon-dev.github.io/2020/06/05/200602dbi2/)
  3. [DDL vs DML vs DCL](https://sowon-dev.github.io/2020/06/05/200605dbi/)
  4. [제약조건의 컬럼레벨과 테이블레벨문법, 제약조건 5가지, 버퍼에 있는 자주 사용할 쿼리구문을 저장하는 방법](https://sowon-dev.github.io/2020/06/07/200608dbi/)
  5. [select as from where, order by, 동일유저 동시접속 가능, 트랜잭션 commit과 rollback](https://sowon-dev.github.io/2020/06/09/200610dbi/)
  6. [트랜잭션(Transaction), 치환변수, save명령어, 리소스부족에러발생시](https://sowon-dev.github.io/2020/07/16/200717dbi/)
  7. [Data Dictionary](https://sowon-dev.github.io/2020/08/03/200804dbi/)

## 🌱Select 구문

  1. [Select 구문을 사용한 데이터 검색, null VS 0 VS 공백, Distinct](https://sowon-dev.github.io/2020/06/22/200623dbi/)
  2. [테이블 전체목록조회, 테이블구조조회, WHERE(조건문)절](https://sowon-dev.github.io/2020/06/25/200626dbi/)
  3. [Order by 정렬](https://sowon-dev.github.io/2020/06/25/200626dbi2/)

## 🌱단일행함수

  1. [단일행함수 : 문자함수](https://sowon-dev.github.io/2020/06/30/200630dbi/)
  2. [단일행함수 : 숫자함수, 날짜함수](https://sowon-dev.github.io/2020/06/30/200630dbi2/)
  3. [단일행함수 : 변환함수, 일반함수](https://sowon-dev.github.io/2020/06/30/200630dbi3/)
  4. [단일행함수 : 조건부 표현식](https://sowon-dev.github.io/2020/08/10/200811dbi/)

## 🌱여러행함수

  1. [여러행함수 : 그룹함수](https://sowon-dev.github.io/2020/06/30/200630dbi4/)
  2. [여러행함수 : Group by절, Having절](https://sowon-dev.github.io/2020/07/07/200707dbi/)

## 🌱중요 구문

  1. [JOIN](https://sowon-dev.github.io/2020/07/09/200710dbi2/)
  2. [Subquery1: Subquery개념, 중첩Subquery](https://sowon-dev.github.io/2020/07/13/200714dbi/)
  3. [Subquery2: Inlineview, Scalar Subquery](https://sowon-dev.github.io/2020/08/23/200824dbi/)
  4. [Subquery3: exists연산자, not exists연산자](https://sowon-dev.github.io/2020/08/24/200825dbi/)
  5. [Subquery4: with절](https://sowon-dev.github.io/2020/08/24/200825dbi/)
  6. [SQL 기억해야 할 쿼리](https://sowon-dev.github.io/2020/07/28/200729dbi3/)
  7. [Top-N분석](https://sowon-dev.github.io/2020/08/19/200820dbi/)

## 🌱데이터조작어 (DML) / 데이터정의어 (DDL)

  1. [데이터조작어DML : insert/update/delete구문](https://sowon-dev.github.io/2020/07/14/200714dbi2/)
  2. [데이터정의어DDL : table 생성 table 복사, varchar2와 varchar와 char비교](https://sowon-dev.github.io/2020/07/20/200721dbi/)
  3. [데이터정의어DDL : 테이블수정(컬럼수정, 제약조건수정, 컬럼명수정, 제약조건명수정), 테이블명변경, 테이블삭제, 테이블절단, truncate과 delete과 drop차이](https://sowon-dev.github.io/2020/07/23/200724dbi/)

## 🌱SQL의 OBJECT 종류

  1. [SQL의 OBJECT종류 : view](https://sowon-dev.github.io/2020/07/27/200728dbi/)
  2. [SQL의 OBJECT종류 : 시퀀스(Sequence)](https://sowon-dev.github.io/2020/07/28/200729dbi/)
  3. [SQL의 OBJECT종류 : 인덱스(Index), 시노님(Synonym)](https://sowon-dev.github.io/2020/07/28/200729dbi2/)

## 🌱DB구조

  1. [Oracle DB구조1 : Database](https://sowon-dev.github.io/2020/08/26/200826dbi/)
  2. [Oracle DB구조2 : Instance의 SGA메모리구조](https://sowon-dev.github.io/2020/08/28/200828dbi/)
  3. [Oracle DB구조3 : Instance의 Background process](https://sowon-dev.github.io/2020/08/31/200831dbi/)
  4. [Oracle DB구조4 : 구조 완벽정리, 상활별 오라클 DB 순서](https://sowon-dev.github.io/2020/09/01/200901dbi2/)

## 🌱DB구현 및 관리

  1. [Oracle DB생성방법 2가지, Oracle DB Tool, Parameterfile 유형](https://sowon-dev.github.io/2020/09/09/200911dbi/)
  2. [오라클의 Database 켜고 끄기](https://sowon-dev.github.io/2020/09/14/200914dbi/)
  3. [오라클의 Datafile 관리하기](https://sowon-dev.github.io/2020/09/18/200918dbi/)
  4. [DB유저관리 : user 생성, 권한부여](https://sowon-dev.github.io/2020/09/20/200921dbi/)
  5. [데이터충돌, DeadLock](https://sowon-dev.github.io/2020/09/21/200922dbi/)
  6. [DB fail 유형](https://sowon-dev.github.io/2020/09/22/200922dbi2/)
  7. [Controlfile다중화, Redoligfile다중화, 데이터베이스로그모드](https://sowon-dev.github.io/2020/09/27/200928dbi/)
  8. [DB BACKUP](https://sowon-dev.github.io/2020/10/16/201016dbi/)
  9. [DB 복구(Recovery)](https://sowon-dev.github.io/2020/10/19/2010120dbi/)

#[ITWILL(JAVA)](/tags/ITWILL-JAVA/)[Oracle](/tags/Oracle/)[List](/tags/List/)
