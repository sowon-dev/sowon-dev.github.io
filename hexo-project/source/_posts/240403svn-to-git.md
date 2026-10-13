---
title: "SVN에서 사내 GITLAB으로 변경하기(ft.migration)"
date: 2024-04-02 20:29:32
tags:
  - "GIT"
  - "SVN"
categories:
  - Reflections
  - Version control
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">SVN에서 사내 GITLAB으로 변경하기(ft.migration)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    현재 SVN을 사용하고있는데 사내 GITLAB서버로 변경하는 업무를 맡게되었다.</p>
</div>

<!-- more -->

현재 SVN을 사용하고있는데 사내 GITLAB서버로 변경하는 업무를 맡게되었다.  
GITHUB는 익숙하지만 GITLAB은 익숙하지않아 초반에 삽질한 시간이 있었다.

# 1 gitlab에 new 프로젝트 생성

사내 gitlab 원격서버에 신규 프로젝트를 생성한다.

  
  
  

# 2 gitlab에 SSH키를 등록하기

SSH 키가 등록되지않으면 COMMIT, PUSH등을 못한다.

  1. SSH 키 생성은 cmd / gitbash 에서 진행가능하다. 

```bash
$ ssh-keygen -t rsa -b 4096 -C "sowon-dev@example.com"
```

암호 설정은 선택 사항으로 암호설정을 원하지 않는다면 Enter키를 계속 누르면 된다.

  2. 사용자 홈 디렉토리의 .ssh 폴더에 id_rsa (개인 키) 및 id_rsa.pub (공개 키) 총 2개의 파일이 생성된다.

  3. SSH 키 읽기 

```bash
$ cat id_rsa.pub
```

위 명령어로 공개키를 콘솔을 통해서 확인할 수 있다.  
복사해서 사내 gitlab 원격서버에 신규 프로젝트에서 계정별로 `SSH 키 등록`에 붙여넣는다.

  
  
  

# 3 로컬에 gitlab환경조성

gitlab의 code에서 `Clone with HTTP`로 http://아이피/testprjt.git 를 clone하여 로컬에 환경 조성

  
  
  

# 4 SVN 커밋 살리기위한 user.txt 파일 만들기

원하는 곳에 users.txt 파일에 다음과 같은 내용을 작성한다

```plain
user1 = user1 <user1@email.com>
user2 = user2 <user2@email.com>
.
.
.
```

  
  
  

# 5 svn을 git으로 clone하기
    
    
    git svn clone <SVN 저장소 URL> --no-metadata -A D:/workspace/svn-gitlab/users.txt D:/workspace/svn-gitlab
    cd D:/workspace/svn-gitlab
    git remote add origin <gitlab의 원격 저장소 URL>
    git pull origin main --allow-unrelated-histories
    git push -u origin main

여기서 절대경로 D:/workspace/svn-gitlab는 gitlab 로컬저장소경로이다.

  
  
  

# 회사에선 왜 GitLab을 쓰라고 할까?

가장 근본적인 질문이었다.  
SVN은 중앙집중 버전 관리 시스템이고 Git은 분산 버전 관리 시스템이다.  
중앙집중 버전 관리 시스템은 편하지만 commit한 내용에 실수가 있을 시에 서버에(다른 개발자에게) 바로 영향을 미치게 되고 만약 중앙 서버에 문제가 생기면 협업 불가능해진다.  
그렇다면 익숙한 GitHub보다 왜 GitLab을 사용하라고 하는 것일까?  
GitHub는 소스가 GitHub에 있다보니 보안에 취약하다.  
따라서, 아예 내부에서 관리하는 GitLab이나 SVN을 고객사는 더 선호한다.

  
  
  

# 참고

  * [SVN과 GIT 차이 포스팅](https://sowon-dev.github.io/2020/12/27/201228svn/)
  * [Gitlab으로 소스 이관하기(SVN 혹은 신규생성)](https://scvspace.kr/1385)
  * [SVN을 Git으로 Migration 하기](https://garve32.tistory.com/43)

#[GIT](/tags/GIT/)[SVN](/tags/SVN/)
