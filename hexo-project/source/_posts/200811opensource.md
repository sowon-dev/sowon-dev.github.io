---
title: "오픈소스 Git 기여순서(취소포함)"
date: 2020-08-10 15:00:00
tags:
  - "TIL"
  - "GIT"
categories:
  - Reflections
  - 오픈소스컨트리뷰톤2020
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">오픈소스 Git 기여순서(취소포함)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * 워드나 한글등의 일반 파일들은 저장이라는 기능으로 한꺼번에 저장을 한다.</p>
</div>

<!-- more -->

## GitHub에서 기여할 소스의 레포를 fork하여 내 레포에 생성하기

  * 클라우드상에서 이루어지는 부분

## `git clone 내fork레포주소`

  * `.git`파일이 자동 생성되며 커밋정보나 이력이 저장됨.

### 아래 3가지의 차이는?

  * fork : 클라우드upstream repo와 서버your fork사이에서 이루어짐. 즉 클라우드상에서만 이루어짐
  * clone: 서버에서 내 로컬로 받아오는 것
  * copy: clone과 동일하다고 생각하면 됨

```ps
git clone 내fork레포주소
```

## `code .`

  * 주력 에디터로 열기

## 열코~ : 작업하기

## `git status`

  * bash에서 `git status` 명령어를 입력하면 내가 수정한 부분이 modified 표시와 함께 빨간색으로 표시됨
  * modified 취소하고싶으면?

```ps
git checkout unmodified하고싶은_파일명
```

## `git add`의 의미

  * 워드나 한글등의 일반 파일들은 `저장`이라는 기능으로 한꺼번에 저장을 한다.
  * 하지만 프로그래머는 소스코드 기능개발중 버그를 유발하는 코드를 수정해야한다. 
  * `git add`의 의미 : 내가 원하는 것만 커밋하기 위해 add를 한다
  * git add를 취소하고싶으면?

```ps
git reset add취소하고싶은_파일명
```

## `git commit -m '의미있는 커밋명'`

  * commit의 단위 : 논리적 변경이 있을 때 1개를 만든다.
  * commit을 잘 나누는 개발자가 능력있는 개발자이다.
  * commit을 잘못 쳐서 지우고 싶다면?

```ps
//git reset을 쓰면되는데 옵션이 3가지임.
--soft : commit후의 Unmodified에서 commit전의 staged상태로 되돌아가는 옵션
--mixed : 기본옵션. commit후의 Unmodified에서 commit전의 modified상태로 되돌아가는 옵션
--hard : commit후의 Unmodified에서 commit 전의 Unmodified로 되돌아가는 옵션

//잘못된 가장 최근의 커밋 한개를 지우고 싶을때 예시
git reset HEAD~1
```

### 불필요한 커밋을 합치려면 또는 큰 커밋을 작은 커밋단위로 쪼개려면?

  * rebase

## `git push 저장소명 브랜치명`

  * 어느 저장소의 어떤 브랜치에 push할지를 잘 체크해야한다.
  * `git remote -v` 에서 origin 하나만 있을 경우 `git push`하면 `git push origin master`와 동일한 결과가 된다.

```ps
//예시
git push origin master
```

## 깃헙에서 내fork레포의 `Pull request`버튼 클릭

  * 실제 현업에선 절대 master로 PR보내는 것이 금지. 대부분 develop등 개발전용 브랜치에 PR보내도록 한다.
  * PR 제목도 회사규칙에 따라 잘 남겨야한다. 
    * 예시 : [주제제목] 작업내용 
  * PR 메세지 남길 때 체크박스 체크하기 원하려면 [X] : 공백없어야 함.
  * PR을 보내면 공식레포메니저에게 알림이메일이 감

## 공식레포메니저는 `Jenkins`서버

  * github에 변경내역을 webhook으로 감지가 되면 jenkis서버가 실행되고 build server가 연동되어 변경내역이 서버에 올라간다

#[TIL](/tags/TIL/)[GIT](/tags/GIT/)
