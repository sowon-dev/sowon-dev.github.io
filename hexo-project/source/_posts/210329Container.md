---
title: "컨테이너, 도커, 쿠버네티스"
date: 2021-03-28 15:45:39
tags:
  - "Docker"
categories:
  - Backend
  - Server
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">컨테이너, 도커, 쿠버네티스의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    컨테이너를 통해 동일한 인터페이스를 제공할 수 있어 프로그램의 배포 및 관리를 단순하게 해준다.</p>
</div>

<!-- more -->

새로운 프로젝트를 진행하면서 팀장급 회의가 있었다. 신규 프로젝트는 어떻게 구성하는 지, 의사결정은 어떻게 이루어지는 지 너무너무 궁금해서 팀장님들 회의에 서기로라도 참석하고싶었지만… 나는 신입이기때문에… 참여할 수 없었다. 하지만 팀전체에 공유된 회의 참고자료를 볼 수 있었고 내가 들어만 봤던 도커와 쿠버네티스라는 단어가 보였다. 이참에 완전히 정리해보려고한다.

## 컨테이너(Container)

쿠버네티스를 알려면 도커를 알아야하고 그럴러면 컨테이너를 알아야한다.

  * 컨테이너란 다양한 프로그램, 실행환경을 패키지로 묶어 추상화하여 격리 환경을 만드는 것

컨테이너를 통해 동일한 인터페이스를 제공할 수 있어 프로그램의 배포 및 관리를 단순하게 해준다.  
컨테이너는 가상머신(VM)과 비교할 수 있다. VM의 경우 Guest OS가 올라가기때문에 컨테이너보다 훨씬 무겁다.

![https://medium.com/@darkrasid/docker%EC%99%80-vm-d95d60e56fdd](https://miro.medium.com/max/2400/1*wOBkzBpi1Hl9Nr__Jszplg.png)

가상머신 서버 | 컨테이너서버  
---|---  
가상 머신의 모든 자원을 사용 | 운영체제의 자원을 필요한 만큼 격리하여 컨테이너에 할당  
  
  
  
  

## 도커(Docker)

  * 컨테이너기반의 오픈소스 가상화 플랫폼
  * 도커의 작동 순서
    1. 코드개발
    2. Dockerfile 생성: Image파일만 생성하면 변경사항을 확인할 수 없기때문에 이미지내용을 코드화함
    3. Dockerfile Image 생성: 컨테이너 실행에 필요한 파일과 설정값등을 포함하고 있는 것을 이미지화한다.(Immutable)
    4. Container Orchestrator를 통한 배포 : Kubernetes, Docker Swarm, Rancher, Apache Mesos등의 컨테이너 오케스트레이션 툴을 사용
    5. Container run
    6. Container image Push

  
  
  

## 쿠버네티스(Kubernetes)

  * 컨테이너를 관리를 위해 나온 오픈소스 플랫폼  
컨테이너 역시 그 수가 많아지게 되면 관리와 운영에 있어서 어려움이 따르는데 이를 관리하고 조율하는 시스템 중 하나가 바로 쿠버네티스이다.

  * [쿠버네티스 시작하기 - Kubernetes란 무엇인가?](https://subicura.com/2019/05/19/kubernetes-basic-1.html)

  
  
  

## 참고

참고라고 적어놓고 필독이라고 읽는다. 하나하나 꼭 읽어봐야한다.  
특히 Container 시리즈는 정말 주옥같다. 

  * [Container 시리즈 전체](https://tech.osci.kr/2020/03/03/91690167/)
  * [Docker와 쿠버네티스의 이해](https://zzsza.github.io/development/2018/04/17/docker-kubernetes/)
  * [Linux) Doker와 Container의 탄생과 설명, 차이점](https://hwan-shell.tistory.com/116)

#[Docker](/tags/Docker/)
