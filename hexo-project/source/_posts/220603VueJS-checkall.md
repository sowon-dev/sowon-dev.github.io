---
title: "[Vue]체크박스 모두 선택 기능 구현하기"
date: 2022-06-02 23:25:35
tags:
  - "VueJS"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">체크박스 모두 선택 기능 구현하기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    Vue.js를 이용하여 체크박스의 모두선택기능 기능을 만들어보자.</p>
</div>

<!-- more -->

Vue.js를 이용하여 체크박스의 모두선택기능 기능을 만들어보자.

## 화면코드

```html
<table>
	<colgroup>
		<col width="10%">
		<col width="*">
		<col width="*">
	</colgroup>
	<thead>
		<tr>
			<th><input type="checkbox" name="checkAll" v-model="isCheckAll"></th>
			<th>고유번호</th>
			<th>이름</th>
		</tr>
	</thead>
	<tbody v-if="mainDataset.getRowCount() == 0">
		<tr>
			<td colspan="8">조회 된 데이터가 없습니다.</td>
		</tr>
	</tbody>
	<tbody v-else>
		<tr v-for="(item, idx) in mainDataset.data">
			<td><input type="checkbox" v-model="userList" :value=item.userNo></td>
			<td>{{item.userNo}}</td>
			<td>{{item.userNm}}</td>
		</tr>
	</tbody>
</table>
```

  
  
  

## 스크립트 코드

모달창을 열때마다 isCheckAll를 false로 초기화해주고 watch로 isCheckAll의 value가 변할때 메서드 checkAll()를 실행한다.  
여기서 핵심은 watch로 기존 값과 변경된 값을 지켜보고있다는 점이다.

```js
var app = new Vue({
	el: '#userPopup',
	data: {
		searchParams: {
			searchText: "",
			pageNumber: 1
		},
		isCheckAll: false,
		userList: [],
		mainDataset: new Dataset(),
		mainDatasetPaging: new PagingSet(5, 10),
	},
	watch: {
		"isCheckAll": {
			handler: function(val, oldVal) {
				this.checkAll();
			}
		}
	},
	mounted: function() {
		var self = this;
		$(this.$refs.userPopup).on("shown.bs.modal", function() {
			self.isCheckAll = false;
		});
	},
	//중략
	 methods: {
		 checkAll: function() {
			var self = this;
			app.userList = [];
			if (self.isCheckAll) {
				_.forEach(self.mainDataset.data, function(obj) {
					app.userList.push(obj.userNo);
				});
			}
		},
	 }
})
```

이렇게해면 체크박스 전체선택시 각 체크박스의 userNo값이 userList배열에 담긴다!

#[VueJS](/tags/VueJS/)
