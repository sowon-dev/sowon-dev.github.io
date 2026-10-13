---
title: "[MySQL]날짜 데이터타입에서 Timestamp를 쓰는 경우"
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
  <p class="tldr-desc">'날짜 데이터타입에서 Timestamp를 쓰는 경우'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    이 둘의 가장 큰 차이점은 time zone의 영향을 받는지 안 받는지이다.</p>
</div>

<!-- more -->

DB를 설계하면서 등록일자, 삭제날짜등의 날짜 데이터타입을 지정해야했다.  
날짜 데이터타입으로는 크게 Date, Datetime, Time, Timestamp 4가지가 있다.

## Date vs Time

| | Date | Time  
---|---|---  
설명 | 날짜만 출력 | 시간만 출력  
예시 | YYYY-MM-DD | HH:MM:SS  
범위 | from 1000-01-01 to 9999-12-31 | from -838:59:59 to 838:59:59  
  
내가 필요한 데이터타입은 날짜뿐만 아니라 시간도 함께 필요하기때문에 Datetime, Timestamp 둘 중에서 무엇을 써야 좋을 지 고민했다.

  
  
  

## Datetime vs Timestamp

이 둘의 가장 큰 차이점은 time zone의 영향을 받는지 안 받는지이다.  
Timestamp는 서버 타임존에 영향을 받기 때문에 시스템 타임존이 변경되면 저장된 데이터도 변경된다.

| | DATETIME | TIMESTAMP  
---|---|---  
설명 | 날짜와 시간 둘다 출력 | 날짜와 시간 둘다 출력  
예시 | YYYY-MM-DD HH:MM:SS | YYYY-MM-DD HH:MM:SS  
범위 | from 1000-01-01 00:00:00   
to 9999-12-31 23:59:59 | from 1970-01-01 00:00:01 UTC   
to 2038-01-19 03:14:07 UTC  
현재시간 호출 | now() | default로 current_timestamp를 사용하여 자동 입력  
데이터 타입 | 문자형 | 숫자형  
용량단위 | 8byte | 4byte  
  
  
  
  

## 🤔 그럼 항상 Datetime만 사용하면 되는거 아닐까?

정답은 NO이다.  
글로벌 서비스를 하면 DB 서버가 해당 지역 타임존을 따를 수 있다.  
따라서 적절하게 선택하여 사용해야한다.

#[MySQL](/tags/MySQL/)[MariaDB](/tags/MariaDB/)
