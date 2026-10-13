---
title: "[GIT]기존 프로젝트를 github에 연결하기"
date: 2021-05-09 15:00:00
tags:
  - "GIT"
categories:
  - Reflections
  - Version control
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">기존 프로젝트를 github에 연결하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    지우기전에 필요한 내용이 있다면 어디 복사해놓은 뒤 pull완료 후 붙여넣기 하면 된다!을 적용할 수 있다.</p>
</div>

<!-- more -->

프로젝트를 한창 만들다가 또는 다 만든 뒤 해당 프로젝트를 깃허브에 올리고 싶을 때 어떻게 해야할까?  
git bash를 이용한 방법을 알아보자.

## 프로젝트 폴더 내 git init 생성

기존 프로젝트가 있는 폴더 열기 -> 마우스 우클릭 -> `git bash here` 클릭하기  
그럼 git bash창이 열리고 아래 명령어를 통해 git 초기화를 한다.

```bash
git init
```

git bash창에서 주소줄 옆에 `(master)`가 생겼다면 잘 생성된 것이다. 

  
  

## GITHUB repository 연결

깃허브에 가서 레포지토리를 생성한 뒤 초록색 `code` 버튼을 클릭하여 깃헙 레포지토리URL을 복사한다.  
그 다음 git bash창에서 아래 명령어를 통해 깃헙 레포지토리와 연결한다.

```bash
git remote add origin 복사해온깃헙레포url
```

잘 연결되었는지 확인하고 싶다면 아래 명령어를 입력한다.  
참고로 `-v`는 version의 약어이다.

```bash
git remote -v
```

  
  

## pull

git bash창에서 아래 명령어를 통해 깃헙 레포지토리를 먼저 PULL 받는다.

```bash
git pull origin main
```

  
  

### pull에러가 발생한다면?

위 명령어를 입력했는데 아래와 같은 error가 발생했다면 어떻게 해야할 까?

```plain
error: The following untracked working tree files would be overwritten by merge:
        .gitignore
        README.md
Please move or remove them before you merge.
Aborting
```

`.gitignore`와 `README.md`파일이 중복되어 pull이 오류가 난 것이므로 로컬에서 해당 파일을 지워주자.  
지우기전에 필요한 내용이 있다면 어디 복사해놓은 뒤 pull완료 후 붙여넣기 하면 된다!

  
  

## checkout main (선택사항)

깃헙정책 변경으로 기본 브랜치 이름이 master에서 main으로 변경되었다.  
나는 master가 아닌 main 브랜치로 push를 하고자 브랜치 체크아웃을 진행했다.  
원하는 브랜치 명을 만들어서 push해도 된다.

```bash
git branch main
git checkout main
git branch -d master

// 브랜치 뭐뭐 있는 지 확인
git branch
```

잘 되었다면 git bash창의 주소줄 맨 오른쪽이 `(master)`에서 `(main)`으로 변경된다.

  
  

## IDE 프로젝트 우클릭 Team > share Project

이제 IDE로 돌아가보자.  
올리고 싶은 프로젝트를 우클릭 한뒤 Team > share Project를 클릭하고 Finish버튼을 클릭한다.  
이로써 git 레포지토리와 로컬에 있는 기존 프로잭트가 잘 연결된 것이다.

잘 연결되었는 지 어떻게 확인할 수 있을까?  
이에 두 가지 방법이 있다.

  1. 프로젝트명 옆에 [깃헙레포명 브랜치명]이 추가되어있는 것을 확인할 수 있다.
  2. Perspective를 Java에서 Git으로 변경하면 왼편 Git Repositories에 깃헙레포가 추가된 것을 확인할 수 있다.

  
  

## git ignore 먼저 commit 후 push하기

연결만 되었을 뿐 로컬에 있는 소스코드를 github에 업로드하지 않았다. 이제 업로드해보자!

프로젝트 폴더를 보면 자동으로 `.gitignore`이 생성되어있다.  
만약 보이지 않는 경우 Perspective를 Java에서 Git으로 변경하면 해당 파일을 찾을 수 있다. 

<https://www.toptal.com/developers/gitignore> 를 통해 ignore 사항들을 추가한 뒤 전체 코드를 복사한다.  
업로드할 프로젝트에 관련된 것들을 입력하면 되는데 나는 주로 `java`, `Eclipse`, `Maven`을 입력한다.  
기존 `.gitignore`파일에 복사한 코드를 붙여준다.

그 뒤 아래 3가지 명령어를 차례대로 입력한다.

```bash
git add .gitignore
git commit -m "git ignore 추가"
git push
```

깃허브 레포지토리에서 `.gitignore`이 보인다면 정상적으로 푸쉬한 것이다.

  
  

## 기존 프로젝트를 스테이지에 올리고 commit 후 push하기

```bash
git add .
git commit -m "소스코드 추가"
git push
```

여기서 잠깐!  
`git add .` 와 `git add *` 차이가 무엇일까?  
[GIT: `git add .` 와 `git add *` 차이 포스팅](https://sowon-dev.github.io/2021/09/08/210909GIT-add-VSadd/)에서 확인할 수 있다.

이로서 깃허브 레포지토리에서 올린 소스코드들이 보인다면 깃허브에 프로젝트 올리기 완료!

#[GIT](/tags/GIT/)
