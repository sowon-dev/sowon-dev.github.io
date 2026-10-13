---
title: "[Eclip/STS]특정 파일이  커밋이 안 될때, 파일아이콘에 체크표시가 되어있을때"
date: 2021-07-07 16:19:12
tags:
  - "Eclipse"
  - "STS"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">특정 파일이  커밋이 안 될때, 파일아이콘에 체크표시가 되어있을때의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    설정을 확인하며 파일을 유심히 보는데 오 홀리!!! 해당 파일의 작은 아이콘 모양이 다른 파일들과 달랐다.</p>
</div>

<!-- more -->

STS에서 열심히 코딩하고 커밋하려고 하는데 특정 파일만 자꾸 Git Staging에 올라오지도 않고 index에 추가되지도 않으며 Commit도 되질 않았다.  
도대체 문제가 뭘까.  
설정을 확인하며 파일을 유심히 보는데 오 홀리!!! 해당 파일의 작은 아이콘 모양이 다른 파일들과 달랐다.  
왕년의 다른그림찾기실력이 여기서 쓰일 줄이야. 😂 

  
  
  

## 원인

다른 파일들은 노란 네모 아이콘이 있는데 해당 파일에만 체크 아이콘이 있었다.  
이 작은 아이콘을 가볍게 여겨선 안된다.  
Assume unchanged라는 의미로 git에서 해당 파일이 무슨 변화가 있든 변화가 없다고 받아드리겠다는 의미이다.  
그러니 내가 아무리 코드를 수정해도 git은 수정사항이 없다고 판단하고 staging에 올리지도 않았다.

  
  
  

## ICON 뜻 알아보기

아래 이미지의 순서대로 아이콘의 의미를 알아보자.

![https://wiki.eclipse.org/EGit/User_Guide/State](https://wiki.eclipse.org/images/0/07/02-IconDecorations.png)

  * floder앞에 닫는 태그 `>` (dirty) : 이 폴더 안의 적어도 하나 이상의 파일이 dirty 하다. 즉 변화가 있는 파일이 있다.
  * 노란 네모 (tracked) : Git 레포지토리에 해당 파일를 추적 중이다.
  * `?` (untracked) : Git 레포지토리에서 처음 보는 파일이다. 즉 신규 파일을 생성한 경우 이렇게 뜬다.
  * 아이콘 없음 (ignored) : .gitignore 파일 안에 명시된 파일이나 git에 올라가지 않는 무시되고있는 파일이다.
    * 설정 및 확인방법 1. 파일 우클릭->Team->ignore
    * 설정 및 확인방법 2. preference->Team->Ignored Resources
  * dirty.txt앞에 닫는 태그`>` (dirty) : 인덱스 및 레포지토리에 추가되지 않은 변경사항이 있는 파일이다.
  * `*` (staged) : 해당 파일이 인덱스에 추가되었다. 
  * `*`와 `>` (partially-staged) : 해당 파일의 수정사항이 인덱스에 추가된 후 해당 파일에 변경사항이 있다.
  * `+` (added) : 해당 파일이 인덱스에 추가되었다.
  * `x` (removed) : 해당 파일이 로컬 디렉토리에서 삭제되면서 버전이 변경되었다. 이 표시는 프로젝트 구조가 아닌 Git staging 메뉴에서 확인할 수 있다.
  * 빨간 마름모 (conflict) : 해당 파일에 merge 충돌이 있다.
  * 파란 `✓` (assume-valid) : 해당 파일에 무슨 변화가 있더라도 변화가 없다고 판단한다.
    * 설정방법 : Team ->Assume unchanged 또는 Not Assume unchanged

  
  
  

## GUI로 해결하기

  1. 체크 아이콘이 있는 파일 우클릭
  2. 아래 이미지처럼 Team -> Advanced -> No Assume Unchanged 클릭  
![](/img/210708sts-icon.PNG)
  3. 2번을 실행해도 여전히 체크 아이콘이 있을 것이다. 당황하지 않고 😁 STS/이클립스를 재시작해준다.
  4. 재시작 후 확인해보면 해당 파일의 체크 아이콘이 노란 네모 아이콘으로 바뀐 것을 확인할 수 있다!

해결!

  
  
  

## CLI로 해결하기

CLI로 설정하는 방법은 [특정 파일만 커밋하지 않기(–assume-unchanged)](https://www.zerocho.com/category/Git/post/60ceb24dcc6ccc0004c38287)를 참고하면 된다.

  
  
  

## 참고

  * <https://wiki.eclipse.org/EGit/User_Guide/State>

#[Eclipse](/tags/Eclipse/)[STS](/tags/STS/)
