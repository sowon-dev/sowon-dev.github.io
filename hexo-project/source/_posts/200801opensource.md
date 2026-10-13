---
title: "오픈소스컨트리뷰톤 온라인미팅1 후기 : 모던 js 오픈소스 기여순서"
date: 2020-07-31 15:00:00
tags:
  - "TIL"
  - "GIT"
categories:
  - Reflections
  - 오픈소스컨트리뷰톤2020
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'오픈소스컨트리뷰톤 온라인미팅1 후기 : 모던 js 오픈소스 기여순서'에 참여하고 주요 발표 내용과 배운 점을 정리한 글이다.
    * 예시 : it works incorrectly면 그냥 작동하지않는다로 번역하는 것이 아니라 대명사 it이 뭔지 제대로 번역할 것.</p>
</div>

<!-- more -->

## 모던 js 오픈소스 기여순서

  1. 본저장소 fork하기
  2. fork한 주소로 로컬에 clone받기
  3. 엑셀 대시보드에서 번역 원하는 작업 찜하기
  4. 본저장소에 진행할 작업 issue하기 
     * issue제목 예시 : 2-js/04-Forms, controls/03-Events: change, input, cut, copy, paste 번역
  5. [로컬서버세팅](https://github.com/javascript-tutorial/ko.javascript.info/wiki/%EB%A1%9C%EC%BB%AC-%EC%84%9C%EB%B2%84-%EC%84%B8%ED%8C%85%ED%95%98%EA%B8%B0)
  6. 에디터에서 pull하기
  7. 작업 시작!
  8. git add.
  9. git commit 메세지
     * commit명 예시 : 다른사람 커밋명 확인할 것
     * [이벤트 루프와 매크로·마이크로태스크] 번역
     * [정적 메서드와 정적 프로퍼티] 1차 리뷰
     * [화살표 함수 다시 살펴보기] 보완
  10. fork한 내저장소에 push.
  11. pr.
     * PR시 체크박스에 체크 `[x]` 필수.
     * CLA(Contributor License Agreement)동의 필수 : 제작물에 나의 저작권을 요구하지 않겠다는 동의.

  
  
  

## 원격저장소 최신버전으로 업데이트하는 방법

  1. 연결고리만들기 git remote add upstream
  2. git fetch 또는 rebase

  
  
  

## 리뷰시 주의사항

  * 여러개 리뷰할꺼면 : start a review
  * 한문장만 리뷰할꺼면 : add single comment

  
  
  

## 번역시 주의사항

  * [모범사례](https://github.com/javascript-tutorial/ko.javascript.info/wiki/%EB%B2%88%EC%97%AD-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80) 정독하기
  * 대명사는 명확하게
    * 예시 : it works incorrectly면 그냥 작동하지않는다로 번역하는 것이 아니라 대명사 it이 뭔지 제대로 번역할 것.
  * 인칭대명사는 생략가능
  * 보라님 번역스타일로 하는 것이 문서 통일성을 높여서 좋다. 번역된거 많이 읽어보기
  * 번역은 소제목단위로 커밋날리고 한 챕터가 다 되면 pr 남기기

#[TIL](/tags/TIL/)[GIT](/tags/GIT/)
