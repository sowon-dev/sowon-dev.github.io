---
title: "Prototype"
date: 2022-01-09 03:28:18
tags:
  - "Node.js"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Prototype의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    java나 python등 객체지향언어에는 Class(클래스)가 존재한다. 클래스를 가지고 상속등의 기능을 구현한다.</p>
</div>

<!-- more -->

js는 프로토타입기반 언어이다.  
여기서 프로토타입이 무엇일까?

java나 python등 객체지향언어에는 Class(클래스)가 존재한다. 클래스를 가지고 상속등의 기능을 구현한다.  
여기서 중요한 점은 js도 객체지향언어라는 점이다. 하지만 js에는 클래스라는 개념이 없다. 그렇다면 상속등의 기능은 어떻게 할 수 있을까? 이때 프로토타입을 사용한다. 기존의 객체를 clone하여 새로운 객체를 생성하는 것이다.

## 프로토타입 상속

사람(person)객체에는 sleep이라는 값이있다.  
학생(student)객체에도 sleep이라는 값이 있고 `person`을 상속한다. 이를 `student`의 프로토타입은 `person`이라고 말한다.

아래 아주 간단한 예시를 보자. 3가지 물음표에는 각각 어떤 값이 나올까?

```js
let person = {
  sleep: null
};
let student = {
  __proto__: person,
  sleep: true,
  study: true,
};

alert( student.sleep ); // ? (1)

delete student.sleep;

alert( student.sleep ); // ? (2)

delete person.sleep;

alert( student.sleep ); // ? (3)
```

답은 아래와 같다.

  1. true
  2. null
  3. undefined

이를 잘 활용하면 효율적인 객체생성이 가능하다. 이를 Class와 비교해보자!

```js
function Pesrson(name){
	this.name = name
}

Person.prototype.sleep = function sleep(){
	return `${this.name}는 자는 중`;
}

function Student(name){
	this.__proto__.constructor(name)
}

Student.prototype.study = function study(){
	return `${this.name}는 공부중`;
}

Object.setPrototypeOf(Student.prototype, Person.prototype) //set해줘야함
```

위와 아래는 똑같다!

```java
class Person(){
	constructor(name){
		this.name = name
	}
	
	sleep(){
		return `${this.name}는 자는 중`;
	}
}

class Student extends Pesrson{
	constructor(name){
		super(name)
	}
	
	study(){
		return `${this.name}는 공부중`;
	}
}

var me = new Student("sowon-dev");
console.log(me.study());
console.log(me.sleep());
```

  
  
  

## 유용한 메서드

메서드명 | 리턴값 | 설명  
---|---|---  
a instanceof b | boolean | a가 b를 상속하는지 확인할 수 있음  
  
  
  
  

## 참고

  * <https://ko.javascript.info/prototype-inheritance>

#[Node.js](/tags/Node-js/)
