---
title: "[JAVA] Gmail SMTP 다중 메일 예제"
date: 2024-11-28 17:10:28
tags: []
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Gmail SMTP 다중 메일 예제의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    핵심 설정과 구현 코드를 단계별로 파악하여 상황에 맞게 유연하게 활용할 수 있다.</p>
</div>

<!-- more -->

java.util.Properties 와 javax.mail 패키지를 이용하여 여러 사람에게 메일을 보내보자.

# 구글 gmail 인증을 위한 Class

```java
public class MailAuthenticator extends Authenticator {
    private String id;
    private String pw;

    public MailAuthenticator(String id, String pw){
        this.id = id;
        this.pw = pw; 
    }
    protected PasswordAuthentication getPasswordAuthentication() {
        return new PasswordAuthentication(id, pw);
    }
}
```

  
  
  

# 구글 gmail 발송 코드

```java
public class MailUtil {
	// 발신자정보
	private String user = "test@gmail.com";
	private String passwd = "test";
		
	private Session mailSession;
	private Properties props = new Properties();
	props.put("mail.smtp.host", "smtp.gmail.com");      // smtp 서버 주소
	props.put("mail.smtp.auth", "true");				        // 자바 메일 API가 사용자 이름과 비밀번호를 제공하여 SMTP 서버에 인증을 시도하겠다는 의미(gmail은 무조건 true 고정)
	props.setProperty("mail.smtp.starttls.enable", "true");     // TLS라는 보안인증서 활성화(SSL)(gmail은 무조건 true 고정)
	props.setProperty("mail.smtp.port", "587");                 // gmail포트587, 네이버 메일포트465
	
	public boolean sendMail(List<InternetAddress> to, String subject, StringBuffer content) {
			if(to == null || to.size() == 0) {
				return false;
			}
			
			//구글 계정 인증
			Authenticator authenticator = new MailAuthenticator(user, passwd);
			
			//세션
			mailSession = Session.getDefaultInstance(props, authenticator);
			MimeMessage msg = new MimeMessage(mailSession);
			
			//보내는사람
			InternetAddress from = new InternetAddress();
			String fromName = "발신자 닉네임";
			from = new InternetAddress(new String(fromName.getBytes(charSet), "8859_1") + "<발신자 구글 이메일@gmail.com>");
			msg.setFrom(from);
			
			//받는사람(여러명)
			InternetAddress[] address = new InternetAddress[to.size()];

			for (int i = 0; i < to.size(); i++) {
				address[i] = to.get(i);
			}
			msg.setRecipients(Message.RecipientType.TO, address);
			
			//제목
			msg.setSubject(subject, "UTF-8");
			
			//내용
			msg.setContent(content.toString(), "text/html; charset=UTF-8"); // HTML 형식
			
			//보내는날짜
			msg.setSentDate(new java.util.Date());
			
			//전송
			Transport.send(msg);
			return true;
	}
}
```
