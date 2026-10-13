---
title: "[mybatis] 객체 안에 객체 매핑하기"
date: 2023-11-14 01:26:31
tags:
  - "MyBatis"
categories:
  - Database
  - MySQL
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">객체 안에 객체 매핑하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    객체를 필드로 사용하는 경우 mybatis에서 ``을 활용할 수 있다.</p>
</div>

<!-- more -->

객체를 필드로 사용하는 경우 mybatis에서 `<association>`을 활용할 수 있다.

# 객체

User객체를 필드로 사용하는 2개의 컬럼이 있는 Board객체가 있다.  
이를 하나의 쿼리로 select해오려면 `resultMap`과 `<association>`을 사용하면 된다.

```java
@Data
public class Board {
	private int idx;
	private String title;
	private String content;
	private int writerIdx;
	private int editorIdx;
	private User writer;
	private User editor;
}
```

```java
@Data
public class User {
	private int idx;
	private String name;
	private String mobile;
}
```

  
  
  

# 쿼리

```xml
<!-- Board 객체 매핑 -->
<resultMap id="boardMap" type="Board">
	<id property="idx" column="IDX"/>
	<result property="title" column="TITLE"/>
	<result property="content" column="CONTENT"/>
	<!-- 아래 userMap 실행해서 가져옴 -->
	<association property="writer" resultMap="userMap" columnPrefix="WRITER_">
	<association property="editor" resultMap="userMap" columnPrefix="EDITOR_"/>
</resultMap>

<!-- userMap 객체 매핑 -->
<resultMap id="userMap" type="User">
	<id property="idx" column="IDX"/>
	<result property="name" column="NAME"/>
	<result property="mobile" column="MOBILE"/>
</resultMap>
```

위처럼 resultMap 매핑코드를 작성해주고 아래와같이 select문을 호출하면 된다

```sql
<select id="getBoardDetail" parameterType="int" resultMap="reportMap">
 SELECT 
	b.*,
	writer.NAME AS WRITER_NAME,
	writer.mobile AS WRITER_MOBILE,
	editor.NAME AS EDITOR_NAME,
	editor.mobile AS EDITOR_MOBILE
FROM BOARD b
JOIN USER writer
ON b.WRITER_IDX = writer.IDX
JOIN USER editor
ON b.EDITOR_IDX = editor.IDX
WHERE 1=1
AND b.IDX = #{idx}
</select>
```

  
  
  

# 주의점

association의 resultMap를 동일한 userMap으로 사용하므로 `association의 속성인 columnPrefix`로 꼭 구분해줘야한다!  
이걸 못찾아서 몇시간을 삽질했는지… 절레절레

#[MyBatis](/tags/MyBatis/)
