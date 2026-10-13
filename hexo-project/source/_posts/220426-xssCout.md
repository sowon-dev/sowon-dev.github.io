---
title: "el태그 대신 <c:out> 사용하는 이유"
date: 2022-04-26 03:25:00
tags: []
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">el태그 대신 <c:out> 사용하는 이유의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    그 중 가장 많이 쓰는건 el태그인데 그 이유는 el태그 사용법이 ${}로 매우 간단하기때문이다.</p>
</div>

<!-- more -->

jsp에서 다양한 방식으로 서버사이드 데이터를 출력할 수 있다.  
그 중 가장 많이 쓰는건 el태그인데 그 이유는 el태그 사용법이 `${}`로 매우 간단하기때문이다.

el태그만 써도 화면에 값이 잘 출력되는데 왜 굳이 `<c:out>`를 사용할까?

## 결론: XSS 방어하기 위해!

`<c:out>`를 사용하면 escapeXml속성을 활용할 수 있다.  
escapeXml를 true로 설정함으로써 가장 간단하게 XSS[(링크)](https://sowon-dev.github.io/2022/04/20/220420XSS/#XSS란)를 방어할 수 있다.

```js
// 1.escapeXml = true 인 경우(디폴트)
<c:out value="<script type='text/javascript'>alert('테스트');</script>"/>

// 2.escapeXml = false 인 경우 == el태그와 동일
<c:out value="<script type='text/javascript'>alert('테스트');</script>" escapeXml="false"/>
```

  1. `escapeXml = true`의 경우, text 그대로 출력된다.
  2. `escapeXml = false` 인 경우나 el태그인 경우, alert창이 실행된다.

따라서 XSS 방어하기 위해서는 `<c:out>`을 사용하는 게 좋다.
