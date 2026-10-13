---
title: "[오류일지]Error creating bean with name 에러 해결 PropertySourcesPlaceholderConfigurer"
date: 2021-03-14 15:00:00
tags:
  - "Eclipse"
  - "오류일지"
  - "STS"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">svn에서 import한 프로젝트를 셋팅하는 과정에서 톰캣을 실행하니 아래와 같은 오류가 발생했다.
    properties를 찾지못해서 bean을 생성하지 못한 경우로 톰캣서버에 연결해줘서 환경별 설정이 가능하도록 해주면 된다.</p>
</div>

<!-- more -->

## 문제 : PropertySourcesPlaceholderConfigurer

svn에서 import한 프로젝트를 셋팅하는 과정에서 톰캣을 실행하니 아래와 같은 오류가 발생했다. 

Error creating bean with name ‘org.springframework.context.support.PropertySourcesPlaceholderConfigurer#0’: Cannot resolve reference to bean ‘properties’ while setting bean property ‘properties’; nested exception is org.springframework.beans.factory.NoSuchBeanDefinitionException: No bean named ‘properties’ available at

## 원인과 해결

properties를 찾지못해서 bean을 생성하지 못한 경우로 톰캣서버에 연결해줘서 환경별 설정이 가능하도록 해주면 된다.

  1. 톰캣서버를 더블클릭한 후 General Information 에서 아래 이미지처럼 `Open launch configuration`을 클릭한다

![](/img/210315springBeanError1.PNG)

  2. Arguments 탭에서 아래 부분을 복붙하여 넣어준 뒤 Apply하고 OK하면 끝!

```xml
-Dspring.profiles.active=local
```

![](/img/210315springBeanError2.PNG)

해결!

#[Eclipse](/tags/Eclipse/)[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)[STS](/tags/STS/)
