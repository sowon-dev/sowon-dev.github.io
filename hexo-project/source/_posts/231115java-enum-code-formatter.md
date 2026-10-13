---
title: "[이클립스/STS] enum 코드 예쁘게 포맷팅하기"
date: 2023-11-15 01:41:29
tags:
  - "Eclipse"
  - "STS"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">enum 코드 예쁘게 포맷팅하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    현재 Google Java Style Guide을 사용하고 있는데 여기서 enum code formatting만 수정했다.</p>
</div>

<!-- more -->

enum을 쓰는데 자동포맷팅이 너무 못생겨서 가독성이 떨어졌다.

현재 [Google Java Style Guide](https://github.com/google/google-java-format)을 사용하고 있는데 여기서 enum code formatting만 수정했다.

# 설정방법

  1. Preferences > Java > Code Style > Formatter 쿨릭
  2. Active profile 옆 edit 클릭
  3. Line Wrapping 탭 클릭
  4. 목록에서 ‘enum’ declaration 찾기
  5. ‘enum’ declaration 하위 Constants 클릭 후 Line wrapping policy를 Wrap all elements, every element on a new line로 변경
  6. OK 클릭 끝!

  * 결과

```java
private enum Food {
	APPLE, 
	BANANA, 
	STRAWBERRY
};
```

가독성도 좋고 속시원한 코드 포맷팅스타일이 완성된다!

코드포맷팅 이클립스/STS 단축키: `ctrl + shift + F`

  
  
  

# 참고

  * [Formatting Java enums using one line for every enum value with Eclipse](https://stackoverflow.com/questions/19424275/formatting-java-enums-using-one-line-for-every-enum-value-with-eclipse)

#[Eclipse](/tags/Eclipse/)[STS](/tags/STS/)
