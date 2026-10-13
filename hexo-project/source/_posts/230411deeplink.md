---
title: "[모바일] deeplink가 뭐길래(개념, 정의)"
date: 2023-04-10 20:55:17
tags:
  - "Backjoon"
  - "패스트캠퍼스(초격차Java/Spring)"
categories:
  - Frontend
  - Android
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">deeplink가 뭐길래(개념, 정의)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    오늘 회의를 하다가 부장님이 deeplink를 사용하면된다고 하셨다.</p>
</div>

<!-- more -->

오늘 회의를 하다가 부장님이 deeplink를 사용하면된다고 하셨다.  
deeplink가 뭐지? 처음 듣는 용어라 공부해봤다.

# Deeplink

  * 링크를 클릭하면 특정 앱으로 이동하거나, 앱이 없다면 설치를 유도하거나, 앱이 있다면 앱 내 특정페이지로 이동시킬 수 있다. 
  * 활용: 모바일 마케팅광고에 흔히 사용하는 방식으로 클릭시 앱이 없다면 앱설치 유도하는 페이지로, 앱이 있다면 앱 내 특정페이지로 이동시킨다.

  
  
  

# Deeplink 3가지 방식

  * URI 스킴 방식 : 앱에 URI 스킴(scheme) 값을 등록하여 딥링크 사용
  * 앱링크(App Link) : Android 제공 - 도메인 주소를 이용한 딥링크 사용
  * 유니버셜 링크 (Universal Link) : iOS 제공 - 도메인 주소를 이용한 딥링크 사용

  
  
  

## 1 URI scheme

![https://www.airbridge.io/blog/deeplink-101-for-marketers-and-developers](https://assets-global.website-files.com/607008c6d94a9d637e9a1b5e/62fc5889746fed112ae27c78_c7tZQN4hmkM2vGCpnagTHfwLO537kliihBl-zdxePv5t5lAYDjk6JfXipcQbtqW4fAq4nKYLoIIxjoekZzvjrt_oD-LxGR3A6OuR0ufs4uBfE2-5nUaKvIYKlVOROqL5m7EclUM9c_WU6OjmDQISyAU.png)

가장 일반적으로 딥링크를 사용하는 방식은 URI Scheme 방식이다.  
이 방식의 한계는 점차 앱이 다양해지면서 앱 스킴값이 중복되는 경우가 존재한다는 것이다. 이런 경우 개발자가 원하는 대로 작동하지 않을 수 있다.

## 2 유니버셜 링크와 앱 링크

유니버설 링크(Universal Links)와 앱 링크(App Links)는 각각 iOS와 Android에서 사용되는 딥 링킹 프로토콜이다.  
도메인은 딱 1개밖에 없기때문에 이들은 URI 스키마의 한계를 극복하기 위해 앱의 도메인 이름을 운영 체제(OS)에 등록하여 소유권을 증명하는 방식을 사용한다.  
여기서 도메인이름이란? `https://sowon-dev.github.io/categories/Android/` 에서 domain name은 `sowon-dev.github.io`이다.

이 방식에도 한계가 존재한다.  
유니버셜링크는 구글에서만, 앱링크는 사파리에서만 정상 작동되고 다른 앱이나 브라우저에서 작동이 안될 수 있다.

![https://www.airbridge.io/blog/deeplink-101-for-marketers-and-developers](https://assets-global.website-files.com/607008c6d94a9d637e9a1b5e/62fc5889bfab9a2428897cee_tMIk_94XMbU_D5iYHKEmxSsZVB4Ei1E8sPF88cajh6AI3Q3YSXwQduYryDxZKEXn0GE1u_t46Pj8exzs9HfHUbNPSle23Q-SbTKG1ntud1ajlXJCzrJL-KW1uwATktTBsPNy3sxiApRfa_9BcckceMg.png)

결론적으로 현재까진 3가지 방식(URI 스킴 방식, 유니버셜링크, 앱링크)을 모두 사용해야한다.

  
  
  

# 참고

  * <https://www.airbridge.io/blog/deeplink-101-for-marketers-and-developers>
  * [https://help.dfinery.io/hc/ko/articles/360039757433-딥링크-Deeplink-URI스킴-유니버셜-링크-앱링크-구분과-이해](https://help.dfinery.io/hc/ko/articles/360039757433-%EB%94%A5%EB%A7%81%ED%81%AC-Deeplink-URI%EC%8A%A4%ED%82%B4-%EC%9C%A0%EB%8B%88%EB%B2%84%EC%85%9C-%EB%A7%81%ED%81%AC-%EC%95%B1%EB%A7%81%ED%81%AC-%EA%B5%AC%EB%B6%84%EA%B3%BC-%EC%9D%B4%ED%95%B4)

#[Backjoon](/tags/Backjoon/)[패스트캠퍼스(초격차Java/Spring)](/tags/%ED%8C%A8%EC%8A%A4%ED%8A%B8%EC%BA%A0%ED%8D%BC%EC%8A%A4-%EC%B4%88%EA%B2%A9%EC%B0%A8Java-Spring/)
