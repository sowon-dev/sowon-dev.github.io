---
title: "사내 101번서버에 접속하세요라는 의미(DNS 정보조회)"
date: 2022-01-05 16:38:12
tags:
  - "오늘또못알아듣고말았습니다"
categories:
  - Backend
  - Server
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">사내 101번서버에 접속하세요라는 의미(DNS 정보조회)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * nslookup: 도메인 이름에 대한 정보를 조회할 때 사용할 수 있는 명령어이다.</p>
</div>

<!-- more -->

한참 모든 것이 궁금한 시기인 나는 오늘도 궁금한 점이 생겼다.  
오늘 팀장님이 사내서버에 프로젝트를 올렸으니 101번(임의번호)서버로 접속해서 확인해보라고 하셨다.

사내 서버의 도메인을 이미 알고있었기때문에 해당 도메인인 link.sowonDev.com(임의도메인)으로 접속하니 잘 접속이 되었다.  
여기서 궁금증한 건 사내도메인 link.sowonDev.com을 왜 101번서버라고 부르는 지였다.

  
  
  

## 도메인 정보를 조회하는 명령어

  * nslookup: 도메인 이름에 대한 정보를 조회할 때 사용할 수 있는 명령어이다.

cmd를 열어 아래와 같이 nslookup명령어를 입력하면 DNS서버에 해당 도메인정보를 요청하는 것이고 응답으로는 도메인정보가 나온다.  
요청을 끝내고 싶으면 exit을 통해서 명령어작성에서 빠져나오면 된다.

```plain
//명령어
$ nslookup [정보를알고싶은도메인]

//명령어 예시
$ nslookup link.sowonDev.com

//응답
권한 없는 응답:
이름: link.sowonDev.com
Address: 123.000.00.101

//명령종료
$ exit
```

자 이제 왜 101서버라고 불리는 지 감이 잡혔다.  
응답을 보면 address부분의 제일 마지막 IP가 101이기 때문이다!  
다른 사이트들도 궁금해졌다.

```plain
$ nslookup naver.com

권한 없는  응답:
이름: naver.com
Address: 223.130.200.107
	223.130.195.200
	223.130.200.104
	223.130.195.95
```

네이버 예시에서 알 수 있듯 네이버급의 규모가 큰 프로젝트는 4개의 서버를 사용한다.  
신기해👍

그리고 좀 더 구글링해보니 굳이 cmd가 아니더라도 DNS recode를 조회할 수 있는 사이트를 찾을 수 있었다.  
IPv4 Address뿐만 아니라 회사위치와 회사명도 나온다!

  * <https://www.nslookup.io/>

위 사이트에서 google.com을 검색하면 IPv4는 물론 AAAA records인 IPv6 address도 확인할 수 있다!  
재밌다😎

  
  
  

## 결론

새로운 지식 습득은 언제나 재밌다.  
그려려니 넘어가지말고 꼭 구글링해보자!

#[오늘또못알아듣고말았습니다](/tags/%EC%98%A4%EB%8A%98%EB%98%90%EB%AA%BB%EC%95%8C%EC%95%84%EB%93%A3%EA%B3%A0%EB%A7%90%EC%95%98%EC%8A%B5%EB%8B%88%EB%8B%A4/)
