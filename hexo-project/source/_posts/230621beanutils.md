---
title: "[JAVA/Spring]BeanUtils"
date: 2023-06-20 23:30:42
tags: []
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">BeanUtils의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    스프링에서 기본으로 제공해주는 메소드로서 객체를 쉽고 간결하게 복사할 수 있다. 너무너무 편하다!을 적용할 수 있다.</p>
</div>

<!-- more -->

이렇게 좋은 유틸이 있었다니 왜 몰랐지?!  
클래스들을 서로 복사하는 작업을 해야하는데 그때마다 엄청난 set때문에 가독성도 떨어지고 코드도 길어지고 참 마음에 안들었다.  
차장님이 쓴 코드를 읽을 기회가 있었는데 BeanUtil를 이용해서 한 줄로 간결하게 짜여진 코드를 보고 감동했다!

유레카! 내가 찾던 것이 바로 이거야!  
그래서 BeanUtils에 대해 공부해봤다.

# Class BeanUtils

스프링에서 기본으로 제공해주는 메소드로서 객체를 쉽고 간결하게 복사할 수 있다. 너무너무 편하다!

  * 패키지: org.springframework.beans

  
  
  

# 기본형

```java
copyProperties(Object source, Object target)
source - 원본 객체
target - 복사 객체
```

  * source에는 setter메소드 필수
  * target에는 getter메소드 필수

동일한 필드명만 복사가 된다.

  
  
  

# 예시

이제 예시를 살펴보자  
아래처럼 2개의 객체가 있다. 교수객체 중 특정 객체는 면접관객체로 복사해야한다고 가정해보자.

```java
@SpringBootApplication
public class SimpleTestApplication {
	@Data @AllArgsConstructor
	static class Professor {
		private String name;
		private String major;
		private String hp;
		private int professorId;
	}

	@Data
	static class Interviewer {
		private String name;
		private String major;
		private String hp;
		private int interviewerId;
	}

	public static void main(String[] args) {
		SpringApplication.run(SimpleTestApplication.class, args);

		Professor p1 = new Professor("김노동", "건축학", "010-1234-1234", 111);
		System.out.println(p1.toString());
		//결과: Professor(name=김노동, major=건축학, hp=010-1234-1234, professorId=111)

		// 1. Setter 사용하기
		Interviewer a = new Interviewer();
		a.setName(p1.getName());
		a.setMajor(p1.getMajor());
		a.setHp(p1.getHp());
		System.out.println(a.toString());
		//결과: Interviewer(name=김노동, major=건축학, hp=010-1234-1234, interviewerId=0)

		// 2. BeanUtils.copyProperties()사용: 동일한 필드 전체 복사
		Interviewer b = new Interviewer();
		BeanUtils.copyProperties(p1, b);
		System.out.println(b.toString());
		//결과: Interviewer(name=김노동, major=건축학, hp=010-1234-1234, interviewerId=0)

		// 3. BeanUtils.copyProperties()사용: p1의 name필드를 제외한 채 c로 복사
		Interviewer c = new Interviewer();
		BeanUtils.copyProperties(p1, c, "name"); //name속성은 무시
		System.out.println(c.toString());
		//결과: Interviewer(name=null, major=건축학, hp=010-1234-1234, interviewerId=0)
	}
}
```

1번 Setter를 이용하는 방법은 직관적이나 코드가 길어져서 필드가 많을 경우 가독성이 매우 떨어진다.  
이땐 2번처럼 `BeanUtils.copyProperties()`을 사용하면 동일한 필드명은 복사가 된다!  
만약 특정 필드를 빼고 싶다면 3번처럼 ignoreProperties 를 사용하면 된다.

  
  
  

# 참고

  * [docs.spring.io/spring-framework](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/beans/BeanUtils.html)
