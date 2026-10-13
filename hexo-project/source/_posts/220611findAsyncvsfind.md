---
title: "findAsync와 find의 차이점"
date: 2022-06-11 05:34:55
tags:
  - "C#"
categories:
  - Backend
  - .NET
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'findAsync와 find의 차이점'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    사용해보니 둘 다 동일한 결과가 나왔는데 둘의 차이점이 궁금해서 공부해보았다.</p>
</div>

<!-- more -->

닷넷프레임워크를 사용하다보면서 find 메서드를 사용했는데 비주얼스튜디오가 FindAsync를 추천해줬다.  
사용해보니 둘 다 동일한 결과가 나왔는데 둘의 차이점이 궁금해서 공부해보았다.

## Find

비교적 간단한 구문이다.  
모든 문서를 한 번에 조회한다.  
따라서 데이터양이 작을 때 사용하면 좋다. 가져오는 데이터양이 클때 Find를 쓸 경우 뷰단이 멈춰버릴 수 있다. 이럴때 비동기인 FindAsync로 처리해야한다.

  
  

## FindAsync

모든 DB를 한 번에 조회하지 않는다. return값이 cursor라서 DB cursor에서 문서를 하나씩 검색할 수 있는 interface를 제공한다.  
따라서 데이터양이 클 때 사용하면 좋다. 

여기서 DB cursor란?  
쿼리문에 의해서 반환되는 결과값들을 저장하는 메모리공간을 말한다.

  
  
  

## 참고

  * <https://docs.microsoft.com/en-us/dotnet/api/system.data.entity.dbset.findasync?view=entity-framework-6.2.0>
  * <https://stackoverflow.com/questions/30650722/difference-between-find-and-findasync>

#[C#](/tags/C/)
