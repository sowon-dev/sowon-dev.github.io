---
title: "유튜브 맞춤동영상/추천영상/관련동영상 안뜨게 하기(ft. youtube API 사용법)"
date: 2021-01-31 21:03:12
tags:
  - "YouTube"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">유튜브 맞춤동영상/추천영상/관련동영상 안뜨게 하기(ft. youtube API 사용법)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    유튜브API를 통해서 관련 동영상 사용 중지할 수 없지만 우회방법이 두 가지 있다.</p>
</div>

<!-- more -->

웹 사이트에 iframe으로 유튜브 동영상을 연결을 하면 영상 재생이 끝나면 관련 동영상이 뜬다.  
유튜브API를 통해서 관련 동영상 사용 중지할 수 없지만 우회방법이 두 가지 있다.

  1. 반복재생을 통해서 관련 동영상 나올 틈을 주지 않는 방법
  2. rel속성 설정으로 재생된 채널에서 관련 동영상을 가지고 오는 방법

아래 예시를 통해 [유튜브 API의 다른 매개변수](https://developers.google.com/youtube/player_parameters?hl=ko) 사용방법도 익힐 수 있다.

  
  
  

# 유튜브 소스코드 복사하기

연결을 원하는 유튜브 동영상에서 우클릭을 하여 `소스 코드 복사`를 클릭한다.  
아래처럼 기본 값이 복사된다.

```html
<iframe width="1065" height="599" src="https://www.youtube.com/embed/영상코드" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

  
  
  

## 반복재생하는 방법

src 뒤에 `VIDEO_ID?version=3&loop=1&playlist=VIDEO_ID` 속성을 이용하면 된다.  
loop 기본값은 0이고 1로 설정할 경우 반복재생된다.  
VIDEO_ID는 물음표앞의 VIDEO_ID와 동일하게 설정해주면 해당 동영상만 반복재생된다.

```html
<iframe width="1065" height="599" src="https://www.youtube.com/embed/영상코드?version=3&loop=1&playlist=VIDEO_ID" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

  
  
  

## rel 매개변수로 동일 채널의 다른 동영상만 보여주는 방법

src뒤에 `VIDEO_ID?rel=1`속성을 넣어주면 된다.  
이 방법은 사용자가 다른 채널로 유출되는 것을 방지한다.

![](/img/210201youtubeAPI.PNG)

```html
<iframe width="1065" height="599" src="https://www.youtube.com/embed/영상코드?rel=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

  
  
  

## 참고

  * <https://rubybox.tistory.com/25>
  * <https://developers.google.com/youtube/player_parameters?hl=ko>

#[YouTube](/tags/YouTube/)
