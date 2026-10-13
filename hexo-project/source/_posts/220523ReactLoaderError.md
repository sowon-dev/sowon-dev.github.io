---
title: "[리액트]Error: Cannot find module loader에러 해결"
date: 2022-05-22 20:05:32
tags:
  - "오류일지"
categories:
  - Frontend
  - React
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">script를 정의하고 npm run start를 했는데 아래와 같은 오류가 발생했다.
    구글링하니 nodejs 레포의 이슈(링크)로 많은 개발자들이 해결방법을 주고받은 걸 확인할 수 있었다.</p>
</div>

<!-- more -->

리액트가 궁금해 정적사이트를 하나 만들고 있다.  
script를 정의하고 `npm run start`를 했는데 아래와 같은 오류가 발생했다.

```js
node:internal/modules/cjs/loader:361
      throw err;
      ^

Error: Cannot find module '/workspace/프로젝트명/node_modules/finalhandler/node_modules/debug/src/index.js'. Please verify that the package.json has a valid "main" entry
    at tryPackage (node:internal/modules/cjs/loader:353:19)
    at Function.Module._findPath (node:internal/modules/cjs/loader:566:18)
    at Function.Module._resolveFilename (node:internal/modules/cjs/loader:919:27)
    at Function.Module._load (node:internal/modules/cjs/loader:778:27)
    at Module.require (node:internal/modules/cjs/loader:1005:19)
    at require (node:internal/modules/cjs/helpers:102:18)
  code: 'MODULE_NOT_FOUND',
  path: '/workspace/프로젝트명/node_modules/finalhandler/node_modules/debug/package.json',
  requestPath: 'debug'
}
```

에러를 보면 알수있듯 loader에서 err가 잡혔다.  
구글링하니 nodejs 레포의 이슈[(링크)](https://github.com/nodejs/help/issues/2644)로 많은 개발자들이 해결방법을 주고받은 걸 확인할 수 있었다.  
이 여러 방법중 나는 아래의 방법으로 해결했다.

  
  
  

## 해결방법

  1. `npm cache clean --force` 명령어로 캐시를 삭제한다.
  2. node_modules 폴더를 삭제한다.
  3. package-lock.json 파일을 삭제한다.
  4. `npm install` 명령어를 입력하면 node_modules와 package-lock.json가 다시 설치된다.

위 조치를 취한 후 `npm run start`를 하니 잘 실행된다.  
해결!

#[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)
