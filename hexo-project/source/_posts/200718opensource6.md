---
title: "특정 소스라인에 대해서 누가 마지막으로 수정을 했는지 찾기 git blame"
date: 2020-07-17 15:00:00
tags:
  - "TIL"
  - "GIT"
categories:
  - Reflections
  - 오픈소스컨트리뷰톤2020
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">특정 소스라인에 대해서 누가 마지막으로 수정을 했는지 찾기 git blame의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    핵심 설정과 구현 코드를 단계별로 파악하여 상황에 맞게 유연하게 활용할 수 있다.</p>
</div>

<!-- more -->

## blame

  * 특정 소스라인에 대해서 누가 마지막으로 수정을 했는지 commit ID로 추적가능하다.

  * `/class 첫글자대문자키워드` : string검색가능

    * ex)`/class Parser`
  * `}` 닫힘 중괄호같은 경우 수정되지 않을 가능성이 많기때문에 옛날것 그대로 유지할 확률이 높다.

  * 복구 (clone받은 데이터로) : `git reset --hard origin/master`

  * 예시 : git blame이용하여 exam.txt파일에서 Parser클래스를 만든 최초의 commit을 찾아보기

```plain
$ git blame exam.txt;
# /class Parser 검색하기 -> 검색결과 하이라이팅됨 -> 해당 커밋ID복사
$ git show 커밋ID
```

#[TIL](/tags/TIL/)[GIT](/tags/GIT/)
