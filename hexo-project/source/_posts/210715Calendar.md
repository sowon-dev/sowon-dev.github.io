---
title: "String으로 날짜 가지고 놀기"
date: 2021-07-14 15:00:00
tags:
  - "java.util.Calendar"
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">String으로 날짜 가지고 놀기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    사용할 라이브러리는 총 3가지이다.</p>
</div>

<!-- more -->

String으로 날짜를 받은 뒤 하루를 더하거나, 하루를 빼거나, 그 달의 마지막 날을 구하거나 첫번째 날을 구하는 등 날짜 연산을 하는 법을 알아보자.  
사용할 라이브러리는 총 3가지이다.

  1. import java.text.SimpleDateFormat;
  2. import java.util.Date;
  3. import java.util.Calendar;

  
  
  

## String으로 날짜 연산하기

```java
SimpleDateFormat sdfYMDHms = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
SimpleDateFormat sdfYMD = new SimpleDateFormat("yyyy-MM-dd");

String test = "2021-07-16";

//String을 날짜 연산을 위해 Date 객체로 변경
Date date = sdfYMD.parse(test); 

//날짜 연산을 위한 Calendar객체 생성 후 date 대입
Calendar cal = Calendar.getInstance();
cal.setTime(date);

// add 하기
cal.add(Calendar.MILLISECOND, 10); //10밀리초 더하기
System.out.println("10밀리초 더하기: "+sdfYMDHms.format(cal.getTime()));

cal.add(Calendar.MINUTE, 10); //10분 더하기 
System.out.println("10분 더하기: "+sdfYMDHms.format(cal.getTime()));

cal.add(Calendar.MINUTE, -10); //10분 빼기 
System.out.println("10분 빼기: "+sdfYMDHms.format(cal.getTime()));

cal.add(Calendar.HOUR, 1); //1시간 후 
System.out.println("1시간 후: "+sdfYMDHms.format(cal.getTime()));

cal.add(Calendar.HOUR, -1); //1시간 전 
System.out.println("1시간 전: "+sdfYMDHms.format(cal.getTime()));

cal.add(Calendar.DATE, 1); // 1일 더하기
System.out.println("1일 더하기: "+sdfYMD.format(cal.getTime()));

cal.add(Calendar.DATE, -1); // 1일 빼기  
System.out.println("1일 빼기: "+sdfYMD.format(cal.getTime()));

cal.add(Calendar.MONTH, 1); // 한달 더하기
System.out.println("한 달 더하기: "+sdfYMD.format(cal.getTime()));

cal.add(Calendar.MONTH, -1); // 한달 빼기  
System.out.println("한 달 빼기: "+sdfYMD.format(cal.getTime()));

// set 하기
cal.set(Calendar.DAY_OF_WEEK, Calendar.MONDAY); // 해당 일자가 있는 주의 월요일 구하기
System.out.println("해당 일자가 있는 주의 월요일 구하기: "+sdfYMD.format(cal.getTime()));   

cal.set(Calendar.DAY_OF_MONTH, cal.getActualMaximum(Calendar.DAY_OF_MONTH)); // 해당 월 마지막날 구하기
System.out.println("해당 월 마지막날 구하기: "+sdfYMD.format(cal.getTime()));   

// 해당 일자 무슨 요일인지 구하기 일요일:0 월요일 1 ~ 토요일 7
System.out.println("해당 월 마지막날의 요일 구하기: "+ cal.get(Calendar.DAY_OF_WEEK));
```

출력값은 아래와 같다.

```java
10밀리초 더하기: 2021-07-16 00:00:00.010
10분 더하기: 2021-07-16 00:10:00.010
10분 빼기: 2021-07-16 00:00:00.010
1시간 후: 2021-07-16 01:00:00.010
1시간 전: 2021-07-16 00:00:00.010
1일 더하기: 2021-07-17
1일 빼기: 2021-07-16
한 달 더하기: 2021-08-16
한 달 빼기: 2021-07-16
해당 일자가 있는 주의 일요일 구하기: 2021-07-12
해당 월 마지막날 구하기: 2021-07-31
해당 월 마지막날의 요일 구하기: 7
```

#[java.util.Calendar](/tags/java-util-Calendar/)
