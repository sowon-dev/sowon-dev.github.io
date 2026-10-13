---
title: "rebase로 commit 추가,수정,삭제하기"
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
  <p class="tldr-desc">rebase로 commit 추가,수정,삭제하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    핵심 설정과 구현 코드를 단계별로 파악하여 상황에 맞게 유연하게 활용할 수 있다.</p>
</div>

<!-- more -->

## rebase 리베이스

```bash
# rebase -i :인터렉트 즉, 되감기를 하겠다는 의미
$ git rebase -i --root

# 감았던 rebase 풀기
$ git rebase --continue

# rebase 취소하는 것
$ git rebase --abort

# rebase 초기화
# rebase
$ git reset --hard HEAD~1
$ git reset --hard origin/master

# vi편집기 나가기
:wq -> write and quit(저장하고 나가기의 줄임말)
```

  
  
  

## 리베이스 예시 : 커밋추가

가장 오래된 것부터 두번째 커밋 이후에 새로운 커밋 3개 추가하기

```bash
# 리베이스감기 : 오래된 것부터 두번째 커밋에 pick을 edit으로 변경
$ git rebase -i --root

# 새로운 커밋 3개 추가
$ touch 새로운파일1.txt
$ git add 새로운파일1.txt
$ git commit -n "Added 새로운파일1"

$ touch 새로운파일2.txt
$ git add 새로운파일2.txt
$ git commit -n "Added 새로운파일2"

$ touch 새로운파일3.txt
$ git add 새로운파일3.txt
$ git commit -n "Added 새로운파일3"

# HEAD위치 확인
$ git log --oneline

# 리베이스풀기
$ git rebase --continue

# 커밋이 잘 추가되었는지 결과확인
$ git shortlog
$ git log --oneline
$ gitk
```

  
  
  

## 리베이스 예시 : 커밋수정

위에서 추가한 커밋 1번2번3번 중에 2번과 3번을 커밋을 한 개로 합치고 싶다면?

  1. `rebase -i --root`에서 커밋3번에 pick을 edit로 변경해야한다.
  2. 그 뒤 커밋 3번을 `reset --soft HEAD~1`를 해주면 커밋에서는 사라졌지만 파일은 남아있다. 
  3. `commit --amend`를 해주면 커밋3번이 커밋2번에 흡수된다.
  4. `show 커밋ID`를 검색하면 2번과 3번이 합쳐진것을 볼 수 있다.

```bash
# 리베이스감기
$ git rebase -i --root

# 위의 세번째커밋에 pick을  edit으로 변경해준다.

# HEAD위치 확인
$ git log --oneline

# 세번째커밋삭제
$ git reset --soft HEAD~1
$ git status

# 두번째커밋에 흡수 합치기
$ git commit --amend
$ git show 커밋ID

# 리베이스풀기
$ git rebase --continue

# 커밋이 잘 수정되었는지 결과확인
$ git log --oneline
$ git show 합쳐진commitID
```

  
  
  

## 리베이스 예시 : 커밋삭제

가장 오래된 것부터 두번째 커밋 “Add secondCommit” 삭제하려면?

```bash
$ git rebase -1 -root
# 두번째 pick Add secondCommit을 edit으로 바꿈
$ git status
$ git reset --hard HEAD~1
$ git rebase --continue

# 커밋이 잘 삭제되었는지 결과확인
$ git log --oneline
$ git shortlog
$ gitk
```

#[TIL](/tags/TIL/)[GIT](/tags/GIT/)
