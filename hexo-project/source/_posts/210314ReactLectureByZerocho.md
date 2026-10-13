---
title: "[리액트] webpack과 hot reloading 설치하기"
date: 2021-03-14 02:37:15
tags: []
categories:
  - Frontend
  - React
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">webpack과 hot reloading 설치하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    @babel/preset-env | 브라우저에 맞게 옛날문법을 최신문법으로 바꿔줌(즉, 옛날 문법을 지원해줌)지원할 브라우저를 옵션으로 설정할 수 있다. 지원을 많이할수록 느려진다을 적용할 수 있다.</p>
</div>

<!-- more -->

## webpack 개념

  * node : 자바스크립트 실행기일뿐 서버가 아니다.

  * 바벨 종류

    * npm i -D @babel/명칭 : 바벨 설치하는 명령어 

바벨종류 | 설명  
---|---  
@babel/core | 바벨 기본적인 것  
@babel/preset-env | 브라우저에 맞게 옛날문법을 최신문법으로 바꿔줌(즉, 옛날 문법을 지원해줌)지원할 [브라우저를 옵션으로 설정](https://github.com/browserslist/browserslist#full-list)할 수 있다. 지원을 많이할수록 느려진다  
@babel/preset-react | jsx 지원  
babel-loader | 바벨과 웹팩을 연결해줌  
@babel/plugin-proposal-class-properties | state문법사용할 수 있게 만듦  
  
  
  
  

## webpack 만드는 순서

  1. 만든 파일 webpack으로 만들기
     1. npm init
     2. npm install –save react react-dom
     3. npm i -D webpack webpack-cli
     4. npm i -D @babel/core @babel/preset-env @babel/preset-react babel-loader @babel/plugin-proposal-class-properties
  2. 위 4가지 설치 완료 후에 webpack.config.js 파일 생성 후 작성
  3. entry파일 생성 -> client.jsx
  4. Gugudan.jsx파일 생성
  5. npm run dev 또는 npx webpack
  6. index.html 파일생성하여 webpack으로 만든 app.js 불러오기

  
  
  

## webpack 데브 서버(dev server)와 핫 리로딩(hot reloading)

개념 | 설명  
---|---  
reloading | 그냥 새로고침  
hot reloading | 기존데이터 유지하고 변경점만 바뀜  
plugins | 확장프로그램  
  
  1. react-refresh-webpack 설치하기
     * npm i react-refresh @pmmmwh/react-refresh-webpack-plugin -D
     * 서버도 필요하기때문에 설치하기 변경점이 생기면 감지하여서 기존데이터 유지하면서 화면을 바꿔줌.
  2. dev-server 설치하기
     * npm i -D webpack-dev-server
  3. pakage.json scripts 수정
     * “dev”: “webpack serve –env development”
  4. webpack.config.js에서 수정
     * plugins추가

```js
plugins[
	new RefreshWebpackPlugin()
]
```
