---
title: "[MyBatis]springboot aliases-package 오류 해결방법(UnsatisfiedDependencyException해결)"
date: 2021-05-06 15:00:00
tags:
  - "오류일지"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">그 결과 컨트롤러와 서비스등에서 UnsatisfiedDependencyException 에러가 발생했다.
    구글링을 해보니 대부분 application.properties파일에서 설정하길래 나도 따라해봤다.</p>
</div>

<!-- more -->

Mapper.xml에서 resultType을 전체 패키지명이 아닌 간단하게 파일명으로 쓰고 싶었다.  
참고로 스프링부트 프로젝트 구조는 아래와 같다.

  * src/main/java 하위에 controller, service, mapper, dto 폴더가 있고 그 하위에 java파일이 있다.
  * src/main/resources 하위에 mappers 폴더가 있고 그 하위에 xml파일이 있다.

## 시도

구글링을 해보니 대부분 `application.properties`파일에서 설정하길래 나도 따라해봤다.

  * `application.properties` 파일

```xml
# mybatis 매핑 type을 짧게 쓰기 위한 설정
mybatis.type-aliases-package=com.test.dto
mybatis.mapper-locations=mappers/*Mapper.xml
mybatis.configuration.map-underscore-to-camel-case=true
```

그 결과 컨트롤러와 서비스등에서 UnsatisfiedDependencyException 에러가 발생했다.

```plain
//결과 콘솔
org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'userController': Unsatisfied dependency expressed through field 'service';
...
```

  
  
  

## 해결

매퍼파일에서 패키지명 전체를 입력할 수 있지만, 약어로 쓰고싶은 마음에 끝까지 해결방법을 파고들었고 드디어 방법을 알아냈다.(😆해피)  
myBatis SqlSessionFactory를 설정하는 파일에서 `setTypeAliasesPackage()`로 진행하면 해결된다!

나의 경우 SpringBootApplication에서 바로 SqlSessionFactory를 연결해줬으므로 `setTypeAliasesPackage("com.test.dto")`을 아래와 같이 코드를 기입했다.

```java
@SpringBootApplication
public class TestApplication {

	public static void main(String[] args) {
		SpringApplication.run(TestApplication.class, args);
	}

	// MyBatis를 App전체에서 활용할 수 있도록 Application Class에서 초기화
    @Bean
    public SqlSessionFactory sqlSessionFactory(DataSource dataSource) throws Exception {
      SqlSessionFactoryBean sessionFactory = new SqlSessionFactoryBean();
      sessionFactory.setDataSource(dataSource);
      
      Resource[] res = new PathMatchingResourcePatternResolver().getResources("classpath:mappers/*Mapper.xml");
      sessionFactory.setMapperLocations(res);
      sessionFactory.setTypeAliasesPackage("com.test.dto"); //여기 추가
      
      return sessionFactory.getObject();
  }

}
```

테스트도 정상적으로 된다!  
드디어 해결🧐

#[오류일지](/tags/%EC%98%A4%EB%A5%98%EC%9D%BC%EC%A7%80/)
