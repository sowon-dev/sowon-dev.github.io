---
title: "걸스인텍 서울 : Git? GitHub? 웨비나후기"
date: 2020-08-25 15:00:00
tags:
  - "Review"
  - "GIT"
categories:
  - Reflections
  - Lectures & Seminars
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'걸스인텍 서울 : Git? GitHub? 웨비나후기'에 참여하고 주요 발표 내용과 배운 점을 정리한 글이다.
    > #걸스인텍 #깃허브 #github #코딩 #여성개발자을 확인했다.</p>
</div>

<!-- more -->

## 🍀 웨비나 후기

1시간반동안 진행되었는데 너무 아쉬웠다. 2시간해도 될듯.  
라면비법이라든지 Azure 개발도구와 Azure 앱 시연이 정말 유익했다.  
Azure 개발도구는 정말 팀플에는 필수적이라는 생각이 들었다.

지금 개인 프로젝트중이지만 적응하고자 사용해봤는데 너무 편했다.  
이전까지 todo list들을 구글 task에 저장하고 사용했었는데 앞으로느 Azure devOps 적극 사용해야겠다!  
깃초보뿐만 아니라 깃중급사용자를 위해 1시간반이라는 짧은 시간동안 다양한 꿀팁을 전수해주셔서 매우 유익했다.  
나뿐만 아니라 다른 참여자들도 취업에 대한 두려움이 가득했는데 뻔하다면 뻔한 질문에 응원가득한 답변을 해주셔서 정말 감사했다.  
할 수 있다. 할 수 있다고 믿자!

> 개발자라면 협업에 반드시 필요한 GitHub! 깃허브 직원들이 쉽고 재밌게 알려주는 깃허브에 대해서 알아봐요 👩🏻‍💻💞 무료 행사신청: https://www.wanted.co.kr/events/git_github 
> 
> #걸스인텍 #깃허브 #github #코딩 #여성개발자
> 
> 게시: [Girls in Tech - Korea](https://www.facebook.com/GirlsinTechKorea/) [2020년 8월 18일 화요일](https://www.facebook.com/GirlsinTechKorea/posts/2751358061767845)

  
  
  

## 🍀 깃이 왜 필요하죠?

  * 작업을 할때 버전 관리가 필요하다.
  * 문서는 save as로 저장하면서 관리할수있다지만 그게 코드면? 점 하나만 달라져도 프로그램의 동작 여부가 달라진다.
  * 어떤 부분을 어떻게 작성했는지 깃을 이용하여 추적을 해야한다.

  
  
  

## 🍀 깃 vs 깃허브

  * 깃 : 분산 버전 관리 시스템
  * 깃허브 : 분산버전 관리 툴인 깃을 사용하는 프로젝트를 지원하는 웹 호스팅 서비스
  * 리누스 토르발스 : 리눅스운영체제 개발, 깃 개발한 천재개발자

  
  
  

## 🍀 깃 주요 개념

개념 | 어떨 때 사용할까  
---|---  
commit | 어느 단위로 변경된 사항을 저장  
conflict | 같은 부분을 협업자들과 동시에 변경하게되면 발생. 어떻게 처리할 것인지가 관건  
branch | 개별적인 버전관리  
merge | 개별적인 버전의 최종본들을 합치기  
  
  
  
  

## 🍀 빌드

개발자들이 쓴 코드를 실행되는 파일로 변환하는 것을 빌드라고 한다

  
  
  

## 🍀 프로젝트 협업도구

  * [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/) : 깃헙이랑 연동가능
  * 깃헙계정이랑 연동하면 됨 + 커밋메세지 AB#번호+ development에 자동으로 트리거됨

  
  
  

## 🍀 draft pull request

  * 깃헙에서 제공하는 기능
  * 작업량이 많은 경우 완성된 pr은 아니지만 중간지점에서 리뷰해줬으면 좋겠을때 사용하는 기능

  
  
  

## 🍀 코드 스페이스

  * <https://github.com/features/codespaces>
  * 올해 ms빌드 개발자빌드에서 굉장히 핫했다.
  * pc에 개발환경이 없어도 개발가능
  * 다른 사람의 브랜치를 vs코드로 볼수있음
  * 디버깅 가능
  * 배타버전이라 정식출시는 2020년 하반기
  * 명령어 `npm test`

  
  
  

## 🍀 깃헙 actions

![https://medium.com/faun/most-popular-ci-cd-pipelines-and-tools-ccfdce429867](https://miro.medium.com/max/700/0*TH1nBsXNDB5Njynk.PNG)

  * ci/cd (지속적인 빌드/지속적인배포) 자동화 가능하게 함.
  * node.js파일을 azure web app으로 바꿈
    * on: 언제 실행하나요? 마스터브랜치일때
    * job:뭘실행하나요?
  * 셋팅즈 -> 시크릿 -> repostiory secrets 에서 중요정보를 보호할수있음 

  
  
  

## 🍀추천무료학습사이트

  * [GitHub Learning lab](https://lab.github.com/)
  * [Microsoft Learn : 컴퓨팅사고](https://educationblog.microsoft.com/en-us/tag/computational-thinking/)
  * [Microsoft Learn : 다양한 무료교육](https://docs.microsoft.com/en-us/learn/browse/)
  * [Microsoft Learn : Azure Web App 소개](https://docs.microsoft.com/en-us/learn/modules/host-a-web-app-with-azure-app-service/)

  
  
  

## 🍀 브랜치는 몇개 생성하면 좋은가요? 브랜치 관리 팁 알려주세요!

> branch 개수는 상관이 없습니다. branch는 merge된 후에 삭제되기도 합니다.  
> branch 관리팁은 [git flow](https://sowon-dev.github.io/2020/08/22/200822opensource2/)개념이 도움됩니다.  
> 간단히 말씀드리면 기능별(feature), 버그별(hotfix), 릴리즈별(release)등 다양하게 만들 수 있습니다. 

  
  
  

## 🍀 실무에서 리뷰어가 따로 있는지?

> 보통은 개발문화가 좋은 회사의 경우 CTO, 팀장님, 동료들이 서로의 코드를 리뷰해줍니다.

#[Review](/tags/Review/)[GIT](/tags/GIT/)
