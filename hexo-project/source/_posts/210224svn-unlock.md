---
title: "SVN lock 해제하기, commit시 already lock 충돌 해결하기"
date: 2021-02-23 19:43:32
tags:
  - "Eclipse"
  - "SVN"
  - "오류일지"
categories:
  - Reflections
  - Version control
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">commit을 치는데 계속 svn 충돌문제가 발생했다. console을 확인해보니 already lock이라는 에러메세지가 보였다. 이로 인해 commit도 update도 되지 않았다.
    문제 발생 원인을 생각해보니 최근 소스파일을 수정하고 commit 명령어를 날렸는데 그 사이 svn서버가 재시작하게된 일이있었다.</p>
</div>

<!-- more -->

## 문제상황

commit을 치는데 계속 svn 충돌문제가 발생했다. console을 확인해보니 already lock이라는 에러메세지가 보였다. 이로 인해 commit도 update도 되지 않았다.  
문제 발생 원인을 생각해보니 최근 소스파일을 수정하고 commit 명령어를 날렸는데 그 사이 svn서버가 재시작하게된 일이있었다.  
이때문에 commit은 svn서버에 정상반영되었으나 내 로컬에는 해당 commit이 반영되지않는 이상한 일있었다. svn의 모든 기능이 잠겨버리는 바람에 해결해야만했다.  
해결하고보니 간단한 문제였다. 미리 겁먹지말자!

[SVN official doc](http://svnbook.red-bean.com/en/1.8/svn.advanced.locking.html)에는 Harry and Sally의 예시를 통해 어떤 경우에 LOCK이 발생하는 지 설명해놓았다.  
다양한 상황에 따라 LOCK발생하지만 딱 한마디로 요약해보자면 clashing commits(커밋충돌)을 방지하기 위해서이다.

  
  
  

## 해결방법

  1. [sqlite browser사이트에서 DB Browser for SQLite를](https://sqlitebrowser.org/) 자신의 상황에 맞게 다운로드한다.  
나는 윈도우 64비트를 사용중이므로 가장 최신 버전중에 설치가 필요없는 파일을 다운로드했다.

![](/img/210224svn-unlock.PNG)

  2. `DB Browser for SQLite.exe` 실행  
설치된 파일안의 DB Browser for SQLite.exe 파일을 실행한다.

  3. `데이터베이스 열기`를 클릭

  4. 사용중인 프로젝트안의 `wc.db` 파일 열기  
나의 경우 D:\workspace\프로젝트명.svn 안의 wc.db 파일을 열었다.

  5. SQL실행 탭에서 unlock명령어 실행  
lock이 생성된 경우 데이터보기 탭에서 WC_LOCK 테이블과 WORK_QUEUE테이블에 데이터가 존재하는 것을 확인할 수 있다.  
svn에 이상이 없는경우 두 테이블에 데이터가 존재하지 않는다.  
두 테이블에 데이터가 존재하는 경우 SQL실행탭을 클릭하여 아래와 같이 명령어를 실행한다.

```sql
DELETE FROM WC_LOCK
DELETE FROM WORK_QUEUE;
```

![](/img/210224svn-unlock2.PNG)

이제 이클립스로 돌아가서 commit이나 update를 하면 svn이 정상적으로 작동된다.  
해결!

#[Eclipse](/tags/Eclipse/)[SVN](/tags/SVN/)[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)
