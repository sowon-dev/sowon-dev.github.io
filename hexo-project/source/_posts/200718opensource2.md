---
title: "개발자가 오픈소스를 읽는 방법(Git log)"
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
  <p class="tldr-desc">개발자가 오픈소스를 읽는 방법(Git log)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    * 프로젝트레포지토리에 있는 Contributing을 꼭 읽어야한다. 그래야 공통작성하는 방법은 코딩스타일을 확인할 수있다. 정해놓은 코딩스타일로 꼭 작성해야한다을 적용할 수 있다.</p>
</div>

<!-- more -->

## 개발자가 오픈소스를 읽는 방법(Git project Reading Skill)

  * 오픈소스개발자입장에서 프로젝트 내용 확인해보려고하는 명령어들
  * 프로젝트를 볼때 커밋히스토리를 기준으로 소스코드리딩하면 훨씬 전략적으로 읽을 수 있다. 
  * 프로젝트레포지토리에 있는 Contributing을 꼭 읽어야한다. 그래야 공통작성하는 방법은 코딩스타일을 확인할 수있다. 정해놓은 코딩스타일로 꼭 작성해야한다
    * ex) 빈칸, 중괄호위치 등등
  * commit ID는 소스파일이 수정될때마다 생기거나 바뀌는 고유한 ID(SHA1해시값)
  * 속성
    * `| wc -l` : 파일 라인개수를 측정.
    * `| nl` : 파일의 line number명시(순위표시용으로 사용)
    * `--no-merges` : 머지커밋은 병합커밋(빈커밋)으로 수정내역을 보고자할때 굳이 필요없기에 no-merges 옵션사용.
    * `--reverse` : 옛날 것부터 출력

```bash
# 1. 전체 소스파일 커밋 리스트
# `q`키 눌러서 나가기
$ git log --oneline

# 2. 전체 소스파일 커밋 자세히 보기
# oneline보다 자세하게 전체 소스파일 수정내역을 확인할 수 있다.
$ git log -p

# 3. 전체 소스파일 커밋 리스트(Merges커밋제외)
$ git log --oneline --no-merges

# 4. 전체 소스파일 수정내역 개수 세기
# | wc -l속성으로 커밋개수를 확인할 수 있다.
$ git log --oneline | wc -l

# 5. ID값으로 어떤 커밋을 언제 어떻게 커밋했는지 확인가능
$ git show ID값 

# 6. 요약 소스파일 리스트
$ git shortlog -sn

# 7. 특정날짜기준 커밋리스트
# 날짜를 기준(inclusive)으로 커밋리스트를 확인할 수 있다
# 예시 : 2020년1월1일부터 2020년6월30일까지의 커밋리스트를 확인
$ git log --oneline --after=2020-01-01 --before=2020-06-30
# 예시 : 2020년6월1일부터 2020년6월30일까지의 폴더명(mnist)의 커밋리스트 갯수(|wc -l)를 확인
$ git log --oneline --after=2020-06-01 --before=2020-06-30 -- mnist/ | wc -l

# 8. 옛날 것부터 소스파일 커밋리스트보기
$ git log --reverse
```

#[TIL](/tags/TIL/)[GIT](/tags/GIT/)
