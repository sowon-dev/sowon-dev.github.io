---
title: "[디자인패턴]생성패턴의 종류와 빌더패턴을 사용해야하는 이유"
date: 2021-09-06 22:37:50
tags:
  - "디자인패턴"
categories:
  - Backend
  - JPA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">생성패턴의 종류와 빌더패턴을 사용해야하는 이유의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    위 코드에서 빌더 패턴만 사용하기 위해 builder 메서드를 추가하면 아래와 같다.</p>
</div>

<!-- more -->

JPA 테스트코드를 공부하면서 패턴에 대해 궁금해졌다.  
DTO를 Entity([참고: Entity와 DTO차이](https://sowon-dev.github.io/2021/09/06/210907Jpa-entityVSDto/))로 변경할 때 주로 3가지 생성 패턴이 쓰인다.

각각의 장단점을 함께 살펴보고 JPA에 적합한 패턴이 무엇인지 찾아보자  
아래 엔티티 예시를 통해 패턴을 적용하는 방법이다.

## ReviewEntity.java

아래 코드 주석으로 적어놓았다.

```java
@Table(name = "review")
@Entity
@Getter @Setter // XXX 자바빈즈 패턴
@NoArgsConstructor(access = AccessLevel.PROTECTED) @AllArgsConstructor // XXX 생성자 패컨
@Builder(builderMethodName = "ReviewEntityBuilder")// XXX 빌드 패턴
public class ReviewEntity extends TimeEntity {
	@ApiModelProperty(value = "게시글 번호")
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
	
    @ApiModelProperty(value = "이메일", example = "example@example.com", required = true)
    @Column(name = "email", nullable = false)
	private String email;
    
    @ApiModelProperty(value = "내용", example = "심장이 떨렸습니다.", required = true)
    @Column(name = "content")
    private String content;
   
}
```

  1. 자바빌드패턴: @Getter @Setter
  2. 생성자패턴: @NoArgsConstructor, @AllArgsConstructor
  3. 빌더패턴: @Builder(builderMethodName = “ReviewEntityBuilder”)

위 코드에서 빌더 패턴만 사용하기 위해 builder 메서드를 추가하면 아래와 같다.

```java
@Table(name = "review")
@Entity
@Builder(builderMethodName = "ReviewEntityBuilder") // 빌드 패턴
public class ReviewEntity extends TimeEntity {
	@ApiModelProperty(value = "게시글 번호")
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
	
    @ApiModelProperty(value = "이메일", example = "example@example.com", required = true)
    @Column(name = "email", nullable = false)
	private String email;
    
    @ApiModelProperty(value = "내용", example = "심장이 떨렸습니다.", required = true)
    @Column(name = "content")
    private String content;
    
    public static ReviewEntityBuilder builder(ReviewDto dto) {
    	return ReviewEntityBuilder()
    			.id(dto.getId())
    			.email(dto.getEmail())
    			.age(dto.getAge())
    			.gender(dto.getGender())
    			.vaccineType(dto.getVaccineType())
    			.shotDate(dto.getShotDate())
    			.shots(dto.getShots())
    			.fever(dto.getFever())
    			.ache(dto.getAche())
    			.sneeze(dto.getSneeze())
    			.bleeding(dto.getBleeding())
    			.chills(dto.getChills())
    			.diarrhea(dto.getDiarrhea())
    			.content(dto.getContent());
    }
   
}
```

  
  

## 결론

객체를 생성하는 대부분의 경우에는 빌더 패턴을 적용하는 것이 좋다.  
생성자패턴보다 가독성을 높이고 휴먼에러를 줄일 수 있으며 인수 확장에 용이하기 때문이다.

가독성이 좋다고? 코드가 길어지기만 하던데? 하며 의아해할 수 있지만 예시를 보는 순간 한방에 이해할 수 있다.  
가독성예시를 보자.

```plain
// 생성자패턴
User user = new User("홍길동", 22, 1, 5000);
```

생성자를 이용하여 객체를 생성한 위의 코드에서는 숫자 22, 1, 3000이 어떤 인자를 나타내는 지 알기 어렵다.  
만약 빌더패턴을 사용한다면?

```plain
// 빌더패턴
User user = User.builder()
			.name("홍길동") 
			.age(22) 
			.yearOfExperience(1) 
			.salary(5000)
			.build();
```

이렇듯 어떤 인수인지 한 눈에 확인 가능하다.

  
빌더 패턴을 사용하면 좋은 경우 

  1. 인자들이 최소 4개이상으로 많은 경우
  2. 선택적 인자들이 많은 경우
  3. 앞으로 추가될 인자들이 많은 경우

#[디자인패턴](/tags/%EB%94%94%EC%9E%90%EC%9D%B8%ED%8C%A8%ED%84%B4/)
