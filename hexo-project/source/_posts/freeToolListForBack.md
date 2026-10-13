---
title: "백앤드 개발시 유용한 사이트모음"
date: 2020-12-03 22:05:20
tags:
  - "Journal"
  - "List"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">백앤드 개발시 유용한 사이트모음의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * 이클립스 마켓플레이스 검색 - ObjectAid UML Explorer : 이클립스에서 바로 사용가능을 적용할 수 있다.</p>
</div>

<!-- more -->

## [UML(Unified Modeling Language 클래스 다이어그램 만들 수 있는 사이트](http://www.nextree.co.kr/p6753/)

  * [이클립스 마켓플레이스 검색 - ObjectAid UML Explorer](https://marketplace.eclipse.org/search/site/aid) : 이클립스에서 바로 사용가능
  * [starUML](http://staruml.io/) : 가장 유명. 최근버전은 유료이므로 이전버전사용가능
  * [draw](https://www.draw.io/)
  * [creately](https://creately.com/diagram-type/class-diagram)
  * [genmymodel](https://www.genmymodel.com/class-diagram-online)

  
  
  

## 변수명짓기

  * <https://www.curioustore.com/#!/util/naming>

  
  
  

## 시스템 아키텍처, 스택 아키텍쳐

  * <https://www.cloudcraft.co/> 한눈에 시스템 구성도를 볼 수 있도록 그릴 수 있음

    * ![](https://global-uploads.webflow.com/57013820ae28654573965bf2/5f960eb6182961e9fff56458_awseditor4.png)
  * [Systemizer](https://honzaap.github.io/Systemizer/) 분산시스템의 하이레벨 아키텍처 디자인을 쉽게 표현하기 위한 다이어그램 도구 오픈소스

    * ![](https://camo.githubusercontent.com/7fb023c9f308f6b2f5f0950441d9b3bfcd3a749fba493988487b91a10589b1d4/68747470733a2f2f686f6e7a6161702e6769746875622e696f2f53797374656d697a65722f6173736574732f676966732f7475746f7269616c302e676966)

  
  
  

## ER 다이어그램

  * [깔끔한 ER다이어그램 ](https://aquerytool.com/)
    * ![](https://aquerytool.com/images/help/PICD91.png)

  
  
  

## 오픈 [API](https://dydrlaks.medium.com/api-%EB%9E%80-c0fd6222d34c)

  * [카카오 API 홈페이지](https://developers.kakao.com) : <https://developers.kakao.com>
  * [네이버 API 홈페이지](https://developers.naver.com/) : <https://developers.naver.com/>
  * [구글 API 홈페이지](https://console.developers.google.com) : <https://console.developers.google.com>
  * [페이스북 API 홈페이지](https://developers.facebook.com/) : <https://developers.facebook.com/>
  * [공공데이터 포털](https://www.data.go.kr/) : <https://www.data.go.kr/>

  
  
  

## 기능 대신하는 서비스

  * 검색엔진 : <https://www.algolia.com>
  * 유저 비밀번호 관리기능
    1. <https://auth0.com/> 로그인/로그아웃/소셜로그인연동이 쉽다
    2. <https://aws.amazon.com/ko/cognito/> 아마존에서 만든 유저인증기능
  * 트랜잭션이메일서비스(트리거나 이벤트 후 발송하는 메일링서비스로 한달에 1만통 무료로 사용가능) : <https://www.mailgun.com/>
    * SMTP를 더이상 사용할 필요가 없다!
  * 마케팅용 이메일서비스 : <https://mailchimp.com>
  * 웹사이트 보안 SSL Certificate (http를 https로 만들고싶을때) : <https://letsencrypt.org/>
  * 에러 리포팅 : <https://sentry.io>
  * 실시간 채팅 : <https://pusher.com>
  * 푸쉬알림 : <https://onesignal.com/>
  * 피드 : <https://getstream.io/>

  
  
  

## 클라이언트

  * REST API를 쉽게 테스트하고 문서화 할 수 있는 swagger : <https://swagger.io/tools/swagger-ui/>  
![swagger](https://static1.smartbear.co/swagger/media/images/tools/opensource/swagger_ui.png?ext=.png)
  * REST API인 경우 : <https://insomnia.rest>  
![insomnia](https://cms-react-testing.cdn.prismic.io/cms-react-testing/bcdf8d48-9646-4fa0-85e4-9e3fce5c4f57_design-editor-preview.svg)
  * GraphQL API인 경우 : <https://altair.sirmuel.design>

  
  
  

## 배포

  * 배포를 대신 해주는 [헤로쿠](https://trend21c.tistory.com/1453) : <https://www.heroku.com/>
    * [히로쿠 무료 서버로 스프링부트 앱 배포하기](https://pinokio0702.tistory.com/118)
    * [How to Deploy From SpringBoot - GitHub - Heroku (DevOps Step by Step Tutorial)](https://youtu.be/ADoQLyOgTus)
  * 1년무료로 사용가능한 아마존 : <https://aws.amazon.com/>
  * [AWS를 쓸까? Heroku를 쓸까? 그 선택의 기준은?](https://youtu.be/NTDhBh1SdZ4)

  
  
  

## [서버리스](https://youtu.be/ufLmReluPww)

  * <https://aws.amazon.com/lambda/>
  * <https://cloud.google.com/functions/>

  
  
  

## 데이터베이스

  * <https://aws.amazon.com/dynamodb/> : 25GB 무료 제공
  * <https://cloud.google.com/firestore/> : 1GB 무료 제공
  * <https://www.mongodb.com/cloud/atlas> : 512GB 무료 제공
  * <https://fauna.com/> : FaunaDB는 graphQL 서버리스 데이터베이스로 100 MB storage 무료 제공

  
  
  

## 파일 업로드

  * <https://cloud.google.com/storage/> : 5GB 무료 제공
  * <https://cloudinary.com/> : 25GB 무료 제공

  
  
  

## 분석

  * <https://analytics.google.com/analytics/web/provision/#/provision>
  * <https://www.hotjar.com>
  * <https://mixpanel.com/>

#[Journal](/tags/Journal/)[List](/tags/List/)
