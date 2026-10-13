---
title: "세번째 팀 프로젝트를 끝내며 코드리뷰가 내게 남긴 것"
date: 2021-11-16 15:00:00
tags:
  - "회고록"
categories:
  - Reflections
  - 회고록
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'세번째 팀 프로젝트를 끝내며 코드리뷰가 내게 남긴 것'에 참여하고 주요 발표 내용과 배운 점을 정리한 글이다.
    코드리뷰를 통해서 내가 배운 내용들을 정리해보았다.</p>
</div>

<!-- more -->

한달동안 내내 매달렸던 세번째 팀 프로젝트가 오늘부로 끝났다.  
매일 야근하는 삶이었다. 프로젝트가 끝나고보니 가을이 성큼 다가오다못해 성큼 지나가고 있었다.🍁  
이번 프로젝트는 끝나고 나서 다음 프로젝트까지 여유가 있어 코드리뷰 시간을 가졌다.  
현재 회사에서 이번 프로젝트까지 총 3개의 프로젝트를 진행했었는데 코드리뷰는 처음이라 무척 신났다.  
항상 해보고싶었어 코드리뷰🤩

## 코드리뷰 시간을 잘 활용하기 위한 생각 팁!

어떻게 하면 코드리뷰 시간을 잘 활용하여 더 많이 성장할 수 있을까?  
코드리뷰 시간을 잘 활용하기 위해선 내 코드 돌아보기 뿐만 아니라 다른 팀원분들의 코드도 훑어봐야한다.  
코드를 보면서 아래와 같이 2가지만 생각하면 끝!!

  1. 나한테 맡겨지면 나는 어떻게 구현했을까?
  2. 왜 이 라이브러리를 사용했을까?

  
  
  

## 코드리뷰 어땠어?

첫 코드리뷰는 성공적이었다.  
궁금했던 부분, 애매했던 부분들을 물어볼 수 있는 좋은 기회였고 왜 해당 라이브러리를 사용했는지, 왜 서비스단에서 처리했는지, 컨트롤러에서 하면 뭐가 안 좋은지 등등 궁금증을 와르르 쏟아냈다.  
다들 프로젝트가 끝나서 그런지(?) 친절하게 알려주셨다. 듣는 내내 오른쪽 뇌의 한 부분이 깨어나는 기분이었다.  
아하 아하의 연속!  
너무 재밌어!!!

코드리뷰를 통해서 내가 배운 내용들을 정리해보았다.  
보안상 모든 내용을 기록할 순 없지만 대중적인 부분들을 골라 적었다.  
잊어버리지 않도록!  
똑같은 실수를 하지 않도록!

  
  
  

## 동영상에 iframe을 쓰지 않은 이유

