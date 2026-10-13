---
title: "블록체인구축프로젝트를 끝내며 내가 배운 것"
date: 2023-06-06 16:34:42
tags:
  - "회고록"
categories:
  - Reflections
  - 회고록
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'블록체인구축프로젝트를 끝내며 내가 배운 것'에 참여하고 주요 발표 내용과 배운 점을 정리한 글이다.
    처음 해보는 대규모 파견 프로젝트! 파견도 처음이었고 블록체인, 앱, 웹, 운영등 다양한 분야의 개발자들과 협업하는 것도 처음이었다. 7개월간 모든 것이 신기하고 재미있었다.</p>
</div>

<!-- more -->

처음 해보는 대규모 파견 프로젝트! 파견도 처음이었고 블록체인, 앱, 웹, 운영등 다양한 분야의 개발자들과 협업하는 것도 처음이었다. 7개월간 모든 것이 신기하고 재미있었다.  
이번 프로젝트에서는 꼭 웹 백엔드를 맡고싶었는데 팀장님이 믿고 맡겨주셨다! 감사합니다 팀장님!

외부 API와 연동API를 개발하면서 다른 개발자가 써놓은 API명세서 읽고 이해하고 수정사항 요청하는 것도 재밌는 경험이었다.  
외부 API팀에서 RestAPI로 설계하셨다고했는데 몇몇 delete메서드에 body param을 넣으셔서 “Restful하지않은데 그냥 해주신 그대로 저도 연계API만들면 될까요?”하고 말씀드렸더니 고려해보시곤 path variable만 받는 걸로 수정해주셨다.뭔가 뿌듯~! 제대로 RestAPI를 이해하고 있구나 나자신 칭찬해!

대부분 나보다 연차가 많으신 시니어개발자분들과 협업하면서 많은 것을 배울 수 있었다. good example이 많았지만 bad example도 있다. 파견이 처음인 나에겐 여러모로 모든 해결과정들이 큰 도움이 되었다. 특히 업무를 대하는 태도와 갑사를 대하는 자세에 대해 많이 배웠다. 찐 어른들… 유연하게 대처하는 자세가 멋있었다.

  
  

# keep

