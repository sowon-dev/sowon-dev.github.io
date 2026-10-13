---
title: "JSON데이터를 어떻게 DB에 넣을까?"
date: 2021-04-01 23:53:08
tags:
  - "Journal"
  - "오늘또못알아듣고말았습니다"
  - "JSON"
  - "xAPI"
categories:
  - Database
  - General
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">JSON데이터를 어떻게 DB에 넣을까?의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    xAPI를 사용하기위해서는 JSON데이터를 LRS에 수집해야한다. JSON데이터를 어떻게 저장할 수 있을까?을 적용할 수 있다.</p>
</div>

<!-- more -->

**오늘 또 못알아듣고 말았습니다.**

xAPI를 사용하기위해서는 JSON데이터를 LRS에 수집해야한다. JSON데이터를 어떻게 저장할 수 있을까?  
내가 알고있는 건 `데이터 저장 = DB`이기때문에 DB에 테이블을 생성하여 어떻게 JSON데이터의 KEY, VALUE, DEPTH를 잘 넣을 수 있는 지 고민했다.  
xAPI에서 필수적인 데이터들로만 이루어져있는 JSON데이터 예시가 있다.  
이 데이터를 어떻게 수집해야 추후에 편하게 DB분석하고 쿼리로 꺼내쓸 수 있을까?

```xml
{
    "id": "12345678-1234-5678-1234-567812345678",
    "actor":{
        "mbox":"mailto:xapi@adlnet.gov"
    },
    "verb":{
        "id":"http://adlnet.gov/expapi/verbs/created",
        "display":{
            "en-US":"created"
        }
    },
    "object":{
        "id":"http://example.adlnet.gov/xapi/example/activity"
    }
}
```

일단은 DEPTH랑 상관없이 모든 키를 컬럼으로 만들면 어떨까 생각해보았다.

```plain
컬럼
id, actor, mbox, verb, id, display, en-US, object, id
```

그렇게되면 key가 추가되는 경우에는 어떻게 할까하는 생각이 들었다.  
xAPI는 구성요소의 유연성이 있기때문에 필요에 따라 Property가 추가 될 수 있어야했다.

  
  
  

## 💬오늘의 대화

오늘 팀장님과의 대화를 요약했다. 이 대화에서 모르는 부분들을 속속들이 알아보자!

팀장님 | 나  
---|---  
| 팀장님 JSON데이터를 DB에 넣고싶은데 이러이러합니다. 괜찮을까요?  
음 JSON 데이터는 한 컬럼에 집어 넣는게 좋습니다. |   
| 그럼 데이터타입이 엄청 커져야하지않을까요?  
| 한 컬럼에 JSON데이터를 넣으면 최대값을 가뿐히 넘길 수도 있을 것 같은데 그럴경우 어떻게 해야할까요?  
VARCHAR말고 CLOB, BLOB같은 다른 데이터 타입을 알아보세요 |   
하지만 해당 데이터타입은 쿼리짤때 상그러울수있어요. 마이그레이션하기도 골치아프고, 바이너리데이터가 들어가서 데이터 분석이 힘들기도하구요. |   
  
  
  
  

## ✍️배움포인트

  1. MySQL기준 VARCHAR를 데이터타입으로 지정할때 최대값은 4000이다. 즉, VARCHAR(4000)까지 가능
  2. CLOB, BLOB이란
  3. DB 마이그레이션: 여러 DB를 하나의 DB로 합치거나, 기존의 DB를 다른 DB로 옮기는 경우 등 DB를 이동시키는 작업을 의미함.
  4. 바이너리데이터: 이진수로 표시한 데이터

  
  

## 🆚CLOB VS BLOB 차이

VARCHAR | CLOB(Character Large Object) | BLOB(Binary Large Object)  
---|---|---  
문자열을 표현할때 사용하는 데이터 타입 | 사이즈가 큰 데이터를 외부 파일로 저장하기 위한 데이터 타입 | 바이너리 데이터를 DB외부에 저장하기 위한 타입  
최대 4000BYTE | 문자열 -변환-> CLOB타입 경우, 최대 길이: 외부 저장소에서 생성 가능한 파일 크기(최대 4GB) | 문자열 -변환-> BLOB타입 경우, 최대 길이: 외부 저장소에서 생성 가능한 파일 크기(최대 4GB)  
가변길이 문자열 저장 | 가변길이 문자열 저장 | 가변길이 문자열 저장  
| 큰 텍스트 데이터 ( text ) 용 | 바이너리 데이터 ( 비디오, 이미지, 문서, 기타 ) 용  
| SQL문에서 문자열 타입으로 입출력 값을 표현함 | SQL문에서 비트열 타입으로 입출력 값을 표현함  
  
  
  
  

## 🤔standard xAPI DB Architechture 나 schema가 있을까?

> 아니요, 표준 LRS데이터베이스 스키마가 없으며, LRS 구현자는 자신의 데이터 스토리지 아키텍처를 자유롭게 선택할 수 있습니다.  
> 보통은 아래 두 가지로 초기 LRS를 구현합니다.
> 
>   * traditional relational structures를 사용하여 구현
>   * NoSQL data stores를 사용하여 구현  
> 다행히도 xAPI를 사용하면 이기종간의 표준화된 데이터베이스 스키마가 필요하지 않습니다.  
> xAPI 그 자체로도 LRS간의 pull 또는 push가 자유롭게 가능합니다  
> [답변의 출처 바로가기](https://support.scorm.com/hc/en-us/articles/206164976-Is-there-a-standard-xAPI-database-architecture-or-schema-)  
> 만약 xAPI를 처음 시작하는 개발자라면 스키마 구현이 어려울 수 있습니다. 파이썬을 활용한 예시([바로가기](https://github.com/adlnet/ADL_LRS/blob/master/lrs/models.py))를 참고하셔도 좋습니다.  
> CouchDB를 backing store LRS로 고려해볼 수 있습니다. CouchDB는 NoSQL JSON document store로 http API가 내장되어있고 JS 함수(map, reduce 등)를 사용하여 쿼리를 만들 수 있습니다.
> 

  
  
  

## 참고

  * <https://github.com/adlnet/xAPI-Spec/blob/master/xAPI-Data.md#24-statement-properties>
  * <https://jeonggi.tistory.com/45>
  * [https://m.blog.naver.com/PostView.nhn?blogId=rlasksdud53&logNo=220595010315&proxyReferer=https:%2F%2Fwww.google.com%2F](https://m.blog.naver.com/PostView.nhn?blogId=rlasksdud53&logNo=220595010315&proxyReferer=https:%2F%2Fwww.google.com%2F)
  * <https://lottoking.tistory.com/3938>

#[Journal](/tags/Journal/)[오늘또못알아듣고말았습니다](/tags/%EC%98%A4%EB%8A%98%EB%98%90%EB%AA%BB%EC%95%8C%EC%95%84%EB%93%A3%EA%B3%A0%EB%A7%90%EC%95%98%EC%8A%B5%EB%8B%88%EB%8B%A4/)[JSON](/tags/JSON/)[xAPI](/tags/xAPI/)
