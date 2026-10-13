---
title: "[오류일지]Error creating bean with name 에러 해결(이클립스, STS), lombok설치 후 오류"
date: 2021-01-24 16:16:02
tags:
  - "Eclipse"
  - "오류일지"
  - "STS"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">프로젝트를 세팅하는 중에 Error creating bean with name "SiteMenuContentServiceImpl"에러를 만났다.
    나의 경우 lombok에러였고 대게 servlet-context.xml에 오류가 있는 경우 발생하는 에러이므로 servlet-context.xml에서 컴포넌트 추가를 통해 해결가능하다.</p>
</div>

<!-- more -->

## Error creating bean with name “SiteMenuContentServiceImpl”

프로젝트를 세팅하는 중에 `Error creating bean with name "SiteMenuContentServiceImpl"`에러를 만났다.  
ServiceImpl.java파일의 빈 생성이 왜 안될까?

  
  
  

## 원인 찾기

  * `SiteMenuContentServiceImpl.java` 파일로 이동한다.  
파일을 열어보니 lombok이 제대로 연결되어있지 않은채 빨간줄이 나타나있었다.  
나의 경우 lombok에러였고 대게 servlet-context.xml에 오류가 있는 경우 발생하는 에러이므로 [servlet-context.xml에서 컴포넌트 추가를 통해 해결가능하다.](https://needneo.tistory.com/10)

STS도 이클립스기반이므로 전반적으로 해결 순서가 동일하다.  
하지만 설치과정에서 각각 다른 문제를 만났기에 나눠서 적어보려고한다.

  
  
  

## 이클립스 해결순서

### `pom.xml`에 lombok이 추가 되어 있는지 확인

나의 경우 잘 추가되어있었다.

```xml
<dependency>
	<groupId>org.projectlombok</groupId>
	<artifactId>lombok</artifactId>
	<version>1.18.6</version>
	<scope>provided</scope>
</dependency>
```

  
  
  

### lombok.jar 설치

  * [projectlombok 사이트](https://projectlombok.org/download)에서 lombok을 다운로드해준 뒤 사용하는 IDE(이클립스, STS등등)경로를 지정하여 INSTALL을 해준다.
  * [참고 링크 : 이미 다운로드 되어있는 lombok 위치 찾고 설치하는 방법](https://blog.naver.com/10hsb04/221659315804)

나의 경우 이미 다운로드 되어있었다.  
처음 다운로드 하는 경우에는 다운 후 롬북을 실행해야한다.

  
  
  

### `eclipse.ini`파일에 lombok을 추가해준다.

  * `eclipse.ini`파일의 위치는 이클립스 설치한 폴더 안에 있다. 예시 : `C:\Users\eclipse-jee-2020-06-R-win32-x86_64\eclipse`
  * `eclipse.ini`에 아래 두 줄을 추가해준다

```xml
-javaagent:lombok.jar
-Xbootclasspath/a:lombok.jar
```

  
  
  

### IDE(이클립스, STS등)을 재시작한다.

  
  
  

### 다시 어노테이션 쓰기.

4단계까지 했는데도 오류가 발생한다면 `@Data`, `@Getter`, `@Setter`등의 어노테이션을 지웠다가 다시 적어본다.

  
  
  

## STS 해결순서

### `pom.xml`에 lombok이 추가 되어 있는지 확인

나의 경우 잘 추가되어있었다.

```xml
<dependency>
	<groupId>org.projectlombok</groupId>
	<artifactId>lombok</artifactId>
	<version>1.18.6</version>
	<scope>provided</scope>
</dependency>
```

  
  
  

### lombok.jar 설치

  * [projectlombok 사이트](https://projectlombok.org/download)에서 lombok을 다운로드해준 뒤 사용하는 IDE(이클립스, STS등등)경로를 지정하여 INSTALL을 해준다.
  * [참고 링크 : 이미 다운로드 되어있는 lombok 위치 찾고 설치하는 방법](https://blog.naver.com/10hsb04/221659315804)

나의 경우 이미 다운로드 되어있었다. `lombok.jar`를 더블클릭했지만 실행이 되지않아 lombok이 프로젝트에 적용되지 않는 문제였다. 

  
  
  

### lombok.jar 실행 안 될때

  1. 자바 설치 확인  
먼저 cmd에서 자바가 잘 설치되어있는지 확인한다.

```plain
javac -version
```

자바가 없는 경우 [JDK를 다운로드해야한다.](https://sowon-dev.github.io/2020/05/15/200515javae/)  
나의 경우 1.8버전으로 잘 설치되어있었다.

  2. lombok.jar 더블클릭으로 실행  
더블클릭하면 바로 실행이 되어야하는데 되지를 않았다.  
jar 파일아이콘이 아닌 알집exe아이콘으로 표시되어있는 점이 수상했다.  
알집이나 반디집등의 환경설정에서 jar파일 체크를 해제해주면 된다.  
[jar 파일 알집으로 실행되는 문제 해결 포스팅](https://eating-coding.tistory.com/69)을  
그리고 더블클릭하니까 성공!

  3. lombok.jar cmd에서 실행  
cmd에서 명령어로 lombok.jar를 실행시키는 방법도 있다.

```html
//cmd 명령어
java -jar lombok.jar
```

  
  
  

### `SpringTools4.ini` 또는 `STS.ini` 파일에 lombok을 추가해준다.

  * 아래 두 줄을 추가해준다

```xml
-javaagent:lombok.jar
-Xbootclasspath/a:lombok.jar
```

  
  
  

### IDE(이클립스, STS등)을 재시작한다.

  
  
  

### 다시 어노테이션 쓰기.

4단계까지 했는데도 오류가 발생한다면 `@Data`, `@Getter`, `@Setter`등의 어노테이션을 지웠다가 다시 적어본다.  
이렇게 나는 문제를 해결했다!

  
  
  

## lombok 설치 후에도 @Data가 적용안된다면?

lombok을 설치하고 위에 ini파일에 추가를 해줘도 @Data가 적용되지 않는 문제가 발생했다.  
lombok 삭제했다가 재설치해보고 메이븐업데이트도 해보았지만 도무지 해결 될 기미가 안 보였다.  
혹시나 하는 마음에 파일명을 바꿔볼까하는 생각이 들었다.

  * 기존 파일명 : `SpringToolSuite4.exe`, `SpringToolSuite4.ini`

![기존 파일명](/img/210325STS-err-lombok1.PNG)

  * 바꾼 파일명 : `sts.exe`, `sts.ini`

![바꾼 파일명](/img/210325STS-err-lombok1.PNG)

sts.ini 에다가 아래 코드도 잘 적어주고 STS를 재시작해보았다.

```xml
-javaagent:lombok.jar
-Xbootclasspath/a:lombok.jar
```

회색이었던 @Data가 파란색으로 정상 적용된 것을 확인할 수 있다!  
이제 Controller에서 get, set 메서드도 사용가능하다!

![해결](/img/210325STS-err-lombok3.PNG)

오늘도 해결!

#[Eclipse](/tags/Eclipse/)[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)[STS](/tags/STS/)
