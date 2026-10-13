---
title: "[Lombok]@build, @Data 차이"
date: 2021-08-17 23:13:17
tags:
  - "Lombok"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'@build, @Data 차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    이제 어노테이션별 차이를 살펴보자.</p>
</div>

<!-- more -->

자바프로젝트를 사용하면서 없어선 안될 라이브러리가 바로 롬복이다.  
스프링부트프로젝트로 생성시 롬복 라이브러리를 바로 추가할 수 있다.  
또는 사이트에서 jar를 다운로드받아 외부라이브러리로 import하여 사용할 수 있다.

  * [Lombok 사이트](https://projectlombok.org/)

이제 어노테이션별 차이를 살펴보자.

## 롬복 어노테이션

구분 | 설명  
---|---  
@Data | @Getter + @Setter + @RequiredArgsConstructor + @ToString + @EqualsAndHashCode 를 한꺼번에 제공  
@Builder | @AllArgsConstructor와 비슷하게 객체를 생성하고 필드값을 주입해주는데 빌더의 형식을 제공함  
@NoArgsConstructor | 파라미터가 없는 생성자 제공. JPA 사용시 필수  
@AllArgsConstructor | 필드의 모든 변수가 있는 생성자 제공  
  
  
  
  

## 예시

  * User.java

```java
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class User {
	private String name;
	private String email;
	private LocalDateTime createdAt = LocalDateTime.now();
	private LocalDateTime updatedAt;
}
```

위 클래스를 jUnit으로 테스트해보자.

  * UserTest.java

```java
class UserTest {

	@Test
	void test() {
		// setter 사용
		User u1 = new User();
		u1.setName("마리아");
		u1.setEmail("maria@example.com");
		u1.setCreatedAt(LocalDateTime.now());
		u1.setUpdatedAt(LocalDateTime.now());
		System.out.println("@ test u1: "+u1);
		
		// @AllArgsConstructor 생성자로 생성
		User u2 = new User("가나다", "ganada@example.com", LocalDateTime.now(), LocalDateTime.now());
		System.out.println("@ test u2: "+u2);
		
		// @NoArgsConstructor 생성자로 생성
		User u3 = new User();
		System.out.println("@ test u3: "+u3);
		
		// @Builder 로 생성
		User u4 = User.builder()
				.name("마바사")
				.email("mabasa")
				.updatedAt(LocalDateTime.now())
				.build();
		System.out.println("@ test u4: "+u4);
	}

}
```

User객체 4개가 생성되었고 그 결과는 아래와 같다.

```plain
@ test u1: User(name=마리아, email=maria@example.com, createdAt=2021-08-18T22:01:39.588614800, updatedAt=2021-08-18T22:01:39.588614800)
@ test u2: User(name=가나다, email=ganada@example.com, createdAt=2021-08-18T22:01:39.588614800, updatedAt=2021-08-18T22:01:39.588614800)
@ test u3: User(name=null, email=null, createdAt=2021-08-18T22:01:39.588614800, updatedAt=null)
@ test u4: User(name=마바사, email=mabasa, createdAt=null, updatedAt=2021-08-18T22:01:39.589613600)
```

  
  
  

## 결론

상황에 맞는 롬복을 사용하면 된다!

#[Lombok](/tags/Lombok/)
