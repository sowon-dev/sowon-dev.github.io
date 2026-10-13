---
title: "클라우드 네이티브(Cloud Native)란? 개념,정의"
date: 2023-01-17 19:24:30
tags: []
categories:
  - Backend
  - Server
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">클라우드 네이티브(Cloud Native)란? 개념,정의의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    > 클라우드 네이티브라는 용어는 클라우드 제공 모델에서 제공하는 분산 컴퓨팅을 활용하기 위해 애플리케이션을 구축 및 실행하는 개념을 의미합니다. 클라우드 네이티브 앱은 클라우드가 제공하는 확장성, 탄력성, 복원성, 유연성을 활용하도록 설계 및 구축되었습니다.(중략) 클라우드 네이티브 서비스는 Kubernetes, Docker, 서버리스 함수, API 및 Kafka와 같은 기술을 사용하여 최신 애플리케이션 개발을 지원합니다. 업계 최고의 클라우드 제공업체를 통해 클라우드 툴과 서비스를 구현하므로 개발자가 운영 작업을 줄이고 애플리케이션을 더 빠르게 구축할 수 있습니다. 클라우드 네이티브 서비스는 개발자에게 마이크로서비스, 서버리스 함수와 같은 클라우드 네이티브 애플리케이션을 구축, 배포, 관리할 수 있는 종합적인 표준 기반 플랫폼을 제공합니다.</p>
</div>

<!-- more -->

클라우드 네이티브(Cloud Native)란 무엇일까? 이번에 교육을 받으면서 도커, 쿠버네티스, MSA등의 용어가 쏟아졌다. 이들이 어떤 Cloud Native와 관계가 있는지 궁금해서 정확히 알아보았다.

# 클라우드 네이티브

> 클라우드 네이티브라는 용어는 클라우드 제공 모델에서 제공하는 분산 컴퓨팅을 활용하기 위해 애플리케이션을 구축 및 실행하는 개념을 의미합니다. 클라우드 네이티브 앱은 클라우드가 제공하는 확장성, 탄력성, 복원성, 유연성을 활용하도록 설계 및 구축되었습니다.(중략) 클라우드 네이티브 서비스는 Kubernetes, Docker, 서버리스 함수, API 및 Kafka와 같은 기술을 사용하여 최신 애플리케이션 개발을 지원합니다. 업계 최고의 클라우드 제공업체를 통해 클라우드 툴과 서비스를 구현하므로 개발자가 운영 작업을 줄이고 애플리케이션을 더 빠르게 구축할 수 있습니다. 클라우드 네이티브 서비스는 개발자에게 마이크로서비스, 서버리스 함수와 같은 클라우드 네이티브 애플리케이션을 구축, 배포, 관리할 수 있는 종합적인 표준 기반 플랫폼을 제공합니다.  
> 출처: [오라클 공식홈페이지](https://www.oracle.com/kr/cloud/cloud-native/what-is-cloud-native/)

클라우드 네이티브란 클라우드의 장점을 모두 활용하는 애플리케이션을 개발하고 실행하기 위한 접근 방식이다.  
그렇다면 클라우드의 장점이 무엇일까?

  
  
  

# 클라우드의 장점

  1. 확장가능성(Scaling) : 사용량에 따라 편리하게 인스턴스를 증가, 감소할 수 있음
  2. CI/CD: 구축, 테스트 및 배포를 자동화하여 소프트웨어가 개발 시스템에서 운영 시스템으로 빠르고 안정적인 프로그램 구축가능
  3. 장애대응: 정 서비스에 오류가 발생해도 다른 서비스에 영향을 주지 않음

  
  
  

# 클라우드 네이티브 핵심 구성요소 4가지

![](https://images.ctfassets.net/o7xu9whrs0u9/2tVV4YzJRE7JGKzXjj4Xsp/af35d764254ead0c720c5761c74c134e/Cloud-Nateive-technologies-pyramid.jpg)  
[사진출처: https://www.influxdata.com/blog/introduction-cloud-native/](https://www.influxdata.com/blog/introduction-cloud-native/)

  1. DevOps
     * 개발 조직과 운영 조직의 통합을 의미: 이전에는 개발과 운영이 분리되어 개발자가 구동할 프로그램 준비를 끝나면, 이후 배포와 운영 작업은 다른 조직이 했다. 만약 우리가 단 몇줄의 코드를 바꿔야 할지라도 바꾼 후에 운영 조직과 다시 소통하여 배포해야 하므로 매우 번거로운 일이 아닐 수 없다. 이를 극복하기 위해 나온 개념으로 서비스의 문제가 생기면 바로 수정해서 즉시 배포하는 과정을 반복하는 것을 목적으로 한다.
  2. CI/CD
     * 지속적인 통합 (CI : Continuous Integration)
       * 소스 관리(형상관리), 빌드, 테스트를 모두 포함한다. e.g. 젠킨스, Team CI, Travic CI등
     * 지속적인 배포 (CD : Continuous Delivery & Deployment)
       * Continuous Delivery인 경우 빌드는 자동이지만 배포는 수동 반영
       * Continuous Deployment인 경우 빌드와 배포까지 모두 자동 반영
  3. Container 가상화 기술
     * 기존에는 서로 다른 OS환경을 위해 가상머신을 사용해야해서 비용, 운영측면에서 부담이 많았지만 도커라는 컨테이너 가상화 기술을 도입하여 각각의 서비스와 앱을 관리할 수 있게 되었음
  4. MSA(Micro Service Architecture)
     * [내가 이해한 MSA(MicroService Architecture)](https://sowon-dev.github.io/2021/04/12/210415MSA/) 참고

  
  
  

# 참고

  * [IT World - 클라우드 네이티브의 진정한 의미](https://www.itworld.co.kr/news/248260)
  * [jimkwon님 - Cloud Native Architecture - (1)](https://born2bedeveloper.tistory.com/51)
