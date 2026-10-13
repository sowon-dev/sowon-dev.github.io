---
title: "[리액트] useEffect에서 props사용하기"
date: 2022-09-12 21:50:43
tags: []
categories:
  - Frontend
  - React
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">useEffect에서 props사용하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    componentDidUpdate용도로 useEffect를 사용했다.</p>
</div>

<!-- more -->

부모 컴포넌트에서 위도와 경도를 props로 전달하여 자식컴포넌트에서 카카오맵API를 통해 특정 장소를 호출하고 싶었으나 오류가 발생했다.

# 목표

useEffect안에서 로직상 상태가 변하지않는 props를 쓰고 싶음

  
  
  

# 상황

부모컴포넌트인 `Detail.js`에서 자녀 컴포넌트인 `Map.js`로 좌표, 위도와 경도를 넘겨주었다.  
이를 `Map.js`에서 props로 위도와 경도를 받아서 카카오맵API로 카카오맵을 호출하고자했다.  
여기서 로직상 props로 받은 위도와 경도는 상태가 변하지 않는다.  
componentDidUpdate용도로 useEffect를 사용했다.

  * Detail.js 코드

```js
// detail.addrLat는 위도이고 detail.addrLng는 경도이다.
<Map latitude={detail.addrLat} longitude={detail.addrLng} />
```

  
  
  

# ❗문제발생

위도와 경도는 업데이트가 되지않는 데이터이기때문에 Hooks버전에서 componentDidMount만 사용하고 무한루프를 예방하기 위해 빈배열로 나뒀다.

  * Map.js 코드

```js
import React, { useEffect, useState } from 'react'

export default function Map(props) {

	console.log(`콘솔1번 props.latitude: ${props.latitude}`)
    
	const { kakao } = window
    const lat = props.latitude
    const long = props.longitude
	
    useEffect(() => {
		console.log(`콘솔2번 props.latitude: ${props.latitude}`)
        const container = document.getElementById('map')
        const options = {
            center: new kakao.maps.LatLng(lat, long),
            level: 3,
        }
        const map = new kakao.maps.Map(container, options)

        // 지도에 마커를 생성하고 표시한다
        var marker = new kakao.maps.Marker({
            position: new kakao.maps.LatLng(lat, long), // 마커의 좌표
            map: map, // 마커를 표시할 지도 객체
        })
    }, [])

    return (
        <>
            <div id="map" style={{ width: '750px', height: '350px' }}></div>
        </>
    )
}
```

그랬더니 콘솔결과는 아래와 같았다.

```js
콘솔1번 props.latitude: undefined Map.js:4 
콘솔1번 props.latitude: undefined Map.js:4
콘솔2번 props.latitude: undefined Map.js:10 
콘솔2번 props.latitude: undefined Map.js:10 

콘솔1번 props.latitude: 35.101425 Map.js:4 
콘솔1번 props.latitude: 35.101425 Map.js:4
```

콘솔2번은 useEffect안에서 호출한 건데 props로 받아온 모든 값이 undefined로 되어있어서 카카오맵 API가 제대로 호출되지않았다.

  
  
  

# 💡해결

