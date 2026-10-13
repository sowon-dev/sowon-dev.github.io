---
title: "내 로컬저장소를 원격저장소를 반영하여 최신 베이스만들기"
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
  <p class="tldr-desc">내 로컬저장소를 원격저장소를 반영하여 최신 베이스만들기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    Git rebase after git fetch | 내 커밋아래에 remote의 커밋이 쌓이고 그 위에 내 커밋이 얹음 | master브랜치에 사용하지말것을 적용할 수 있다.</p>
</div>

<!-- more -->

## 내 로컬저장소를 원격저장소를 반영하여 최신 베이스만들기

세가지 방법이 있다.

명령어 | 결과 | 특징  
---|---|---  
Git pull | 내 로컬머신이 remote저장소베이스 그대로 갱신(브랜치까지 싹 다) | 로컬과 remote변경사항 확인불가  
Git merge after git fetch | fetch후 충돌/차이점 확인 후 내 로컬머신에 갱신, 머지커밋생성됨 | 로컬과 remote변경사항 확인가능  
Git rebase after git fetch | 내 커밋아래에 remote의 커밋이 쌓이고 그 위에 내 커밋이 얹음 | master브랜치에 사용하지말것  
  
![https://tapaswenipathak.blog/2016/02/15/git-fetch-merge-git-fetch-rebase-git-pull/](https://tapaswenipathak.files.wordpress.com/2016/02/xwvzt.png)

![https://medium.com/datadriveninvestor/git-rebase-vs-merge-cc5199edd77c](https://miro.medium.com/max/700/1*pzT4KMiZDOFsMOKH-cJjfQ.png)

  
  
  

## 공통 설정 두가지

### `git remote -v`

  * origin 저장소만 있다면 최신레포를 가져올 upstream저장소를 연결해줘야한다.
  * origin과 upstream 두개가 있어야하며 
    * origin: 내 아이디가 있는 내fork한 레포주소.
    * upstream: 최신레포를 가져 올 공식레포주소.
  * origin 저장소 주소 변경하고싶다면?

```ps
gir remote -v
git remote set-url origin 변경할주소
```

  
  
  

### `git remote add 최신반영하고싶은_저장소이름 최신반영하고싶은_레포주소`

```ps
git remote add upstream 공식레포주소
```

  
  
  

## 최신베이스만들기 첫번째 방법 : pull

  * fetch + merge = pull

```ps
git pull upstream master
```

  
  
  

## 최신베이스만들기 두번째 방법 : fetch + rebase

  1. `git fetch 최신반영하고싶은_저장소이름 가져올브랜치명`
     * fetch는 임시 저장해놓은 것이라서 fetch했다고 내 로컬의 브랜치에 반영되지 않는다 -> fetch분과 내 로컬 브랜치를 merge해줘야한다.
     * 보통 upstream을 많이 사용함. upstream말고 다른 저장소명써도 상관없음.
     * fetch를 쓰는 이유 : 내 로컬저장소와 원격저장소르 비교하여 차이점을 볼 수 있기때문
  2. `git rebase upstream/master` : 임시저장분(fetch)을 내 로컬머신의 커밋 아래로 저장해야한다.
  3. `git log` : 머지커밋이 생성안됨. 신규 커밋 없음을 확인할 수 있다.
  4. `git push origin 브랜치명` : 최신베이스가 반영된 내 로컬의 데이터를 깃헙 내fork한레포에 반영하고싶다면 git push하면된다

```plain
//상황
//현재 체크아웃한 브랜치는 fix-blah이고 updatream저장소의 master는 최신베이스이다. 
//fix-blah의 베이스를 master의 베이스로 만들고 싶다
git checkout fix-blah

//1. upstream의 master브랜치에 있는 최신 변경분을 가져오다는 의미
git fetch upstream master

//2. 현재 체크아웃된 fix-blah의 베이스를 upstream의 master베이스로 바꾸겠다는 의미
git rebase upstream/master

//3. 로그에 rebase 커밋이 남지않음.
git log

//4. 최신베이스가 반영된 내 로컬의 데이터를 깃헙 내fork한레포에 반영하고싶을때
git push origin fix-blah
```

  
  
  

## 최신베이스만들기 세번째 방법 : fetch + merge

  1. `git fetch 최신반영하고싶은_저장소이름 가져올브랜치명`
     * fetch는 임시 저장해놓은 것이라서 fetch했다고 내 로컬의 master브랜치에 반영되지 않는다 -> fetch분과 내 로컬 master브랜치를 merge해줘야한다.
     * 보통 upstream을 많이 사용함. upstream말고 다른 저장소명써도 상관없음.
  2. `git merge upstream master`
     * 임시저장분(fetch)을 내 로컬머신으로 저장하기위해서는 master브랜치로 가야한다
     * 임시저장분(fetch)이 내 로컬머신의 브랜치로 저장된다.
  3. `git log` : 머지커밋이 생성된걸 확인 할 수 있음
  4. `git push origin 브랜치명` : 최신베이스가 반영된 내 로컬의 데이터를 깃헙 내fork한레포에 반영하고싶다면 git push하면된다

```plain
//1. upstream의 master브랜치에 있는 최신 변경분을 가져오다는 의미
git fetch upstream master

//2.  임시저장분(fetch)이 내 로컬머신의 브랜치로 저장
git checkout master
git merge upstream/master

//3. log에 merge커밋이 남음
git log

//4. 최신베이스가 반영된 내 로컬의 데이터를 깃헙 내fork한레포에 반영하고싶을때
git push origin master
```

  
  
  

## 최신베이스 유지를 위해 `pull`이 아닌 `fetch > rebase`를 해야하는 이유

  1. 깃헙저장소 master를 로컬 master로 pull받아온다.
  2. 로컬에서 작업 하는 동안 깃헙 저장소에 새로운 커밋이 추가되었다.
  3. 여기서 내 로컬과 원격 저장소의 싱크를 맞추고싶다면 즉, 원격의 새로운 커밋을 내 로컬에 반영시키고싶다면 **무조건 리베이스해야한다**
  4. git pull하면 나중에 커밋한 내용을 합칠 수 없다.
  5. git fetch upstream master -> git rebase upstream/master 하면 싱크를 맞출 수 있다. 
  6. 리베이스는 혼자만 하는 브랜치에서만 작업하는 것이 좋다.
  7. 커밋을 하나로 합칠때 interactive rebase 사용해야한다.

#[TIL](/tags/TIL/)[GIT](/tags/GIT/)
