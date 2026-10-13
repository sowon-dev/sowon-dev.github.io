---
title: "Git config(깃설정), 오픈소스 참여를 위한 GIT 순서 (팀협업)"
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
  <p class="tldr-desc">Git config(깃설정), 오픈소스 참여를 위한 GIT 순서 (팀협업)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * 원하는 편집기 설정가능 : vim, emacs, nano, notepad 등을 적용할 수 있다.</p>
</div>

<!-- more -->

## 깃이란?

  * git은 텍스트파일로 변화내역(역사)를 관리하는 것
  * [참고링크 : git 버전관리](https://sowon-dev.github.io/2020/06/19/200619python/)

  
  
  

## 오픈소스 개발 참여를 위한 Git config(깃설정)

### Github ID/PW 캐싱데이터 삭제

  * 삭제해도 문제없음
  * 목적 : 다른 github계정과 충돌방지

```bash
$ git config --global --unset credential.helper
$ git config --system --unset credential.helper
```

### 내 github계정연결

  * 차후 소스코드 커밋파일에 저자정보에 기입됨

```bash
$ git config --global user.email "본인이메일주소"
$ git config --global user.name "본인이름"
```

```bash
$ git config --global user.email "본인이메일주소"
$ git config --global user.name "본인이름"
```

### 소스코드 수정할 기본 편집기 설정

  * 원하는 편집기 설정가능 : vim, emacs, nano, notepad 등

```bash
# 예시 : nano편집기로 설정
$ git config --global core.editor nano

# nano편집기 사용시 설치필요
$ sudo apt install -y nano
```

### git 설정 내용 확인

  * 수정원할시 위의 명령어로 재입력하면 덮어쓰기됨.

```bash
$ git config --list
```

  
  
  

## 오픈소스 참여를 위한 GIT 순서 (팀협업)

오픈소스에 참여하기 위해서는 공식 오픈소스 프로젝트 레포지토리에서 프로젝트를 복사하여 내 로컬에서 사용할 수 있게해야한다.

### 공식 레포에 가서 Fork버튼을 누른다.

### Fork해온 레포의 code를 클릭하여 `Clone with HTTPS`를 복사한다.

### git bash 또는 IDE의 터미널을 연다.

### 아래 명령어를 입력한다.

```bash
# 오픈소스 프로젝트 소스코드 준비
$ git clone 복사한 https://github.com/본인깃허브ID/fork한프로젝트명.git
$ cd fork완료한폴더 -> (master) 라는 브랜치명이 생성됨. 

# remote저장소에 공식레포 upstream으로 준비
$ git remote add upstream 공식레포주소
```

### 코딩을 하기전 최신base로 갱신하기

내가 clone을 해온 뒤 공식레포 base가 변경될수도 있다.  
따라서 작업전 공식레포에서 최신base를 내 fork레포로 가져와야한다  
로컬저장소를 최신으로 만드는 방법에는 두가지가 있다. pull과 fetch이다.

```bash
# 1. pull사용
# upstream(팀프로젝트)의 최신버전을 가져오기.
$ git pull upstream 레포주소

# 가져온 최신버전을 내 fork한 저장소에 저장하기 
$ git push origin master

# 2. fetch사용
# upstream(팀프로젝트)에서 새로운 commit가져오기
$ git fetch upstream

# 가져온 upstream을 내 fork저장소의 master브랜치에 병합하기
$ git merge upstream/master

# 병합된 내역을 내 fork저장소에 푸쉬하기
$ git push origin master
```

[ Git 협업하기 : Upstream Merge 후, 최신상태 Pull 받기](https://medium.com/@yms0214/git-%ED%98%91%EC%97%85%ED%95%98%EA%B8%B0-upstream-merge-%ED%9B%84-%EC%B5%9C%EC%8B%A0%EC%83%81%ED%83%9C-pull-%EB%B0%9B%EA%B8%B0-213bc2c1c249)

### 코딩 후 내 fork레포에 commit하기.

내 fork레포에만 저장된다.

```bash
# 1. 내가 수정한 파일 add하기
$ git add 내가수정한파일명

# 2. add상태확인
$ git status

# 3. commit하기
$ git commit -m "커밋이유 자세히"

# 4. 내가 작성한 커밋 확인하기
# q키 누르면 나감.
$ git show

# 5. 현재 작업 브랜치 확인
$ git branch

# 6. 내 fork저장소에 업로드하기
$ git push origin 브랜치명
```

### 로컬저장소 최신버전으로 갱신하기

현재 내 커밋은 내 fork레포에만 있다.  
내가 수정한 코드를 공식 레포에 올려달라고(Merge) 요청해야한다(Pull request).  
하지만 내가 코드수정하는 동안 또다시 공식레포의 base가 달라질수있다.  
따라서 pr전에 merge충돌을 방지하기 위해서 rebase한 뒤 내 커밋을 얹어서 함께 push해야한다.

  * fetch : 최신 base가져오기
  * rebase : 
    * rewind : 내 커밋전의 과거시점으로 감
    * 가져온 fetch를 그 위에 올린다(다른사람의 PR한 커밋포함) 
    * 그 위에 내 커밋을 올린다 (이때 다른사람의 커밋과 내커밋이 충돌날수있다)
    * 자동PR됨

```bash
# 원격저장소확인
$ git remote -v

# 공식 upstream 저장소에서 최신 commit history가져오기
$ git fetch upstream master

# 최신 comit history 기준으로 베이스 갱신 = rebase 감기
$ git rebase upstream/master

# 충돌 상황확인하기
$ git status
$ git diff

# 충돌부분 수정후 add하기
$ vi 수정할려는파일명(GIT BASH상에서) 또는 IDE상에서는 패널에 파일열어서 수정가능
$ git add 수정할려는파일명

# rebase 풀기
$ git rebase --continue

# 내 fork한 레포에 최신 master브랜치에 가져온 commit내용 갱신하기
$ git checkout master
$ git reset --hard upstream/master
$ git push origin master -f
```

### 공식저장소에 PR하기

```bash
# PR 하기 두가지방법
# 첫번째 : 추천방법
$ git push origin 브랜치명
# PR 하기 예시 : master 브랜치인 겨우
$ git push origin master -f

# 두번째 : PR시 force push(강제푸시)사용
# 두번째 방법을 이용하면 내 fork한 저장소가 수정되면서 PR자동갱신된다. 따라서 아래 7번8번을 생략할수있다.
# 강제푸시이므로 팀프로젝트에 이용시 꼬일 수 있다
$ git push --force origin master
```

### upstream저장소의 pull request게시판에서 회색 merge버튼이 초록색으로 변했는지 확인후 maintainer에게 merge요청하기

  
  
  

## fetch 와 pull 차이

  * pull은 하는 순간 merge가 된다.
  * fetch + merge = pull

  
  
  

## force push

  * fork한 저장소가 꼬인 경우는 로컬에서 잘 정리해서 force push(강제푸시)를 쓰면된다. 나혼자 쓰니까 괜찬.
  * 하지만 다같이쓰는 저장소는 절대 force를 쓰면 안된다.

  
  
  

## origin의 의미

> 수업중 질문 : origin은 master처럼 기본적으로 지정된 폴더 이름인가요? origin이 어떤 의미를 가지는지 알고싶습니다  
> 답변 : origin이나 upstream은 remote repository에 붙이는 이름표같은거라고 생각하시면되요. 그런데 대부분의 튜토리얼들이 fork뜬 저장소는 origin으로, 원본 저장소는 upstream이라고 식별한걸 가정하고 진행되기때문에 미리 알아두시는게 좋구요

#[TIL](/tags/TIL/)[GIT](/tags/GIT/)
