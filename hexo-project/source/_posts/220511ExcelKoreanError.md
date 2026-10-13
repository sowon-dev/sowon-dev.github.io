---
title: "JSP에서 엑셀다운로드할때 한글깨짐현상을 해결하는 가장 간단한 방법"
date: 2022-05-10 21:48:42
tags: []
categories:
  - Backend
  - JSP
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'JSP에서 엑셀다운로드할때 한글깨짐현상을 해결하는 가장 간단한 방법' 실행 및 개발 과정에서 발생하는 오류 현상과 원인을 분석한 글이다.
    JSP에서 엑셀다운로드를 할때 한글깨짐 현상이 나타났다. 이를 해결할 수 있는 가장 간단한 방법이 있다.</p>
</div>

<!-- more -->

JSP에서 엑셀다운로드를 할때 한글깨짐 현상이 나타났다. 이를 해결할 수 있는 가장 간단한 방법이 있다.

## 원인

이럴때는 meta태그에 utf-8이 잘 설정되어있는지 확인하면 된다.  
만약 utf-8설정을 찾을 수 없다면 코드를 head사이에 추가하면 된다.

  
  
  

## 해결

```html
<head>
// (중략)
<meta http-equiv='Content-Type' content='application/vnd.ms-excel; charset=utf-8'/>
</head>
```
