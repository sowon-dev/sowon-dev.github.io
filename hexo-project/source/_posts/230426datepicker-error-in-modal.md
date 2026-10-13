---
title: "팝업(모달)창에서 datepicker 적용 안되는 오류 해결법"
date: 2023-04-25 21:32:46
tags: []
categories:
  - Backend
  - JSP
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">근데 문제는 리스트화면의 datepicker는 잘 작동하는데 팝업창의 datepicker는 전혀 작동하지않았다.
    이런 에러가 있고 이런 것까지 오전내내했는데 안되는데 뭐가 문제일까요 하고 여쭤봤더니 5분만에 해결해주셨다.</p>
</div>

<!-- more -->

화면작업을 하는데 리스트화면에서도 부트스트랩 datepicker를 사용하고 리스트화면의 상세보기 버튼을 눌러 팝업창을 띄우는데 거기서도 datepicker를 써야했다.  
근데 문제는 리스트화면의 datepicker는 잘 작동하는데 팝업창의 datepicker는 전혀 작동하지않았다.  
달력아이콘을 클릭해도 달력이 안나오고 input을 클릭해도 포커싱은 되는데 달력이 안나오니 환장할 노릇.

오전 내내 이 문제를 가지고 구글링해서 여러 방법을 시도했다.

# 원인찾기

디버깅해보니 캘린더 클릭시 아래 div태그가 disploy:none에서 display:block으로 바뀌지않는 문제였다.

```html
<div id="ui-datepicker-div" style="display=none;">
	//중략
</div>
```

  
  
  

# 시도1 : 팝업화면 show 이벤트 적용

리스트화면에 팝업show 이벤트 적용하기 실패했다.

```java
$('#modal').on('show', function () {
    $.fn.modal.Constructor.prototype.enforceFocus = function () { };
});
```

혹시몰라서 팝업창 스크립트에서도 아래 코드 적용해봤지만 실패했다.

```java
$.fn.modal.Constructor.prototype.enforceFocus = function () { };
```

  
  
  

# 시도2 : 팝업화면 shown 이벤트 적용

리스트화면에 팝업 shown 이벤트 적용도 실패했다.

```java
$('#modal').on('shown', function () {
    $.fn.modal.Constructor.prototype.enforceFocus = function () { };
});
```

  
  
  

# 시도3 : z-index주기

혹시나하고 z-index를 줘봤지만 역시나 실패했다.

```java
style="z-index:10000;
```

  
  
  

# 시도4 : 강제로 div태그 display:block주기

팝업창 내에서 달력아이콘에 온클릭이벤트를 걸어 toggle을 줘봤지만 실패했다.

```js
$('#달력아이콘').on('click', function () {
    $("#ui-datepicker-div").toggle()
});
```

  
  
  

# 해결

비흡연자지만 담타를 가시는 차장님을 쫄래쫄래 따라가서 여쭤봤다.  
이런 에러가 있고 이런 것까지 오전내내했는데 안되는데 뭐가 문제일까요 하고 여쭤봤더니 5분만에 해결해주셨다.

나의 경우 스크립트와 link를 중복 선언한게 문제였다.  
그래서 리스트화면의 스크립트태그, link태그는 그대로 두고 팝업창에 선언한 스크립트태그와 link태그를 삭제했더니 잘 작동했다!

```
<link rel="stylesheet" type="text/css" href="/resources/css/bootstrap.css" /> //삭제
<link rel="stylesheet" type="text/css" href="/resources/css/base.css" /> //삭제
<link rel="stylesheet" type="text/css" href="/resources/css/jquery_ui.css" /> //삭제
<script src="/resources/js/jquery_min.js"></script> //삭제
<script src="/resources/js/jquery-ui.min.js"></script> //삭제
```

유레카!  
감사합니다 차장님!
