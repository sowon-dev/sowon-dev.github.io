---
title: "[HEXO]링크 미리보기 이미지 변경하기(ft.Open Graph)"
date: 2023-06-13 19:31:39
tags:
  - "Hexo"
categories:
  - Frontend
  - HTML&CSS
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">링크 미리보기 이미지 변경하기(ft.Open Graph)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    메타태그는 HEAD사이에 작성하는 웹사이트의 안내자이다.</p>
</div>

<!-- more -->

내 블로그글의 링크를 복사하여 카카오톡에 공유하는데 미리보기 이미지가 hexo-theme-icarus 이었다.  
이 부분을 커스텀하고 싶어서 head 소스에서 찾아보니 Open Graph가 담당하고 있었다.

# 메타태그란?

메타태그는 HEAD사이에 작성하는 웹사이트의 안내자이다.  
대부분의 포털사이트는 웹 사이트의 제목, 태그의 내용, 본문의 첫 100여 단어등을 검색한 후 사용자의 검색어와 비교해서 검색 결과를 나열해준다.

  * 참고: [meta태그, 내부링크, id와 name속성의 차이](https://sowon-dev.github.io/2020/07/09/200710webi/)
  * 개념글로 강추: [링크의 미리보기 제목, 설명, 이미지를 결정하는 open graph 태그](https://blog.ab180.co/posts/open-graph-as-a-website-preview)

메타태그를 편하게 사용할 수 있도록 정의해놓은 프로토콜이 바로 Open Graph이다.

  
  
  

# Open Graph

Open Graph는 HTML 파일의 메타정보를 쉽게 표시하기 위해서 메타정보에 해당하는 제목, 종류, 이미지, url 등 다양한 요소들을 통일해서 사용할 수 있도록 정의해놓은 프로토콜이다.

오픈그래프 기본 태그 | 설명  
---|---  
og:title | 사이트의 제목  
og:type | 사이트의 종류([참고링크: type에 들어갈 수 있는 값](https://ogp.me/#types))  
og:image | 사이트 링크 미리보기 이미지  
og:url | 사이트의 대표 url  
  
  
  
  

# 헥소블로그에 적용하기

미리보기 이미지를 하나로 고정하고 싶다면 아래와 같은 config.yml 파일에서 `open_graph:` 하위 `image:`를 찾은 뒤 그 옆에 `/img/고정이미지이름.png`를 입력하면 된다.

  * config.yml

```java
head:
    # URL or path to the website's icon
    favicon: /img/star.svg
    # Open Graph metadata
    # https://hexo.io/docs/helpers.html#open-graph
    open_graph:
        # Page title (og:title) (optional)
        # You should leave this blank for most of the time
        title: 
        # Page type (og:type) (optional)
        # You should leave this blank for most of the time
        type: article
        # Page URL (og:url) (optional)
        # You should leave this blank for most of the time
        url: 
        # Page cover (og:image) (optional)
        # You should leave this blank for most of the time
        image: /img/고정이미지이름.png
        # Site name (og:site_name) (optional)
        # You should leave this blank for most of the time
        site_name: 
        # Page author (article:author) (optional)
        # You should leave this blank for most of the time
        author: sowon-dev
```

  
  
  

# 해결

하지만 나는 썸네일이 있는 게시글은 썸네일이 미리보기 이미지로 보이고 썸네일이 없다면 내가 지정한 기본 이미지로 보이고 싶었다.  
따라서 config.yml 파일의 `open_graph:` 하위 `image:` 를 다시 공백으로 한 뒤

```java
head:
    # URL or path to the website's icon
    favicon: /img/star.svg
    # Open Graph metadata
    # https://hexo.io/docs/helpers.html#open-graph
    open_graph:
        # Page title (og:title) (optional)
        # You should leave this blank for most of the time
        title: 
        # Page type (og:type) (optional)
        # You should leave this blank for most of the time
        type: article
        # Page URL (og:url) (optional)
        # You should leave this blank for most of the time
        url: 
        # Page cover (og:image) (optional)
        # You should leave this blank for most of the time
        image: 
        # Site name (og:site_name) (optional)
        # You should leave this blank for most of the time
        site_name: 
        # Page author (article:author) (optional)
        # You should leave this blank for most of the time
        author: sowon-dev
```

아래 경로의 `og_image.png` 찾은 뒤 내가 원하는 이미지로 바꿔치기 해주면 해결!

  * 경로: public/img/og_image.png

  
  
  

# 카카오톡 미리보기에는 여전히 반영이 안된다면?

카카오톡에서 만든 공유 디버거에 해당 글 주소를 입력하면 OG(Open Graph) 프로토콜을 통해 파싱하고 스크랩 결과도 친절하게 알려준다.  
여기서 캐시 초기화를 누르면 카카오톡 미리보기가 반영된다!

  * [공유 디버거](https://developers.kakao.com/tool/debugger/sharing)

카카오 천재들….덕분에 넘 편하다

  
  
  

# 참고

  * [hexo 공식문서 open-graph](https://hexo.io/docs/helpers.html#open-graph)
  * [The Open Graph protocol 공식문서](https://ogp.me/)

#[Hexo](/tags/Hexo/)
