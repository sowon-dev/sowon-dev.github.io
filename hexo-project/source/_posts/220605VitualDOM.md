---
title: "DOM과 가상DOM"
date: 2022-06-05 05:17:57
tags: []
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">DOM과 가상DOM의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    HTML태그들을 작성하면 자바스크립트는 어떻게 읽을까? 한 번쯤 궁금했을 것이다.</p>
</div>

<!-- more -->

React나 Vue.js를 쓸때 가상돔을 많이 얘기한다.  
가상돔을 제대로 알고 싶어 DOM이 뭔지 공부해봤다.

# DOM(Document Object Model)

DOM은 문서객체모델로서 xml이나 html문서에 접근하기 위한 일종의 인터페이스이다.

DOM | 종류  
---|---  
Core DOM | 모든 문서 타입을 위한 DOM 모델,  
HTML DOM | HTML 문서를 위한 DOM 모델, 모든 HTML 요소는 HTML DOM를 통해 접근가능  
XML DOM | XML 문서를 위한 DOM 모델, 모든 XML 요소는 XML DOM를 통해 접근가능  
  
HTML태그들을 작성하면 자바스크립트는 어떻게 읽을까? 한 번쯤 궁금했을 것이다.  
자바스크립트는 HTML, head, body등의 요소를 구조화 한다.  
구조화에는 다양한 방식이 있다.  
이때 DOM은 [트리구조](https://sowon-dev.github.io/2023/02/02/230203Btree/#%ED%8A%B8%EB%A6%AC%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%EB%9E%80)를 형성한다. 

![https://www.w3schools.com/js/js_htmldom.asp](https://www.w3schools.com/js/pic_htmltree.gif)

즉 상위 노드와 하위 노드가 트리처럼 연결되어 있는데 여기서 만약 서른마흔다섯번째 노드를 update시키면 어떻게 될까?  
DOM은 수많은 노드들 중에서 특정 노드를 찾게 되고 그 과정에서 비용이 발생한다.  
만약 한 번의 update가 연결된 다른 500개의 노드들에 변경을 일으킨다면? 점점 더 많은 비용이 발생하게 된다.

이를 해결하기 위해 등장한 것이 바로 가상돔(Virtual DOM)이다.

  
  
  

# 가상돔(Virtual DOM)

가상돔은 이름 그대로 실제DOM이 아닌 가짜DOM(HTML돔의 추상화)이다.  
웹페이지에서 사용자에 의해 이벤트가 발생된다면(update) 실제돔을 바로 수정하지않고, 가상돔을 랜더링한 뒤 이전의 돔과 비교해서 변경된 부분만 실제돔에 반영한다. 이로써 실제돔의 변경을 최소화하여 성능을 향상시킬 수 있다.
