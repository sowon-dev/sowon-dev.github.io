---
title: "gson을 이용하여 JSON을 HashMap으로 변환하기(영화관 좌석 예매 예시)"
date: 2022-08-10 15:02:02
tags:
  - "JSON"
  - "Gson"
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">gson을 이용하여 JSON을 HashMap으로 변환하기(영화관 좌석 예매 예시)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    클라이언트에서 json형태로 넘긴 데이터를 컨트롤러에서 String으로 받아 Json으로 변환한 뒤 Map으로 변환하여 사용하고싶었다.</p>
</div>

<!-- more -->

클라이언트에서 json형태로 넘긴 데이터를 컨트롤러에서 String으로 받아 Json으로 변환한 뒤 Map으로 변환하여 사용하고싶었다.

## 코드

영화관 좌석을 체크하면 원하는 정보가 Object형태로 생성한 뒤 리스트에 담아서 form태그로 서버에 전송하고싶었다.

  * jsp파일

html태그에는 체크박스 클릭시 클릭이벤트를 달아준다.

```html
<input type="checkbox" name="chkSeat" value="'+idx+'" data-movieId="17" data-row="F" data-seatNo="7" onclick/>
```

편의상 제이쿼리로 클릭이벤트를 달았다.

```js
// 각 행 체크박스 클릭시 이벤트
let chkMovieSeatList = []; // 전역변수로 설정
function tickSeatCheckbox(event){
	let currentEl = event.currentTarget;
	
	// 체크박스 체크시
    if(this.checked) {
		let tickSeat = new Object();
		tickSeat.idx = $(this).val();
		tickSeat.movieId = $(this).data('movieId');
		tickSeat.row = $(this).data('row');
		tickSeat.seatNo = $(this).data('seatNo');
		chkMovieSeatList.push(tickSeat)
	// 체크박스 체크해제시
	 } else { 
	 	chkMovieSeatList = chkMovieSeatList.filter((element)=>element.idx != $(currentEl).val());
    }
	// 리스트에 담기
	$("input[name=chkMovieSeatList]").val(JSON.stringify(chkMovieSeatJson));
}

$(document).ready(function(){
	// 체크박스 변화시 체크박스 클릭이벤트 실행
	$("input[name=chkSeat]").change(function(){
		tickSeatCheckbox();
    });
});
```

전송은 form태그로 했다.

```js
$("form[name=saveFrm]").submit();
```

  * DTO파일

```java
public class Seat {
	private int id;
	// 중략
	private String chkMovieSeatList; 
}
```

혹시 [DTO vs Model vs Entity 이 세가지의 차이가 궁금하다면 여기를](https://sowon-dev.github.io/2022/07/14/220714dtovsmodelvsentity/) 클릭하면 된다.

  * controller파일

```java
@PostMapping("/save")
public String save(Seat param, RedirectAttributes redirectAttributes) {
	String redirect = "redirect:주소";

	BooleanAndMessageResult result = new BooleanAndMessageResult();
	try {
		result = seatService.save(param);
		if (result.isResult()) {
			redirectAttributes.addFlashAttribute("message", "success");
		} else {
			redirectAttributes.addFlashAttribute("message", "fail");
		}
	} catch (Exception e) {
		result.setResult(false);
		result.setMessage("등록에 실패 하였습니다.");
		redirectAttributes.addFlashAttribute("message", "fail");
	}
	redirectAttributes.addFlashAttribute("result", result);
	return redirect;
}
```

  
  
  

## gson을 이용하여 JSON을 HashMap으로 변환

String 형태로 받은 chkMovieSeatList을 Map형태로 변환한 뒤 체크된 갯수만큼 반복문을 돌려 db에 insert를 했다.  
자바 JSON 라이브러리인 [goolge.gson](https://github.com/google/gson)를 이용해서 변환했다.  
chkMovieSeatList에서는 쌍따옴표가 "로 들어가 있기때문에 replaceAll()을 이용해서 변경해줬다.

  * SeatServiceImpl.java

```java
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.JsonParser;

// 중략

@Override
@Transactional
public BooleanAndMessageResult save(Seat param){
	BooleanAndMessageResult result = new BooleanAndMessageResult();
	
	// 중략
	
	JsonParser jsonParser = new JsonParser();
	JsonArray jsonArray = (JsonArray) jsonParser.parse(req.getChkMovieSeatList을().replaceAll("&quot;","\""));
	
	for(JsonElement seatEl : jsonArray){
		JsonObject seatObj = (JsonObject) seatEl;	
		HashMap<String, Object> seatMap;
		try {
			seatMap = new ObjectMapper().readValue(seatObj.toString(), HashMap.class);
			seatDAO.insertSeat(seatMap);
		} catch (JsonParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (JsonMappingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}	
}
```

#[JSON](/tags/JSON/)[Gson](/tags/Gson/)
