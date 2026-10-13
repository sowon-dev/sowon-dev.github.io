---
title: "STS git clone 깃허브연동하여 스프링 maven프로젝트 가져오기"
date: 2021-08-09 19:23:00
tags:
  - "STS"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">STS git clone 깃허브연동하여 스프링 maven프로젝트 가져오기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    github 레포지토리의 springboot maven(메이븐)프로젝트를 가져오는 방법이다.</p>
</div>

<!-- more -->

프로젝트 셋팅을 자주하지 않기때문에 헷갈릴 염려가 있어 아예 순서를 적어두려고 한다.  
github 레포지토리의 springboot maven(메이븐)프로젝트를 가져오는 방법이다.

## 1 STS에서 Perpectives를 git으로 변경

![](/img/210810STSgitClone1.PNG)

  1. STS 또는 이클립스에서 Perspectives의 돋보기 아이콘을 클릭한다.
  2. git 검색
  3. Perpectives git 선택

  
  
  

## 2 Clone a Git repository

![](/img/210810STSgitClone2.PNG)

  1. `Clone a Git repository` 클릭
  2. 깃헙 레포에서 복사한 clone URI를 붙여넣기한다.  
깃헙에서 초록색 `Code`버튼을 클릭한 뒤 URI를 복사했다면 붙여넣지 않아도 자동적으로 기입된다.
  3. NEXT를 클릭한 뒤 Clone을 원하는 브랜치를 선택한다.  
기본값은 main 또는 master 브랜치가 체크되어 있다.  
Tag fetching strateguy는 기본값으로 진행하나 필요에 따라 바꾸면 된다.
  4. LocalDestination의 Directory를 선택한다.  
저장은 원하는 곳에 설정하면 된다. 나는 보통 D 드라이브로 경로를 설정한다.

이제 깃헙 연동이 끝났다!  
잘 가져왔는 지 어떻게 확인할까?  
아래 이미지에서 체크한 부분을 보자.

![](/img/210810STSgitClone3.PNG)

STS의 Progress탭을 보면 클론이 진행중인 걸 확인할 수 있다.  
프로젝트 크기에 따라 시간이 꽤 걸릴 수 있다.

  
  
  

## 3-1 STS에서 Perpectives를 git으로 그대로 유지한채로 진행하는 방법

![](/img/210810stsgitclone2.JPG)

  1. 클론한 git repository에서 Working Tree 를 클릭한다
  2. import projects를 클릭하고 위치를 맞추면 끝!

  
  
  

## 3-2 STS에서 Perpectives를 java로 변경해서 진행하는 방법

![](/img/210810STSgitClone4.PNG)

  1. import projects 클릭
  2. maven 검색
  3. Existing Maven Projects선택

![](/img/210810STSgitClone5.PNG)

  4. Browe 선택 후 위에서 저장된 경로 선택  
나는 D에 저장햇으므로 D에 있는 파일 경로를 선택했다.

  5. pom.xml 선택 확인  
자동적으로 pom.xml이 검색되고 체크되므로 확인한다.

  6. finish 버튼  
조금만 기다리면 불러오기가 완료된다!  
끝!

## gradle 프로젝트라면?

1,2번은 동일하게 진행하면 되고 3번에서 maven이 아니라 gradle폴더를 선택한 후 `Existing Gradle Project`를 클릭하면 된다!  
참 쉽죠?!

#[STS](/tags/STS/)
