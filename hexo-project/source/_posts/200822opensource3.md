---
title: "Merge시 create a merge commit과 rebase and merge 차이"
date: 2020-08-21 15:00:00
tags:
  - "TIL"
  - "GIT"
categories:
  - Reflections
  - 오픈소스컨트리뷰톤2020
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'Merge시 create a merge commit과 rebase and merge 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    * 체크아웃된 브랜치에 따라 가르키는 값이 다르다.</p>
</div>

<!-- more -->

## 머지시 create a merge commit과 rebase and merge 차이

  * `create a merge commit` : 머지시 머지커밋이 생성됨.
    * 배포가 자주 일어나는 저장소에서 주로 사용
    * 아래 사진처럼 `HEAD~1`과 `HEAD~2`가 뭔지 한 번에 알 수 없다.

![머지](/img/200822merge.PNG)

  1. develop브랜치생성 > 커밋 3개 생성
  2. master브랜치에서 커밋3개 생성
  3. master브랜치체크아웃상태에서 develop브랜치를 머지 `git merge develop`

  * `rebase and merge` : 머지커밋이 생성안됨.
    * 많은 사람이 기여하면 리베이스앤머지전략을 사용함
    * ex) 모던자바스크립트 한국어저장소 ko저장소
    * 아래 사진처럼 한 줄로 깔끔하게 커밋내역을 관리할 수 있고 순서가 정확히 나타나기 때문에 `HEAD~1`과 `HEAD~2`가 뭔지 한 번에 알 수 있다.

![리베이스](/img/200822rebase.PNG)

  1. develop브랜치생성 > 커밋 3개 생성
  2. master브랜치에서 커밋3개 생성
  3. master브랜치에체크아웃상태에서 develop브랜치를 리베이스 `git rebase develop`

  
  
  

## 머지커밋에서 head~1과 head2가 뭘 가르킬까?

![](/img/200822merge.PNG)

위의 사진에서 아래 3단계가 진행된 상태이다. 여기서 HEAD~1과 HEAD~2는 어떤 커밋을 가르킬까?

  1. develop브랜치생성 > 커밋 3개 생성
  2. master브랜치에서 커밋3개 생성
  3. master브랜치에서 develop브랜치 merge

  * 체크아웃된 브랜치에 따라 가르키는 값이 다르다. 
  * master브랜치에서 HEAD~2했을떼

![](/img/200822mergeHEAD2.PNG)

  * develop브랜치에서 HEAD~2헸을때
    * master브랜치의 커밋내역은 변경되지않는다.

![](/img/200822mergeHEAD2dev.PNG)

#[TIL](/tags/TIL/)[GIT](/tags/GIT/)
