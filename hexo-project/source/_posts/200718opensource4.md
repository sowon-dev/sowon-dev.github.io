---
title: "add 취소, commit 명령어 수정, commit 취소, 라이센스 commit 생성,"
date: 2020-07-17 15:00:00
tags:
  - "TIL"
  - "GIT"
categories:
  - Reflections
  - 오픈소스컨트리뷰톤2020
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">add 취소, commit 명령어 수정, commit 취소, 라이센스 commit 생성,의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * 어떤 경우에 사용할까?을 적용할 수 있다.</p>
</div>

<!-- more -->

## add 명령 취소하기

```bash
$ git add 파일명
# git status에서 add 되어있는지 확인 (초록색)
$ git status 

# add 명령 취소
$ git reset

# git status에서 add 취소되어있는지 확인 (빨간색)
$ git status
```

  
  
  

## commit 메세지 수정하기 = commit amend

  * 최신 히스토리 기준으로 커밋명 수정 가능
  * 수정하면 커밋ID는 바뀌게 된다

```bash
$ git commit --amend
```

## commit 삭제하기

커밋이 크면 어떻게 나누는게 적당할까? 그리고 커밋이 크다는 건 어느정도를 말할까?

  * 정답 : 테스트의 단위로 나누는 것이 좋다.

```bash
$ git add 파일명
$ git commit -m "커밋메세지입력"

# 생성한 커밋정보확인
$ git show
$ git log --oneline -1

# commit 정보삭제
# 예시 : 가장 최근 commit 한개 삭제하기
# HEAD위치 확인
$ git log --oneline
# HEAD의 커밋 한개 삭제
$ git reset --hard HEAD~1
# 삭제 후 최신 commit 확인
$ git log --oneline -1
```

## 라이센스넣어서 커밋하기

  * 일반 커밋이외에 라이센스를 넣어서 커밋을 할 수 있다.
  * 어떤 경우에 사용할까? 
    * 라이센스를 정확히 이해했을때 
    * 오픈소스 커밋시 의무사항인 곳도 있다.
    * 자신의 라이센스 권리를 주장할 수 있다.

```bash
라이센스를 이해하고 넣는 속성 `-sm`.
$ git commit -sm "커밋명"
```

#[TIL](/tags/TIL/)[GIT](/tags/GIT/)
