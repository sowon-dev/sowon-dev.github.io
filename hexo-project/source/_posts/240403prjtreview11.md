---
title: "SSO(Single Sign-On) 프로젝트를 끝내며 내가 배운 것"
date: 2024-04-02 20:23:06
tags:
  - "회고록"
categories:
  - Reflections
  - 회고록
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'SSO(Single Sign-On) 프로젝트를 끝내며 내가 배운 것'에 참여하고 주요 발표 내용과 배운 점을 정리한 글이다.
    실무 적용 사례를 통해 개발자의 역할과 협업, 지속적인 학습의 중요성을 확인할 수 있다.</p>
</div>

<!-- more -->

이번 프로젝트에서는 개인정보관리페이지(마이페이지)를 주 업무로 맡았다.  
편리함과 어려움이 공존한 프로젝트였는데 아래와 같다.

편리함

  1. 스프링부트의 편리함에 감탄했다. 작업하는 동안 서버때문에 불편한 일이 거의 없었다.
  2. Thymeleaf 간편함에 감탄했다. JSTL과 EL사용하던데 손에 익어서 초반에 조금 버벅거렸지만 이내 Thymeleaf의 가독성 높은 표현방법에 반해버렸다.

어려움

  1. 이번 작업은 꽤나 어려웠는데 그 이유는 클라이언트의 비협조로 레거시의 조각조각난 쿼리를 받아서 작업해야했기 때문이다. 테이블과 컬럼, 데이터도 알려주지않아서, 테이블과 프로시저를 상상하고 유추하면서 작업을 진행해야했다. 덕분에 정보가 불충분한 상황에서도 요구사항대로 기능을 구현하는 능력을 키울 수 있었다. 

이렇게 프로젝트 경험치가 차곡차곡 쌓이고 있다. 좋은 거맞지..?!

  
  
  

# keep

현재 만족하고 있는 부분과 계속해서 이어갔으면 하는 부분

  1. Thymeleaf 적극 활용
     * `th:block` 를 사용하여 논리적 코드 블록화하여 가독성 높였으며 Thymeleaf만의 formatting utilities를 사용하여 편리하게 작업할 수 있었다.

```html
//자주 사용했던 formatting utilities
${#strings.isEmpty()}
${#calendars.format()}
```

  2. 사용자별 권한별 바로가기 메뉴 구현
     * 바로가기 메뉴를 만드는데 사용자별로 원하는 메뉴들을 순서대로 지정할 수 있고 사용자가 자신의 바로가기메류를 지정하지않았다면 시스템관리자가 권한(role)별로 설정해놓은 바로가기를 순서대로 보여주는 것을 구현했다. 순서대로를 어떻게 구현할 지 고민했는데 Array를 사용해서 클릭 순서대로 `Array.push()`했고 제거시 해당 index의 요소를 삭제하면서 Array 순서가 그대로 유지될 수 있도록 구현했다.
  3. 타이머 만들기: setInterval을 활용하여 3분 타이머 구현
     * 오랜만에 함수로 만드니까 재밌었다.
  4. jQuery 비중을 줄이고 Vanilla JS 사용
     * 지난 프로젝트부터 의식적으로 jQuery 사용을 줄이고 Vanilla JS를 더 많이 사용했다. 바닐라JS는 제이쿼리보다 코드는 길어지지만 제이쿼리API를 다녀오지않아도 되기에 속도가 빠르다. 이미 손에 익어버린 jQuery를 의식적으로 바닐라JS를 사용하려니 처음에는 버벅거렸지만 프로젝트 갈수록 코딩속도가 붙었다. 다음 프로젝트도 바닐라JS를 의식적으로 사용해야겠다.
  5. SVN 저장소에서 GitLab으로 마이그레이션하기
     * 단독으로 마이그레이션을 담당한 것이 처음이라서 재밌었다.
     * 관련 포스팅: [SVN에서 사내 GitLab으로 변경하기(ft.migration)](https://sowon-dev.github.io/2024/04/02/240403svn-to-git/)

  
  
  

# Problem

개선이 필요하다고 생각되는 부분

  1. 오라클 DB 프로시저 mybatis와 연동하여 사용법

```
<select id="callSampleProcedure" statementType="CALLABLE">
  { call SAMPLE_PROCEDURE(
      #{param1, mode=IN, jdbcType=VARCHAR},
      #{param2, mode=OUT, jdbcType=VARCHAR}
  )}
</select>
```

```java
Map<String, Object> parameterMap = new HashMap<>();
parameterMap.put("param1", "input_value");
parameterMap.put("param2", null); // Output 파라미터도 선언해줘야
```

statementType=”CALLABLE” 을 사용하여 프로시저를 호출해야했다. 그걸 모르고 얼마나 삽질했는지… 또한 out파라미터도 null로 선언해줘야한다.

  
  
  

# Try

Problem의 해결책이 될 수 있는 부분

  1. 네트워크 공부를 하면서 겸사겸사 네트워크 관리사2급를 취득할 것이다.
     * ONE ACTION: 24년 제03회 필기신청 2024-07-26, 필기응시 2024-08-25, 실기 2024-09-29 최종 합격발표 2024-10-08
  2. Oracle DB 공부

#[회고록](/tags/%ED%9A%8C%EA%B3%A0%EB%A1%9D/)
