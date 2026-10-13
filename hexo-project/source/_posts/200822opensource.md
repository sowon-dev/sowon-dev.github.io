---
title: "오픈소스컨트리뷰톤 온라인미팅5 후기 : GIT 케이스 스터디"
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
  <p class="tldr-desc">'오픈소스컨트리뷰톤 온라인미팅5 후기 : GIT 케이스 스터디'에 참여하고 주요 발표 내용과 배운 점을 정리한 글이다.
    * 개발자도구 열고 (f12) 새로고침 버튼에서 마우스 오른쪽 클릭하면 3개 버튼 -> 강력 새로고침 또는 캐시비우고 강력 새로고침을 확인했다.</p>
</div>

<!-- more -->

## 두번째 브랜치 생성하고 커밋했는데 첫번째 브랜치의 커밋이 함께 들어가 있을때

> 두개의 PR을 날렸는데 첫번째는 마스터, 두번째는 새로운 브랜치에서 했었는데요. 두번째에 새로운 브랜치에서 날린 커밋이 첫번째 마스터 아래로 들어갔더라구요

  * 원인 : master브랜치에서 커밋 -> PR -> 다시 master브랜치에서 새로운 브랜치 생성했기 때문!
    * master에서 이미 PR 날린 상태에서 branch를 만들면 새로만든 branch에도 PR보낸게 적용 됨.
  * 해결 방법 2가지
    1. HEAD를 뒤로 돌린 뒤 새로운 브랜치 생성.
    2. 커밋을 체크아웃한 뒤 새로운 브랜치 생성.

  
  
  

## rebase를 사용해 브랜치를 최신화 해주세요. 머지 커밋을 없애주시기 바랍니다에 대한 해결

<https://github.com/javascript-tutorial/ko.javascript.info/pull/694>

  1. 기존 작업중인 브랜치를 임시저장하고 빠져나옴 : git status > git stash
  2. git 머지커밋 삭제하기 : git log > q > git reset HEAD^ (git reset HEAD~1) > git push 오류남 > git push -f > upstream깃헙 > 머지커밋 사라지고 원하는 커밋만 남음 > 해결!

  
  
  

## 팁 : CSS 변경 후 실시간으로 반영이 안될때

  * 원인 : CSS 캐쉬때문에 안나옴
  * empty cache and hard reload 진행
  * 개발자도구 열고 (f12) 새로고침 버튼에서 마우스 오른쪽 클릭하면 3개 버튼 -> 강력 새로고침 또는 캐시비우고 강력 새로고침
    * 단축키 : ctrl + shift + r

#[TIL](/tags/TIL/)[GIT](/tags/GIT/)
