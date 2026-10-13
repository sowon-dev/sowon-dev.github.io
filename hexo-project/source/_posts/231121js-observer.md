---
title: "[js]observer 사용하기"
date: 2023-11-20 22:45:55
tags: []
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">observer 사용하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    현재 프로그램에서 사용하는 커스텀js파일은 비동기를 호출하는데 load가 되어도 비동기때문에 removeFile이 아직 생성되지 않은 상태에서 클릭이벤트를 추가하려고하니 생기는 순서의 문제였다.</p>
</div>

<!-- more -->

load 후에 removeFile 버튼들에 click이벤트를 걸고 싶었다.

```js
$(window).on('load', function(){
	let removeFileButtons = document.querySelectorAll('[data-role="removeFile"]');
	removeFileButtons.forEach(function(button) {
	    button.addEventListener('click', function() {
	    	let fileItem = this.closest('.fileItem');
			let uploadFileNm = fileItem.querySelector('[name="attachFileNm"]').value;
	        let uploadFileKey = fileItem.querySelector('[name="attachFileKey"]').value;
	    	deleteFile(uploadFileKey, uploadFileNm);
	    });
	});	
})
```

하지만 이벤트가 걸렸다 안 걸렸다해서 팀장님께 문의드리고 답을 얻었다.  
현재 프로그램에서 사용하는 커스텀js파일은 비동기를 호출하는데 load가 되어도 비동기때문에 removeFile이 아직 생성되지 않은 상태에서 클릭이벤트를 추가하려고하니 생기는 `순서의 문제`였다.  
커스텀js파일의 콜백함수가 따로 없기때문에(레거시라서 수정할 수가 없다….) 동적변화를 잡기위해 observer를 사용하면 해결할수있다.

  
  
  

# 해결코드

```js
$(document).ready(function() {
	var targetNode = $("[data-role=fileUploader]");
	var observer = new MutationObserver(function(mutations) {
	    mutations.forEach(function(mutation) {
	    	for(var i = 0; i < mutation.addedNodes.length; i++ ) {
	    		var tag = mutation.addedNodes[i];
	    		$(tag).find('[data-role="removeFile"]').click(function(event) {
	    			event.preventDefault()
	    			let fileItem = this.closest('.fileItem');
					let uploadFileNm = fileItem.querySelector('[name="attachFileNm"]').value;
					let uploadFileKey = fileItem.querySelector('[name="attachFileKey"]').value;
	    	    	deleteFile(uploadFileKey, uploadFileNm);
	    		});
	    	}
	    });
	});
	observer.observe(targetNode[0],{ attributes: false, childList: true, subtree: true} );
})
```

observer를 사용해서 해결!

  
  
  

# 참고

  * 팀장님 지식
  * <https://ko.javascript.info/mutation-observer>
