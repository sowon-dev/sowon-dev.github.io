---
title: "스프링부트에 ModelMapper 적용하기(ft.더블콜론::)"
date: 2022-07-07 19:36:01
tags: []
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">스프링부트에 ModelMapper 적용하기(ft.더블콜론::)의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    서버API 실습과정에서 DTO를 Entity로 변경하기 위해 Builder패턴을 사용했지만 나는 ModelMapper를 사용해보았다.</p>
</div>

<!-- more -->

책 [React.js, 스프링 부트, AWS로 배우는 웹 개발 101](http://www.acornpub.co.kr/book/reactjs-springboot#toc)을 가지고 5주 스터디를 진행중이다. 책 내용이 정말 좋다! 강력추천  
서버API 실습과정에서 DTO를 Entity로 변경하기 위해 [Builder패턴](https://sowon-dev.github.io/2021/09/06/210907DesignPattern-builder/)을 사용했지만 나는 ModelMapper를 사용해보았다.

  
  

## ModelMapper 추가하기

책의 코드에서는 builder를 사용했는데 나는 ModelMapper를 사용하고 싶어서 바꿨다.  
TodoDTO의 toEntity메서드는 없애주고 Gadle에 ModelMapper를 임포트했다.

  * build.gradle

```xml
dependencies {
	//중략
	implementation group: 'org.modelmapper', name: 'modelmapper', version: '2.4.2'
}
```

그 다음 config 패키지를 추가하고 ModelMapperConfig.java파일을 생성했다.

  * ModelMapperConfig.java

```java
import org.modelmapper.ModelMapper;
import org.modelmapper.convention.MatchingStrategies;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ModelMapperConfig {

	@Bean
	public ModelMapper modelMapper() {
		ModelMapper modelMapper = new ModelMapper();
		modelMapper.getConfiguration().setMatchingStrategy(MatchingStrategies.STRICT);
		return modelMapper;
	}
}
```

  
  

## 기존 코드

책의 코드는 [도서 공식 리포지토리](https://github.com/fsoftwareengineer/todo-application)에서 확인할 수 있다.

  * TodoDTO.java

```java
@NoArgsConstructor
@AllArgsConstructor
@Data
public class TodoDTO {
	private String id;
	private String title;
	private boolean done;
	
	public TodoDTO(final TodoEntity entity) {
		this.id = entity.getId();
		this.title = entity.getTitle();
		this.done = entity.isDone();
	}
	public static TodoEntity toEntity(final TodoDTO dto) {
		return TodoEntity.builder()
						.id(dto.getId())
						.title(dto.getTitle())
						.done(dto.isDone())
						.build();
	}
}
```

  * TodoController.java

```java
@RestController
@RequestMapping("todo")
public class TodoController {
	@Autowired
	private TodoService service;
	@PostMapping
	public ResponseEntity<?> createTodo(@RequestBody TodoDTO dto) {
		try {
			String temporaryUserId = "temporary-user"; // temporary user id.
			// (1) TodoEntity로 변환한다.
			TodoEntity entity = TodoDTO.toEntity(dto);
			// (2) id를 null로 초기화 한다. 생성 당시에는 id가 없어야 하기 때문이다.
			entity.setId(null);
			// (3) 임시 유저 아이디를 설정 해 준다. 이 부분은 4장 인증과 인가에서 수정 할 예정이다. 지금은 인증과 인가 기능이 없으므로 한 유저(temporary-user)만 로그인 없이 사용 가능한 어플리케이션인 셈이다
			entity.setUserId(temporaryUserId);
			// (4) 서비스를 이용해 Todo엔티티를 생성한다.
			List<TodoEntity> entities = service.create(entity);
			// (5) 자바 스트림을 이용해 리턴된 엔티티 리스트를 TodoDTO리스트로 변환한다.
			List<TodoDTO> dtos = entities.stream().map(TodoDTO::new).collect(Collectors.toList());
			// (6) 변환된 TodoDTO리스트를 이용해ResponseDTO를 초기화한다.
			ResponseDTO<TodoDTO> response = ResponseDTO.<TodoDTO>builder().data(dtos).build();
			// (7) ResponseDTO를 리턴한다.
			return ResponseEntity.ok().body(response);
		} catch (Exception e) {
			// (8) 혹시 예외가 나는 경우 dto대신 error에 메시지를 넣어 리턴한다.
			String error = e.getMessage();
			ResponseDTO<TodoDTO> response = ResponseDTO.<TodoDTO>builder().error(error).build();
			return ResponseEntity.badRequest().body(response);
		}
	}
}
```

컨트롤러의 create메서드를 확인하다가 생소한 더블콜론(::)을 만났다.  
더블콜론(::)이 뭐지?

  
  

## 더블콜론(::)이 뭐지? 물고기 대신 물고기 잡는 법

모르는 걸 만났을때 어떻게 검색해야할까?  
구글링해도 사용법만 나올뿐 더블콜론이 뭐하는 애다~라는 정의가 없었다.  
답답해하다가 팀장님께 살포시 질문을 들으니 물고기가 아닌 물고기 잡는 법을 알려주셨다.  
감사합니다 팀장님👍

> 언어를 사용하다 모르는 걸 만나면 `언어 + 언어버전 + Language Specification`의 조합으로 검색해보세요. 원하는 정보를 기본부터 얻을 수 있을 거예요  
> From 팀장님

Language Specification을 검색할 생각은 전혀 못하고 있었는데 팀장님이 알려주신 덕에 얼른 [java 1.8 language specification ::](https://docs.oracle.com/javase/specs/jls/se8/jls8.pdf)을 검색해서 찾아냈다! 내가 궁금했던 근본적인 정보가 다 들어있었다!  
이렇게 찾는 거구나! 또 하나 배웠다! 재밌어!😻

  
  

## 그래서 더블콜론이 뭔데?

더블콜론은 Method Reference Expressions(메소드 참조 표현식)의 하나로 실제로 호출을 수행하지 않고 특정 형식의 메서드를 참조하는 역할을 한다.

```plain
MethodReference:
	ExpressionName :: [TypeArguments] Identifier
	ReferenceType :: [TypeArguments] Identifier
	Primary :: [TypeArguments] Identifier
	super :: [TypeArguments] Identifier
	TypeName . super :: [TypeArguments] Identifier
	ClassType :: [TypeArguments]
```

간단한 예시([예시 더 공부하기](https://www.geeksforgeeks.org/double-colon-operator-in-java/))로 println을 보자.

```java
// Get the stream
Stream<String> stream = Stream.of("치킨", "이랑", "여행", "가", "고싶다");

// Print the stream
stream.forEach(s -> System.out.println(s));
```

위의 결과값은 아래와 같다.

```plain
//결과값
치킨
이랑
여행
가
고싶다
```

이를 더블콜론으로 간단하게 표현할수도 있다.

```java
stream.forEach( System.out::println);
```

결과값은? 당연히 위와 동일하다!

  
  

## 완성된 내 코드

짠! 서버도 잘 동작한다!  
공부해서 하나하나 알아가는 게 즐겁다!

  * TodoDTO.java

```java
@NoArgsConstructor
@AllArgsConstructor
@Data
public class TodoDTO {
	private String id;
	private String title;
	private boolean done;
}
```

  * TodoController.java

```java
@RestController
@RequestMapping("todo")
public class TodoController {
	@Autowired
	private  ModelMapper modelMapper;
	@Autowired
	private TodoService service;
	@PostMapping
	public ResponseEntity<?> createTodo(@RequestBody TodoDTO dto) {
		try {
			String temporaryUserId = "temporary-user"; // temporary user id.
			// (1) TodoEntity로 변환한다.
			TodoEntity entity = modelMapper.map(dto, TodoEntity.class);
			// (2) id를 null로 초기화 한다. 생성 당시에는 id가 없어야 하기 때문이다.
			entity.setId(null);
			// (3) 임시 유저 아이디를 설정 해 준다. 이 부분은 4장 인증과 인가에서 수정 할 예정이다. 지금은 인증과 인가 기능이 없으므로 한 유저(temporary-user)만 로그인 없이 사용 가능한 어플리케이션인 셈이다
			entity.setUserId(temporaryUserId);
			// (4) 서비스를 이용해 Todo엔티티를 생성한다.
			List<TodoEntity> entities = service.create(entity);
			// (5) 자바 스트림을 이용해 리턴된 엔티티 리스트를 TodoDTO리스트로 변환한다.
			List<TodoDTO> dtos = entities.stream().map(e -> modelMapper.map(e, TodoDTO.class)).collect(Collectors.toList());
			// (6) 변환된 TodoDTO리스트를 이용해ResponseDTO를 초기화한다.
			ResponseDTO<TodoDTO> response = ResponseDTO.<TodoDTO>builder().data(dtos).build();
			// (7) ResponseDTO를 리턴한다.
			return ResponseEntity.ok().body(response);
		} catch (Exception e) {
			// (8) 혹시 예외가 나는 경우 dto대신 error에 메시지를 넣어 리턴한다.
			String error = e.getMessage();
			ResponseDTO<TodoDTO> response = ResponseDTO.<TodoDTO>builder().error(error).build();
			return ResponseEntity.badRequest().body(response);
		}
	}
}
```

재밌다!
