---
title: "[Hexo]헥소블로그 방문자수 조회수 간단하게 처리하기(초간단)"
date: 2021-03-22 15:00:00
tags:
  - "Hexo"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">헥소블로그 방문자수 조회수 간단하게 처리하기(초간단)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    busuanzi플러그인은 중국어지만 구글의 힘을 빌려서 사용가능하다. 간단하게 스크립트코드와 html태그를 넣어서 조회수를 처리할 수 있다.</p>
</div>

<!-- more -->

블로그를 운영하다보면 조회수가 궁금해지기마련이다.  
구글서치콘솔로 조회수를 확인할 수 있지만 블로그에서 바로 확인하면 더욱 좋을 것이다. 헥소블로그는 지킬블로그보다 정보가 많이 없어서 구글링을 좀 많이 했다. 그랬더니 내가 쓰고 있는 hexo-icarus테마는 busuanzi플러그인을 통하여 초간단하게 조회수와 방문자수를 처리할 수 있었다.

  * 사용중인 hexo테마 : [icarus](https://github.com/ppoffice/hexo-theme-icarus)

  
  
  

## 조회수 기능 등록 방법

[busuanzi](http://busuanzi.ibruce.info/)플러그인은 중국어지만 구글의 힘을 빌려서 사용가능하다. 간단하게 스크립트코드와 html태그를 넣어서 조회수를 처리할 수 있다.  
하지만 내가 사용중인 hexo icarus테마는 true/false만으로도 적용이 가능하다! 세상 간편!  
물론 커스텀하고 싶다면 [공식사이트](http://ibruce.info/2015/04/04/busuanzi/)를 통해 원하는 대로 적용할 수 있다.

  1. 프로젝트에서 `themes/hexo-theme-icarus/_config.yml` 파일을 연다.
  2. `busuanzi`를 검색하여 false를 true로 변경해준다.
  3. 끝!

```xml
# BuSuanZi site/page view counter
# https://busuanzi.ibruce.info
busuanzi: true
# CNZZ statistics
# https://www.umeng.com/web
```

true로 바꿔주기만하면 블로그 footer에 전체 방문자수와 조회수가 출력될뿐아니라 각 포스팅의 조회수도 확인 가능하다!

![](/img/210323postvisitercmt.png)

초간단!

  
  
  

## 참고

  * <https://blog.zhangruipeng.me/hexo-theme-icarus/Plugins/Analytics/icarus-user-guide-web-analytics-plugins/#BuSuanZi-Web-Counter>

#[Hexo](/tags/Hexo/)
