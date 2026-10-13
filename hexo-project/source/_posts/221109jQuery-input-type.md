---
title: "[jQuery] checkbox와 select 다루기"
date: 2022-11-08 23:04:34
tags:
  - "jQuery"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">checkbox와 select 다루기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    핵심 설정과 구현 코드를 단계별로 파악하여 상황에 맞게 유연하게 활용할 수 있다.</p>
</div>

<!-- more -->

jQuery로 checkbox와 select 다루는 법을 전체적으로 정리해보자.

# ✍Checkbox

  
  

## 1\. 체크하기

```js
// ID로 지정하는 방법
$('#체크박스아이디').prop('checked',true);

// input 속성으로 지정하는 방법
$('input:checkbox[name="체크박스네임"]').prop('checked',true);
```

  
  

## 2\. 체크여부 확인

```js
$('#체크박스아이디').is(':checked');

// 반환값: true, false
```

참고로 `$('#체크박스아이디').val()`을 하면 반환값이 on이나 undifined가 뜬다.

  
  

## 3\. 한번에 전체 체크하기

```js
$('#allCheck').click(function(){
		var isChecked = $('#allCheck').is(':checked');
		
		if(isChecked)
			$('input:checkbox').prop('checked',true);
	});
```

  
  

# ✍ Select

  
  

## 1\. 값 읽기(가져오기)

```js
// ID로 접근하는 방법
$("#셀렉트박스아이디 option:selected").val();

// input 속성으로 접근하는 방법
$("select[name=셀렉트박스네임]").val();
```

  
  

## 2\. 옵션 추가하기

```js
// 옵션추가
$("#셀렉트박스아이디").append("<option value='1번'>1번 테스트</option>");

// 옵션을 맨 앞에 추가
$("#셀렉트박스ID").prepend("<option value='맨앞'>맨앞</option>");
```

  
  

## 3\. 옵션 삭제하기

```js
// 옵션 전체 삭제
$("#셀렉트박스아이디 option").remove();
$("select[name=셀렉트박스네임] option").remove();

// 특정 옵션 벨류 값으로 삭제
$("#셀렉트박스아이디 option[value='맨앞']").remove();

// 특정 옵션 인덱스 값으로 삭제
$("#셀렉트박스아이디 option:eq(0)").remove();

// 첫번째 옵션 삭제
$("#셀렉트박스아이디 option:first").remove();

// 마지막 옵션 삭제
$("#셀렉트박스아이디 option:last").remove();
```

  
  

## 4\. 선택하기

```js
// 옵션 전체 삭제
$("#셀렉트ID option:eq(1)").attr("selected", "selected");
```

#[jQuery](/tags/jQuery/)
