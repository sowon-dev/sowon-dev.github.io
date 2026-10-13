---
title: "[이클립스/STS] 보기 편하게 code style 설정하기 - 포맷팅설정"
date: 2022-03-01 21:09:29
tags:
  - "Eclipse"
  - "STS"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">보기 편하게 code style 설정하기 - 포맷팅설정의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    자바코드스타일은 구글 스타일을 사용하고 있다.</p>
</div>

<!-- more -->

이클립스나 STS 기본 코드 스타일은 너무 많은 tab공백 등으로 지저분해보이기도 한다.  
보기 편하도록 신규 프로젝트 시작시 코드 스타일을 적용하고 있다.

코드 스타일 적용 단축키: `Ctrl + Shift + F`

아래는 내가 주로 사용하는 코드 스타일이다.

  
  

## JAVA code style 🎀

자바코드스타일은 구글 스타일을 사용하고 있다.  
먼저 [google/styleguide 레포지토리안의 eclipse-java-google-style](https://github.com/google/styleguide/blob/gh-pages/eclipse-java-google-style.xml)를 선택하여 xml파일로 다운로드한다.

  1. 이클립스 상단의 Windows > Preferences
  2. Formatter 검색 후 Java > Code Style > Formatter 클릭 
  3. Import 버튼 클릭 후 미리 다운로드한 eclipse-java-google-style.xml 파일을 선택한 후 apply 버튼 클릭

자바 코드 스타일 적용 끝!

  
  
  

## JavaScript code style 🎀

jsp에서 script태그를 이용해 js를 사용하는 경우 이 설정도 함께 해줘야 보기 편하다.

  1. 이클립스 상단의 Windows > Preferences
  2. Formatter 검색 후 JavaScript > Code Style > Formatter 클릭 
  3. New 버튼 클릭 후 `Profile name: 원하는 이름` 기입하고 `Initialize settings with the following profile: Eclipse[built-in]` 선택 후 OK버튼
  4. Indentation 에서 `Tab policy : Spaces only`와 `Indentation size : 2`, 그리고 `Tab size : 2`를 기입
     * ![Indentation 참고](/img/220302jsCodeStyle1.JPG)
  5. Line Wrapping > `Maximem line width : 180` 기입
     * ![Line Wrapping 참고](/img/220302jsCodeStyle2.JPG)

자바스크립트 코드 스타일 적용 끝!

  
  
  

## HTML code style 🎀

  1. 이클립스 상단의 Windows > Preferences
  2. html 검색 후 Web > HTML Files > Editor 클릭 
     * Line width : 120
     * Indent using spaces 체크
     * Indentation size = 2
     * Inline Elements > 인라인으로 보이기 싫은 태그들 선택 > Remove
       * 나는 주로 select, tr, td를 remove한다.
  3. apply 버튼 클릭 후 OK버튼 클릭

![HTML 설정 참고](/img/220302jsCodeStyle2.JPG)

HTML 코드 스타일 적용 끝!

  
  
  

## JSP Validation OFF 🎀

JSP파일이 많다면 Validation OFF를 하는 게 로딩도 빠르고 보기 편하다.

  * Window > Preference > Web > JSP Files > Validation
    * Validate JSP fragemtns 체크해제

끝!

#[Eclipse](/tags/Eclipse/)[STS](/tags/STS/)
