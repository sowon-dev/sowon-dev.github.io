---
title: "[Java]익숙한 for each말고 Stream도 써봐야지"
date: 2023-01-10 15:56:45
tags:
  - "차이"
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'익숙한 for each말고 Stream도 써봐야지'에 참여하고 주요 발표 내용과 배운 점을 정리한 글이다.
    > 오늘의 결론이다. 스트림 사용이 for-loop보다 의미가 있으려면 Collection이 되는 스트림 소스의 크기가 충분히 크거나, 컴퓨팅 연산이 CPU-intensive할 정도로 비용이 매우 비싸야 한다. 병렬 스트림을 사용하려면, 스트림 소스인 Collection은 split하기 쉬운 자료 구조이어야 하며, 웬만해서는 연산이 stateful하지 않아야 한다. 성능차이는 개발자의 로컬환경에 따라 다를 수 있다.</p>
</div>

<!-- more -->

코드리뷰를 통해 익숙한 for each대신 Stream을 써보게되었다. 너무 재밌는 배움이라 기록하기로 마음먹었다.

정책상의 이유로 동일한 데이터를 서로 다른 User DB와 Wallet DB에 각각 저장하고 있다. 이 두 DB의 값들이 싱크가 맞는지 확인하는 메서드가 필요했다.

  
  
  

# 상황

  * User.java

```java
@Data
public class User{
  private int id;
  private String name;
  private int balance;
}
```

  * Wallet.java

```java
@Data
public class Wallet{
  private int walletId;
  private int userId;
  private int balance;
  private Boolean isAvailalbe;
}
```

  
  
  

# 내 코드

DiffVO를 담을 객체를 구현하고 User 디비를 호출해서 userDBValue에 셋팅하고 Wallet를 호출해서 walletDBValue에 셋팅한 뒤 if조건문으로 두 값을 비교해서 같으면 isTheSame = true로 바꿔주도록 구현했다.  
주의점은 User 디비 호출메서드 리턴데이터타입(User)과 Wallet 디비 호출메서드 리턴데이터타입(List)이 다르게 고정되어 있다는 점이다. 

  * DiffVO.java

```java
@Data
public class DiffVO{
  private int userDBValue;
  private int walletDBValue;
  private Boolean isTheSame = false; // 디폴트 false로
}
```

  * service

```java
public testService{

  private DiffVO checkTheSameValue(int id){
    DiffVO diffInfo = new DiffVO();
	
	// 1. A디비 값 가져오기
	User userInfo = dao.selectUserInfo(id);
	diffInfo.setUserDBValue(userInfo.getBalance());
	
	// 2. B디비 값 가져오기
	List<Wallet> walletInfo = balanceAllWallet(); // 기 구현된 서비스 balanceAllWallet()이용 필수
	for(Wallet w : walletInfo){
	  if(w.getUserId() == id){
  	    diffInfo.setWalletDBValue(w.getBalance());
	  }
	}
	
	// 3. 비교하기
	if(diffInfo.getUserDBValue() == diffInfo.getWalletDBValue()){
	  diffInfo.setIsTheSame(true);
	}
	
	return diffInfo;
  }

}
```

3단계로 비교했다. 팀장님이 내 코드를 보시곤 Stream을 사용하는 건 어떻겠냐고 말씀해주셨다.

  
  
  

# 팀장님 코드

내 코드는 for each문이고 팀장님은 stream을 사용하셨다.  
stream에 대한 자세한 설명은 [블로그 글 - 스트림 API 개념](https://sowon-dev.github.io/2020/08/26/200827javai2/)에 엄청 친절하게 적어놓았다.  
stream을 써보고싶었는데 익숙한 for 문만 쓰다 이렇게 코드리뷰하다가 쓰게되니 무척 재밌었다. 너무 재밌어!

  * service

```java
// (중략)

// 2. B디비 값 가져오기 -> 코드리뷰
List<Wallet> walletInfo = balanceAllWallet(); // 기 구현된 서비스 balanceAllWallet()이용 필수

Stream<Wallet> walletStream = walletInfo.stream().filter(d -> id.equals(d.getUserId()));
Wallet wallet = walletInfo.findFirst().orElse(null);
diffInfo.setWalletDBValue(wallet.getBalance());

// 3. 비교하기
if(diffInfo.getUserDBValue() == diffInfo.getWalletDBValue()){
diffInfo.setIsTheSame(true);
}

return diffInfo;
```

Stream을 쓰니 가독성도 좋아졌다.  
여담이지만 팀장님은 정말 천재같다. 

  
  
  

# 스트림과 for반복문 어느 것이 더 좋을까?

이렇게 스트림을 쓰고나니 for문과 비교해서 뭐가 더 좋은지가 궁금했다. 여러 구글링 끝에 흥미로운 미디엄 글 [Sigrid Jin님의 Java Stream API는 왜 for-loop보다 느릴까?](https://jypthemiracle.medium.com/java-stream-api%EB%8A%94-%EC%99%9C-for-loop%EB%B3%B4%EB%8B%A4-%EB%8A%90%EB%A6%B4%EA%B9%8C-50dec4b9974b)를 찾았다.

> 오늘의 결론이다. 스트림 사용이 for-loop보다 의미가 있으려면 Collection이 되는 스트림 소스의 크기가 충분히 크거나, 컴퓨팅 연산이 CPU-intensive할 정도로 비용이 매우 비싸야 한다. 병렬 스트림을 사용하려면, 스트림 소스인 Collection은 split하기 쉬운 자료 구조이어야 하며, 웬만해서는 연산이 stateful하지 않아야 한다. 성능차이는 개발자의 로컬환경에 따라 다를 수 있다.

#[차이](/tags/%EC%B0%A8%EC%9D%B4/)