현재 만족하고 있는 부분과 계속해서 이어갔으면 하는 부분

  1. `레거시 코드를 분석하고 리팩토링하는 능력`
     * 레거시 프로젝트를 고도화하면서 블록체인시스템을 추가하는 프로젝트였기에 레거시 코드를 정확히 읽고 추가 및 수정해서 기존 기능은 문제 없이 사용할 수 있어야하는 것이 이번 작업의 핵심이었다. 처음 해보는 금융관련 도메인이었는데 평소 은행, 증권사 앱을 많이 사용해서 그런지 친숙하게 느껴졌다. 다양한 분야에 관심을 가지고 있어야겠다는 생각이 들었다. 
  2. `다른 분야 개발자와 협업하는 능력`
     * 처음에는 용어 정리도 안되고 동일한 내용을 다른 명칭을 사용해서 소통에 혼선이 있었는데 시간을 내어 타 팀 개발자분들과 용어를 맞추고 공통코드 및 공통 용어 적립한 뒤에는 의사소통이 원활하게 이루어졌다.
  3. `프로젝트 전체를 보는 눈`
     * 요구사항 기능을 내 서비스에서만 생각하지않고 타팀 프로세스까지 고려할 수 있게 되었다. 예를 들어, 구매하기기능을 구현할때 내가 담당한 서비스 로직에서만 국한된게 아니라 타팀 서비스에선 해당 기능이 어떻게 구현되는 지까지 고려하여 내 서비스를 설계하다보니 처음에는 너무 헷갈렸는데 나중에는 자연스럽게 프로젝트 전체 흐름을 이해할 수 있게 되었고 아직 정의되지 않은 부분은 확장성있게 짤 수 있게 되었다.
  4. `확장성있는 공통함수 설계 능력`
     * 외부연계API를 만들면서 중복코드를 최대한 없애면서도 언제 생길지 모르는 갑사의 추가 요구사항에 대비해 확장성있게 공통함수로 정의하는데 각고의 노력을 기울였다. 노력이 빛을 봤는지 대부분의 추가, 수정사항에서도 공통함수를 건들이는 일 없이 잘 처리할 수 있었다.팀장님이 잠깐 해당 코드 리뷰도 해주셨는데 은근 튼튼하게 잘 짰다고 칭찬해주셨다. 전부 팀장님한테 배운건데도 칭찬해주셔서 뿌듯했다. 팀장님의 칭찬은 날 춤추게 해~💃
  5. `잘잘못따지기 전에 버그부터 해결하는 마인드`
     * 이번 프로젝트에서는 개발시간이 턱없이 부족했기에 시간단축이 생명이었는데 많은 개발자들이 한 리포에 커밋을 하다보니 잘못된 커밋이나 머지, 엘리야스실수등으로 인해 런타임오류가 발생해 원인을 찾느라 시간을 많이 쓰게 되었다. 이때 잘잘못을 따지고 싶은 마음을 굴뚝같았지만 잘잘못을 따지기보단 일단 빨리 해결부터 하자 마인드가 확고해졌다. 누가 잘못 커밋했는 지 파헤치기전에 일단 버그부터 잡았다. 이는 차장님의 영향이 컸다. 누군지 잡아낸다고 하시면서도 “지금 알아서 뭐하겠어~ 귀찮다~” 하며 버그부터 잡는 모습이 크게 와닿았기때문이다. 앞으로도 해결부터하는 개발자가 되어야지!
  6. `json 다루는 능력`
     * objectMapper와 Gson 통해서 자유자재로 json과 객체를 만들 수 있게 되었다. 
  7. `double과 float 변환시 부동소수점 오류`
     * 해당 문제가 있는지도 몰랐는데 이번에 금융프로젝트를 하면서 돈에 민감하다보니 자연스레 주의깊게 구분해서 쓰게 되었다. 
     * 관련 포스팅: [float, double 소수점 오류(부동소수점) 해결하기](https://sowon-dev.github.io/2023/05/21/230522bigdecimal/)
  8. `RestTemplate을 통한 외부API통신 자신감`
     * 외부API 통신을 위해 RestTemplate 자유자재로 사용하였고 제네릭 클래스 오류를 해결했다. 
     * 관련 포스팅1: [제네릭과 ParameterizedTypeReference](https://sowon-dev.github.io/2022/12/09/221210spring-resttemplate/)
     * 관련 포스팅2: [ResponseEntity 코드리뷰](https://sowon-dev.github.io/2022/12/20/221221java-responseentity-refactoring/)

  
  
  

# Problem

개선이 필요하다고 생각되는 부분

  1. `다중 팝업 jsp화면 구현시 속도 개선 필요`
     * 백엔드 작업하다가 화면에 도움이 필요하여 jsp화면 몇개를 만들었다. 다중 팝업에 데이터를 제이쿼리로만 이동 시켜야해서 굉장히 재미없었다. 흥미를 못 느끼다보니 속도가 늦어졌고 결국 맡았던 3개 화면 중 1개를 다 끝내지 못해서 결국 차장님이 도와주셨고 나는 기능테스트에 투입되어 버그를 잡았다. 아무리 흥미가 없더라도 맡은 업무는 빠르게 쳐내야하는데 이 부분이 개선되어야한다.
  2. `파일서비스를 욕심내지 못한 것`
     * 기능테스트에 치여서 파일서비스 개발에 욕심을 내지 못했다. 잘 만들려면 한도끝도없이 잘 만들어 낼 수 있는 부분인다. File 클래스를 다뤄본 적이 거의 없어서 한 번은 꼭 필요한 부분이다.
  3. `객체는 어디까지 확장되어야할까?`
     * VO객체를 어디까지 확장해야하는 지가 제일 어려웠다. 기획이 수시로 변경되고 DB테이블에 컬럼들이 추가,수정,삭제되면서 서비스별로 나눠놨던 VO의 경계가 흐려졌다. 언제나 그렇듯 완벽하게 설계된 채 시작하는 프로젝트는 없으니까 유연하게 한 개의 VO에 다 담아야하는 지, 중간에 새로운 기준으로 다시 VO를 나눠야하는 지 아니면 속편하게 HashMap을 쓸 지 고민스러웠다. 한 번 바뀌면 화면 파라미터명부터 controller, xml까지 다 변경해야하니 여간 번거로운게 아니였다. 팀장님께 질문드리니 프로젝트에 맞게 설계하면 된다고 하셨는데 아직 많은 프로젝트를 만나보지 않아서 그런지 감이 잡히질 않는다. 
  4. `CUD 쿼리 전 set으로 코드 가독성 하락`
     * CUD 쿼리 전 dto를 set하는 코드가 너무 길어져서 가독성이 떨어졌다. set하면서도 항상 바꾸고 싶었는데 어떻게 해야할 지 알 수가 없었다.

  
  
  

# Try

Problem의 해결책이 될 수 있는 부분

  1. `다중팝업 jsp화면을 다루는 연습할 것`: 테이블이 각 화면마다 있는 다중 팝업데이터 다루는 연습이 필요하다.
  2. `파일서비스 따로 만들어볼 것`: 깃헙 리포생성해서 File객체로 오픈소스도움없이 파일 업로드/다운로드 서비스를 따로 만들어봐야겠다. 멀티파트써서 이미지랑 텍스트 다 되게끔 만들어봐야겠다.
  3. `설계에 관한 글과 책을 찾아 읽어볼 것`
  4. `BeanUtils를 적극 활용할 것`: 차장님 코드를 살펴보는데 [Class BeanUtils](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/beans/BeanUtils.html)을 이용하여 간편하게 set을 한 줄로 끝낸 코드를 보고 감탄했다. 사막에서 오아시스를 발견한 기분이었다. 내가 찾던 게 바로 이거! 역시 간절히 원하니까 보였다.
     1. 관련 포스팅: [BeanUtils](https://sowon-dev.github.io/2023/06/20/230621beanutils/)

  
  
  

# 관련 포스팅

  * [제네릭과 ParameterizedTypeReference](https://sowon-dev.github.io/2022/12/09/221210spring-resttemplate/)
  * [ResponseEntity 코드리뷰](https://sowon-dev.github.io/2022/12/20/221221java-responseentity-refactoring/)
  * [List에서 중복값을 제외하는 방법2가지](https://sowon-dev.github.io/2023/04/06/230407removeduplicatevalueinlist/)
  * [String.valueOf() vs toString() 차이 알고쓰자](https://sowon-dev.github.io/2023/02/06/230207stringvalueof-vs-tostring/)
  * [ClassCastException발생 Java.lang.Integer cannot be case to Java.lang.String 해결방법(ft. ChatGPT)](https://sowon-dev.github.io/2023/02/13/230214integervalueof/)
  * [MVC패턴과 MVP패턴 차이](https://sowon-dev.github.io/2023/02/16/230217MVPpattern/)
  * [MalformedJsonException 에러해결](https://sowon-dev.github.io/2023/03/02/230303malformedjsonexception/)
  * [no qualifying bean of type available: expected at least 1 bean which qualifies as autowire candidate 오류해결](https://sowon-dev.github.io/2023/03/12/230313autowirederror/)
  * [Kafka(카프카)가 뭐길래(개념, 정의)](https://sowon-dev.github.io/2023/04/09/230410kafka/)
  * [deeplink가 뭐길래(개념, 정의)](https://sowon-dev.github.io/2023/04/10/230411deeplink/)
  * [팝업(모달)창에서 datepicker 적용 안되는 오류 해결법](https://sowon-dev.github.io/2023/04/25/230426datepicker-error-in-modal/)
  * [Double/Float 변환시 ClassCastException오류 NaN 해결](https://sowon-dev.github.io/2023/05/09/230509double-NaN/)
  * [float, double 소수점 오류(부동소수점) 해결하기](https://sowon-dev.github.io/2023/05/21/230522bigdecimal/)

#[회고록](/tags/%ED%9A%8C%EA%B3%A0%EB%A1%9D/)