iframe을 사용하면 동적제어가 되지 않는다. 따라서 iframe을 쓰지 않고 [video.js](https://videojs.com/getting-started) 를 사용했다.

  * iframe예시

```html
<iframe id="inlineFrameExample"
    title="Inline Frame Example"
    width="300"
    height="500"
    src="동영상url">
</iframe>
```

  * video.js 예시  
비디오보기 버튼을 클릭시 video.js를 이용하여 모달에 비디오가 출력되는 예시이다.

```html
<button type="button" name="비디오보기"></button>
<div class="modal-body" id="videoModalView"></div>
<script>
$(function() {
	$("button[name=비디오보기]").click(function() {
		let videojs = `<video style="height:500px;width:300px" class="video-js vjs-big-play-button vjs-fluid vjs-time-control" controls autoplay="false" preload="auto" data-setup="{}" controlsList="nodownload"><source src="${동영상url}"/>`;
		$("#videoModalView").html(videojs);
	}
});
</script>
```

  
  
  

## try catch를 했으면 꼭 예외처리를 해야한다.

예외처리 정책을 몰라서 catch 부분에서 error를 log찍고 throw로 던졌다.  
log만 찍으면 예외가 처리된 것이 아니기때문에 아예 없는 것이 낫다.  
차라리 try catch문을 없애면 500에러가 발생해서 문제 발생시 바로 확인 및 처리가 가능하다.

  * 컨트롤러  
현재 상태로는 로그에 에러가 찍히지만 서버는 계속 돌아가므로 에러를 확실히 잡을 수 없다.

```java
@DeleteMapping("/{id}")
public ResponseEntity<String> delete(@PathVariable(name = "id") int id) throws Exception {
	String msg = "";
	try {
		sampleService.delete(id);
		msg = "정상적으로 삭제되었습니다.";
	} catch (Exception e) {
		// TODO: 예외처리정책 필요
		log.error("삭제 중 오류가 발생하였습니다.", e);
		throw e;
	}
	return ResponseEntity.status(HttpStatus.OK).body(msg);
}
```

  * 코드리뷰 후 컨트롤러  
try catch문을 아예 없애 500을 발생시켜 서비스가 멈추도록 했다.  
global error 처리단계에서 500에러인 경우, 잡아서 500에러 페이지를 보여준다.

```java
@DeleteMapping("/{id}")
public ResponseEntity<String> delete(@PathVariable(name = "id") int id) {
	sampleService.delete(id);
	return ResponseEntity.status(HttpStatus.OK).body("정상적으로 삭제되었습니다.");
}
```

  
  
  

## 다중 insert시 서비스에서 처리할 지, 퀴리에서 처리할 지?

경우에 따라 다르다.  
insert 후 바로 수정, 삭제시 id값이 있어야하는 경우, 쿼리에서 for each 돌리는 것보다 서비스에서 for문으로 insert해주는 것이 낫다.

  
  
  

## 쿼리 parameterType과 resultType에 DTO가 들어가도 되는 지?

VO는 readonly이니 쿼리에서 사용해도 될지 고민스러웠다.  
DTO와 VO를 구분하여 사용한다면 쿼리에 parameterType에는 DTO를 resultType에는 VO를 넣어도 된다.

  
  
  

## DB요청은 적을수록 좋다.

상황에 따라 다르지만 기본적으로 DB요청이 적을수록 성능이 빨라진다.

  
  
  

## 쿼리에서 부등호 연산을 한다면 CDATA 구문 말고 대신

쿼리에서 부등호로 연산을 한다면 CDATA대신 `&lt;` 와 `&gt;`를 사용하는 것이 간편하다.

  * 잘못 사용한 예  
CDATA를 사용할때 if조건등이 있는경우 꺽쇠가 있어서 쿼리가 실행 되지않는 오류가 생기기 쉽다.

```sql
<select id="selectList" parameterType="testVO" resultType="testVO">
	/* selectList by sowon-dev 2021.11.23 */
	<![CDATA[
	SELECT	id
				, user_name
				, user_no
	FROM 	testTable
	WHERE 	1 = 1
	<if test="startSearchDate != null and endSearchDate != null">
	AND		regist_dt >= date_format(#{startSearchDate}, '%Y-%m-%d %H:%i:%s')
	AND		regist_dt <= date_format(#{endSearchDate}, '%Y-%m-%d %H:%i:%s')
	</if>
	]]>
</select>
```

  * CDATA 잘 사용한 예  
따라서 해당 부등호에만 CDATA를 적용하는 것을 습관화하면 좋다.

```sql
<select id="selectList" parameterType="testVO" resultType="testVO">
	/* selectList by sowon-dev 2021.11.23 */
	SELECT	id
				, user_name
				, user_no
	FROM 	testTable
	WHERE 	1 = 1
	<if test="startSearchDate != null and endSearchDate != null">
	AND		regist_dt <![CDATA[ >= ]]> date_format(#{startSearchDate}, '%Y-%m-%d %H:%i:%s')
	AND		regist_dt <![CDATA[ <= ]]> date_format(#{endSearchDate}, '%Y-%m-%d %H:%i:%s')
	</if>
</select>
```

  * `&lt;`, `&gt;`를 사용한 예  
CDATA문을 사용하지 않고 HTML방식으로도 가능하며 CDATA문보다 간편하다.

```
<select id="selectList" parameterType="testVO" resultType="testVO">
	/* selectList by sowon-dev 2021.11.23 */
	SELECT	id
				, user_name
				, user_no
	FROM 	testTable
	WHERE 	1 = 1
	<if test="startSearchDate != null and endSearchDate != null">
	AND		regist_dt &gt;= date_format(#{startSearchDate}, '%Y-%m-%d %H:%i:%s')
	AND		regist_dt &lt;= date_format(#{endSearchDate}, '%Y-%m-%d %H:%i:%s')
	</if>
</select>
```

#[회고록](/tags/%ED%9A%8C%EA%B3%A0%EB%A1%9D/)
