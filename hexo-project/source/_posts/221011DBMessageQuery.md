---
title: "[Spring/MySQL] 현재 서버에서 접속한 DB 이름 로그에 나타내기"
date: 2022-10-10 21:46:45
tags:
  - "MySQL"
categories:
  - Database
  - MySQL
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">현재 서버에서 접속한 DB 이름 로그에 나타내기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    DB를 여러 가지 쓰는 경우 현재 어느 DB에 접속되어있는지 서버 런할때 로그로 알 수 있으면 좋겠다고 생각했는데 팀장님이 그 방법을 알려주셨다.</p>
</div>

<!-- more -->

DB를 여러 가지 쓰는 경우 현재 어느 DB에 접속되어있는지 서버 런할때 로그로 알 수 있으면 좋겠다고 생각했는데 팀장님이 그 방법을 알려주셨다.  
바로 local.properties에 message.query를 이용하면 된다.

# local.properties에 message.query 속성 사용하기

local.properties파일에서 message.query 속성을 이용하면 된다.  
아래처럼 입력해주면 끝!

```plain
message.query=SELECT 'ko' as LOCALE, '0000001' as CODE, concat(database(), ' ver.', version() , ' hostname - ', @@hostname) as MSG FROM DUAL
```

#[MySQL](/tags/MySQL/)
