---
title: "[Hexo]헥소블로그 구글애드센스설정(초간단)"
date: 2021-04-25 17:08:55
tags:
  - "Hexo"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">헥소블로그 구글애드센스설정(초간단)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    블로그 프로젝트에서 _config.yml를 연다. 혹시나 _config.yml이 두 개인 경우 사용하는 테마내의 _config.yml를 열어주면 된다.</p>
</div>

<!-- more -->

Hexo 블로그에 구글애드센스를 설정해보자. 

# 구글애드센스 가입

[구글애드센스](https://www.google.co.kr/intl/ko_kr/adsense/start/?utm_campaign=1001272-adsense-acquisition-kr-ko-hybrid-bkws)에서 시작하기 버튼을 클릭한 뒤 아래 정보를 입력한다.

  * 웹사이트: 자신의 헥소 블로그 주소 
  * 이메일주소: 자신의 구글 이메일주소

저장하고 계속하기를 클릭하면 구글 애드센스 코드를 입력하라는 안내메세지가 나온다.  
여기서 클라이언트ID를 복사한다.  
참고로 client_id는 ‘ca-알파벳세글자-숫자여러개’로 구성된다.

  
  
  

# 헥소블로그에 구글애드센스 아이디 넣기

블로그 프로젝트에서 `_config.yml`를 연다. 혹시나 `_config.yml`이 두 개인 경우 사용하는 테마내의 `_config.yml`를 열어주면 된다.  
헷갈릴 경우 `_config.yml` 둘 다 연뒤 `AdSense` 키워드로 검색해서 검색결과가 있는 `_config.yml`를 찾으면 된다.  
복사해둔 클라이언트ID를 작은 따옴표 안에 붙여넣고 DEPLOY해준다.  
구글봇이 내 블로그가 구글애드센스에 적합한지 체크를 한 뒤 구글애드센스를 이용할 수 있다. 이 과정은 최대 2주일정도 소요된다고한다.  
나는 5일정도 걸렸다. 

```xml
# Google AdSense unit configurations
-
	# Where should the widget be placed, left sidebar or right sidebar
	position: left
	type: adsense
	# AdSense client ID
	client_id: '웹게시자 ID입력' 
	# AdSense AD unit ID
	slot_id: '고객 ID입력'
```

  
  
  

# slot_id넣기

구글 애드센스가 정상적으로 등록되었다면 [구글 애드센스](https://www.google.co.kr/intl/ko_kr/adsense/start/?utm_campaign=1001272-adsense-acquisition-kr-ko-hybrid-bkws)에서 로그인하면 대시보드를 볼 수 있다.  
여기서 [계정] - [계정정보]를 클릭하면 웹게시자ID와 고객 ID를 확인할 수 있다.  
이때 고객 ID를 복사 한뒤 사용하는 테마내의 `_config.yml`를 열고 slot_id의 작은 따옴표 안에 붙여넣는다.  
slot_id는 오로지 숫자여러개로 구성되어있다.

```xml
# Google AdSense unit configurations
-
	# Where should the widget be placed, left sidebar or right sidebar
	position: left
	type: adsense
	# AdSense client ID
	client_id: '웹게시자 ID입력'
	# AdSense AD unit ID
	slot_id: '고객 ID입력'
```

이렇게 설정하면 끝!

#[Hexo](/tags/Hexo/)
