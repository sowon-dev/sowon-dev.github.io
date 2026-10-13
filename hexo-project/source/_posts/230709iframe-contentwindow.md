---
title: "[바닐라JS/Pure JS]iframe 내 태그에 접근하고 싶을때(선택자)"
date: 2023-07-08 21:39:21
tags:
  - "VanillaJS"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">iframe 내 태그에 접근하고 싶을때(선택자)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    HTML구조를 최대한 간략하게 작성해보았고 스크립트는 아래와 같이 만들어봤다.</p>
</div>

<!-- more -->

자주 보는 사이트 중 table의 첫번째 tr을 숨기고 싶어서 스크립트 코드를 만들었다.

해당 사이트 HTML 구성이 어떻게 되어있는지 몰라서 차근차근 뜯어보았는데  
iframe 하위에 iframe을 또 부르고 그 하위에 table이 있고 그 하위에 내가 숨기고싶은 tr이 있는 구조였다.

# 코드

```html
<body>
	<iframe id="sub2">
		<iframe id="ifrm">
			<table id="tableList">
				<thead>
				// 중략
				</thead>
				<tbody>
					<tr>첫번째 - 숨김처리 하고싶다</tr>
					<tr>두번째</tr>
					<tr>세번째</tr>
				</tbody>
			</table>
		</iframe>
	</iframe>
</body>
```

HTML구조를 최대한 간략하게 작성해보았고 스크립트는 아래와 같이 만들어봤다.

```js
// 첫번째 tr 숨기기
document.getElementById("sub2").contentWindow.document.getElementById("ifrm").contentWindow.document.getElementById("tableList").querySelector("tbody > tr").style.display = "none";
```

  
  
  

# 개선 필요점

크롬 브라우저에서 테스트하면 가끔 `TypeError: Cannot read properties of null (reading 'contentWindow')` 에러가 발생한다. 어떻게 해결해야하는지 모르겠다. 이 부분 개선필요하다.

  
  
  

# 팀장님 꿀팁🍯

크롬브라우저에선 개발자도구를 통해 1초만에 js선택자코드를 복사할수있다.  
F12에서 요소탭의 HTML코드에서 원하는 HTML태그를 우클릭한 후 복사 > JS경로 복사를 선택하면 자동으로 js선택자코드가 클립보드에 복사된다! 그래서 복붙만 해주면 간편하게 이용하면 끝!

```js
// JS경로 복사를 활용한 간단 버전 
document.querySelector("#tableList > tbody > tr:nth-child(1)").style.display = "none";
```

잘 적용은 되나 가끔 `TypeError: Cannot read properties of null (reading 'contentWindow')` 에러가 여전히 발생한다. 어떻게 해결할수있을까…

#[VanillaJS](/tags/VanillaJS/)
