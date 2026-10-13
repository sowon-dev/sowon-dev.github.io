---
title: "JPA VS JDBC"
date: 2021-03-22 15:00:00
tags:
  - "Journal"
  - "오늘또못알아듣고말았습니다"
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'JPA VS JDBC'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    왜냐하면 이전 기술의 불편한 점을 보완하여 새로운 기술인 나왔기때문이다. 그래서 불편한 점이 무엇이었고 그것을 어떻게 해결했는지가 두 기술의 차이점이 된다.</p>
</div>

<!-- more -->

**오늘 또 못알아듣고 말았습니다.**

회의시간만되면 신입개발자인 나는 참 바쁘다. 모르는 용어들이 쏟아지기때문에 볼펜을 놓쳐선 안된다. 회의 중 모르는 용어들은 다 적어놨다가 회의가 끝나고 혼자 구글링해보곤한다. 그럴때마다 아 그렇구나하고 뒤돌아선 까먹기 일수!  
그래서 아예 포스팅을 하기로 했다. 역시 기억보단 기록이지!  
TAGS는 `오늘또못알아듣고말았습니다`로 정해봤다.  
언젠가 내가 회의를 다 알아들으며 주도하는 그 날이 올때까지 열심히 공부해야겠다.

  
  
  

## 💬오늘의 물음표

신규프로젝트 회의 중에 팀장님이 말씀하셨다.

> JPA를 사용하면 비즈니스 로직이 복잡해져서 사용하지 않을거예요

이 말의 뜻을 이해하지 못했기에 회의끝나고 찾아볼 요량으로 회의 중에 후다닥 노트에 적었다. 

  
  
  

## 😁JPA(Java Persistent API)란 뭘까? 그전에 역사부터!

그 이름에 답이있다. 

  * Persistent(영속성)이란 데이터를 생성한 프로그램의 실행이 종료되더라도 사라지지않는 데이터의 특성이다.

기술은 발전된 순서로 공부하는 것이 이해하기 편하다.  
왜냐하면 이전 기술의 불편한 점을 보완하여 새로운 기술인 나왔기때문이다. 그래서 불편한 점이 무엇이었고 그것을 어떻게 해결했는지가 두 기술의 차이점이 된다.  
그럼 JPA전에는 뭐가 있었을까?  
바로 JDBC이다.

  
  
  

## 😮JDBC는 DB연결할때 쓰는 거아냐?

JDBC(Java Database Connectivity)도 그 이름에 답이 있다. 

  * DB에 접근(Connectivity)할 수 있도록 Java에서 제공하는 API이다.

