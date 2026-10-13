---
title: "[STS] 자바버전 안 바뀔때 해결! 자바버전 바꾸는 방법(1.8에서 11로)"
date: 2022-03-11 03:54:33
tags:
  - "STS"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'자바버전 안 바뀔때 해결! 자바버전 바꾸는 방법(1.8에서 11로)' 실행 및 개발 과정에서 발생하는 오류 현상과 원인을 분석한 글이다.
    Window -> Preferences -> 검색어: Compiler -> Java 하위 Compiler클릭 -> JDK Compliance에서 Compiler compliance level에서 1.8을 11로 변경을 통해 문제를 해결할 수 있다.</p>
</div>

<!-- more -->

자바버전을 깔~끔하게 1.8에서 11로 바꿔보자!

## 1 Preferences 설정

Window -> Preferences -> 검색어: Compiler -> Java 하위 Compiler클릭 -> JDK Compliance에서 Compiler compliance level에서 1.8을 11로 변경  
![](/img/220311javaVersion1.JPG)

  
  
  

## 2 pom.xml 설정

pom.xml을 더블클릭하여 연 뒤 아래 2가지를 수정한다.

  1. properties 하위 java-version을 1.8에서 11로 변경  
![](/img/220311javaVersion2.JPG)

  2. plugins 하위 artifactId가 maven-compiler-plugin를 찾은 뒤 그 하위 source와 target을 ${java-version} 으로 변경

     * `${java-version}`으로 설정해놓으면 1번에서 설정한 java-version을 그대로 따라가므로 11로 변경하든 16으로 변경하든 다시 1.8로 변경하든 동일한 자바 버전을 바라봐서 추후 변경할 필요가 없다.  
![](/img/220311javaVersion3.JPG)

#[STS](/tags/STS/)