[구글링해본 결과 props를 사용하려면 두번째 인수인 빈 배열에다가 props를 넣으면](https://www.reddit.com/r/learnreactjs/comments/oc23du/how_to_use_props_in_useeffect/)된다고 한다.  
물론 두번째 파라미터를 사용하는 경우 useEffect는 componentDidMount + componentDidUpdate역할을 동시에 하게 된다.

  * Map.js 코드

```js
import React, { useEffect, useState } from 'react'

export default function Map(props) {

	console.log(`콘솔1번 props.latitude: ${props.latitude}`)
    
	const { kakao } = window
    const lat = props.latitude
    const long = props.longitude
	
    useEffect(() => {
		console.log(`콘솔2번 props.latitude: ${props.latitude}`)
        const container = document.getElementById('map')
        const options = {
            center: new kakao.maps.LatLng(lat, long),
            level: 3,
        }
        const map = new kakao.maps.Map(container, options)

        // 지도에 마커를 생성하고 표시한다
        var marker = new kakao.maps.Marker({
            position: new kakao.maps.LatLng(lat, long), // 마커의 좌표
            map: map, // 마커를 표시할 지도 객체
        })
    }, [props])

    return (
        <>
            <div id="map" style={{ width: '750px', height: '350px' }}></div>
        </>
    )
}
```

그랬더니 콘솔결과는 아래와 같았다.

```js
콘솔1번 props.latitude: undefined Map.js:4 
콘솔1번 props.latitude: undefined Map.js:4
콘솔2번 props.latitude: undefined Map.js:10 
콘솔2번 props.latitude: undefined Map.js:10 

콘솔1번 props.latitude: 35.101425 Map.js:4 
콘솔1번 props.latitude: 35.101425 Map.js:4
콘솔2번 props.latitude: 35.101425 Map.js:10
```

콘솔2번에 제대로 된 값이 들어오면서 카카오맵이 내가 원하는 지도를 호출해줬다!  
해결~!

이 과정을 해결하면서 2가지 궁금증이 생겼다.  
첫번째는 왜 undefined일까? 였고 두번째는 동일한 콘솔로그가 왜 두번씩 호출될까?였다.

  
  
  

# 💬근데 왜 undefined일까?

리액트의 실행순서때문이다.

  1. Map.js(이하 자식컴포넌트) 호출
  2. Detail.js(이하 부모컴포넌트) 호출
  3. 자식컴포넌트의 useEffect 실행
  4. 부모컴포넌트의 useEffect 실행 -> axios 완료
  5. 부모컴포넌트 호출
  6. 자식컴포넌트 호출

처음 자식컴포넌트를 호출되므로 부모한테서 props를 받을 수 없기에 아예 없는 값이다.  
그리곤 부모컴포넌트에서 useEffect로 axios가 실행되어야지 setState()를 통해서 props를 자식컴포넌트에 전달할 수 있다.  
근데 axios다녀오기도 전에 자식컴포넌트의 useEffect를 실행해버리니 props값이 undefined일수밖에 없다!

이 상황을 말씀드리니 팀장님이 한 가지 더 미션을 주셨다.

팀장님 | 나  
---|---  
| 팀장님, 아까 리액트 질문에서요~ 실행순서 때문에 undefined가 났었고 useEffect 두번째 인자에 props를 주니 해결되었습니다.  
props 받아서 고치는게 맞을것 같네요. 대신에 undefined에 대한 대책이 필요한 것 같아요. |   
| 오호 대책이요?  
props가 값이 없을 때는 카카오 생성하고 하면 그만큼 비효율적일 것 같아서요 |   
  
오 역시 팀장님께 말씀드리길 잘했다. 생각도 못한 부분인데 어떻게 하면 해결할수 있을지 고심해봤다.

  
  
  

# 💬undefined에 대한 대책

props가 없을땐 자식컴포넌트를 실행시키지 않으면 되니까~ 내 머리속에 떠오른 방법은 크게 두 가지였다.

  1. 자식컴포넌트에서 props가 없을 땐 실행하지않기.
  2. 부모컴포넌트에서 axios다녀온 뒤에, 즉 데이터가 있을때 자식컴포넌트 실행하기 

  
  
  

## 자식컴포넌트에서 useEffect 조건을 걸어볼까?

아래와 같은 소스코드에서 props가 없을땐 카카오의 maps객체르 호출하지 않아야겠다고 생각하고 if조건문을 걸어주려고 했다.

  * 자식컴포넌트 (Map.js) 소스코드

```js
export default function Map(props) {
    const { kakao } = window
    const lat = props.latitude
    const long = props.longitude
    console.log('Map 컴포넌트 실행.')
	
    useEffect(() => {
        //if (props) {
        debugger
        const container = document.getElementById('map')
        const options = {
            center: new kakao.maps.LatLng(lat, long),
            level: 3,
        }
        const map = new kakao.maps.Map(container, options)

        // 지도에 마커를 생성하고 표시한다
        var marker = new kakao.maps.Marker({
            position: new kakao.maps.LatLng(lat, long), // 마커의 좌표
            map: map, // 마커를 표시할 지도 객체
        })
        // }
    }, [])

    return (
        <>
            <div id="map" style={{ width: '750px', height: '350px' }}></div>
        </>
    )
}
```

하지만!  
디버깅해보니 디버킹타이밍에선 props가 아예 없는 객체였다! 두둥-  
1번 방법은 실패!

  
  
  

## 부모컴포넌트에서 props로 줄 데이터가 있을때 자식컴포넌트 호출하기

props로 넘겨줄 `detail.addr1` 라는 데이터가 있을때만 자식컴포넌트인 Map을 호출했다.

```js
{detail.addr1 && (
	<Map
		latitude={detail.addrLat}
		longitude={detail.addrLng}
	/>
)}
```

이렇게 undefined일때는 아예 자식컴포넌트를 호출하지 않는 방법으로 문제 해결!!

  
  
  

# 💬또 다른 궁금증, 왜 두번씩 호출될까?

useEffect안에서 props를 사용하는 과정에서 동일한 콘솔로그가 두 번씩 호출되는 게 궁금해져서 친구 중에 리액트 천재에게 물어봤다.  
친구가 `혹시 index.js에 React.StrictMode 사용했어?` 라고 물어봤고 확인해보니 진짜였다!  
어떻게 안거지? 😱  
마치 내 코드를 본 것만 같은 정확도였다.

[리액트공식문서: Strict 모드](https://ko.reactjs.org/docs/strict-mode.html)에 따르면 Strict 모드는 개발 모드에서만 활성화되기 때문에, 프로덕션 빌드에는 영향을 끼치지 않고 애플리케이션의 잠재적인 문제를 알아내기 위해 사용한다고 한다. 

  * 잠재적인 문제란?
    * 안전하지 않은 생명주기를 사용하는 컴포넌트 발견
    * 레거시 문자열 ref 사용에 대한 경고
    * 권장되지 않는 findDOMNode 사용에 대한 경고
    * 예상치 못한 부작용 검사
    * 레거시 context API 검사
    * Ensuring reusable state

  
  
  

# 참고

  * [컴포넌트 생명주기](https://sowon-dev.github.io/2021/03/22/210323React-componentLifeCycle/)
