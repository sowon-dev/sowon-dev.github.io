---
title: "[스프링SPRING MVC]구글 로그인 API(google login API)"
date: 2020-10-30 06:11:53
tags:
  - "TIL"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">구글 로그인 API(google login API)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    나는 일반 회원가입과 로그인도 만들고 구글 아이디로 회원가입과 동시에 로그인하는 코드를 구현했다.</p>
</div>

<!-- more -->

## 기본배경지식

팀프로젝트로 SNS API 로그인 기능을 구현했다.  
간단할 줄 알았는데 이틀이나 고생을 했다. 안되겠다싶어서 생활코딩으로 개념을 잡고 다시 차근차근하니 성공했다!  
역시 기본기가 중요하다. 그냥 코드붙여넣지말고 개념을 챙기자!

나는 일반 회원가입과 로그인도 만들고 구글 아이디로 회원가입과 동시에 로그인하는 코드를 구현했다.  
간단한 방식으로 만들었으므로 완벽한 코드가 아님을 미리 알린다.

  * [구글 WEB 로그인 문서](https://developers.google.com/identity/sign-in/web/sign-in)
  * [구글 버튼 디자인 바꾸기](https://developers.google.com/identity/sign-in/web/build-button)

  
  
  

## 폴더구조

![](/img/201030googlelogin.PNG)

  
  
  

## 구글 APIs에서 사용자 인증정보생성

  * [구글 API 사용자 인증 정보](https://console.developers.google.com/apis/credentials?authuser=3&project=bestpricemarket-294001&supportedpurview=project)
  * 프로젝트이름과 URI 그리고 리디렉션 URI 를 설정한다.
    * URI : 로그인하는 URI
    * 리디렉션 URI : 로그인 후에 이동할 URI

![](/img/201030googlelogin2.PNG)

  
  
  

## `MemberController` 코드

```java
import javax.inject.Inject;
import javax.servlet.http.HttpSession;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.bestpricemarket.domain.MemberVO;
import com.bestpricemarket.service.MemberService;

@Controller
@RequestMapping(value = "/member/*")
public class MemberController {

	@Inject
	//@Autowired
	private MemberService service;
	
	private static final Logger l = LoggerFactory.getLogger(MemberController.class);
	
	/* 회원가입 */
	// http://localhost:8088/member/join
	
	@RequestMapping(value = "/join", method = RequestMethod.GET)
	public String insertGET() throws Exception {
		return "/member/loginandjoin";
	}
	
	@RequestMapping(value = "/join", method = RequestMethod.POST)
	public String insertPOST(MemberVO vo) throws Exception{
		l.info("C: 회원가입포스트메서드"+ vo);
		service.joinMember(vo);		
		return "redirect:/member/login";
	}
	
	//회원가입시 아이디중복확인
	@RequestMapping(value = "/idCheck", method = RequestMethod.POST)
	public @ResponseBody int idCheck(@RequestParam("id") String id) throws Exception {
		MemberVO ck = service.idCheck(id);
		if(ck != null) return 1;
		else return 0;
	}
	
	/* 로그인 기능 */
	// http://localhost:8088/member/login
	
	@RequestMapping(value = "/login", method = RequestMethod.GET)
	public String loginGET() throws Exception{
		return "/member/loginandjoin";
	}
	
	@RequestMapping(value = "/login", method = RequestMethod.POST)
	public String loginPOST(MemberVO vo, HttpSession session, RedirectAttributes rttr) throws Exception{
		MemberVO returnVO = service.loginMember(vo);
		System.out.println("C: 리턴VO결과(서비스에서 예외처리를 진행했으므로 null이 출력되면 코드에 문제있다는 의미) "+returnVO);
		
		if(returnVO != null) {
			session.setAttribute("id", returnVO.getId());			
			rttr.addFlashAttribute("mvo", returnVO);
			return "redirect:/member/main"; 
		} else {
			return "redirect:/member/login";
		}
	}
	
	/* 로그아웃 */
	@RequestMapping(value = "/logout", method = RequestMethod.GET)
	public void logoutGET(HttpSession session) throws Exception{
		l.info("C: 로그아웃 GET");
		session.invalidate();
		// return "redirect:/member/main"; 얼럿창출력안하고싶을때 사용
	}
	
	/* 구글아이디로 로그인 */	
    @ResponseBody
	@RequestMapping(value = "/loginGoogle", method = RequestMethod.POST)
	public String loginGooglePOST(MemberVO vo, HttpSession session, RedirectAttributes rttr, MemberVO mvo) throws Exception{
		MemberVO returnVO = service.loginMemberByGoogle(vo);
		String mvo_ajaxid = mvo.getId(); 
		System.out.println("C: 구글아이디 포스트 db에서 가져온 vo "+ vo);
		System.out.println("C: 구글아이디 포스트 ajax에서 가져온 id "+ mvo_ajaxid);
		
		if(returnVO == null) { //아이디가 DB에 존재하지 않는 경우
			//구글 회원가입
			service.joinMemberByGoogle(vo);	
			
			//구글 로그인
			returnVO = service.loginMemberByGoogle(vo);
			session.setAttribute("id", returnVO.getId());			
			rttr.addFlashAttribute("mvo", returnVO);
		}
		
		if(mvo_ajaxid.equals(returnVO.getId())){ //아이디가 DB에 존재하는 경우
			//구글 로그인
			service.loginMemberByGoogle(vo);
			session.setAttribute("id", returnVO.getId());			
			rttr.addFlashAttribute("mvo", returnVO);
		}else {//아이디가 DB에 존재하지 않는 경우
			//구글 회원가입
			service.joinMemberByGoogle(vo);	
			
			//구글 로그인
			returnVO = service.loginMemberByGoogle(vo);
			session.setAttribute("id", returnVO.getId());			
			rttr.addFlashAttribute("mvo", returnVO);
		}
		
		return "redirect:/member/main";
	}
```

  
  
  

## 일반 회원가입, 로그인, 로그아웃 기능 구현

아래 포스팅을 참고해서 일반 회원가입과 로그인 로그아웃기능을 구현했다.  
구글 SNS API를 추가한 코드만 작성하고자한다.

  * [회원가입 및 로그인기능 구현](https://sowon-dev.github.io/2020/10/18/201019spring-2/)
  * [로그아웃](https://sowon-dev.github.io/2020/10/19/201020spring/)

  
  
  

## `MemberService.java` 코드

```java
import com.bestpricemarket.domain.MemberVO;

// 일반적으로는 DAO랑 같은 메소드명을 사용하여 일관성을 유지한다
public interface MemberService {
	// 회원 가입 (일반회원가입테이블에 sns계정 컬럼 추가하기)	
	public void joinMember(MemberVO vo);
	
	// 로그인
	public MemberVO loginMember(MemberVO vo);

	// 회원가입시 아이디중복확인
	public MemberVO idCheck(String id);
	
	// 회원정보 보기
	public MemberVO readMember(String id);
	
	// 회원정보 수정
	public void updateMember(MemberVO vo);
	
	// 회원탈퇴
	public void deleteMember(MemberVO vo);
	
	//구글회원가입
	public void joinMemberByGoogle(MemberVO vo);
	
	//구글로그인
	public MemberVO loginMemberByGoogle(MemberVO vo);
	
}
```

  
  
  

## `MemberServiceImpl.java` 코드

일반 회원가입/로그인과 구글을 이용한 회원가입/로그인을 나누어서 작성해보았다.

```java
import javax.inject.Inject;

import org.springframework.stereotype.Service;

import com.bestpricemarket.domain.MemberVO;
import com.bestpricemarket.persistence.MemberDAO;

@Service
public class MemberServiceImpl implements MemberService{

	//DB와 연결 (의존주입)
	@Inject
	//@Autowired
	private MemberDAO mdao;

	// 회원가입
	@Override
	public void joinMember(MemberVO vo) {
		mdao.joinMember(vo);		
	}

	// 로그인
	@Override
	public MemberVO loginMember(MemberVO vo) {
		MemberVO returnVO = null;
		try {
			returnVO = mdao.readMemberWithIDPW(vo.getId(), vo.getPw());
			System.out.println("S: 로그인 아디: "+vo.getId()+" 비번: "+vo.getPw()+" 이름: "+vo.getUsername());
		} catch (Exception e) {
			e.printStackTrace();
			returnVO = null; //실행하다 문제가 생겼을때 해당 데이터를 보내지않겠다는 의미 = 예외처리
		}
		return returnVO; 
	}
	
	// 회원가입시 아이디중복확인
	@Override
	public MemberVO idCheck(String id) {
		return mdao.idCheck(id);
	}

	// 회원정보보기
	@Override
	public MemberVO readMember(String id) {
		MemberVO vo = null;
		try {
			vo = mdao.readMember(id);
			System.out.println("S: 로그인 정보 리턴");
		} catch (Exception e) {
			e.printStackTrace();
		}
		return vo;
	}

	// 회원정보 수정
	@Override
	public void updateMember(MemberVO vo) {
		try {
			mdao.updateMember(vo);
		} catch (Exception e) {
			e.printStackTrace();
		}	
	}

	// 회원탈퇴
	@Override
	public void deleteMember(MemberVO vo) {
	    try {
			mdao.deleteMember(vo);
			System.out.println("S: vo 확인"+vo);
	    } catch (Exception e) {
		
			e.printStackTrace();
		}
	}

	//구글 회원가입
	@Override
	public void joinMemberByGoogle(MemberVO vo) {
		mdao.joinMember(vo);
	}

	//구글 로그인
	@Override
	public MemberVO loginMemberByGoogle(MemberVO vo) {
		MemberVO returnVO = null;
		try {
			returnVO = mdao.readMemberWithIDPW(vo.getId(), vo.getPw());
			System.out.println("S: 로그인 아디: "+vo.getId()+" 비번: "+vo.getPw()+" 이름: "+vo.getUsername());
		} catch (Exception e) {
			e.printStackTrace();
			returnVO = null; //실행하다 문제가 생겼을때 해당 데이터를 보내지않겠다는 의미 = 예외처리
		}
		return returnVO;
	}
}
```

  
  
  

## `loginandjoin.jsp` 코드

가장 중요한 건 뷰이다. Ajax를 이용하여 데이터를 넘겼다.

  * 구글 로그인 버튼

```html
<span id="google_login" class="circle google" onclick="init();"> <i class="fa fa-google-plus fa-fw"></i> </span>
```

  * 스크립트 코드  
구글에 따르면 profile.getId()값을 id로 서버로 전송하지말고 id_token사용을 사용하라고 적혀있다.  
보안문제가 발생할 수 있기 때문이다.

```html
<!-- google signin api -->
<script src="https://apis.google.com/js/platform.js?onload=init" async defer></script>

// google signin API
var googleUser = {};
function init() {
	 gapi.load('auth2', function() {
	  console.log("init()시작");
	  auth2 = gapi.auth2.init({
	        client_id: '구글API의 클라이언트 ID 입력'
	        cookiepolicy: 'single_host_origin',
	      });
	      attachSignin(document.getElementById('google_login'));
	 });
}

//google signin API2
function attachSignin(element) {
    auth2.attachClickHandler(element, {},
        function(googleUser) {
    	var profile = googleUser.getBasicProfile();
    	var id_token = googleUser.getAuthResponse().id_token;
	  	  console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
	  	  console.log('ID토큰: ' + id_token);
	  	  console.log('Name: ' + profile.getName());
	  	  console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
			$(function() {
				$.ajax({
				    url: '/member/loginGoogle',
				    type: 'post',
				    data: {
						"id" : <!-- 필요한 데이터 담기 -->,
						"pw" : <!-- 필요한 데이터 담기 -->,
				        "username": profile.getName(),
						"email": profile.getEmail()
					    },
				    success: function (data) {
				            alert("구글아이디로 로그인 되었습니다");
				            location.href="/member/main";
				        }
				});
			})
        }, function(error) {
          alert(JSON.stringify(error, undefined, 2));
        });
    console.log("구글API 끝");
  }
```

  
  
  

## 결과물

![](/img/201030googlelogin3.gif)

  
  
  

## 참고

  * [생활코딩 WEB2 - OAuth 2.0개념](https://opentutorials.org/course/3405)
  * [생활코딩 Google Login](https://opentutorials.org/course/3424)

#[TIL](/tags/TIL/)
