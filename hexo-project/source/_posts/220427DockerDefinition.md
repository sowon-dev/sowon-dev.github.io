---
title: "Docker는 어떻게 HostOS와 다른 운영체제에서 돌아갈까?"
date: 2022-04-27 02:22:51
tags:
  - "Docker"
categories:
  - Backend
  - Server
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Docker는 어떻게 HostOS와 다른 운영체제에서 돌아갈까?의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    이 리눅스엔진을 통해서 리눅스OS나 우분투OS를 사용할 수 있다!을 적용할 수 있다.</p>
</div>

<!-- more -->

오늘 VM에 대해 팀장님과 이야기하다가 문득 Docker로 어떻게 리눅스OS를 쓸 수 있는지가 궁금해졌다.  
HostOS가 원도우 환경에서 VM은 GuestOS를 원하는 대로 설치할 수 있으니 리눅스든 우분투든 원하는 OS를 쓸 수 있다.  
하지만 Docker는? 

Docker는 GuestOS를 설치하지 않고 HostOS를 활용한다. 그래서 VM보다 훨씬 가볍고 빠르다.  
![https://medium.com/@darkrasid/docker%EC%99%80-vm-d95d60e56fdd](https://miro.medium.com/max/2400/1*wOBkzBpi1Hl9Nr__Jszplg.png)

## HostOS가 원도우 환경인 Docker에서 어떻게 리눅스OS를 사용할 수 있을까?

여러 구글링을 끝에 내가 내린 결론이다. 따라서 정확하지않을 수 있다. (잘못된 부분은 댓글로 알려주시면 이 글을 읽는 모두에게 도움이 됩니다. 감사하겠습니다!)  
[Docker Desktop for Windows(링크)](https://www.docker.com/products/docker-desktop/)를 다운로드 받으면 리눅스 엔진이 함께 설치된다.  
이 리눅스엔진을 통해서 리눅스OS나 우분투OS를 사용할 수 있다!

  
  

## 같이 읽으면 좋은 글

  * [컨테이너, 도커, 쿠버네티스](https://sowon-dev.github.io/2021/03/28/210329Container/)

#[Docker](/tags/Docker/)
