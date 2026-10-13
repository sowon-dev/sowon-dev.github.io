---
title: "AP(Access Point)란? 개념,정의"
date: 2022-12-29 16:09:24
tags:
  - "오늘또못알아듣고말았습니다"
categories:
  - Backend
  - Network
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">AP(Access Point)란? 개념,정의의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    AP는 유선랜의 유선신호를 무선으로 변경해주는 것이다. → 회사 내부망이 유선랜인데 다양한 기기에서 사용하려면 무선랜으로 바꿔주면 편리하다.</p>
</div>

<!-- more -->

회의때 무수히 들었던 AP. 도대체 AP가 뭘까?  
일단 Access Point의 약어이다. 네트워크와 관련된 느낌 물씬!

# AP란

AP는 유선랜의 유선신호를 무선으로 변경해주는 것이다. → 회사 내부망이 유선랜인데 다양한 기기에서 사용하려면 무선랜으로 바꿔주면 편리하다.  
AP는 DHCP 서버에서 IP를 할당해줘야한다.

> 무선랜을 구성하는 장치중 하나로, 유선랜과 무선랜을 연결시켜주는 장치이다.  
> AP는 Access Point의 약어이나, Wireless Access Point라고 하여 WAP 라고도 한다.  
> AP는 대체로 독립형 장치로, 이더넷 허브(Ehternet Hub)나 서버(Server)에 꽂아 사용할 수 있다.  
> AP는 휴대폰(Cellular Phone)처럼 사용자의 위치에 따라 하나의 AP에서 다른 AP로 핸드오프(Hand-off : 넘겨주기) 되므로, 사용자가 이동하면서 이동형 무선장치를 사용할 수 있다.  
> 출처: [Just Blue - AP(Access Point)](https://m.blog.naver.com/twers/50118628879)

  
  
  

# AP와 일반 무선공유기 차이점

일반 무선공유기 | AP  
---|---  
한 개의 IP로 여러 명의 네트워크를 사용할 수 있음 | 건물의 각 층과 사무실별로 설치할 경우 사무실 내에서 자유롭게 네트워크를 사용할 수 있다는 장점이 있고 안테나의 개수에 따라 사용할 수 있는 범위가 정해지며 넓은 곳일수록 안테나가 많이 달린 제품을 활용하면 좋음  
SSID 3개까지 가능 | SSID 512개까지도 가능  
네트워크선 따로, 전원선 따로 | 특정 모델에 따라 네트워크선 하나로 전원까지 공급가능  
| 일반공유기보다 많은 라우팅 기능을 지원  
  
  * SSID란?  
Service Set IDentifier의 약자로 무선네트워크 이름이다.

  
  
  

# 참고

  * [https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=futuremain&logNo=221618229181](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=futuremain&logNo=221618229181)

#[오늘또못알아듣고말았습니다](/tags/%EC%98%A4%EB%8A%98%EB%98%90%EB%AA%BB%EC%95%8C%EC%95%84%EB%93%A3%EA%B3%A0%EB%A7%90%EC%95%98%EC%8A%B5%EB%8B%88%EB%8B%A4/)
