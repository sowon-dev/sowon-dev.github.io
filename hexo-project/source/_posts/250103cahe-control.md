---
title: "웹 캐싱방지"
date: 2025-01-02 16:54:36
tags: []
categories:
  - Backend
  - CS
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">메타데이터 설정시 캐싱 방지 가능하지만 불필요한 트래픽을 많이 유발할 수 있으므로 정적 리소스 버전 명시 추가 추천</p>
</div>

<!-- more -->

테스트까지 확인 다하고 실서버배포했는데 js함수를 못찾는다는 에러가 떴다.  
바뀐 js를 못 찾는 문제였다. 

웹 캐싱문제는 강력새로고침을 하면 해결되지만 일반 사용자는 그마저도 복잡할 수 있다.  
따라서 캐싱을 방지해야했다.

# 캐싱

캐시를 확인해보니 페이지마다 세세하게 처리되어있었다.  
에러가 발생한 곳은 주문하기 페이지였다. 

  * cache-control: private
  * [Cache-Control](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Cache-Control);

  
  
  

# 해결법1. 메타데이터 설정

메타데이터에 아래 설정울 추가하면 캐싱을 방지할 수 있지만 수정이 별로 없는 사이트나 페이지에 설정하는 경우 불필요한 트래픽을 많이 유발할 수 있다.

```plain
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
```

불필요하게 트래픽을 유발하면 사이트가 느려지므로 정적리소스에 버전을 명시하기로 했다.

  
  
  

# 해결법2. 정적 리소시 버전 명시

쿼리스트링에 버전을 직접 명시해줘도 되지만 레거시는 컴포넌트가 전혀 분리되지않은 화면이었다.  
특정 부분 1개만 수정하더라도 관련된 페이지가 20개가 넘어가서 불필요하게 복붙을 해야만했다.  
따라서 자주 사용하는 common js파일이나 css파일에만 쿼리스트링으로 항상 새로 불러오도록 했다.

```js
// Header.jsp나 공통.jsp에 명시
<c:set var="dateNow" value="<%=new java.util.Date()%>" />
<c:set var="verStamp"><fmt:formatDate value="${dateNow}" pattern="yyyyMMddhhmmss" /></c:set>

// 각 jsp 화면상단에 버전 명시
<script type="text/javascript" src="/js/common.js?ver=${verStamp}" ></script>
```
