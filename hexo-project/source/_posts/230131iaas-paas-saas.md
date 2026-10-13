---
title: "IaaS, PaaS, SaaS 차이"
date: 2023-01-30 22:58:49
tags:
  - "차이"
categories:
  - Backend
  - Network
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'IaaS, PaaS, SaaS 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    * 장점: 환경 구축 자유도가 높다, 시스템관리자의 부하가 적다.</p>
</div>

<!-- more -->

프로젝트에서 사용중인 클라우드네이티브 서비스가 있는데 PaaS서비스이다. 예전에 이와 관련해서 공부한 적이 있는데 기록하지 않으니 벌써 기억이 가물가물하다. 이참에 다시 정리해보았다.

참고로 클라우드네이티브가 무엇인지 궁금하다면 블로그 글 [클라우드 네이티브(Cloud Native)란? 개념,정의](https://sowon-dev.github.io/2023/01/17/230118cloudnative/)을 참조하면 된다.

# 한눈에 비교하기

![출처: redhat](https://www.redhat.com/cms/managed-files/iaas-paas-saas-diagram3-1638x1046.png)

  
  
  

# IaaS(Infrastructure as a Service)

  * 정보시스템의 모든 인프라를 인터넷상에서 제공한다. 
  * 언뜻 호스팅 서비스같아오이지만 IaaS의 경우,서버를 이용할 때에 필요한 하드웨어의 스펙이나 OS등을 사용자가 자유롭게 선정할 수 있다.
  * 장점: 환경 구축 자유도가 높다, 시스템관리자의 부하가 적다.
  * 단점: 환경 구축에 전문성 필요, 유지보수 범위가 넓다. 

  
  
  

# PaaS(Platform as a Service)

  * 정의: 개발 환경이 플랫폼화되어있는 서비스
    * 플랫폼화란? 클라우드 환경의 서버, OS, 미들웨어, 데이터베이스 등 애플리케이션 개발에 필요한 환경이 플랫폼으로 갖추어져 있음.
  * 장점: 개발환경의 플랫폼화로 인해 서비스·어플리케이션의 개발에 전념 가능, 초기 비용 및 시간 비용 절감 가능
  * 단점: 개발환경의 커스텀마이징이 낮다.

  
  
  

# SaaS(Software as a Service)

  * 정의: 패키지 제품으로 아예 서비스를 제공
    * 예시: Office365, Gmail 등등
  * 장점: 필요한 서비스를 월별요금제 등으로 결제해서 즉시 사용 가능
  * 단점: 커스터마이징 불가, 데이터마이그레이션 어려움.

  
  
  

# 참고

  * <https://www.redhat.com/ko/topics/cloud-computing/what-is-paas>
  * <https://tagilog.tistory.com/1138>

#[차이](/tags/%EC%B0%A8%EC%9D%B4/)
