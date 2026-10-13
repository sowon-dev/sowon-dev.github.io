---
title: "[JAVA] java.util.properties 개념과 예시, properties파일과 차이점"
date: 2024-11-28 17:05:27
tags: []
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">java.util.Properties는 문자열 기반의 키-값 쌍을 다루며 실행 중에도 설정값을 동적으로 변경할 수 있는 자바 내부 메모리 객체다.
    반면 .properties 파일은 애플리케이션 구동 시 초기 설정 정보를 제공하는 정적 외부 파일로, 상황과 목적에 맞게 두 방식을 적절히 구분하여 활용할 수 있다.</p>
</div>

<!-- more -->

레거시를 분석하던 중 이메일전송 서비스에서 java.util.Properties 객체를 발견했다.  
처음보는 객체라서 무엇인지 확인해보았다.

# java.util.Properties

  * [오라클 java.util.Properties](https://docs.oracle.com/javase/7/docs/api/java/util/Properties.html)  
오라클문서에 따르면 Properties객체는 (String, String)을 가진 객체로 Hashtable에서 상속했다.  
따라서 Hashtable의 메서드인 put(), putAll()을 사용할 수 있으나 setProperty() 사용을 권장한다.  
그 이유는 put(), putAll()에는 String이외의 값이 들어갈 수 있기 때문에 에러 발생활률이 높다.

  
  
  

# 장단점

  * 장점

**장점** | **설명**  
---|---  
**간단한 키-값 관리** | 문자열 기반의 키-값 쌍을 쉽게 관리할 수 있습니다.  
**파일 입출력 지원** | `.properties` 파일을 간편하게 읽고 쓸 수 있습니다.  
**기본값 제공 기능** | 다른 `Properties` 객체를 기본값으로 설정할 수 있어 유연합니다.  
**국제화 (i18n) 지원** | 다국어 지원을 위한 리소스 번들과 통합이 용이합니다.  
**동적 설정 변경** | 실행 중에도 설정 값을 동적으로 변경할 수 있습니다.  
  * 단점

**단점** | **설명**  
---|---  
**문자열 기반 한계** | 복잡한 데이터 구조를 저장하기 어렵고 문자열로만 저장됩니다.  
**보안 취약성** | 설정 파일이 평문으로 저장되므로 민감한 정보 노출 위험이 있습니다.  
**데이터 형 변환 필요** | 숫자, 불리언 등 다른 데이터 타입은 변환 코드가 필요합니다.  
**스레드 안전성 부족** | 스레드 안전하지 않아 여러 스레드에서 접근 시 동기화가 필요합니다.  

  
  
  

# 사용예시

```java
//선언
private Properties props = new Properties();

//입력 
props.put("mail.smtp.host", "smtp.gmail.com");      // smtp 서버 주소
props.put("mail.smtp.auth", "true");				        // 자바 메일 API가 사용자 이름과 비밀번호를 제공하여 SMTP 서버에 인증을 시도하겠다는 의미(gmail은 무조건 true 고정)
props.setProperty("mail.smtp.starttls.enable", "true");     // TLS라는 보안인증서 활성화(SSL)(gmail은 무조건 true 고정)
props.setProperty("mail.smtp.port", "587");                 // gmail포트587, 네이버 메일포트465

//출력
properties.getProperty("mail.smtp.host");
properties.getProperty("mail.smtp.starttls.enable");

//아웃풋
smtp.gmail.com
true
```

  
  
  

# 그동안 왜 몰랐을까?

속성들 관리를 `.properties`에서 했기때문에 몰랐었다!

  
  
  

## 사용예시

```xml
// 스프링부트인 경우 application.properties에 동일하게 선언
mail.smtp.host=smtp.gmail.com         # smtp 서버 주소
mail.smtp.auth=true                   # 자바 메일 API가 사용자 이름과 비밀번호를 제공하여 SMTP 서버에 인증을 시도하겠다는 의미
mail.smtp.starttls.enable=true        # TLS라는 보안 인증서 활성화 (SSL)
mail.smtp.port=587                    # gmail 포트 587, 네이버 메일 포트 465

// 사용
@Value("\${mail.smtp.port:465}") //만약 properties에 지정된 값이 없을 경우 465
```

  
  
  

# java.util.Properties 클래스와 `.properties`주요 차이점:

  1. 파일과 코드의 역할:
     * `.properties` 파일: 외부 파일로서 애플리케이션의 설정 정보를 저장합니다.
     * `java.util.Properties` 클래스: 이 파일을 읽고 쓰기 위한 자바의 내부 메모리 표현입니다.
  2. 데이터 접근:
     * 파일: 사람이 읽기 쉽고, 외부에서 직접 수정할 수 있습니다.
     * 클래스: 프로그램 내에서 동적으로 프로퍼티를 읽거나 설정할 수 있습니다.
  3. 동적 변경:
     * 파일: 파일을 수정하고 저장해야만 값이 바뀝니다.
     * 클래스: 런타임에 setProperty() 메서드로 변경이 가능합니다.
  4. 로드 및 저장:
     * `.properties` 파일은 주로 애플리케이션 시작 시 설정값을 불러올 때 사용됩니다.
     * Properties 객체는 메모리 내에서 이 설정 값을 관리하며, 필요 시 다시 파일에 저장할 수도 있습니다.

이외에도 싱글톤패턴일때 java.util.Properties를 사용한다고한다.  
프로젝트에 적합한 방법을 선택하면 된다.
