---
title: "[jQuery] attr과 prop차이"
date: 2022-10-27 19:42:41
tags:
  - "jQuery"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'attr과 prop차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    제이쿼리를 사용하면서 attr와 prop는 아주 유사한 기능인데 어떠한 차이점이 있고 어떤 상황일때 어떤 걸 쓰는 게 더 좋은지 궁금해서 찾아봤다.</p>
</div>

<!-- more -->

제이쿼리를 사용하면서 attr와 prop는 아주 유사한 기능인데 어떠한 차이점이 있고 어떤 상황일때 어떤 걸 쓰는 게 더 좋은지 궁금해서 찾아봤다.

역시 제일 좋은 건 jQuery 공식문서이다.  
jQuery 1.6.0 버전에서부터 jQuery.attr()과 jQuery.prop()가 나눠졌다.

| | jQuery.attr() | jQuery.prop()  
---|---|---  
정의 | changes attributes for that HTML tag. | changes properties for that HTML tag as per the DOM tree  
취급 | HTML 속성 (Attribute) 취급 | javascript 프로퍼티 (Property) 취급  
반환값 | returns the default value (Original state) | returns the current value (Current state)  
  
많은 상황에서 둘은 같은 값을 반환하지만 attr()는 원래 값을 prop()는 현재 값을 반환한다.  
예를 들어보자.

```js
<input type="checkbox" id="test1" checked="checked"> 테스트1
<input type="checkbox" id="test2"> 테스트2
```

위 두가지 체크박스의 차이는 checked가 기본값인지 아닌지이다.  
이를 콘솔에 찍어보면 차이를 발견할 수 있다.

```plain
$("#test1").attr("checked")
$("#test2").attr("checked")

//결과값
checked
undefined
```

```plain
$("#test1").prop("checked")
$("#test2").prop("checked")

//결과값
true
false
```

attr()은 최초 element 랜더링시 defalut value를 반환하지만 prop()는 현재상태를 반환한다.

  
  
  

# 결론

  * `.attr()` : element가 가지는 속성 조회 권장
    * style, src, rowspan
  * `.prop()`: element가 가지는 실제적인 상태 제어 사용 권장
    * form요소의 disabled, selected, checked 속성값 확인 혹은 변경

  
  
  

# 참고

  * <https://api.jquery.com/attr/>
  * <https://api.jquery.com/prop/>
  * <http://net-informations.com/jq/iq/prop.htm>

#[jQuery](/tags/jQuery/)
