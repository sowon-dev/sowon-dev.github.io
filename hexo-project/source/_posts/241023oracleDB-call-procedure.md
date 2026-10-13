---
title: "오라클DB에서 프로시저 출력값 보는 방법"
date: 2024-10-22 15:46:18
tags:
  - "TIL"
  - "Oracle"
categories:
  - Database
  - Oracle
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">오라클 DB에서 프로시저의 DBMS_OUTPUT.PUT_LINE 메시지를 콘솔에서 확인하려면 출력 기능 활성화가 필수적이다.
    PL/SQL 블록을 실행하기 전 최상단에 SET SERVEROUTPUT ON; 명령어를 선언해야 결과값이 정상적으로 표시된다.</p>
</div>

<!-- more -->

프로시저를 작성하다가 오라클DB에서 바로 출력값을 보고 싶었다.

# 코드

```sql
SET SERVEROUTPUT ON;
DECLARE 
    V_RSLT VARCHAR(1);
    V_MSG VARCHAR(1000);
BEGIN
   PKG_TEST.P_TEST
  (
    IN_YR   => '2024'
  , IN_CD   => '100110'
  , IN_NM   => '나혜석'
  , O_RSLT  => V_RSLT
  , O_MSG   => V_MSG
  );

  DBMS_OUTPUT.PUT_LINE('RESULT: '|| V_RSLT);
  DBMS_OUTPUT.PUT_LINE('MSG: '|| V_MSG);
END;
```

기본적으로 Oracle 서버는 DBMS_OUTPUT.PUT_LINE에서 생성된 메시지를 자동으로 보여주지 않는다.  
이를 활성화하기 위해 `SET SERVEROUTPUT ON`을 선언해줘야한다.  
`SET SERVEROUTPUT ON`이 없으면 PL/SQL 블록에서 출력된 메시지는 콘솔에 나타나지 않는다.

#[TIL](/tags/TIL/)[Oracle](/tags/Oracle/)
