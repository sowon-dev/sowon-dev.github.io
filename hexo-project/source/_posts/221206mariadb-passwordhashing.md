---
title: "[MySQL/MariaDB] xml파일에 PASSWORD()가 뭐길래"
date: 2022-12-05 20:16:15
tags:
  - "MariaDB"
categories:
  - Database
  - MySQL
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">xml파일에 PASSWORD()가 뭐길래의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    xml파일에 선언하지 않았던 AES_DECRYPT(), UNHEX(), PASSWORD() 함수들이 보였다. 쿼리를 읽었을때 암호화와 복호화인건 알았으나 구체적인 사용방법을 알고 싶어 구글링해보니 MARIADB가 제공하는 내장함수였다.</p>
</div>

<!-- more -->

xml파일에 선언하지 않았던 AES_DECRYPT(), UNHEX(), PASSWORD() 함수들이 보였다. 쿼리를 읽었을때 암호화와 복호화인건 알았으나 구체적인 사용방법을 알고 싶어 구글링해보니 MARIADB가 제공하는 내장함수였다.

  * 예시코드

```sql
select USER_NO
	, AES_DECRYPT(UNHEX(USER_NUM), #{encrypt_key}) AS USER_NUM
	, PASSWORD(#{user_login_pin}) AS USER_LOGIN_PIN
	-- 중략
from USER
```

마리아DB 공식문서에 너무 잘 나와있어서 이해하기 훨씬 편했다.

  * [마리아DB 공식 문서-영어](https://mariadb.com/kb/en/)
  * [마리아DB 공식 문서-한국어](https://mariadb.com/kb/ko/)

한글버전이 있지만 번역되지 않은 페이지가 더 많으므로 영어로 보는 것을 추천한다.  
그리고 공식문서를 보기위해선 현재 프로젝트가 어떤 버전을 사용하고 있는지 알아야한다. 사용하고 있는 마리아DB버전에 따라 지원되지 않는 함수가 있을 수 있기때문이다.  
db를 열어 아래 쿼리를 입력해주면 된다.

  
  
  

# MariaDB 버전확인 하는 방법

```sql
select version();

// 쿼리 결과 예시
10.3.32-MariaDB-log
```

  
  
  

# PASSWORD()

> Calculates and returns a hashed password string from the plaintext password str. Returns an empty string (>= MariaDB 10.0.4) if the argument was NULL.  
> The return value is a nonbinary string in the connection character set and collation, determined by the values of the character_set_connection and collation_connection system variables.  
> This is the function that is used for hashing MariaDB passwords for storage in the Password column of the user table (see privileges), usually used with the SET PASSWORD statement. It is not intended for use in other applications  
> 출처: [https://mariadb.com/kb/en/password](https://mariadb.com/kb/en/password/)

순수 문자열을 입력하면 해시처리된 문자열로 바꿔주는 함수이다. 만약 순수 문자열이 NULL인 경우에는 빈 문자열이 반환된다.  
왜 PASSWORD() 함수를 사용해야할까? 사용자가 입력한 비밀번호를 개발자도 모르는 암호화된 값으로 바꿔서 DB에 저장하기때문이다.  
어떤 방식으로 암호화될까? [마리아DB 버전4.1까지는 기존의 SHA-1 알고리즘을 사용했으나 보안의 취약성으로 인해 마리아DB 5.2부터는 ed25519 인증플러그인을 사용한다.](https://mariadb.com/kb/en/authentication-plugin-ed25519/)

  
  
  

## 구문

```sql
PASSWORD(str)
```

  
  
  

## 예시

```sql
SELECT PASSWORD('notagoodpwd');
+-------------------------------------------+
| PASSWORD('notagoodpwd')                   |
+-------------------------------------------+
| *3A70EE9FC6594F88CE9E959CD51C5A1C002DC937 |
+-------------------------------------------+
```

  
  
  

# HEX()와 UNHEX()

  * HEX(): 기존 텍스트를 16진수 값의 문자로 변환하여 반환한다.
  * UNHEX(): HEX의 역산으로 16진수를 숫자로 해석을 하고 그 숫자에 대응하는 문자로 변환한다. 그 결과, 문자들은 바이너리 스트링으로 리턴된다. 그리고 UTF8로 CONVERT 작업을 해주면 기존 텍스트로 변환이 가능하다.

  
  
  

## 예시

```sql
SELECT HEX('MariaDB');
+----------------+
| HEX('MariaDB') |
+----------------+
| 4D617269614442 |
+----------------+

SELECT UNHEX('4D617269614442');
+-------------------------+
| UNHEX('4D617269614442') |
+-------------------------+
| MariaDB                 |
+-------------------------+
```

  
  
  

# 참고

  * <https://mariadb.com/kb/en/password/>
  * <https://victorydntmd.tistory.com/144>
  * <https://shxrecord.tistory.com/238>

#[MariaDB](/tags/MariaDB/)
