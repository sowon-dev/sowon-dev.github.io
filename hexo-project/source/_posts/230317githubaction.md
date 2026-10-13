---
title: "[GITHUB]깃허브액션(github action)"
date: 2023-03-16 15:56:43
tags:
  - "GIT"
categories:
  - Reflections
  - Version control
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">깃허브액션(github action)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    버전관리시스템에서 가장 많이 사용하는 GIT과 그걸 배포할 수 있는 GITHUB가 있다.</p>
</div>

<!-- more -->

어제 부장님이 젠키스와 깃헙액션을 이용해서 CI/CD에 관한 걸 말씀해주셨다.

젠킨스랑 깃헙액션이 같은 역할을 한다고 생각했는데 아닌거 같아 깃헙액션을 공부하게 되었다.  
깃헙액션을 가장 잘 소개한 영상이 있다면 바로 드림코딩 엘리님이다.  
정말 쉽게 잘 설명해주시니까 깃헙액션을 알고싶은 사람이라면 필수 시청해야하는 영상이다!

이번 글은 위 영상을 요약하면서 추가적으로 구글링한 내용을 덧붙였음을 밝혀둔다.  
😍엘리님 매번 좋은 영상 감사합니다😍

  
  
  

# 깃과 깃헙, 깃헙액션의 관계

버전관리시스템에서 가장 많이 사용하는 GIT과 그걸 배포할 수 있는 GITHUB가 있다.  
여기서 자동화(CI/CD)를 이용하려면 GITHUB의 레포지토리에다가 jenkins, buildkite, circleci 중 하나를 연결해야 가능했다.  
하지만 2018년에 깃헙액션이 등장하면서 별도의 외부툴없이 자동화프로세스를 만들 수 있다.

  
  
  

# 여기서 잠깐 CI/CD란?

  * CI: 지속적인 통합
  * CD: 지속적인 배포

깃헙 메인 리포지토리에 새롭게 추가되는 기능들을 CI서버에서 자동으로 빌드하고 테스트하고 지속적으로 배포하는 것을 말한다.  
CI와 CD의 차이점과 데브옵스까지 궁금하다면 [블로그 글 - DevOps와 CI/CD차이](https://sowon-dev.github.io/2020/12/04/201205devOpsandCICD/)에 쉽게 작성해두었으니 참고하면 좋다.

  
  
  

# 깃헙액션 개념

깃헙액션에는 중요한 5가지 개념이 있다.

![https://www.freecodecamp.org](https://www.freecodecamp.org/news/content/images/2022/01/build-your-first-github-action_components.png)

## 1 Events

어떤 일이 발생했는지를 지정하는 곳  
아래 예시처럼 특정한 이벤트가 일어났을때 그 후로 뭘 해야할지 wrokflows로 지정해줄 수 있다.  
e.g

  * 1) main브랜치로 머지했을때
  * 2) 커밋을 푸쉬했을때
  * 3) 이슈를 누군가 만든다면

  
  
  

## 2 Workflows

특정한 이벤트가 발생하면 어떤 걸 해야하는지 순서를 명시하는 곳.  
Workflows안에는 하나 또는 다수의 job이 있다.

  
  
  

## 3 Job

무언가를 실행하는 걸 명시하는 곳  
job안에는 쉘스크립트로 step을 만들어줄수있다.

  
  
  

## 4 Action

깃헙액션에서 제일 유용한 부분이다.  
우리가 자주 사용하는 공개적으로 오픈된 Action들이 미리 정해져 제공된다.  
npm에서 라이브러리 가져다쓰는 것처럼 깃헙액션도 동일한 것이라고 생각하면 된다.

  
  
  

## 5 Runner

Job을 실행하는 것이 바로 Runner이다.  
JOB의 갯수만큼 RUNNER가 존재하며 이들은 독립적으로 실행된다.  
러너는 VM 혹 도커컨테이너라고도 생각할 수 있다.

  
  
  

# 깃헙액션 흐름

![https://engineering.empathy.co/](https://engineering.empathy.co/content/images/size/w1000/2022/07/CI-CD-Blog-Graphic-Final_Medium_CI_CD-1200x400---1-.jpg)

#[GIT](/tags/GIT/)
