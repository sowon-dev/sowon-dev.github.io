---
title: "[Spring] 새로운 컨트롤러(Controller)를 생성했는데 호출이 안될때"
date: 2023-01-04 20:02:22
tags: []
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">새로운 컨트롤러(Controller)를 생성했는데 호출이 안될때의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    핵심 설정과 구현 코드를 단계별로 파악하여 상황에 맞게 유연하게 활용할 수 있다.</p>
</div>

<!-- more -->

레거시 프로젝트에 신규 패키지를 만들고 그 패키지안에 신규 컨트롤러를 생성했다. 컨트롤러에 서비스 메서드를 만들고 포스트맨으로 호출했는데 웬걸?! 서버가 전혀 반응을 안한다. 왜일까?

기본적으로 해봐야하는 것은 build 탭 > clean > 서버 재시작이다. 빌드가 제대로 안되어있으면 컨트롤러가 새로 생성된지도 모르기때문이다. 하지만 나는 여전히 반응하지않았다. 수석연구원님께 물어 알게된 것은 컴포넌트 스캔문제였다.

# 문제점

`servlet-context.xml`파일에서 아래처럼 컴포넌트 스캔 코드가 있는데 나는 테스트용 새로운 패키지인 `com.test.preview`를 만들고 그곳에다 신규 컨트롤러를 생성했다. 따라서 컴포넌트가 스캔이 되지않았던 것이다.

  * 기존코드 

```java
<context:component-scan base-package="com.test.controller" />
```

  
  
  

# 해결

콤마를 이용해서 베이스패키지를 추가해주면 해결!  
감사합니다 김수석연구원님!

```java
<context:component-scan base-package="com.test.controller,com.test.preview" />
```
