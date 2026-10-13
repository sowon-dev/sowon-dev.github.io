---
title: "[요약/후기]The End Of Localhost"
date: 2022-06-26 21:46:42
tags:
  - "GeekNews"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'The End Of Localhost'에 참여하고 주요 발표 내용과 배운 점을 정리한 글이다.
    * 2030년대 개발자가 위시리스트를 보면 로컬호스트가 아닌 클라우드 환경이 요구됨을 확인했다.</p>
</div>

<!-- more -->

구독중인 GeekNews에서 아주 흥미로운 글을 봤다. 제목부터가 [Localhost시대의 종말](https://news.hada.io/topic?id=6799&utm_source=weekly&utm_medium=email&utm_campaign=202226)이다.  
GeekNews에서는 친절하게 한글번역 요약을 해주지만 원문이 궁금해서 원문을 읽고 나름 요약해봤다.

  * [원문 바로가기](https://dx.tips/the-end-of-localhost)  
글쓴이는 어떻게 Localhost가 종말한다는 걸까?

## 클라우드 덕분에!

  * 미래에는 모든 환경은 클라우드가 될 것이고, 모든 노트북은 클라이언트가 될 것
  * 2030년대 개발자가 위시리스트를 보면 로컬호스트가 아닌 클라우드 환경이 요구됨
  * dev환경과 prod환경간에 낭비되는 시간을 단축시킬 수 있음

  
  
  

## The “Future is Just Not Evenly Distributed” Argument

  * 이미 빅테크 기업들은 전적으로 클라우드 환경에서 일하고 있음.

> Google Cider : 구글의 웹 IDE. 거대한 Piper 파일 시스템을 탑재하고 코드리뷰/빌드/테스팅을 통합. 로컬머신에 코드를 내려받을 필요 없음  
> FB On-Demand : 로컬보다 더 충실하게 실시간 기능 프리뷰가 가능하게 “On-Demand”로 환경을 프로비저닝. FB에선 “로컬 개발” 자체가 없음  
> Etsy : 모든 개발이 Cloud VM에서 진행 “VSCode가 VM으로 SSH해서 동작하기 때문에, VM 외부로 코드를 체크아웃 해본 적이 없음”  
> Tesla : 자동차 OS 개발을 로컬에서 클라우드로 전환 (그 전엔 개발자에게 빌드용 비싼 데스크탑을 제공했었다고)  
> Palantir : Coder(리모트 개발환경 SaaS)와 EKS를 사용하는 Remote Ephemeral Workspace로 옮겨감  
> Shopify : 대부분의 개발자가 Spin 이라 불리는 클라우드 개발환경으로 이전 (xhyve 위에서 실행되는 경량 VM)  
> GitHub : 깃헙의 개발의 대부분을 Codespaces로 이관  
> 출처: [https://news.hada.io/topic?id=6799&utm_source=weekly&utm_medium=email&utm_campaign=202226](https://news.hada.io/topic?id=6799&utm_source=weekly&utm_medium=email&utm_campaign=202226)

  * “sure, but does it work for my small team?” 위 예시 기업들은 이미 큰 회사들이니까 가능한거고 작은 기업에는 그게 가능할까?
    * 맞는 말임. 클라우드로 환경변화는 상당한 규모의 내부 투자가 이루어진 후에야 그 이득을 취할 수 있음. 하지만 기술이 상용화되면 점점 클라우드환경으로의 이동은 점점 더 확산될 것임

  
  
  

## Jobs to Be Done of Localhost

  * 이미 많은 프로그램에서 로컬을 실행하지 않고 원격으로 코드를 수정하고 실행하고 있음.

  
  
  

## The Inevitability Argument

  * 클라우드로의 이동을 피할 수 없는 일임. 언젠가는 일어날 일임.

  
  
  

## The Potential of Edge Compute

  * CRDT 및 에지 컴퓨팅과 같은 기술의 부상은 우리가 실제로 “로컬”이라고 생각하는 것의 경계를 흐리게 할 가능성이 더 높음.

  
  
  

## Pushback: It’s Still Not Good Enough

  * 김칫국은 ㄴㄴ 아직 충분하지 않음.
  * 개발자들이 습관처럼 Preview가 빠른 로컬호스트를 사용함

  
  
  

## 내생각

개발환경으로 더이상 로컬호스트를 사용하지 않을 수 있다는 사실이 흥미로웠다.  
작은 업체에서 여전히 가능할까 의문이지만 그래도 클라우드환경으로의 변화는 막을 수 없을 것으로 보인다.  
그쪽으로 공부를 열심히 해봐야지

  
  
  

## 재밌는 표현

  * going the way of the Dodo: 인간에 의해 멸종된 도도새처럼 멸종된다는 의미이다.

#[GeekNews](/tags/GeekNews/)
