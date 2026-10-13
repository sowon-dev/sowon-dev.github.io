---
title: "[Vue]computed를 찾다가 명령형프로그래밍과 선언형 프로그래밍 차이점까지 알게된 썰"
date: 2022-06-27 21:35:59
tags:
  - "VueJS"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'computed를 찾다가 명령형프로그래밍과 선언형 프로그래밍 차이점까지 알게된 썰'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    VueJS로 화면을 구성하다가 computed와 watch를 사용하는 데 있어 차이점이 궁금했다.</p>
</div>

<!-- more -->

VueJS로 화면을 구성하다가 computed와 watch를 사용하는 데 있어 차이점이 궁금했다.  
둘이 역할이 비슷한 거 같은데 어떤 차이가 있을까?

[Vue.js 한글 공식문서](https://kr.vuejs.org/v2/guide/computed.html#computed-%EC%86%8D%EC%84%B1-vs-watch-%EC%86%8D%EC%84%B1)에도 이와 관련해서 자세히 설명되어있다.

## computed 속성

원래 computed 속성은 계산이 필요한 속성이 반복 호출될때 사용하는 속성이다.  
아래 코드와 같이 표현식으로 간단한 계산을 할 수 있지만 저 코드가 반복되서 사용되어야한다면? 여러 코드에 반복사용될수록 소스 코드가 지저분해질것이다.

```js
// 간단한 계산

<p>책을 가지고 있다:</p>
<span>{{ author.books.length > 0 ? 'Yes' : 'No' }}</span>
```

이때 computed 속성을 사용할 수 있다.  
Vue코드에서 아래처럼 호출한 뒤

```js
export default {
  data() {
    return {
      author: {
        name: 'John Doe',
        books: [
          'Vue 2 - Advanced Guide',
          'Vue 3 - Basic Guide',
          'Vue 4 - The Mystery'
        ]
      }
    }
  },
  computed: {
    // 계산된 값을 반환하는 속성
    publishedBooksMessage() {
      // `this`는 컴포넌트 인스턴스를 가리킵니다.
      return this.author.books.length > 0 ? 'Yes' : 'No'
    }
  }
}
```

화면에서는 아래처럼 간단하게 쓸 수 있어 가독성이 좋아진다.

```html
<p>책을 가지고 있다:</p>
<span>{{ publishedBooksMessage }}</span>
```

  
  
  

## watch

watch속성은 직관적인 이름에서 알 수 있듯 특정데이터의 변화를 감지하고 지정한 함수를 실행하는 속성이다.

아래 예제는 firstName이나 LastName이 바뀌면 이를 각각 감지하고 fullName에 바뀐 부분을 반영해준다.

```html
<div id="demo">{{ fullName }}</div>
```

```js
var vm = new Vue({
  el: '#demo',
  data: {
    firstName: 'Foo',
    lastName: 'Bar',
    fullName: 'Foo Bar'
  },
  watch: {
    firstName: function (val) {
      this.fullName = val + ' ' + this.lastName
    },
    lastName: function (val) {
      this.fullName = this.firstName + ' ' + val
    }
  }
})
```

여기엔 어떤 문제점이 있을까?

  1. firstName과 lastName안의 코드는 동일하게 바뀐 함수를 조합해 fullname을 리턴하는 데 불필요하게 코드를 반복한다. 
  2. 명령형 프로그래밍이다. 

watch속성대신 computed속성을 사용하면 위 두 문제를 해결할 수 있다.

```js
var vm = new Vue({
  el: '#demo',
  data: {
    firstName: 'Foo',
    lastName: 'Bar'
  },
  computed: {
    fullName: function () {
      return this.firstName + ' ' + this.lastName
    }
  }
})
```

깔끔하긴 한데 왜 명령형 프로그래밍과 선언형 프로그래밍이 무엇이고 왜 선언형 프로그래밍이 더 좋다고 하는걸까?

  
  
  

## 명령형 프로그래밍 vs 선언형 프로그래밍

일반적으로 선언형 프로그래밍이 명령형 프로그래밍보다 코드 반복이 적어서 좋다고 한다.  
명령평 프로그래밍과 선언형 프로그래밍을 검색하면 아래와 같은 정의를 마주하게 된다.

  * 명령형 프로그래밍: How you do something 어떻게 할 것인지에 초점
  * 선언형 프로그래밍: What you do 무엇을 할지에 초점.

머리로는 알겠는데(?) 언뜻 잘 와닿지 않는다!  
예시를 들으면 쉽게 와닿는다. 식당에 들어갔다고 생각해보자.

  * 선언형 프로그래밍: 두사람이요~라고 말한다.
  * 명령형 프로그래밍: 식당 내부 전체를 둘러본다 -> 오른쪽 두번째 창가자리가 비어있음을 확인한다 -> 거기까지 걸어간다 -> 자리에 앉는다.

이렇듯 선언형 프로그래밍은 How를 알 필요가 없다. 결과만 잘 받으면 된다. 결과에만 신경쓰려면 뭐가 준비되어있어야할까?  
바로 잘 훈련된 종업원 즉, 명령형으로 이미 추상화가 되어있어야한다!  
선언형 프로그래밍은 추상화 된 코드는 독립적으로 사용할 수 있기때문에 재사용성이 높고 코드반복이 적다!

  * 선언형 프로그래밍 언어 예시: SQL, HTML
  * 명령형 프로그래밍 언어 예시: C, C++, JAVA
  * 선언형과 명령형이 섞인 프로그래밍 언어 예시: JavaScript, C#, Python

  
  
  

## 참고

  * <https://ui.dev/imperative-vs-declarative-programming>
  * <https://v3-docs.vuejs-korea.org/guide/essentials/computed.html#basic-example>

#[VueJS](/tags/VueJS/)
