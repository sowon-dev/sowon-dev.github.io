---
title: "[닷넷] Url.Action사용해서 원하는 URL연결하기"
date: 2022-05-24 19:22:47
tags:
  - "C#"
categories:
  - Backend
  - .NET
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Url.Action사용해서 원하는 URL연결하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    routeValues를 사용해서 area를 지정해주었다.</p>
</div>

<!-- more -->

cshtml에서 Url.Action으로 a태그 href를 변경하고 싶었다. 

파일구조 

  * Areas
    * Student
      * Controller
        * LearningController.cs
      * View
        * Index.cshtml
    * Professor
      * Controller 
        * StudyController.cs
      * View
        * Index.cshtml

내가 원하는 것은 아래처럼 2개의 a태그에 각각 다른 컨트롤러의 url이다.

```plain
// url결과
/Student/Learning
/Professor/Study
```

  
  
  

## 기존코드

```html
<a href="@Url.Action("Index","Learning")" id="menuUrl">
<a href="@Url.Action("Index","Study")" id="menuUrl">
```

url결과는 아래와 같다

```plain
// url결과
/Student/Learning
/Student/Study
```

`Action(string, string)`은 처음 URI를 잡고있기때문에 Professor의 Study가 아니라 Student에서 Study를 찾는다.

  
  
  

## 해결법 Action(String, String, Object)

routeValues를 사용해서 area를 지정해주었다.

```html
<a href="@Url.Action("Index", "Learning", new { area = "Student" })" id="menuUrl">
<a href="@Url.Action("Index", "Study", new { area = "Professor" })" id="menuUrl">
```

new 연산자로 area를 지정했기에 해당 area아래의 Url을 각각찾느다

```plain
// url결과
/Student/Learning
/Professor/Study
```

  
  
  

## 참고

MS사의 docs는 예시도 많이 없고 UI자체도 가독성이 많이 떨어진다. 그래도 docs 질은 괜찮은 건지 블로그글이 많이 없다. 닷넷개발자들은 영어고수인게 틀림없다.

  * <https://docs.microsoft.com/en-us/dotnet/api/system.web.mvc.urlhelper.action?view=aspnet-mvc-5.2#system-web-mvc-urlhelper-action(system-string-system-string-system-object)>

#[C#](/tags/C/)
