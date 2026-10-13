---
title: "Git flow 전략"
date: 2020-08-21 15:00:00
tags:
  - "TIL"
  - "GIT"
categories:
  - Reflections
  - 오픈소스컨트리뷰톤2020
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Git flow 전략의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * 다음 출시 버전과 관련된 개발자분들은 develop브랜치에 병합하는 전략을 사용.</p>
</div>

<!-- more -->

## Git flow 전략

  * master : 제품으로 출시될 수 있는 브랜치
  * develop : 다음 출시 버전을 개발하는 브랜치
    * 다음 출시 버전과 관련된 개발자분들은 develop브랜치에 병합하는 전략을 사용.
    * 상시로 버그를 수정한 커밋들이 추가
  * feature : 기능을 개발하는 브랜치 / 새로운 기능 개발하는 브랜치
  * release : 이번 출시 버전을 준비하는 브랜치
  * hotfix : 출시 버전에서 발생한 버그를 수정 하는 브랜치

  
  
  

## 일반 사용자에게 프로토타입을 공개하지 않는다면?

  * 브랜치 master, develop, feature브랜치 이 세 브랜치 정도만 사용해도 충분.
  * 팁 : master와 develop은 ci서버를 따로 구성하여 계속 빌드가 될 수있게끔 + develop브랜치에 자주 병합 필수.

  
  
  

## 가장 유명한 git-flow전략이미지와 설명

  * 항상 유지되는 브랜치 : master, develop
  * 일정 기간 동안만 유지되는 보조 브랜치들 : feature, release, hotfix

![https://woowabros.github.io/experience/2017/10/30/baemin-mobile-git-branch-strategy.html](https://woowabros.github.io/img/2017-10-30/git-flow_overall_graph.png)

  1. master브랜치르 생성한다
  2. master브랜치에서 develop브랜치를 생성한다. 여기에는 상시로 버그 수정한 커밋을 추가
  3. 혹시 새로운 기능 추가 작업이 있다면 develop브랜치에서 feature브랜치를 생성 -> 기능 추가 작업이 완료되었다면 feature브랜치는 develop브랜치로 머지
  4. QA(Quality Assurance)를 위해 develop브랜치에서 relase브랜치 생성 -> QA를 진행하면서 발생한 버그를 relase브랜치에서 수정.
     * QA란 제품개발단계에서 품질보증. 결함을 예방.
     * QA의 모적 : 고품질 제품확보
  5. QA를 무사히 통화 -> relase브랜치를 master와 develop브랜치에 머지
  6. master브랜치에서 버전 태그를 추가.

  * [참고링크 : 우아한형제들의 git flow전략](https://woowabros.github.io/experience/2017/10/30/baemin-mobile-git-branch-strategy.html)

#[TIL](/tags/TIL/)[GIT](/tags/GIT/)
