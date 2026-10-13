---
title: "delete mapper에서 여러 테이블의 데이터 한꺼번에 삭제 오류"
date: 2021-08-04 21:17:49
tags:
  - "MyBatis"
categories:
  - Database
  - General
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">delete메서드이다보니 조심스럽게 run을 돌렸는데 syntax에러가 나타났다! 원인을 파악했다.
    이를 한꺼번에 아래 코드처럼 처리할 수 있다.</p>
</div>

<!-- more -->

개인정보와 같은 경우 회원 탈퇴를 할때 여러 테이블에 있는 해당 사용자 정보를 전부 다 삭제해야한다.  
이를 한꺼번에 아래 코드처럼 처리할 수 있다.

## 다중쿼리

아래는 user id를 가지고 userinfo테이블, payment테이블, authority테이블, board테이블, 총 4개의 테이블에서 해당 유저정보를 삭제하는 다중쿼리이다.

```
<delete id="deletePersonalData" parameterType="String">
	DELETE FROM userinfo
	 WHERE user_id = #{userId};

	DELETE FROM payment
	 WHERE user_id = #{userId};

	DELETE FROM authority
	 WHERE user_id = #{userId};

	DELETE FROM board
	 WHERE user_id = #{userId};
</delete>
```

delete메서드이다보니 조심스럽게 run을 돌렸는데 syntax에러가 나타났다!

![](/img/210805MyBatis-multiqueries.PNG)

해당 쿼리를 전혀 읽지 못하고 있었다.  
구글링으로 엄청 삽질하다가 과장님께 물어보니 멀티 쿼리 허용했는 지를 물어보셨다  
내 대답은 아뇨…였다.

과장님 감사합니다🙏

  
  
  

## 멀티쿼리 허용하기

`application.properties`에 기재되어있는 DB주소 정보 뒤에 멀티쿼리를 설정해줘야한다!

  * `allowMultiQueries=true`

아래는 코드 예시이다.

```java
jdbc:log4jdbc:mariadb://DB서버IP주소/DatabaseName?allowMultiQueries=true
```

설정해야지만 쓸 수 있는 것이 다중쿼리이다!  
까먹지말고 DB주소 뒤에 설정하자!

#[MyBatis](/tags/MyBatis/)
