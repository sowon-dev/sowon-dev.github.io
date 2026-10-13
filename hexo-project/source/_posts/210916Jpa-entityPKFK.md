---
title: "[JPA/MariaDB]Entity에 복합키와 FK 제약조건 넣기"
date: 2021-09-15 21:58:53
tags: []
categories:
  - Backend
  - JPA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Entity에 복합키와 FK 제약조건 넣기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    JPA에서 복합키에서 식별관계를 매핑 즉, 복합키를 설정한 뒤 복합키 중 하나는 FK조건을 걸어보자.</p>
</div>

<!-- more -->

JPA에서 복합키에서 식별관계를 매핑 즉, 복합키를 설정한 뒤 복합키 중 하나는 FK조건을 걸어보자.

만들고 싶은 테이블은 아래와 같이 3개이다  
![](/img/210915commoncodegrup3.PNG)

## 1 reviewEntity 생성

먼저 중심이 되는 review테이블을 생성한다.  
날짜는 다른 곳에서 자주 사용하므로 TimeEntity를 따로 생성했다.

  * ReviewEntity.java

```java
@Table(name = "review")
@Entity
@Getter @Setter // XXX 자바빈즈 패턴
@NoArgsConstructor(access = AccessLevel.PROTECTED) @AllArgsConstructor // XXX 생성자 패컨
public class ReviewEntity extends TimeEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // 게시글 번호
	
    @Column(name = "email", nullable = false)
	private String email;
    
    @Column(name = "age", nullable = false)
    private int age;
    
    @Column(name = "gender", nullable = false)
    private Boolean gender;

    @Column(name = "shots", nullable = false)
    private int shots;
    
    @Column(name = "shot_date", nullable = false)
    @DateTimeFormat(pattern = "yyyy-MM-dd")
	private LocalDate shotDate;
    
    @Column(name = "vaccine_type_code", nullable = false)
	private String vaccineTypeCode;
	
	@Column(name = "content") // 접종후기
    private String content;
  }  
}
```

  * TimeEntity.java  
@MappedSuperclass는 테이블로 매핑하지 않고 자식 entity에게 매핑정보를 상속하는 에노테이션이다.  
@EntityListeners(AuditingEntityListener.class)은 JPA에게 해당 Entity는 auditing기능을 사용한다고 알리는 에노테이션이다.

```java
@Getter @Setter
@MappedSuperclass
@EntityListeners(AuditingEntityListener.class)
public class TimeEntity {
    @Column(name = "create_at", updatable = false)
    @CreatedDate
    private LocalDateTime createAt; //게시글 작성일
    
    @Column(name = "update_at")
    @LastModifiedBy
	private LocalDateTime updateAt; //게시글 수정일
}
```

  
  
  

## 2 SymptomEntity 생성

  * SymptomEntity.java

```java
@Table(name = "symptom")
@Entity
@Getter @Setter
@NoArgsConstructor(access = AccessLevel.PROTECTED) @AllArgsConstructor
@IdClass(SymptomId.class)
public class SymptomEntity {
	
    @Id // XXX 연관관계의 주인은 FK(외래키)가 명시된 Entity클래스로 설정
    @ManyToOne
    @JoinColumn(name="review_id")
	private ReviewEntity reviewId; //게시글 번호
	
    @Id 
    @Column(name = "symptom_code")
	private String symptomCode; //증상코드
}
```

  
  
  

### 1 외래키

reviewEntity와 SymptomEntity는 1대다의 관계이다.  
FK로 연관관계를 맺을때는 누가 주인이 될지를 고민해봐야한다.  
해당 고민을 도와줄 포스팅은 [siyoon210님 - JPA Entity간의 연관관계(방향) 설정하기](https://siyoon210.tistory.com/27)를 참조하면 된다.

나는 FK가 걸리는 테이블을 주인으로 삼았다. 그래야 연관관계의 주인이 되어 오류없이 수정 및 삭제가 가능하기 때문이다. 

  1. @ManyToOne: symptom클래스와 review클래스는 다 대 1의 관계에 해당하는 어노테이션을 달아주었다.
  2. @JoinColumn(name=”review_id”): FK로 매핑을 해주는 어노테이션이다. name속성의 구성은 `테이블명_컬럼명`이다. 즉, 여기선 review테이블의 id를 FK로 삼겠다는 의미이다.

  
  
  

### 2 복합키

  1. @IdClass(SymptomId.class): 복합키를 설정하는 어노테이션이다. 복합키를 매핑하기 위해 식별자 클래스(여기선 SymptomId.class)를 별도로 만들어야 한다.이는 아래에서 자세히 설명하겠다.
  2. 복합키를 설정하는 곳에 동일하게 @Id를 붙여준다. 나는 모든 필드가 복합키를 주고싶으므로 둘 다 @Id 를 달아줬다.

  
  
  

## 3 SymptomId 생성

복합키를 매핑하기 위해 식별자 클래스를 별도로 만들어야 한다.

  * 식별자 클래스의 필수 조건 5가지
    1. 필드명 일치
    2. Serializable 인터페이스구현
    3. equals, hashcode 구현
    4. 기본생성자 필요
    5. 식별자 클래스는 public이어야함

이제 식별자 클래스 코드를 보자.

  * SymptomId.java

```java
@NoArgsConstructor @AllArgsConstructor
@EqualsAndHashCode
public class SymptomId implements Serializable {
	private Long reviewId;
	private String symptomCode;
}
```

  
  
  

## 여담

이 구조를 파악하기위해 꼬박 하루가 걸렸다. 특히 FK키 에러가 발생해서 2시간이나 써버렸다. 해당 내용은 [[JPA: errno: 150 Foreign key constraint is incorrectly formed 해결방법]](https://sowon-dev.github.io/2021/09/15/210916JPA-FKincorrectlyformed/) 포스팅에 상세히 적어두었다.  
그냥 바로 DDL구문으로 생성했다면 훨씬 빨랐겠지만 JPA만을 이용하여 생성하려니 여간 답답한게 아니었다. 기본으로 알아야하는 지식들도 많아서 시간이 오래걸렸다.  
시간이 오래 걸린만큼 기초가 확실해진 느낌이다.  
가장 큰 힘이 된 것은 바로 구글링도 포스팅도 아닌 바로 책 [김영한지음 - 자바 ORM 표준 JPA 프로그래밍](http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9788960777330)이었다.  
처음에는 무슨소리인지 도저히 모르겠다😵‍💫였는데 이제는 확실히 알겠다.  
역시 하다보면 된다.  
이런게 학습의 기쁨일까?! 알고나니 JPA가 더 재밌다😁  
더이상 복합키와 FK키 두렵지 않다!
