---
title: "[mybatis] update시 모두 if test를 써야 할 경우"
date: 2023-11-14 01:21:04
tags:
  - "MyBatis"
categories:
  - Database
  - MySQL
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">update시 모두 if test를 써야 할 경우의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    아래와 같이 사용하면 된다.</p>
</div>

<!-- more -->

mybatis에서 update시 모든 컬럼에 if 조건물을 걸어야할때가 있다.

아래와 같이 사용하면 된다.

```sql
<update id="testUpdate" parameterType="VO">
   UPDATE testTable
   <trim prefix="SET" suffixOverrides=",">
      <if test="testItem1 != null">testItem1 = #{testItem1},</if>
      <if test="testItem2 != null">testItem2 = #{testItem2},</if>
   </trim>
   WHERE
      idx = #{idx}
</update>
```

#[MyBatis](/tags/MyBatis/)
