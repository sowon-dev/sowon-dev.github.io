---
title: "바이너리 파일이란? 텍스트파일이랑 뭐가 다를까? ft.MIME"
date: 2022-03-09 04:05:04
tags: []
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">바이너리 파일이란? 텍스트파일이랑 뭐가 다를까? ft.MIME의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    이렇게 바이너리 데이터를 텍스트기반인 HTTP 프로토콜에 보내려면 방법이 두 가지가 있다.</p>
</div>

<!-- more -->

바이너리 파일이란 무엇일까?  
바이너리 파일은 텍스트파일과 비교하면 이해가 쉽다.

표로 간단하게 정리해볼 수 있다.

| | Text File | Binary File  
---|---|---  
정의 | 문자만 저장된 파일 | 문자와 숫자가 저장된 파일  
읽기 특징 | 문자만 읽을 수 있음. 전부 문자로 읽음 | 데이터를 있는 그대로 읽음  
쓰기 특징 | 문자만 쓸 수 있음. 숫자를 쓴 경우 모두 문자로 변환 후 씀 | 데이터를 있는 그대로 씀  
  
text파일에 숫자를 쓰는 예를 들어보자.  
앞서 text파일에은 숫자를 문자로 변환 후 쓴다고 했다.  
만약 숫자 17을 썼다면 text파일은 17을 ‘1’과 ‘7’로 변환 후 저장한다. 이로 인해 메모장(텍스트에디터)으로 특정 문서를 열면 깨지는 경우가 생긴다.

이렇게 바이너리 데이터를 텍스트기반인 HTTP 프로토콜에 보내려면 방법이 두 가지가 있다.

  1. MIME 타입으로 바이너리 데이터를 그대로 보내기
  2. Base64로 바이너리 데이터를 텍스트로 변환하여 보내기
     * 장점: 안전하게 전송가능
     * 단점: 데이터이 사이즈가 커짐

  
  
  

## MIME(Multipurose Internet Mail Extensions)

MIME은 마임이라고 읽으며 텍스트기반 프로토콜에서 바이너리 데이터(예를 들어 이미지, 동영상, 파일)를 전송하기 위해 HTTP의 Context-Type 헤더에 데이터 타입을 명시하여 사용한다.  
마임타입의 형태는 `타입/서브타입`으로 기입하면 된다.

![https://www.researchgate.net](https://www.researchgate.net/profile/Max-Kaiser-9/publication/220273642/figure/tbl1/AS:667773340487683@1536220979214/Selection-of-MIME-types-encountered.png)

  
  
  

## 인코딩: Base64 vs ASCII

바이너리 데이터를 텍스트 데이터로 변환할때 크게 두 가지 방식이 있다. 아스키코드와 Base64이다.

| | 갯수 | 진법 | 비트 | 어떤 텍스트데이터가 있는지?  
---|---|---|---|---  
Base64 | 64개 = 2^6 | 64진법 | 6비트 | [0-9 a-z A-Z + / 가 포함됨](https://en.wikipedia.org/wiki/Base64)  
ASCII | 128개 = 2^7 | 128진법 | 7비트 | [0-9 a-z A-Z + / 와 특수문자 포함](https://en.wikipedia.org/wiki/ASCII)  
  
ASCII는 Base64에서 특수문자가 포함되어있는데 몇몇 특수문자는 출력이 되지않으므로 ASCII로 변환하면 제대로 되지 않을 수 있다.  
어떤 인코딩이라든지 Base64의 데이터들은 다 있다. 따라서 안정적인 Base64인코딩을 사용하면 된다.
