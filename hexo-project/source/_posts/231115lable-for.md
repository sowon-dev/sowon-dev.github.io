---
title: "[HTML] radio/checkbox 클릭 안 되는 오류가 label for 때문이라고?"
date: 2023-11-14 16:22:56
tags:
  - "HTML&CSS"
categories:
  - Frontend
  - HTML&CSS
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">radio와 checkbox가 클릭이 안되는 오류가 발생했다.
    css문제인 줄 알고 디자인팀에 문의했는데 css문제가 전혀 없었고 id를 추가하면 됩니다~하는 답변을 받았다.</p>
</div>

<!-- more -->

radio와 checkbox가 클릭이 안되는 오류가 발생했다.  
css문제인 줄 알고 디자인팀에 문의했는데 css문제가 전혀 없었고 `id를 추가하면 됩니다~`하는 답변을 받았다.

# 문제코드

FORM으로 데이터를 넘길거니까 name과 value만 신경써서 작업했다.

```html
<input type="radio" name="reply_type" value="email" checked><label for="email">E-mail</label>
<input type="radio" name="reply_type" value="post" ><labelfor="post">우편</label>
```

그런데 라디오버튼이 클릭도 안되고 post로 보내도 값이 넘어오지않았다!  
어디가 문제일까?

  
  
  

# 해결코드

원인은 `label for`이었다.  
웹접근성을 위해 디자인팀에서 추가했는데 내가 미처 확인하지 못했다.  
`label for`를 쓴다면 input 속성에 id값과 일치 시켜줘야한다!

```html
<input type="radio" name="reply_type" value="email" id="email" checked><label for="email">E-mail</label>
<input type="radio" name="reply_type" value="post" id="post" ><labelfor="post">우편</label>
```

해결!

  
  
  

# 그럼 checkbox의 경우는?

checkbox도 이와 동일하다.  
name과 value를 잘 넣었는데도 눌러지지않는다면 `lable for`값과 `id`값이 일치하는지 의심해보자  
그리고 사소한 실수 하지말자!

  
  
  

# 근데 label은 왜 쓸까?

  1. input 태그 타입 중 month, number, password, radio, range같은 경우 placeholder속성이 없기에 어떤 input인지 설명해줄수가 없다. 따라서 label을 사용해서 명시적으로 용도를 나타내줄수있다.
  2. 웹접근성을 위해 필요하다.

  
  
  

# 참고

  * [TCP SCHOOL - label태그의 for 속성](https://www.tcpschool.com/html-tag-attrs/label-for)
  * [개발자의 낙원 - label태그 왜 쓸까?](https://batcave.tistory.com/79)

#[HTML&CSS](/tags/HTML-CSS/)
