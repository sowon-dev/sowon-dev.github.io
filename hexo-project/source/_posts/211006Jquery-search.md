---
title: "[jQuery] 3depth가 있는 ul의 검색기능 구현"
date: 2021-10-05 15:00:00
tags:
  - "jQuery"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">3depth가 있는 ul의 검색기능 구현의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    제이쿼리를 이용하여 3뎁스 검색기능을 추가하고 싶었다.</p>
</div>

<!-- more -->

제이쿼리를 이용하여 3뎁스 검색기능을 추가하고 싶었다.  
구글링한 예시들은 죄다 1뎁스여서 내가 원하는대로 만들 수 없었다.  
내가 원하는 것은 검색어입력시 1뎁스와 2뎁스는 그대로 노출되고 3뎁스에 검색이 적용되어 결과가 노출되는 것이다.

## html코드

```html
<input type="text" placeholder="메뉴 검색" id="searchInput" onkeyup="func.filter();return false">
<ul id="top">
  <li>
    <h5><div style="display:inline;">전체메뉴</div></h5>
	<ul style="display: block;" id="topLevel">
      	<li data-menu-nm="댑스1" data-depth="1">
		<h5>메뉴1</h5>
			<ul style="">
        		<li data-menu-nm="메뉴1-1" data-depth="2">
					<h5>메뉴1-1</h5>
				</li>
          		<li data-menu-nm="메뉴1-2" data-depth="2">
					  <h5>메뉴1-2</h5>
				</li>
			</ul>
    	</li>
      	<li data-menu-nm="댑스1" data-depth="1">
		<h5>메뉴2</h5>
			<ul style="">
				<li data-menu-nm="메뉴2-1" data-depth="2">
					<h5>메뉴2-1</h5>
				</li>
				<li data-menu-nm="메뉴2-2" data-depth="2">
					<h5>메뉴2-2</h5>
				</li>
			</ul>
     	</li>
	</ul>
	</li>
</ul>
```

  
  
  

## js코드

```js
let func;
$(document).ready(function() {
  func = {
   filter: function(){
          $("#top ul").slideDown(100);
          if($('#searchInput').val()=="")
            $("#topLevel ul li").css('display','');
            else{
            $("#topLevel ul li").css('display','none');
            $("#topLevel ul li[data-menu-nm*='"+$('#searchInput').val()+"']").css('display','');
          }
          return false;
    }
  }
});
```

  
  
  

## 예시

result 탭에서 메뉴검색 인풋에 `2-1`을 검색하면 전체메뉴, 메뉴1, 메뉴2 그리고 메뉴2-1가 잘 출력되는 것을 확인할 수 있다.

See the Pen [ ](https://codepen.io/gracehopperdev/pen/MWoMdxZ) by sowon-dev ([@gracehopperdev](https://codepen.io/gracehopperdev)) on [CodePen](https://codepen.io).

  
  
  

## 여담

제이쿼리로 선택자와 그 하위 태그 선택을 하는데 있어 많이 헷갈렸다.  
구글링하다가 에라이 던질뻔했다.  
그냥 get방식으로 where 조건절 걸어서 db 다시 다녀올까 했지만 이미 list뿌리면서 가져온 데이터인데 굳이 db까지 다시 다녀오는 건 자원낭비라는 생각이 들었다.  
어떻게든 제이쿼리로 끝내고싶어서 열심히 구글링하였다.  
포기하지않고 끝까지 해낸 나자신 칭찬해!  
이 경험으로 선택자에 대해 깊이 알 수 있었다.

#[jQuery](/tags/jQuery/)
