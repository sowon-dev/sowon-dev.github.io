---
title: "JSP 페이지 등록일순 역순출력"
date: 2021-01-28 19:56:39
tags:
  - "오류일지"
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">JSP 페이지 등록일순 역순출력의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    ${pageInfo.data} 가 어떤 데이터를 들고 오는 지 먼저 확인한 후 필요한 변수들을 체크했다.</p>
</div>

<!-- more -->

프로그래머는 매 순간 버그와의 싸움이다.  
한 번에 문제 원인을 찾고 해결하면 정말 좋겠지만 아직 나는 많이 부족하다.  
그렇게 될 수 있도록 문제상황에 어떻게 원인을 찾고 해결을 했는지 기록하고자 한다.  
기억보다 기록은 힘이 세다고 믿으니까.

## 문제상황

리스트를 idx순으로 출력하는데 순번이상했다.

![](/img/210129pagination.PNG)

  
  
  

## 원인

쿼리 먼저 돌려보면서 SELECT되는 데이터를 체크해보았다.  
DB를 테스트 한 뒤 테스트데이터를 삭제해야하는데 그 위에 타DB의 데이터를 이관하면서 DB의 INDEX순서와 게시글 등록순서가 아래 예시처럼 일치하지 않았다.

  * 예시 idx | reg_date  
---|---  
1 | 2021-01-20  
2 | 2021-01-25  
3 | 2020-12-10  
4 | 2021-01-23  

  
  
  

## 기존 코드

  * Mapper.xml 코드

```xml
<select id="List" parameterType="model" resultType="model" >
	<include refid="pagingStart"/>
	<![CDATA[
		SELECT
			ROW_NUMBER() OVER (ORDER BY IDX DESC) rn
			, IDX, NAME, REGDATE, CONTENT 
		FROM
				테이블명
	]]>
	<include refid="withSearchWhere"/>
	ORDER BY IDX DESC
	<include refid="pagingEnd"/>
</select>
```

  * view.jsp코드

```
<c:forEach var="result" items="${pageInfo.data}" varStatus="i">
	<tr>
		<td>${result.idx}</td>
		<td>${result.name}</td>
		<td><c:if test="${not empty result.content}">${result.content}</c:if></td>
	</tr>
</c:forEach>
```

DB에서 순번을 가져오지말고 뷰단에서 직접 게시글을 카운팅해주는 것으로 해결 방향을 잡았다.  
${pageInfo.data} 가 어떤 데이터를 들고 오는 지 먼저 확인한 후 필요한 변수들을 체크했다.  
totalCount, pageIndex, pageSize를 사용할 수 있을 것 같아 가져왔다.

또한 DB데이터들 중 index 순서 대신 다른 정렬기준을 찾아야헸고 나는 REG_DATE를 선택했다.

  
  
  

## 수정한 코드

  * Mapper.xml 코드

```xml
<select id="List" parameterType="model" resultType="model" >
	<include refid="pagingStart"/>
	<![CDATA[
		SELECT
			ROW_NUMBER() OVER (ORDER BY IDX DESC) rn
			, IDX, NAME, REGDATE, CONTENT 
		FROM
				테이블명
	]]>
	<include refid="withSearchWhere"/>
	ORDER BY REGDATE DESC
	<include refid="pagingEnd"/>
</select>
```

  * view.jsp코드

총 게시글이 14개가 있고 한 페이지당 10개씩 보여준다고 설정했다고 하자.  
그렇다면 총 2페이지가 될 것이다.  
첫번째페이지에서는 14부터 5까지 출력되고 두번째페이지에서는 4부터 1까지 번호가 출력되어야한다.  
핵심은 2번째페이지이다. 두번째 페이지 번호가 4부터 출력되어야한다.  
총 14개 중에서 pageSize인 10을 빼야 4가 출력된다.  
이를 식으로 나타내면 `(PageIndex - 1)*pageSize`이다.

```
<c:set value="${pageInfo.totalCount}" var="totalCountj_JO" />
<c:set value="${pageInfo.pageIndex}" var="PageIndex_JO" />
<c:set value="${pageInfo.pageSize}" var="pageSize_JO" />
<% 
int cntJO = (int)pageContext.getAttribute("totalCountj_JO");
int PageIndex_JO = (int)pageContext.getAttribute("PageIndex_JO");
int pageSize_JO = (int)pageContext.getAttribute("pageSize_JO");
cntJO = cntJO - ((PageIndex_JO - 1)*pageSize_JO);
%> 
<c:forEach var="result" items="${pageInfo.data}" varStatus="i">
	<tr>
		<td class="tit"><%=cntJO %></td>
		  <%
		  cntJO = cntJO - 1 ;
		  %>
	</tr>
</c:forEach>
```

EL과 JSTL, 스크립틀릿을 왔다갔다하면서 컨트롤러에서 처리한 데이터를 받을 때 익숙하지 않아서 많이 해맸다.  
처음에는 for문을 사용하려고 했으나 forEach문이 이미 있기에 코드가 복잡해졌다.  
더 좋은 코드가 있을 것 같은데 시간도 부족해서 `cntJO = cntJO - 1;`처럼 직관적으로 처리했다.  
코드 리팩토링을 생각해봐야겠다.

  
  
  

## 또 다른 문제 발생

위에서 수정한 코드는 로그인 세션이 있을때는 정상출력되었지만 로그인 세션이 없는 경우 404페이지가 발생했다.  
DB에 바로 갈 수 없도록 해야했다.  
그래서 `int cntJO = 0`으로 초기화 먼저 한 후 if문 안에서 DB에서 데이터를 가져오는 변수를 생성했다. 

  * view.jsp코드

```jsp
<% 
int cntJO = 0;
if(request.getAttribute("conText") != null){
	cntJO = (int)pageContext.getAttribute("totalCountj_JO");
	int PageIndex_JO = (int)pageContext.getAttribute("PageIndex_JO");
	int pageSize_JO = (int)pageContext.getAttribute("pageSize_JO");
	cntJO = cntJO - ((PageIndex_JO - 1)*pageSize_JO);			
}
%>
```

TA-DA 문제해결!

#[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)
