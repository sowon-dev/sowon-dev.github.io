---
title: "[이클립스/STS] // TODO 주석말고 다른 거, 뭐 없을까?"
date: 2021-05-12 16:22:55
tags:
  - "Eclipse"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">// TODO 주석말고 다른 거, 뭐 없을까?의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    기능구현을 하다보면 시간에 쫓기거나 우선순위때문에 잠깐 미뤄둬야 할 일들이 있다.</p>
</div>

<!-- more -->

기능구현을 하다보면 시간에 쫓기거나 우선순위때문에 잠깐 미뤄둬야 할 일들이 있다.  
모든 걸 다 기억해놓을 수도 없고, 그냥 주석을 쓰면 눈에 잘 띄지않는다.  
이때 도움이 되는 것이 Task tag 기능이다.  
이클립스나 STS에 자체적으로 있는 기능으로 하단에 Tasks 탭을 확인할 수 있다.

Task tag로 메모해놓으면 바로 확인할 수 있고 클릭시 해당 소스코드로 바로 이동하여 정말 편하다.

![https://dzone.com/articles/to-do-lists-with-eclipse-tasks-view](https://mcuoneclipse.files.wordpress.com/2016/05/markers-ini-source-view.png)

또한 해당 소스코드 왼쪽편에 노트와 연필모양으로 표시까지 해준다

  
  
  

## Tasks 탭 열기

Tasks탭이 하단에 없는 경우 아래 경로를 통해서 볼 수 있다.

  * 이클립스나 STS -> Window -> Show View -> Tasks

  
  
  

## Task tag 종류

기본적으로 3종류가 있다.

  * TODO : 좀더 최적화시키고 리팩토링시킬 수 있을만한 구석이 있을때. 미래에 뭔가 의미있는 작업을 더 해야 할 필요성을 느낄때.
  * FIXME : 문제가 있는것이 확실하지만, 그걸 지금 당장 그것을 수정할 필요는 없을 때.
  * XXX : 해당 부분에 대해서는 더 생각해볼 필요성이 있을 때. 또는 해당 부분에 질문이 생길 때. 또는 코드에서 문제가 일어날만한 부분을 강조 표기할때. 완벽하게 정확히 구현되지 않은 부분이 있을 때. 나중에 고쳐야만하는 부분일 때. 주로 팀보단 자신을 위한 용도로 사용.

예시

  * TODO: How about auto-correcting small spelling errors?
  * FIXME: This won’t work if the file is missing.
  * XXX: This method badly needs refactoring: should switch by core type.

## 커스텀 tag 추가하기

기존 3종태그뿐만아니라 나만의 커스텀태그를 추가할 수 있다.

  * Window -> Preferences -> Java -> Compiler -> Task Tags

New와 Edit, Remove를 이용하여 태스크 태그를 추가, 수정,삭제할 수 있고 각 우선순위도 상/중/하로 설정할 수 있다.

![https://dzone.com/articles/to-do-lists-with-eclipse-tasks-view](https://mcuoneclipse.files.wordpress.com/2016/05/task-tag-settings.png)

  
  
  

## 출처

  * <https://dzone.com/articles/to-do-lists-with-eclipse-tasks-view>
  * <http://egloos.zum.com/rucaus/v/2455594>

#[Eclipse](/tags/Eclipse/)
