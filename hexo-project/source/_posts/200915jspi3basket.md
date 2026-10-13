---
title: "Servlet장바구니2 : 장바구니에 담기"
date: 2020-09-14 18:32:10
tags:
  - "TIL"
  - "ITWILL(JAVA)"
categories:
  - Backend
  - JSP
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Servlet장바구니2 : 장바구니에 담기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    이미 장바구니에 담았던 상품을 또 장바구니담기를 선택한 경우 모든 옵션이 같다면 수량을 1 증가시키는 메서드를 구현해보자.</p>
</div>

<!-- more -->

## `BasketFrontController.java`의 doProcess()의 주소비교 후 처리부분에 코드 추가

```java
// 주소에 따른 처리 구분 (주소 매핑후 이동)
if(command.equals("/BasketAdd.ba")){
	//장바구니 추가 : .jsp -> DB
	System.out.println("C: /BasketAdd.ba 호출");
	//.ag -> .jsp로 이동
	//컨트롤러 -> 뷰페이지 이동
	action = new BasketAddAction();
	try { forward = action.execute(request, response);
	} catch (Exception e) { e.printStackTrace(); }
}
```

  
  
  

## `BasketAddAction.java` 생성

```java
public class BasketAddAction implements Action {

	@Override
	public ActionForward execute(HttpServletRequest request, HttpServletResponse response) 
			throws Exception {
		System.out.println("M : BasketAddAction의 execute() 호출");
		// 로그인 정보 (로그인 처리필요)
		HttpSession session = request.getSession();
		String id = (String) session.getAttribute("id");
		ActionForward forward = new ActionForward();
		if(id == null){
			forward.setPath("./MemberLogin.me");
			forward.setRedirect(false);
			return forward;
		}
		
		//한글처리
		request.setCharacterEncoding("UTF-8");
		
		// 장바구니 저장
		// 상품정보 저장가능 (GoodsDetail 페이지에서 전달)
		// BasketDTO / BasketDAO 객체 	
		// 장바구니 객체 생성
		// 파라미터값 저장(상품번호,구매수량,옵션(크기,색상)) + ID
		BasketDTO bdto = new BasketDTO();
		bdto.setB_g_num(Integer.parseInt(request.getParameter("gno")));
		bdto.setB_g_amount(Integer.parseInt(request.getParameter("amount")));
		bdto.setB_g_size(request.getParameter("size"));
		bdto.setB_g_color(request.getParameter("color"));
		bdto.setB_m_id(id);
		//bdto.setB_date(b_date);
		//bdto.setB_num(b_num);
		System.out.println("장바구니 객체정보: "+bdto);
		
		// BasketDAO 객체 생성
		BasketDAO bdao = new BasketDAO();
		//해당상품(+옵션까지)이 장바구니에 동일한게 있는지 체크
		int result = bdao.checkGoods(bdto);
		
		// basketAdd() - 추가
		if(result != 1){ //장바구니에 해당상품이 없다
			bdao.basketAdd(bdto);
		}
		
		//장바구니list로 이동
		forward.setPath("./BasketList.ba");
		forward.setRedirect(true);
		return forward;
	}
}
```

  
  
  

## `BasketDAO.java`에 checkGoods()메서드 코드 추가

이미 장바구니에 담았던 상품을 또 장바구니담기를 선택한 경우 모든 옵션이 같다면 수량을 1 증가시키는 메서드를 구현해보자.

```java
//동일한 상품이 있는지 체크
public int checkGoods(BasketDTO bkdto) {
	int result = 0;

	try{
		getCon();
		//sql : id, gno, size, color 모두 만족하는 대상 검색
		sql ="select * from itwill_basket "
				+ "where b_m_id=? and b_g_num=? and b_g_size=? and b_g_color=?";
		pstmt = con.prepareStatement(sql);
		pstmt.setString(1, bkdto.getB_m_id());
		pstmt.setInt(2, bkdto.getB_g_num());
		pstmt.setString(3, bkdto.getB_g_size());
		pstmt.setString(4, bkdto.getB_g_color());
		rs = pstmt.executeQuery();
		if(rs.next()){ //중복상품인 경우
			result = 1;
			//구매수량 수정
			sql ="update itwill_basket set b_g_amount=b_g_amount+? "
					+ "where b_m_id=? and b_g_num=? and "
					+ "b_g_size=? and b_g_color=?";
			pstmt = con.prepareStatement(sql);
			pstmt.setInt(1, bkdto.getB_g_amount());
			pstmt.setString(2, bkdto.getB_m_id());
			pstmt.setInt(3, bkdto.getB_g_num());
			pstmt.setString(4, bkdto.getB_g_size());
			pstmt.setString(5, bkdto.getB_g_color());
			pstmt.executeUpdate();
			System.out.println("기존의 상품에 수량 변경완료!");
		}
		System.out.println("기존의 상품 확인 결과: "+(result==1? "중복상품이 있다":"중복상품이 없다"));
		sql = "insert into itwill_basket";
	}catch(Exception e){
		e.printStackTrace();
	}finally {
		closeDB();
	}
	return result;
}//end of checkGoods()
```

  
  
  

## `BasketDAO.java`에 basketAdd()메서드 코드 추가

```java
//장바구니에 담기
public void basketAdd(BasketDTO bkdto) {
	int b_num = 0;
	try{
		getCon();
		//1. 장바구니 번호계산		
		sql = "select max(b_num) from itwill_basket";
		pstmt = con.prepareStatement(sql);
		rs = pstmt.executeQuery();
		if(rs.next()){
			b_num = rs.getInt(1)+1; //인덱스 사용 호출
			//rs.getInt("max(bno)"); // 컬럼명 사용 호출
		}
		System.out.println("DAO : b_num은 "+b_num);

		//2.나머지 전달정보 DB에 저장
		sql = "insert into itwill_basket values(?,?,?,?,?,"
				+ "?,now())";
		pstmt = con.prepareStatement(sql);
		pstmt.setInt(1, b_num);
		pstmt.setString(2, bkdto.getB_m_id());
		pstmt.setInt(3, bkdto.getB_g_num());
		pstmt.setInt(4, bkdto.getB_g_amount());
		pstmt.setString(5, bkdto.getB_g_size());
		pstmt.setString(6, bkdto.getB_g_color());
		pstmt.executeUpdate();
		System.out.println("장바구니 담기 성공");
	}catch(Exception e){
		e.printStackTrace();
	}finally {
		closeDB();
	}
}//end of basketAdd()
```

#[TIL](/tags/TIL/)[ITWILL(JAVA)](/tags/ITWILL-JAVA/)
