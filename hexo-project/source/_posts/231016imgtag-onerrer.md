---
title: "[HTML]IMG태그 기본이미지설정(DEFAULT IMG, ONERROR속성) 에러 해결"
date: 2023-10-15 20:01:56
tags:
  - "HTML&CSS"
categories:
  - Frontend
  - HTML&CSS
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">찾아보니 onerror 속성을 찾아서 손쉽게 처리할 수 있었다. 그런데 여전히 디폴트이미지를 못 불러오는 에러가 발생했다.
    이미지태그사용시 src경로에 이미지가 없다면 기본 이미지를 설정하고 싶었다.</p>
</div>

<!-- more -->

이미지태그사용시 src경로에 이미지가 없다면 기본 이미지를 설정하고 싶었다.  
찾아보니 onerror 속성을 찾아서 손쉽게 처리할 수 있었다. 그런데 여전히 디폴트이미지를 못 불러오는 에러가 발생했다.

# 기존코드

```jsp
<img src="/resources/custom/images/main_${idx}.png" onerror="/resources/custom/images/main_default.png" alt="${name}이미지">
```

잘했다고 생각했으나 여전히 이미지가 엑박이 떴다.  
해당 경로에 이미지도 제대로 있는 걸 확인했는데 왜 onerror에서 설정한 경로의 기본이미지가 보이지않을까?

  
  
  

# 해결코드

```jsp
<img src="/resources/custom/images/main_${idx}.png" onerror="this.src='/resources/custom/images/main_default.png'" alt="${name} 아이콘">
```

onerror는 함수가 들어가는 곳으로 src속성과는 다르다. 따라서 그냥 경로를 입력하는 것이 아니라 함수로 입력해야한다.  
따라서 `this.src=`를 추가하여 함수로 디폴트png가 있는 src로 연결하도록 바꿔주니 원하는대로 정상작동했다.

해결!

  
  
  

# 참고

  * [onerror Event](https://www.w3schools.com/jsref/event_onerror.asp)

#[HTML&CSS](/tags/HTML-CSS/)
