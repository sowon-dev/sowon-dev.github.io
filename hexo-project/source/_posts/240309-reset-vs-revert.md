---
title: "[GIT]reset과 revert의 차이"
date: 2024-03-08 07:23:52
tags:
  - "GIT"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'reset과 revert의 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    동작 원리와 장단점을 비교 파악하여 프로젝트 개발 상황에 적합한 방식을 선택할 수 있다.</p>
</div>

<!-- more -->

오늘 타 팀의 꼬여버린 커밋을 해결하면서 reset과 revert를 사용했다.  
오랜만에 쓰다보니 기억이 잘 안나서 예전에 쓴 포스팅를 봤는데 내용이 부족해서 보완을 해봤다.

# reset과 revert의 차이

  * revert: 커밋을 취소한다고 커밋을 남기며 되돌림.
  * reset: 커밋을 작성한 걸 아예 되돌림. 이전 커밋기록은 삭제.
    * 프로덕션에 올라간 커밋은 reset을 하면 안된다. 히스토리가 안 남기때문.

| | 로그 | 추천 사용상황  
---|---|---  
reset | 생성X | 로컬 저장소에서 작업시 사용 추천  
revert | 생성O | 원격저장소에 이미 올렸을때 사용 추천  
  
  
  

# 취소 기록을 남기면서 커밋취소하는 revert

```plain
git revert 커밋넘버 --옵션
```

만약 커밋넘버가 c,b,a순으로 있고 a번으로 되돌리고 싶다면 아래 명령어를 입력하면 된다.

```plain
1. 커밋순서 확인하기
git log --oneline
- c커밋 blahblah
- b커밋 blahblah
- a커밋 blahblah

2. 취소하고싶은 커밋넘버로 취소하기
git revert b커밋넘버 --hard
```

이제 c,b커밋은 취소되고 a커밋만 남게 된다.  
그럼 c,b커밋에 staged되었던 파일들은 어떻게 될까?  
staging Area전인 working directory로 가게 된다!

  
  

# 아무도 모르게 커밋을 취소하는 reset

reset은 주의사항이 있다!

  * 주의: reset은 로컬 저장소에서만 실행할 것

원격저장소에 올라간 뒤 reset을 실행하면 이전 커밋 내역들이 전부 삭제된다.  
만약 다른 개발자들과 함께 작업했는데 reset을 한 걸 모른채로 커밋을 하면 삭제한 커밋들이 다시 살아난다.  
따라서 미리 공지를 하거나 `git revert사용을 추천`한다.

```plain
git reset 커밋넘버 --옵션
git reset b커밋넘버 --hard
```

  
  

# 가장 최근 commit 한개 취소하기

가장 최근 커밋을 삭제하기 위해선 가장 최근 커밋을 가리키는 HEAD가 어디있는지 중요하다.

```plain
1. HEAD위치 확인
$ git log --oneline

2. HEAD의 커밋 한개 삭제
$ git reset --hard HEAD~1

3. 삭제 후 최신 commit 확인
$ git log --oneline
```

  
  

# 옵션

  * soft: 취소한 커밋안의 작업 파일들을 staging단계로 돌린다. 따라서 add되어있다.
  * hard: 취소한 커밋안의 작업 파일들을 working directory단계로 돌린다. 따라서 add되어있지도 않다.

#[GIT](/tags/GIT/)
