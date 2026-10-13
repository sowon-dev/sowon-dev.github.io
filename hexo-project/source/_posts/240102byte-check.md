---
title: "[JSP/JAVA]글씨쓸때마다 바이트 계산하기"
date: 2024-01-01 14:54:53
tags:
  - "JAVA"
  - "JavaScript"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">글씨쓸때마다 바이트 계산하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    핵심 설정과 구현 코드를 단계별로 파악하여 상황에 맞게 유연하게 활용할 수 있다.</p>
</div>

<!-- more -->

문자전송 서비스를 만들고있다. 이번에 만드는 문자전송서비스는 바이트 제한이 있으므로 textarea에 글씨를 입력할때마다 자동으로 byte가 계산되며 2000바이트를 넘지 않게 만들고 싶었다.

  
  
  

# 화면 jsp

onkeyup 이벤트를 통해서 textarea에 무언가를 기입하는 순간 바이트 계산이 messagebyte에 실시간으로 보여진다.

```js
<script type="text/javascript">
let pickUserList = [];
let maxByte = 2000; //sms 는 90바이트 이내로 작성,lms 는 2000바이트
let totalByte = 0;

function fn_chk_byte(obj){
    totalByte = 0;
    let message = $(obj).val();

    let rlen = 0;
    let one_char = "";
    let str2 = "";
    
    for(let i=0; i<message.length; i++) {
        one_char = message.charAt(i);
        
        if(escape(one_char).length > 4) {
            totalByte += 2; //한글2Byte
        }else{
            totalByte++; //영문 등 나머지 1Byte
        }
        
        if(totalByte <= maxByte){
            rlen = i+1; //return할 문자열 갯수
        }
     }
    
    $("#messagebyte").text(totalByte);
     
     if(totalByte > maxByte) {
        // alert("한글 "+(maxByte/2)+"자 / 영문 "+maxByte+"자를 초과 입력할 수 없습니다.");
        toastr.error("메세지는 최대 " + maxByte + "byte를 초과할 수 없습니다.");
        str2 = str.substr(0,rlen);                                  //문자열 자르기
        obj.value = str2;
        fnChkByte(obj, maxByte);
		return false;
     }

};
</script>

<!-- 문자내용 -->
<div class="row">
	<h4>[문자 내용 작성]</h4>
	<div class="col-xs-12 col-sm-12 col-md-12">
		<div class="form-group">
			<textarea id="msg" name="msg" class="form-control" placeholder="문자내용을 입력하세요. 최대 2000Byte까지 작성 가능하며 90Byte가 넘으면 단문(SMS)에서 장문(LMS)발송으로 변경됩니다. " rows="5" onkeyup="fn_chk_byte(this);"></textarea>
			<span id="messagebyte">0</span><span>/ 2000 Byte</span>
			<div style="text-align: right;">* 최대 2000Byte까지 작성 가능하며 90Byte가 넘으면 단문(SMS)에서 장문(LMS)발송으로 변경됩니다.</div>
		</div>
	</div>
</div>
```

  
  
  

# 자바코드

컨트롤러에서 받은 뒤 바이트 계산하는 코드는 아래와 같다.  
특히 getBytes()에서 한글 인코딩을 제대로 해야지 js와 동일한 바이트수가 계산된다.

```java
int bytesLength = param.get("msgCn").toString().getBytes("KSC5601").length;
```

#[JAVA](/tags/JAVA/)[JavaScript](/tags/JavaScript/)