![https://velog.io/@seculoper235/DB-%EC%9E%91%EC%97%85-JDBC](https://media.vlpt.us/images/seculoper235/post/d1758470-aa23-489f-965f-b205c245f30a/JDBC%20%EA%B5%AC%EC%A1%B0.PNG)

JDBC API가 있고 JDBC DriverManager가 DB제품에 따른 드라이버를 생성하여 JDBC API에 맞게 동작할 수 있게 처리해준다.  
따라서 우리는 JDBC API 변경없이 JDBC 드라이버만 바꿔주면 어떤 제품의 DB든 연결할 수 있다.

![https://velog.io/@seculoper235/DB-%EC%9E%91%EC%97%85-JDBC](https://media.vlpt.us/images/seculoper235/post/a2277b92-85a2-4c40-992d-762e5871a923/JDBC%20%EA%B3%BC%EC%A0%95.PNG)

위 사진처럼 쿼리를 실행하기 전과 후에 연결 생성, 명령문, ResultSet 닫기등과 같은 많은 코드를 작성해야한다.  
또 connection 관리, 예외처리등에 불편함이 있어 나온게 Spring JDBC이다.

  * 코드 예시

```java
//1. 드라이브로드 & 디비연결 : 로그인한 사용자의 정보를 가져오기
final String DRIVER = "com.mysql.jdbc.Driver";
final String DBURL = "jdbc:mysql://localhost:3306/jspdb";
final String DBID = "root";
final String DBPW = "1234";
Class.forName(DRIVER);
Connection con = DriverManager.getConnection(DBURL, DBID, DBPW);
System.out.println("드라이브로드와 디비연결성공");

//2. SQL & PSTMT & 실행
String sql = "select * from itwill_member where id=?";
PreparedStatement pstmt = con.prepareStatement(sql);
pstmt.setString(1, id);

//3. 실행-> rs에 결과저장 -> 데이터처리
ResultSet rs = pstmt.executeQuery();

//지역변수초기화-자동으로 안됨.

String name = "";
int age = 0;
String gender = "";
String email = "";
Timestamp reg_date = null; // Timestamp의 초기값은 null임

if(rs.next()){
	//id=rs.getString("id"); 세션으로 가져와서 필요없음
	name = rs.getString("name");
	age = rs.getInt("age");
	gender = rs.getString("gender");
	email = rs.getString("email");
	reg_date = rs.getTimestamp("reg_date");
}
```

  
  
  

## 😥Spring JDBC는 또 뭐야?

  * 핵심 : JdbcTemplate

Spring JDBC는 JDBC에서 DriveManager가 하는 일들을 JdbcTemplate에게 맡긴다. 따라서 개발자는 메서드에 쿼리를 직접 매핑한다.  
쿼리작성이 줄어들고(여전히 쿼리를 적지만…) 불편한 점들을 추상화시켜놓았다.  
SQL Query 직접 사용하여 데이터 조작하므로 JdbcTemplate은 SQL Mapper 중 하나이다

![https://skyblue300a.tistory.com/7](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcibMem%2FbtqDJf5WUpi%2FCoMEm3JcjkF5SamoI5Xk81%2Fimg.png)

![https://velog.io/@injoon2019/%EB%B6%80%EC%8A%A4%ED%8A%B8%EC%BD%94%EC%8A%A4-%EC%9B%B9-Spring-JDBC](https://media.vlpt.us/images/injoon2019/post/76bfd7e5-ddfe-466e-b5bb-a0616d66ab25/%EC%8A%A4%ED%94%84%EB%A7%81%ED%95%B4%EC%95%BC%ED%95%A0%EC%9D%BC.png)

  * 코드 예제  
코드 출처: [Spring JDBC](https://velog.io/@injoon2019/%EB%B6%80%EC%8A%A4%ED%8A%B8%EC%BD%94%EC%8A%A4-%EC%9B%B9-Spring-JDBC) 참고

```java
// 여러 건 select하기
List<Actor> actors = this.jdbcTemplate.query(
  "select first_name, last_name from t_actor",
  new RowMapper<Actor>() {
    public Actor mapRow(ResultSet rs, int rowNum) throws SQLException {

      Actor actor = new Actor();
      actor.setFirstName(rs.getString("first_name"));
      actor.setLastName(rs.getString("last_name"));
      return actor;
    }
  });
```

  
  

## 🤔SQL Mapper는 또 뭐야?

SQL Mapper는 SQL 문장으로 직접 데이터베이스 데이터를 다룬다.  
그럼 직접 데이터를 다루지 않는 것도 있을까?  
직접 다루지 않는 것을 ORM(Object-Relational Mapping)이라고 부른다.

  
  

## 🆚SQL Mapper vs ORM

SQL Mapper | ORM  
---|---  
SQL 문장으로 직접 데이터베이스 데이터를 조작함 | 객체를 통해 간접적으로 데이터베이스 데이터를 조작함  
SQL Query 직접 사용하여 데이터 조작 | SQL Query가 아닌 메서드로 데이터 조작  
SQL이 java코드와 분리되어 있기 때문에 유지보수가 편하지만 분리되어있기에 객체와 쿼리문 모두 관리해주어야 함 | 객체 중심으로 개발가능  
복잡한 쿼리, 다이나믹 쿼리 이점 | 프로시저등 복잡한 쿼리는 해결이 까다로움, 자동으로 생성되는 쿼리가 많기 때문에 성능저하의 가능성이 있어 최적화 필요  
비슷한 쿼리 남발, 자주쓰는 CRUD 메소드를 직접 다 작성필수 | CURD 메소드를 기본적으로 제공  
특정 DB에 종속적 | 설정파일에서 어떤 DB를 사용하고 있는지 알려주기만 하면 얼마든지 DB를 변경가능  
MyBatis, Spring JDBC | JPA, Hibernate  
  
  
  
  

## 🤔그럼 MyBatis는?

MyBatis도 SQL Mapper 중 하나이다.  
MyBatis는 Plain JDBC의 문제점을 Spring JDBC와 다르게 보았다.  
MyBatis는 자바코드에서 SQL을 쓰는 것을 문제라고 생각했고 SQL을 분리하고자했다. 따라서 SQL쿼리를 Java에서 XML로 옮겼서 적는다.

  * 코드예제  
EMemberVO.java 생성한 뒤 xml파일에서 MyBatis사용한 코드이다.

```java
<?xml version="1.0" encoding="UTF-8"?>

<!-- DTD지정  -->
<!DOCTYPE mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
  
<!-- SQL 구문 작성후 사용  -->
<mapper namespace="com.example.mappers.memberMapper">
	<select id="getTime" resultType="string">
		select now()
	</select>
</mapper>

<!-- DAO패키지(com.itwillbs.persistence)와 연결  -->
<context:component-scan base-package="com.example.persistence" />
```

  * [MyBatis(iBatis) 적용순서 및 사용방법 3가지, 예시, 코드 예제](https://sowon-dev.github.io/2020/10/13/201014spring/)

Mybatis는 쿼리가 수정되어 데이터 정보가 바뀌면 그에 사용되고있던 DTO와 함께 수정해주어야하는 불편함이 생긴다. 즉, 물리적으로 분리시켜놨지만 논리적으로는 서로 강한 의존관계가 있다.  
이 불편함을 해결하기 위해 나온 것이 ORM이다.  
ORM은 객체만 바꾸어주면 된다. 즉, 객체 중심으로 개발가능해진다.

  
  
  

## 😉SQL Mapper은 알았으니 이제 ORM이 뭔지 알려줘

ORM(Object-Relational-Mapping)의 이름 그대로 객체와 관계형데이터베이스의 데이터를 자동으로 매핑(연결)해준다. 

ORM의 구조는 아래와 같다.

![https://stackoverflow.com/questions/4477082/what-is-a-jpa-implementation/21719070](https://i.stack.imgur.com/4sVPQ.png)

ORM기준 표준인터페이스인 JPA(Java Persistence API)가 있고, 그 구현체로는 제일 유명한 Hibernate, EclipseLink, DataNucleus등이 있다.  
ORM의 핵심은 [엔티티매니저](https://ict-nroo.tistory.com/130)이다.

  
  
  

## 😝드디어 JPA가 나오네

직접적인 SQL 문을 사용하지 않고 자바 코드를 사용해서 DB에 접근, 조작할 수 있는 기술이다. JPA 역시 내부적으로 JDBC를 사용한다.

  * 자바 ORM 기술에 대한 API 표준 명세로, Java에서 제공하는 API이다.
  * 장점
    * SQL문을 직접 java application내에서 적을 경우가 적어짐 
      * 기본적인 CRUD 쿼리를 반복적으로 작성하지 않아도 됨
      * 수정사항이 발생하였을 때 수정해야 할 코드가 적음
    * SQL구조를 java application내에서 적용하지 않아도 됨. 어노테이션을 사용한다 EX) @Id, @ManyToOne …등 -> SQL 의존성 줄어듬. 객체지향적으로 데이터 관리 가능
  * 단점
    * 메서드 호출로 쿼리 실행은 직접 SQL을 호출하는 것보다 성능이 떨어질 수 있음
    * 복잡한 통계 분석 쿼리를 메서드 호출로 처리하는 것음 어려움 -> 로직이 복잡하거나 불필요한 쿼리가 발생할 수 있음
    * 러닝커브가 높음

JPA를 쓰는데 EntityManager를 쓴 적 없다면 그것은 Spring Data JPA를 사용했기 때문일 것이다.

  
  
  

## 😳Spring Data JPA는 또 뭐야?

Spring Data JPA는 JPA를 쓰기 편하게 만들어놓은 모듈이다.  
Spring Data JPA의 핵심은 Repository이다.  
이 JpaRepository를 뜯어보면 안에 EntityManager가 있다는 것을 알 수있다.

  * 코드예제  
코드 출처: [JPA - CRUD RestController 만들기](https://megazonedsg.github.io/tutorial-jpa/)

```java
@RestController()  
public class BookController {  
  
  @Autowired  
  private BookRepository bookRepository;  

  @PostMapping("/book")  
  public BookEntity createBook(@RequestBody BookEntity bookEntity) {  
	BookEntity created = bookRepository.save(bookEntity);  
	return created;  
  }  

  @GetMapping("/book")  
  public List<BookEntity> listAllBooks() {  
	List<BookEntity> list = new ArrayList<>();  
	Iterable<BookEntity> iterable = bookRepository.findAll();  
	for (BookEntity bookEntity : iterable) {  
	  list.add(bookEntity);  
	}  
	return list;  
  }
}
```

  
  
  

## 📝분류

JDBC | SQLMAPPER | ORM  
---|---|---  
JDBC API | MyBatis | JPA  
| Spring JDBC | Hibernate  
|  | Spring JDBC/JPA  
  
  
  
  

## 😎JPA를 쓰면 왜 비즈니스 로직이 복잡해질까?

[비즈니스 로직](https://m.blog.naver.com/anjdieheocp/20117559228)이란 업무에 필요한 데이터처리를 수행하는 것을 의미한다.  
예를 들어 DB에서 휴대전화 데이터를 가져와 웹에서 마스킹한 형태로 출력할 때 그 가공 과정을 비즈니스 로직이라고 한다.

JPA를 사용하면 제공되는 메소드로 복잡한 SQL를 수행하려할때 비즈니스 로직이 길어질 수 밖에 없다.

> JPA는 통계 쿼리처럼 복잡한 SQL을 수행하기 힘들기 때문에, 비즈니스에 따라 Mybatis를 사용할 지 Hibernate를 사용할 지 상황에 맞는 선택이 중요할 것입니다.  
> 처음에 살펴본 구글 트렌드를 볼 때 우리나라는 대부분 Mybatis를 사용하고 있는데, 그 이유는 우리나라 시장 대부분이 SI, 금융 시장이기 때문입니다.  
> 비즈니스가 매우 복잡하고, 안정성을 중요시 하는 서비스일 경우에는 JPA보다 SQL을 작성하는 것이 더 좋다는 의도일 것입니다.  
> 이미 SQL을 사용하여 개발된 애플리케이션이라면 JPA로 바꾸는 일도 쉽지 않기 때문에, 우리나라에서는 JPA가 많이 사용되지 못하는 것 같습니다.  
> 출처: <https://victorydntmd.tistory.com/195>

  
  
  

## 참고

  * <https://thefif19wlsvy.tistory.com/249>
  * <https://youtu.be/Ppqc3qN75EE>
  * <https://gmlwjd9405.github.io/2018/12/25/difference-jdbc-jpa-mybatis.html>
  * <https://youtu.be/mezbxKGu68Y>
  * <https://velog.io/@seculoper235/DB-%EC%9E%91%EC%97%85-JDBC>
  * <https://bk-investing.tistory.com/35>

#[Journal](/tags/Journal/)[오늘또못알아듣고말았습니다](/tags/%EC%98%A4%EB%8A%98%EB%98%90%EB%AA%BB%EC%95%8C%EC%95%84%EB%93%A3%EA%B3%A0%EB%A7%90%EC%95%98%EC%8A%B5%EB%8B%88%EB%8B%A4/)
