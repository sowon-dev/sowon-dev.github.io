---
title: "[HEXO]링크공유하기 버튼을 헥소블로그에 커스텀하게 적용하기(ft.AddToAny)"
date: 2023-06-19 19:34:06
tags:
  - "Hexo"
categories:
  - Frontend
  - HTML&CSS
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">링크공유하기 버튼을 헥소블로그에 커스텀하게 적용하기(ft.AddToAny)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    내가 이용중인 Icarus 테마에서는 아래와 같이 총 5가지 공유 플러그인을 제공한다. 다른 플러그인을 원하면 설치해서 사용하면 된다,을 적용할 수 있다.</p>
</div>

<!-- more -->

Hexo를 이용해서 간편하게 개발블로그를 운영하고 있다.  
블로그의 좋은 글을 편하게 공유해갈 수 있는 링크 공유하기 버튼을 만들고 싶었다.

Hexo에선 이미 다양한 플러그인을 제공한다.  
내가 이용중인 Icarus 테마에서는 아래와 같이 총 5가지 공유 플러그인을 제공한다. 다른 플러그인을 원하면 설치해서 사용하면 된다,

  1. AddThis
  2. AddToAny
  3. Baidu Share
  4. Share.js
  5. ShareThis

이 5가지 중 나는 AddToAny의 디자인이 마음에 들었기에 이걸 선택했다.  
나머지 4가지 공유 플러그인에 대한 자세한 내용은 [Icarus User Guide - Share Buttons](http://ppoffice.github.io/hexo-theme-icarus/Plugins/Share/icarus-user-guide-share-buttons/)에서 확인할 수 있다.

  
  
  

# 적용하기

아래 경로의 config파일에서 `share`를 검색한 뒤 `AddToAny`를 기입해준다.

  * 경로: `../themes/hexo-theme-icarus/_config.yml`

```yml
# Share plugin configurations
# https://ppoffice.github.io/hexo-theme-icarus/categories/Plugins/Share/
share:
    type: addtoany #원하는 공유플러그인 기입
    # URL to the ShareThis share plugin script
    install_url: ''
```

이렇게 설정만 하더라도 바로 공유버튼이 생기는 걸 알 수 있다.  
디폴트대로 이용해도 되지만 블로그의 재미는 커스텀 아니겠는 가.  
커스텀하는 방법도 [AddToAny의 공식문서](https://www.addtoany.com/buttons/customize/)를 따라하면 금방이다.

  
  
  

# addtoany.jsx 생성하기

커스텀하기위해서는 아래 share폴더 하위에 addtoany.jsx 파일을 생성해야한다.

  * 경로: ../themes/hexo-theme-icarus/layout/share/addtoany.jsx

그리고 생성한 파일에 커스텀한 코드를 입력해준다.  
커스텀 코드는 [AddToAny의 공식문서](https://www.addtoany.com/buttons/customize/)를 참고하면 된다.

이건 참고용 내 커스텀 코드!

```jsx
/**
 * AddToAny share buttons JSX component.
 * @module view/share/addtoany
 */
const { Component, Fragment } = require('inferno');
const { cacheComponent } = require('hexo-component-inferno/lib/util/cache');

/**
 * AddToAny share buttons JSX component.
 *
 * @see https://www.addtoany.com/buttons/
 * @example
 * <AddToAny />
 */
class AddToAny extends Component {
    render() {
        return <Fragment>
			<div class="a2a_kit a2a_kit_size_32 a2a_default_style" style="display:flex; justify-content:center;" data-a2a-icon-color="lightseagreen">
				<a class="a2a_dd" href="https://www.addtoany.com/share"></a>
				<a class="a2a_button_copy_link"></a>
				<a class="a2a_button_facebook"></a>
			</div>
			<script>
				var a2a_config = a2a_config || {};
				a2a_config.locale = "ko";
				a2a_config.num_services = 2;
			</script>
			<script async src="https://static.addtoany.com/menu/page.js"></script>
        </Fragment>;
    }
}

/**
 * Cacheable AddToAny share buttons JSX component.
 * <p>
 * This class is supposed to be used in combination with the <code>locals</code> hexo filter
 * ({@link module:hexo/filter/locals}).
 *
 * @see module:util/cache.cacheComponent
 * @example
 * <AddToAny.Cacheable />
 */
AddToAny.Cacheable = cacheComponent(AddToAny, 'share.addtoany', props => {
    return {};
});

module.exports = AddToAny;
```

적용 끝!

#[Hexo](/tags/Hexo/)
