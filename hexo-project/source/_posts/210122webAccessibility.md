---
title: "웹접근성"
date: 2021-01-22 02:45:31
tags:
  - "Web Development"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">웹접근성의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    웹 접근성(web accessibility)은 장애인이나 고령자들이 웹 사이트에서 제공하는 정보를 비장애인과 동등하게 접근하고 이용 할 수 있도록 보장하는 것으로 웹 접근성 준수는 법적의무사항이다.</p>
</div>

<!-- more -->

## 웹접근성이란?

웹 접근성(web accessibility)은 장애인이나 고령자들이 웹 사이트에서 제공하는 정보를 비장애인과 동등하게 접근하고 이용 할 수 있도록 보장하는 것으로 웹 접근성 준수는 법적의무사항이다.  
브라우저들은 HTML의 사소한(?) 에러들은 자동으로 고쳐준다.  
따라서 태그가 닫혔는지 굳이 체크하지않아도 괜찮다. 하지만 웹접근성을 준수하기 위해선 직접 닫아줘야한다.

  * 원칙 1 인식의 용이성 (Perceivable) : 모든 콘텐츠는 사용자가 인식할 수 있어야 한다.
    1. 적절한 대체 텍스트 제공해야 한다.
    2. 멀티미디어 콘텐츠에는 자막, 원고 또는 수화를 제공해야 한다.
    3. 콘텐츠는 색에 관계없이 인식될 수 있어야 한다.
    4. 명확한 지시사항 제공해야 한다.
    5. 텍스트 콘텐츠와 배경 간의 명도 대비는 4.5대 1 이상이어야 한다.
    6. 자동 재생 금지
    7. 이웃한 콘텐츠는 구별될 수 있어야 한다.
  * 원칙 2 운용의 용이성(Operable) : 사용자 인터페이스 구성요소는 조작 가능하고 내비게이션 할 수 있어야 한다.
    1. 키보드 사용 보장
    2. 터치(touch) 기반 모바일 기기의 모든 컨트롤은 누르기 동작으로 제어할 수 있어야 한다. (모바일웹)
    3. 깜빡임과 번쩍임 사용 제한
    4. 제목 제공
    5. 적절한 링크 텍스트
  * 원칙 3 이해의 용이성(Understandable) : 콘텐츠는 이해할 수 있어야 한다.
  * 원칙 4 견고성(Robust) : 웹 콘텐츠는 미래의 기술로도 접근할 수 있도록 견고하게 만들어야 한다.
    1. 마크업 오류 방지
    2. 웹 애플리케이션 접근성 준수

![](http://www.cnweb.co.kr/images/business/accessibility_13.gif)

  
  
  

## 웹 접근성 확인 가능한 웹사이트

  * [W3C Markup Validation](https://validator.w3.org/) : 웹 접근성을 위한 HTML 유효성을 확인할 수 있다.
  * [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) : 웹 접근성을 위한 CSS 유효성을 확인할 수 있다.

  
  
  

## 참고

  * <http://www.wa.or.kr/m1/sub1.asp>
  * <https://seulbinim.github.io/WSA/accessibility.html#%EC%9B%B9%EC%A0%91%EA%B7%BC%EC%84%B1%EC%9D%98-%EA%B0%9C%EC%9A%94>
  * <http://www.websoul.co.kr/accessibility/define.asp>

#[Web Development](/tags/Web-Development/)
