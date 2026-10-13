---
title: "[ajax]분명 success인데 왜 계속 error로 가는걸까?"
date: 2023-09-10 15:39:57
tags:
  - "ajax"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">body에 리턴값을 담아주지 않았기때문에 ajax의 success가 아닌 error로 빠진것이다.
    ajax에서 잘못된 dataType설정했을 가능성이 높다!을 통해 문제를 해결할 수 있다.</p>
</div>

<!-- more -->

DB저장도 잘되고 controller를 디버그에서 확인해보니 result값도 정상적으로 잘 작동되었는데 화면에서만 오면 ajax에서 success를 타지않고 error로 빠져버렸다.  
왜일까?

  
  
  

# 문제와 원인

  * controller 코드

```java
@PostMapping(value = "/admin/new")
public BooleanAndMessageResult save(HttpServletRequest request, RedirectAttributes redirectAttributes, @RequestBody List<Admin> list) {
	BooleanAndMessageResult result = new BooleanAndMessageResult();
	Site site = (Site) request.getAttribute("site");
	for (Admin a : list) {
		a.setSiteid(site.getSiteid());
	}

	result.setResult(true);
	result.setMessage("정상적으로 등록 되었습니다.");

	try {
		adminService.insertAdminList(list);
	} catch (Exception e) {
		result.setResult(false);
		result.setMessage("등록에 실패 하였습니다.");
		LOGGER.error("error : ", e);
	}
	
	return result;
}
```

  * js코드

```js
$.confirm({
	theme: 'supervan',
	title: '운영정보관리 저장',
	content: '저장하시겠습니까?',
	confirmButton: '예',
	cancelButton: '아니오',
	confirm: function(){        	
		$.ajax({
			type: "POST"
			, url: "/admin/new"
			, contentType : "application/json; charset:utf-8"
			, data: JSON.stringify(jList)
			, dataType: 'json'
			, success: function(data){
				if(data.result == true){
					alert("저장에 성공했습니다.");
					setTimeout(function() {location.reload(true);}, 2000);
				} else if(data.result == false){
					alert(data.message);
					return false;
				}	
			}
			, error: function(request,status,error){  
				alert("에러가 발생했습니다. 새로고침합니다.");
				location.href = "/admin/infosetting";					
			}
		});	
	},
	cancel: function(){}
});
```

위 코드는 한 가지 잘못된 점이 있다.

  
  

## 원인: @ResponseBody 누락

@ResponseBody 어노테이션을 이용하면 자바 객체를 HTTP 응답 분문의 객체로 변환하여 클라이언트에 전송 할 수 있다.  
body에 리턴값을 담아주지 않았기때문에 ajax의 success가 아닌 error로 빠진것이다.

  
  
  

# 해결코드

  * controller코드

```java
@PostMapping(value = "/admin/new")
@ResponseBody // 까먹자말고 추가
public BooleanAndMessageResult save(HttpServletRequest request, RedirectAttributes redirectAttributes, @RequestBody List<Admin> list) {
	BooleanAndMessageResult result = new BooleanAndMessageResult();
	Site site = (Site) request.getAttribute("site");
	for (Admin a : list) {
		a.setSiteid(site.getSiteid());
	}

	result.setResult(true);
	result.setMessage("정상적으로 등록 되었습니다.");

	try {
		adminService.insertAdminList(list);
	} catch (Exception e) {
		result.setResult(false);
		result.setMessage("등록에 실패 하였습니다.");
		LOGGER.error("error : ", e);
	}
	
	return result;
}
```

  * js코드

```js
$.confirm({
	theme: 'supervan',
	title: '운영정보관리 저장',
	content: '저장하시겠습니까?',
	confirmButton: '예',
	cancelButton: '아니오',
	confirm: function(){        	
		$.ajax({
			type: "POST"
			, url: "/admin/new"
			, contentType : "application/json; charset:utf-8"
			, data: JSON.stringify(jList)
			, dataType: 'json'
			, success: function(data){	
				if(data.result == true){
					alert("저장에 성공했습니다.");
					setTimeout(function() {location.reload(true);}, 2000);
				} else if(data.result == false){
					alert(data.message);
					return false;
				}	
			}
			, error: function(request,status,error){  
				alert("에러가 발생했습니다. 새로고침합니다.");
				location.href = "/admin/infosetting";	
			}
		});	
	},
	cancel: function(){}
});
```

  
  

## 그래도 해결이 안된다면?

ajax에서 잘못된 dataType설정했을 가능성이 높다!  
jQuery ajax의 setting 중 dataType은 response를 어떤 데이터 형식으로 파싱할 지를 설정하는 것이다.  
`dataType: 'json'`으르 설정했기에 리턴타입을 json으로 주어야하는데 단순 String타입으로 준건 아닌지 체크해보자.  
데이터형식이 맞지않으면 ajax의 success가 아닌 error로 빠진다.

#[ajax](/tags/ajax/)
