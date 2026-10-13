---
title: "Git branch 기초"
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
  <p class="tldr-desc">Git branch 기초의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * -d는 정상적인 상황일 때 사용가능한 옵션을 적용할 수 있다.</p>
</div>

<!-- more -->

## 브랜치(Branch)활용

  * 브랜치 : 같은 폴더인데 다른 세상처럼 이용할 수 있음
  * 기본 브랜치 : master
  * 브랜치생성 : 브랜치네이밍을 할때 꼭 작업키워드에 맞출것

```bash
$ git checkout -b 브랜치명

# 예시 : fix-mnist브랜치 만들기
$ git checkout -b fix-mnist
```

  * 브랜치 master로 변경

```bash
$ git checkout 연결할브랜치명

# 예시 : 현재 작업중인 브랜치를 master브랜치로 변경
$ git checkout master
```

  * 브랜치삭제
    * 속성 `-d`와 `-D`의 차이
      * `-d`는 정상적인 상황일 때 사용가능한 옵션
      * `-D`는 강제로 처리하게 하는 옵션

```bash
# 추가생성한 브랜치 삭제를 위해 master브랜치로 이동
$ git checkout master
# 브랜치삭제
$ git branch -d fix-mnist
```

  * 어떤 브랜치에 접속되어있는지 확인
    * git status는 정말 다양한 정보를 가지고 있는데 그 중 현재 내가 작업진행중인 브랜치를 알려준다.

```bash
$ git status
```

#[TIL](/tags/TIL/)[GIT](/tags/GIT/)
