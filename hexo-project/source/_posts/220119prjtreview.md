---
title: "닷넷프로젝트를 끝내며 코드리뷰가 내게 남긴 것"
date: 2022-01-19 02:32:49
tags:
  - "회고록"
categories:
  - Reflections
  - 회고록
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'닷넷프로젝트를 끝내며 코드리뷰가 내게 남긴 것'에 참여하고 주요 발표 내용과 배운 점을 정리한 글이다.
    기존 4개의 역할(Admin / Owner / Super / Member)이 있었다. 한 눈에 봐도 Super의 역할이 모호했다.</p>
</div>

<!-- more -->

한 달간 진행되었던 네번째 프로젝트가 끝이 났다!  
처음 사용하는 C#에다가 닷넷프레임워크, 그리고 Visual Studio, MSSQL, Azure까지!  
모든 것이 새롭게 다가왔고 정말 열심히 배웠고 큰 성장을 이루어냈다.  
잠깐만 갑자기 C#에다가 닷넷??!

그렇게 됐다.  
회사의 일은 가끔(또는 자주) 내 뜻대로 되지 않는 법. 이번에 맡은 프로젝트는 닷넷 프레임워크를 사용했다.  
아직 스프링프레임워크도 깊게 보지 못한 내게 새로운 언어와 새로운 프레임워크는 혼돈의 카오스 그 자체였다.  
절망하기보단 `이왕 해야 할 거! 최선을 다해 빨리 성장하자 하나라도 더 알자`는 마음가짐으로 열정적으로 임했다.  
그래서 그런지 정말 많은 것들을 배울 수 있었다.

DDD도 처음이고 CQRS도 처음이었다. 혼자 부트스트랩으로 페이지도 만들고 저장 프로시저 이용해서 쿼리도 짜고 EF도 이용해봤다.  
성장하고자하는 마음 하나로 한달  
닷넷프레임워크의 여러 장점 중 가장 좋았던 점은 시간연산이 굉장히 편하다는 점이다!! 날짜 포맷팅도 `.ToString("yyyy-MM-dd")` 이런식으로 정말 간단하다! 최고

  
  

## Keep

현재 만족하고 있는 부분과 계속해서 이어갔으면 하는 부분

  1. 명확한 단어 사용을 위한 단어 합의를 위해 노력했다.  
기존 4개의 역할(Admin / Owner / Super / Member)이 있었다. 한 눈에 봐도 Super의 역할이 모호했다.  
프로젝트 구조와 요구사항을 파악하고 나서 역할의 이름을 Super에서 Manager로 변경을 제안했다.  
몇몇 기능 개발이 되어있던 상태였기때문에 변경에 있어서 고민이 많았지만 “지금이라도 잡아야 나중에 유지보수까지 편해집니다”라는 의견을 피력했고 다행히 내 의견이 받아들여졌고 초반에 합의한 덕분에 후반부 작업이 훨씬 수월해졌다!

  2. CSR와 SSR 구분 명확하게 할 수 있다.  
서버사이드랜더링(SSR)과 클라이언트사이드랜더링(CSR)을 확실하게 구분할 수 있고 나만의 우선순위도 생겼다.

  * 우선순위: SSR > CSR  
꼭 필요한 경우가 아니면 서버사이드랜더링을 사용하는 것이 좋다.  
그 이유로는 첫째, 최초 로딩 속도가 빠르다 두번째, SEO최적화, 크롤러에 대응하기 용이하다는 점이 있다.

닷넷프레임워크에서는 서버사이드랜더링으로 Razor를 사용해보았다. `@`를 사용하며 간단한 처리는 컨트롤러를 통하지않고 html에서 직접 서비스를 호출하여 처리할 수도 있다.

  3. Bootstrap을 자유자재로 구사할 수 있다.  
항상 템플릿을 가져와서 써봤지 직접 bootstrap으로 화면을 구현한 적은 처음이다.  
처음에는 내가 원하는 대로 row와 col 나누는 게 너무 어려웠는데 한 번 적응하고 나니 훨씬 편했다.  
또 기존에는 style속성으로 각 태그에 css를 변경하곤 했으나 비효율적이며 통일성이 떨어졌다. Bootstrap class를 사용하니 훨씬 편했다.

  * [참고: Bootstrap Docs](https://getbootstrap.com/docs/5.1/getting-started/introduction/)

  4. Auth policy등 enum타입으로 사용하여 휴먼에러를 줄였다.

  
  
  

## Problem

개선이 필요하다고 생각되는 부분

  1. DDD의 심도깊은 이해와 EF 사용  
이번에 처음 CQRS를 사용하면서 ORM(object-relational mapper)인 Entity Framework를 사용해봤다.  
Application Layer는 다루었으나 Domain Layer는 많이 다루지 못해 아쉬움이 있다.  
EF는 아주 간단한 Include와 Where만을 사용했다. 조금 복잡하다싶으면 나에게 익숙한 저장 프로시저를 이용했다. EF만 잘 사용한다면 효율적인 쿼리를 구현할 수 있었을텐데 아쉬움이 남는다.

  * [참고: ORM vs SQL Mappeer](https://sowon-dev.github.io/2021/03/22/210323jpaVSjdbc/#%F0%9F%86%9ASQL-Mapper-vs-ORM)
  * [참고: DDD Application Layer란?](https://incheol-jung.gitbook.io/docs/q-and-a/architecture/ddd)

  2. UnitTest를 못한 점  
프로젝트기한이 촉박해 UnitTest를 거의 하지 못해서 아쉬움이 무척 남는다.

  
  
  

## Try

Problem의 해결책이 될 수 있는 부분

  1. DDD의 여러 사례 공부와 Domain Layer 공부하기  
[Entity Framework Docs](https://docs.microsoft.com/en-us/ef/core/querying/)

  2. UnitTest를 손에 익히기  
손에 익으면 프로젝트 기한이 촉박해도 빠르게 test code를 짤 수 있다.

  
  
  

## 코드리뷰

이번 코드리뷰는 질문과 답변을 통해 이루어졌다. 회사코드라서 모든 걸 다 적을 수 없고 적을 수 있는 것만 포편적인 예시를 들어 적어보려고 한다.

### 페이지 이동할 때 3가지 방식 중 우선순위가 있나요?

페이지 이동할 때 3가지 방식이 있다.

  1. razor : `@Url.Action("Board", "Admin", new {id=@id})`
  2. asp.net: `<a asp-action="Board" asp-controller="Admin" asp-route-id="@id">`
  3. js: `location.href="/Admin/Board/"+@id`

이 중 razor와 asp-action을 이용한 방식은 SSR이고 js는 CSL이다.  
세 가지 방식 중에 우선순위가 있는 방식은 없다. 상황에 맡게 사용하면 된다!

#[회고록](/tags/%ED%9A%8C%EA%B3%A0%EB%A1%9D/)
