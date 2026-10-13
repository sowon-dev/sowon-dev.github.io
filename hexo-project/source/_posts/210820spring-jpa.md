---
title: "[JPA] 기초 Query Method(쿼리메서드)와 Entity(엔티티)"
date: 2021-08-19 16:48:21
tags:
  - "패스트캠퍼스(초격차Java/Spring)"
categories:
  - Backend
  - JPA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">기초 Query Method(쿼리메서드)와 Entity(엔티티)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    JPA를 왜 사용할까? SQL 중심적인 개발에서 객체중심으로 개발이 가능하고 CRUD와 같은 간단한 메서드 생산성이 올라간다.</p>
</div>

<!-- more -->

JPA(Java Persistnece API)란  
JPA를 왜 사용할까? SQL 중심적인 개발에서 객체중심으로 개발이 가능하고 CRUD와 같은 간단한 메서드 생산성이 올라간다.  
[JPA VS JDBC](https://sowon-dev.github.io/2021/03/22/210323jpaVSjdbc/) 포스팅에 DB CONNECT 프로그램에 대해 자세히 정리해놓았다.

## Query Method 예시

Query Method는 예시를 통해 공부하는 것이 좋다.  
별 어려움없이 Method이름 그대로 결과값이 출력된다.

### User.java

Entity의 경우 @Data보다 @Getter와 @Setter를 주로 사용한다. 하지만 @Getter만 쓰는 것이 좋다. @Setter를 사용하면 어디서든 값을 변경시킬 수 있기 때문에, Entity의 불변성을 지키기 위해 필요한 필드 변경은 함수를 따로 생성하여 관리해야한다. 이는 [DTO, Entity의 빌더패턴 적용기](https://devfunny.tistory.com/409)에서 참고했다.

```java
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
@Getter @Setter
@Entity
@Builder
public class User {
	@Id
	@GeneratedValue
	private Long id;
	@NonNull
	private String name;
	@NonNull
	private String email;
	private LocalDateTime createdAt;
	private LocalDateTime updattedAt;	
}
```

  
  
  

### UserRepository.java

```java
public interface UserRepository extends JpaRepository<User, Long>{
	// 1 jpa는 optional, set 등 굉장히 많은 return 타입을 제공하고 있다.
	User findByName(String name);
	//Optional<User> findByName(String name); 
	//Set<User> findByName(String name);

	// 2 nameing규칙 extends로 User를 받았다면 필드 전체를 사용가능
	User findByEmail(String email);
	User getByEmail(String email);
	User readByEmail(String email);
	User queryByEmail(String email);
	User searchByEmail(String email);
	User streamByEmail(String email);
	User findUserByEmail(String email);
	User findSomethingByEmail(String email);

	// 3 
	List<User> findFirst2ByName(String name);
	List<User> findTop2ByName(String name);
	List<User> findLast1ByName(String name);

	// 4 조건절 and, or 
	List<User> findByEmailAndName(String email, String name);
	List<User> findByEmailOrName(String email, String name);

	// 5 시간 비교
	List<User> findByCreatedAtAfter(LocalDateTime yesterday);
	List<User> findByIdAfter(Long id);
	List<User> findByCreatedAtGreaterThan(LocalDateTime yesterday);
	List<User> findByCreatedAtGreaterThanEqual(LocalDateTime yesterday);
	List<User> findByCreatedAtBetween(LocalDateTime yesterday, LocalDateTime tomorrow);
	List<User> findByIdBetween(Long id1, Long id2);
	List<User> findByIdGreaterThanEqualAndIdLessThanEqual(Long id1, Long id2);

	// 6
	List<User> findByIdIsNotNull();
	// 잘 사용하지 않음 주의) 문자열의 empty가 아닌 collection의 empty를 체크한다
	//    List<User> findByAddressIsNotEmpty();   

	// 7 in, not in 실무에서 자주 사용함
	List<User> findByNameIn(List<String> names);

	// 8 LIKE
	List<User> findByNameStartingWith(String name);
	List<User> findByNameEndingWith(String name);
	List<User> findByNameContains(String name);
	List<User> findByNameLike(String name);

	List<User> findTop1ByName(String name);
	List<User> findTopByNameOrderByIdDesc(String name);
	List<User> findFirstByNameOrderByIdDescEmailAsc(String name);
	List<User> findFirstByName(String name, Sort sort);

}
```

  
  
  

### UserRepositoryTest.java

src/test/java 경로에 UserRepositoryTest.java를 생성한다.  
jUnit을 통해서 Test를 해보자.

```java
@SpringBootTest
public class UserRepositoryTest {
	@Autowired
	UserRepository userRepository;

	@Test
	void crud() {
		// 1. save
		userRepository.save(new User(null, "가나다", "ganada@fast.com", LocalDateTime.now(), LocalDateTime.now()));
		userRepository.save(new User());
		userRepository.save(new User(null, "마바사", "mabasa@fast.com", LocalDateTime.now(), LocalDateTime.now()));
		userRepository.save(new User(null, "ma", "ma@slow.com", LocalDateTime.now(), LocalDateTime.now()));
		userRepository.save(new User(null, "라", "ra@slow.com", LocalDateTime.now(), LocalDateTime.now()));

		userRepository.findAll().forEach(System.out::println);

		// 2. matcher
		ExampleMatcher matcher1 = ExampleMatcher.matching().withIgnorePaths("name").withMatcher("email", endsWith());
		Example<User> example1 = Example.of(new User("ma", "ma@fast.com"), matcher1);

		userRepository.findAll(example1).forEach(System.out::println);
	}

	@Test
	void select() {
		userRepository.save(new User(null, "가나다", "ganada@fast.com", LocalDateTime.now(), LocalDateTime.now()));
		userRepository.save(new User());
		userRepository.save(new User(null, "마바사", "mabasa@fast.com", LocalDateTime.now(), LocalDateTime.now()));
		userRepository.save(new User(null, "ma", "ma@slow.com", LocalDateTime.now(), LocalDateTime.now()));
		userRepository.save(new User(null, "ma", "ma@slow.com", LocalDateTime.now(), LocalDateTime.now()));
		userRepository.save(new User(null, "라", "ra@slow.com", LocalDateTime.now(), LocalDateTime.now()));
		
		userRepository.findAll().forEach(System.out::println);
		// 1
		System.out.println(userRepository.findByName("마바사"));
		
		// 2
		System.out.println("@ findByEmail : " + userRepository.findByEmail("ra@slow.com"));
		System.out.println("@ getByEmail : " + userRepository.getByEmail("ra@slow.com"));
		System.out.println("@ readByEmail : " + userRepository.readByEmail("ra@slow.com"));
		System.out.println("@ queryByEmail : " + userRepository.queryByEmail("ra@slow.com"));
		System.out.println("@ searchByEmail : " + userRepository.searchByEmail("ra@slow.com"));
		System.out.println("@ streamByEmail : " + userRepository.streamByEmail("ra@slow.com"));
		System.out.println("@ findUserByEmail : " + userRepository.findUserByEmail("ra@slow.com"));
		System.out.println("@ findSomethingByEmail : " + userRepository.findSomethingByEmail("ra@slow.com"));

		// 3
		System.out.println("findTop2ByName : " + userRepository.findTop2ByName("ma"));
		System.out.println("findFirst2ByName : " + userRepository.findFirst2ByName("ma"));
		System.out.println("findLast1ByName : " + userRepository.findLast1ByName("ma"));
		
		// 4 조건절 and, or 
		System.out.println("findByEmailAndName : " + userRepository.findByEmailAndName("ma@slow.com", "ma"));
		System.out.println("findByEmailOrName : " + userRepository.findByEmailOrName("ma@slow.com", "마바사"));

		// 5 시간 비교
		System.out.println("findByCreatedAtAfter : " + userRepository.findByCreatedAtAfter(LocalDateTime.now().minusDays(1L)));
		System.out.println("findByIdAfter : " + userRepository.findByIdAfter(4L));
		System.out.println("findByCreatedAtGreaterThan : " + userRepository.findByCreatedAtGreaterThan(LocalDateTime.now().minusDays(1L)));
		System.out.println("findByCreatedAtGreaterThanEqual : " + userRepository.findByCreatedAtGreaterThanEqual(LocalDateTime.now().minusDays(1L)));
		System.out.println("findByCreatedAtBetween : " + userRepository.findByCreatedAtBetween(LocalDateTime.now().minusDays(1L), LocalDateTime.now().plusDays(1L)));
		System.out.println("findByIdBetween : " + userRepository.findByIdBetween(1L, 3L));
		System.out.println("findByIdGreaterThanEqualAndIdLessThanEqual : " + userRepository.findByIdGreaterThanEqualAndIdLessThanEqual(1L, 3L));

		// 6
		System.out.println("findByIdIsNotNull : " + userRepository.findByIdIsNotNull());
	    System.out.println("findByIdIsNotEmpty : " + userRepository.findByAddressIsNotEmpty());

		// 7 in, not in 실무에서 자주 사용함
		System.out.println("findByNameIn : " + userRepository.findByNameIn(Lists.newArrayList("ma", "가나다")));

		// 8 LIKE
		System.out.println("findByNameStartingWith: " + userRepository.findByNameStartingWith("m"));
		System.out.println("findByNameEndingWith : " + userRepository.findByNameEndingWith("다"));
		System.out.println("findByNameContains : " + userRepository.findByNameContains("나"));
		System.out.println("findByNameLike : " + userRepository.findByNameLike("%" + "나" + "%"));
	}
}
```

  
  
  

## JpaRepository

  1. 메소드 Retrurn 타입  
JPA는 optional, set 등 굉장히 많은 return 타입을 제공하고 있다.

```java
// 리턴타입 3가지
User findByName(String name); 
Optional<User> findByName(String name);
Set<User> findByName(String name);

// 결과: 세 가지 모두 동일한 결과
[User(id=4, name=ma, email=ma@slow.com, createdAt=2021-08-20T21:14:05.439217, updattedAt=2021-08-20T21:14:05.439217), User(id=5, name=ma, email=ma@fast.com, createdAt=2021-08-20T21:14:05.439217, updattedAt=2021-08-20T21:14:05.439217)]
```

  2. 메서드 nameing 규칙

![](/img/210820jpa1.PNG)

위 이미지처럼 다양한 네이밍 규칙이 있고 실무에서 가장 자주 사용하는 규칙은 select코드인 `find…By, read…By, get…By, query…By, search…By, stream…By`이다.  
왜이렇게 여러이름일까?

```java
User findByEmail(String email);
User getByEmail(String email);
User readByEmail(String email);
User queryByEmail(String email);
User searchByEmail(String email);
User streamByEmail(String email);
User findUserByEmail(String email);
User findSomethingByEmail(String email); -> 이상없이 동작함!

// 결과값
[User(id=4, name=ma, email=ma@slow.com, createdAt=2021-08-20T21:14:05.439217, updattedAt=2021-08-20T21:14:05.439217)]
```

위 코드 전두 동일한 결과값이 나온다. 따라서 코드가독성이 가장 잘 어울리는 이름을 선택해서 사용하면 된다.

  3. Query Keywords

![](/img/210820jpa2.PNG)

  * 날짜와 시간을 비교하는 키워드 

키워드 | 설명 | 비교  
---|---|---  
AFTER, BEFORE | 날짜와 시간에만 사용하는 조건, EQUALS(=)포함하지 않음 | 초과 또는 미만  
GREATER_THAN | 모든 숫자값, 날짜값 사용가능한 AFTER보다 범용적인 조건 | 초과  
GREATER_THAN_EQUALS | GREATER_THAN에서 EQUALS(=)이 포함된 조건 | 이상  
BETWEEN | 모든 숫자값, 날짜값 사용가능. EQUALS(=)이 포함된 조건 | 이상과 이하  
  
  * 빈값에 대한 키워드

키워드 | 설명 | 쿼리  
---|---|---  
IS_NOT_NULL | NULL이 아닌 것을 출력하는 조건 | WHERE A IS NOT NULL  
IS_NOT_EMPTY | 주의) 문자열의 empty가 아닌 collection의 empty를 체크함. 잘 사용하지 않는 쿼리 | WHERE exists (select id from 테이블 where id = id and address = address)  
  
  
  
  

## Entity

어노테이션 | 설명  
---|---  
@Id | Entity는 PK가 필수적으로 필요하다. 이를 나타내주는 어노테이션  
@GeneratedValue | @Id값을 null로 insert하면 AUTO_INCREMENT함  
@Table | 기본값으로 Entity이름과 동일한 table name을 사용 -> name속성: 원하는 테이블로 매핑가능  
@Colum | name속성: 원하는 컬럼으로 매핑가능, nullable속성: NULL을 허용할 지 말지 결정, updateable: update구문실행시 해당 필드를 함께 수정할지 결정  
@Transient | 영속성 대상에서 해당 컬럼을 제외한다. 해당 객체와 생명주기를 같이한다. DB에 반영하지않고 필드를 쓰고 싶을때 사용  
@Enumerated | 열거형을 사용할 때는 EnumType.STRING속성을 주로 사용  
@PrePersist | manager persist 의해 처음 호출될 때 실행, 현재시간을 자동으로 DB에 insert할때 주로 사용  
@PreUpdate | SQL UPDATE 전에 실행, 현재시간을 자동으로 DB에 update할때 주로 사용  
  
실무에서 자주 사용하는 어노테이션 3가지

  1. @Id @GeneratedValue(strategy=GenerationType.AUTO): PK 자동증감
  2. @Colum(nullable=false): 값에 NULL허용하지 않음
  3. @Enumerated(EnumType.STRING): 꼭 STRING속성을 설정해주어야 Enum에 값이 추가되었을때 순서변경이 없음 -> 실무에서도 실수를 많이 하는 부분!

  
  
  

## 참고

  1. <https://docs.spring.io/spring-data/jpa/docs/2.5.4/reference/html/#populator.namespace-reference>

참고로 잘 정리해 논 블로그 글을 찾았다.  
2\. [leyuri - Spring-boot JPA 어노테이션](https://velog.io/@leyuri/Spring-boot-JPA-%EC%96%B4%EB%85%B8%ED%85%8C%EC%9D%B4%EC%85%98-Entity-Table-Column-Id-Lombok)  
3\. [탁구치는 개발자 - @Enumerated](https://lng1982.tistory.com/280)

#[패스트캠퍼스(초격차Java/Spring)](/tags/%ED%8C%A8%EC%8A%A4%ED%8A%B8%EC%BA%A0%ED%8D%BC%EC%8A%A4-%EC%B4%88%EA%B2%A9%EC%B0%A8Java-Spring/)
