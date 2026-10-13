---
title: "이클립스 svn 계정변경, 비밀번호 잊어버렸을 때 해결하기"
date: 2021-01-25 03:31:27
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
  <p class="tldr-desc">문제는 변경할 계정의 비밀번호가 기억이 안난다는 사실… 원인을 파악했다.
    이클립스에서 svn 계정을 변경해야할 상황이 생겼다.</p>
</div>

<!-- more -->

## 비번이 뭐더라…?

이클립스에서 svn 계정을 변경해야할 상황이 생겼다.  
문제는 변경할 계정의 비밀번호가 기억이 안난다는 사실…  
그나저나 아이디는 뭐였더라? 아이디도 함께 찾아보자.

  
  
  

## svn 계정 아이디찾기

먼저 실행 중인 이클립스를 종료한다.  
파일탐색기를 통해 `C:\Users\[컴터아이디]\AppData\Roaming\Subversion\auth\svn.simple` 로 이동한다.  
폴더 안에는 계정정보가 담겨져있다.  
하단에 username을 통해 아이디를 찾을 수 있다!  
이제 비밀번호만 찾으면 된다!

  
  
  

## svn 계정 비밀번호찾기

비밀번호를 찾는 방법보다 새로운 비밀번호로 설정하는 방법이 더 쉬워보였다.  
VisualSVN server를 통해 새로운 비밀번호를 설정할 수 있다.  
나는 svn서버를 관리하지않기때문에 서버관리자의 도움을 받아 비밀번호를 재설정했다.

![출처 : https://jsp-making.tistory.com/347](https://t1.daumcdn.net/cfile/tistory/214BF03E57C7DE3C2D)

  
  
  

## 이클립스 내 svn 계정 바꾸기

이제 이클립스의 svn계정을 변경해보자 그럴려면 이클립스를 종료해야한다.  
파일탐색기를 통해 `C:\Users\[컴터아이디]\AppData\Roaming\Subversion\auth\svn.simple` 로 이동한다.  
안의 파일들 중 svn주소가 일치하는 파일을 찾은 뒤 필요없는 username인 경우 해당 파일을 삭제한다.  
그리고 이클립스를 재접속하면 svn 로그인창이 열리고 새로 등록할 계정을 입력해주면 된다!

  * 파일을 건드리지 않고 [이클립스 설정에서 SNV 계정정보를 변경](https://blog.nachal.com/1213)할 수도 있다.

해결!

#[Eclipse](/tags/Eclipse/)[SVN](/tags/SVN/)[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)
