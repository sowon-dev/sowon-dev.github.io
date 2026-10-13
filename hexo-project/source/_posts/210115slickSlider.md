---
title: "[오류일지] slick slider 라이브러리 적용 안 되는 에러"
date: 2021-01-14 16:56:40
tags:
  - "오류일지"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'slick slider 라이브러리 적용 안 되는 에러' 실행 및 개발 과정에서 발생하는 오류 현상과 원인을 분석한 글이다.
    관련 환경 설정과 코드를 알맞게 수정하여 정상적으로 동작하도록 해결할 수 있다.</p>
</div>

<!-- more -->

## [slick slider 라이브러리](http://kenwheeler.github.io/slick/)

슬라이드배너기능을 구현하기위해 슬릭 라이브러리를 사용했다.  
slick slider는 jQuery 기반으로 만들어진 라이브러리이다. 따라서 jQuery가 필요하다.  
슬라이더 라이브러리는 다양하지만 슬릭 슬라이더 라이브러리의 홈페이지가 가장 친절하다.

라이브러리를 사용하기 위해서 스크립트와 css를 연결해줘야한다.  
홈페이지에서 `Downliad Now`를 통해서 ZIP파일로 다운로드한 뒤 프로젝트에 넣어도 좋고 아래 jsDelivr CDN를 이용해도 좋다.  
아래 코드를 프로젝트에 붙여넣기만 하면 바로 사용가능하다.

```js
CSS

<link rel="stylesheet" type="text/css" href="//cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css"/>

JS

<script type="text/javascript" src="//cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js"></script>
```

  
  
  

## 문제상황

CSS와 JS headerSet에 적용시켰으나 slick.css가 제대로 적용되지않았다.  
슬릭의 클래스명이 자동으로 적용되어야한다.

  * 적용되지 않은 모습  
![정상작동되지 않는 모습](/img/210115slickBad.PNG)

  
  
  

## 해결방법

CSS는 우선순위가 있다. 이 순서는 외워야한다.

>   1. 기본적으로 뒤에 나오는 css가 우선순위가 높습니다. 
>   2. !important > inline style attribute > id > class, 다른 attribute, 수도클래스(:first-child같은 것) > tag element, 수도엘레먼트(::before같은 것) 순으로 우선순위가 높습니다.
>   3. 우선순위가 같다면 개수가 많은 css가 우선순위가 높습니다.  
> 출처 : [ZeroCho 블로그](https://www.zerocho.com/category/CSS/post/588cb95ca63e64132496a5d5)
> 

  * 잘 적용된 모습  
![정상작동](/img/210115slickGood.PNG)

#[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)
