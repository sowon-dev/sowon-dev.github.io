---
title: "[JPA]@CreatedDate에 날짜가 안 담길때 오류"
date: 2021-11-29 15:57:08
tags:
  - "패스트캠퍼스(초격차Java/Spring)"
categories:
  - Backend
  - JPA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">이런 오류는 대부분 auditing이 제대로 적용되지 않았을때 발생한다.
    Entity클래스에 @EntityListeners 추가되어있지 않아서 Auditing기능이 작동하지않았다.</p>
</div>

<!-- more -->

@CreatedDate를 사용하여 save()메서드로 데이터를 insert하는데 날짜가 null로 나왔다.  
이런 오류는 대부분 auditing이 제대로 적용되지 않았을때 발생한다.

![created_at 컬럼이 현재시간이 아닌 null값이다](/img/211130jpaAuditing1.PNG)

  
  
  

## 원인

Entity클래스에 @EntityListeners 추가되어있지 않아서 Auditing기능이 작동하지않았다.

  * Sample.java

```java
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Entity
public class Sample {

	@Id
	@GeneratedValue(strategy =GenerationType.IDENTITY)
	protected Long id;

    private String name;
    private Integer age;

    @CreatedDate
    private LocalDateTime createdAt;
}
```

  
  
  

## 해결

  1. `패키지Application.java`에 @EnableJpaAuditing 어노테이션 추가  
JpaAuditing 기능을 사용하기 위해서는 패키지Application.java파일에서 @EnableJpaAuditing 추가해줘야한다.

```java
@EnableJpaAuditing // 추가
@SpringBootApplication
public class 패키지Application {

	public static void main(String[] args) {
		System.out.println("@아아");
		SpringApplication.run(패키지Application.class, args);
	}

}
```

  2. Entity클래스에 @EntityListeners 추가  
이걸 빼먹으면 @CreatedDate등 Auditing기능이 작동하지않는다.

  * Sample.java

```java
@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Entity
@EntityListeners(AuditingEntityListener.class) // 추가
public class Sample {

	@Id
	@GeneratedValue(strategy =GenerationType.IDENTITY)
	protected Long id;

    private String name;
    private Integer age;

    @CreatedDate
    private LocalDateTime createdAt;
}
```

![정상적으로 날짜값이 isnert되었다.](/img/211130jpaAuditing2.PNG)

#[패스트캠퍼스(초격차Java/Spring)](/tags/%ED%8C%A8%EC%8A%A4%ED%8A%B8%EC%BA%A0%ED%8D%BC%EC%8A%A4-%EC%B4%88%EA%B2%A9%EC%B0%A8Java-Spring/)
