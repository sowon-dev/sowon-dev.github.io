---
title: "[Java]List에서 중복값을 제외하는 방법2가지"
date: 2023-04-06 15:42:04
tags: []
categories:
  - Backend
  - JAVA
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">List에서 중복값을 제외하는 방법2가지의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    커스텀한 객체를 가지는 List에서 중복된 객체를 제거하고 싶었다. 차장님께 물어보니 2가지 방법을 알려주셨다.</p>
</div>

<!-- more -->

커스텀한 객체를 가지는 List에서 중복된 객체를 제거하고 싶었다. 차장님께 물어보니 2가지 방법을 알려주셨다.

# 기존코드

```java
// 커스텀한 User 객체
@Data
class User {
	String name;
	int age;
	
	@Override
	public String toString() {
        return name + ":" + age;
    }
 
}

// List 선언하기
List<User> userList = new ArrayList<>();
userList.add(new User("조지", 7));
userList.add(new User("휘슬", 8));
userList.add(new User("브라이언", 9));
userList.add(new User("브라이언", 9));

userList.forEach(System.out::println);

// 결과값
조지:7
휘슬:8
브라이언:9
브라이언:9
```

위 userList에서 중복을 제거하는 방법은 2가지이다.  
생성자를 활용하거나 stream().distinct()를 사용하는 방법이다.

  
  
  

# 1 생성자 활용

기본 타입이 아닌 참조 타입인 경우 클래스에서 hashCode() 메서드와 equals() 메서드를 재정의 먼저 해줘야한다.

```java
// hashCode(), equals() 메서드 추가
@Data
class User {
	String name;
	int age;
	
	@Override
	public String toString() {
        return name + ":" + age;
    }
	
	@Override
	public int hashCode(){
		return Objects.hash(name, age);
	}
	
	@Override
	public boolean equals(Object obj){
		if(this == obj) return true;
		if(obj == null) return false;
		if(getClass() != obj.getClass()){
			retyrn false;
		}
		User other = (User) obj;
		return name == other.name && Objects.equals(age, other.age);
	}	
}

// 생성자활용
List<User> distinctUserList = new ArrayList<User>(new HashSet<User>(userList));
distinctUserList.forEach(System.out::println);

// 결과값
조지:7
휘슬:8
브라이언:9
```

  
  
  

# 2 stream 활용

기본 타입이 아닌 참조 타입인 경우 클래스에서 hashCode() 메서드와 equals() 메서드를 재정의 먼저 해줘야한다.

```java
// hashCode(), equals() 메서드 추가
@Data
class User {
	String name;
	int age;
	
	@Override
	public String toString() {
        return name + ":" + age;
    }
	
	@Override
	public int hashCode(){
		return Objects.hash(name, age);
	}
	
	@Override
	public boolean equals(Object obj){
		if(this == obj) return true;
		if(obj == null) return false;
		if(getClass() != obj.getClass()){
			retyrn false;
		}
		User other = (User) obj;
		return name == other.name && Objects.equals(age, other.age);
	}	
}

// stream().distinct() 활용
List<User> distinctUserList = userList.stream()
                                      .distinct()
                                      .collect(Collectors.toList());

distinctUserList.forEach(System.out::println);

// 결과값
조지:7
휘슬:8
브라이언:9
```

  
  
  

## 출처

  * 차장님 지식
