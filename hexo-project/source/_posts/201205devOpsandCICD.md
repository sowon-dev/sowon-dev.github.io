---
title: "DevOps와 CI/CD차이"
date: 2020-12-04 22:33:53
tags:
  - "TIL"
  - "Journal"
categories:
  - Reflections
  - Journal
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">'DevOps와 CI/CD차이'에서 다루는 각 기술의 핵심 개념과 동작 방식의 차이점을 분석한 내용이다.
    DevOps와 CI/CD차이의 차이를 고려하여 상황에 맞게 적용해야 한다.</p>
</div>

<!-- more -->

팀프로젝트를 웹호스팅한 후 소스코드 하나 바꿀때마다 jar파일 다시 업로드하고 서비스url에서 잘 작동되는지 다시 테스하는 일들을 매번 반복하고 있다.  
이를 효율적으로 할 수 있는 방법이 없는지 깃헙에 공개된 다른 팀프로젝트 개발문서들을 읽으며 공부하다가 DevOps와 CI/CD단어를 동시에 그리고 자주 마주쳤다.  
정확히 무엇인지 몰라서 이번 기회에 확실히 정리해보려고 한다.

  
  
  

## DevOps란?

![https://www.dotnettricks.com/learn/devops/what-is-devops-and-devops-advantages](https://dotnettrickscloud.blob.core.windows.net/img/devops/devops-whatisdevops.png)

  * DevOps = Development(개발+테스트) + Operations(운영)  
DevOps란 개발과 운영의 합성어로 운영환경에서부터 개발, 배포까지 진행되는 프로세스의 속도를 높이는 접근방식을 의미한다. 이러한 접근 방식을 적용하려면 개발 팀과 운영 팀간의 장벽을 허물고 자주 협력해야함에 따라 필요한 것을 정리해둔 모델이 있다. 바로 CALMS 모델이다.

  
  
  

## DevOps의 CALMS MODEL

이 중 눈에 띄는 것은 역시 CI/CD이다. 자동화는 DevOps의 핵심이다.

![](https://image.slidesharecdn.com/devopsguys-devops101forrecruiters-140117090454-phpapp02/95/devopsguys-devops-101-for-recruiters-19-638.jpg?cb=1390435671)

  
  
  

## CI/CD란?

  * CI (Continuous Integration) 다수의 개발자가 작성·수정한 소스코드를 지속적으로 통합·테스트하는 것을 의미한다.
  * CD (Continuous Delivery/Deployment)란 개발, 통합, 배포, 릴리즈, 테스트를 자동화하여 지속적으로 배포하는 것을 의미한다.

전통적인 방식으로는 코드수정하고 배포하는데 까지 많은 시간이 소요되었다. 특히 QA테스팅에서 많은 버그가 발생되었다.

![https://blog.oursky.com/2019/08/19/how-to-build-cicd-pipeline/](https://blog.oursky.com/wp-content/uploads/2019/08/image-1160x553.png)

CI/CD를 통해 지속적으로 통합·테스트·배포를 하고 이 흐름을 자동화하여 효율적으로 일을 처리할 수 있게 되었다.

![https://blog.oursky.com/2019/08/19/how-to-build-cicd-pipeline/](https://blog.oursky.com/wp-content/uploads/2019/08/image-1-1160x571.png)

  
  
  

## CI/CD 예시

  1. [[Delfood] CI/CD 서버 구축과 첫 배포](https://deveric.tistory.com/82?category=350852)  
CI/CD의 이해하기 쉽도록 잘 정리된 적용사례이다. 개인적으로 만든 프로젝트를 배포한 경험에 관한 글을 볼 수 있다. 

![https://deveric.tistory.com/106](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FAfO7u%2FbtqE1wewJny%2F2BBNTXLqwuEfgFMgPF6PHk%2Fimg.png)

  2. 라인개발자가 작성한 CI/CD적용 글 : [데이터 기반으로 지속적인 CI/CD 개선 환경 만들기](https://engineering.linecorp.com/ko/blog/build-a-continuous-cicd-environment-based-on-data/)

  
  
  

## DevOps단계별 사용하는 기술

DevOps에선 어떤 기술들이 사용될까? 아래 이미지에서 확인해볼 수 있다!

![http://nearcoding.com/what-is-devops/](http://nearcoding.com/wp-content/uploads/2018/11/devops.png)

## 요약

DevOps와 CI/CD차이  
DevOps는 개발과 운영을 통합하여 프로세스의 속도를 높이는 접근방식이다.  
CL/CD는 지속적으로 통합·테스트·배포를 하고 이 흐름을 자동화하는 것을 말한다.

  
  
  

## 참고

  * <https://blog.oursky.com/2019/08/19/how-to-build-cicd-pipeline/>
  * <https://www.dotnettricks.com/learn/devops/what-is-devops-and-devops-advantages>
  * <https://aws.amazon.com/ko/devops/what-is-devops/>
  * [DevOps 엔지니어는 어떤 사람일까요? by RedHat](https://www.redhat.com/ko/topics/devops/devops-engineer#:~:text=DevOps%20%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%8A%94%20%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4%2C%20%ED%88%B4,%EB%8A%94%20%EC%84%9C%EB%A1%9C%20%EB%8B%A4%EB%A5%BC%20%EC%88%98%20%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4.)
  * <https://www.redhat.com/ko/topics/devops>
  * <https://deveric.tistory.com/106>

#[TIL](/tags/TIL/)[Journal](/tags/Journal/)
