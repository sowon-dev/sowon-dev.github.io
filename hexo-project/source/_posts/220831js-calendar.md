---
title: "[Moment.js]동적 달력(캘린더)만들기"
date: 2022-08-30 20:43:18
tags:
  - "Moment.js"
categories:
  - Frontend
  - JavaScript
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">동적 달력(캘린더)만들기의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    해당 코드를 사용하기 위해서는 moment.js가 있어야한다.</p>
</div>

<!-- more -->

JS로 달에 맞게 생성되는 동적 달력을 그려보자.

## html 태그로만 달력그리기

html코드로만 달력을 그린다면 아래와 같은 것이다.  
하지만 이렇게 그린다면 달마다 바뀌는 달력이 아닌 정적달력이 되버린다.  
매달 달라지는 달력은 어떻게 만들까?

```html
<div>
	<div>
		<a><i class="fa fa-arrow-left" aria-hidden="true"></i>이전달</a>
		<p id="title-date">----년 -월</p>
		<a><i class="fa fa-arrow-right" aria-hidden="true"></i>다음달</a>
	</div>
	<div>
		<table id="month-table" class="table_cal">
			<thead>
			<tr>
				<th>일</th>
				<th>월</th>
				<th>화</th>
				<th>수</th>
				<th>목</th>
				<th>금</th>
				<th>토</th>
			</tr>
			</thead>
			<tbody>
			<tr>
				<td>
					<p></p>
					<span></span>
				</td>
				<td>
					<p></p>
					<span></span>
				</td>
				<td>
					<p></p>
					<span></span>
				</td>
				<td>
					<p></p>
					<span></span>
				</td>
				<td>
					<p></p>
					<span></span>
				</td>
				<td>
					<p>1</p>
					<span></span>
				</td>
				<td>
					<p>2</p>
					<span></span>
				</td>
			</tr>
			<tr>
				<td>
					<p>3</p>
					<span>

					</span>
				</td>
				<td>
					<p>4</p>
					<span>

					</span>
				</td>
				<td>
					<p>5</p>
					<span>
						<a href="javascript:void(0);"></a>
					</span>
				</td>
				<td>
					<p>6</p>
					<span>
					</span>
				</td>
				<td>
					<p>7</p>
					<span>
					</span>
				</td>
				<td >
					<p>8</p>
					<span>
					</span>
				</td>
				<td>
					<p>9</p>
					<span>

					</span>
				</td>
			</tr>
			<tr>
				<td>
					<p>10</p>
					<span>

					</span>
				</td>
				<td>
					<p>11</p>
					<span>

					</span>
				</td>
				<td>
					<p>12</p>
					<span>

					</span>
				</td>
				<td>
					<p>13</p>
					<span>

					</span>
				</td>
				<td>
					<p>14</p>
					<span>

					</span>
				</td>
				<td class="possible">
					<p>15</p>
					<span>
						<a href="javascript:void(0);"></a>
					</span>
				</td>
				<td>
					<p>16</p>
					<span>

					</span>
				</td>
			</tr>
			<tr>
				<td>
					<p>17</p>
					<span>

					</span>
				</td>
				<td>
					<p>18</p>
					<span>

					</span>
				</td>
				<td>
					<p>19</p>
					<span>

					</span>
				</td>
				<td>
					<p>20</p>
					<span>

					</span>
				</td>
				<td>
					<p>21</p>
					<span>

					</span>
				</td>
				<td class="possible">
					<p>22</p>
					<span>
						<a href="javascript:void(0);"></a>
					</span>
				</td>
				<td>
					<p>23</p>
					<span>

					</span>
				</td>
			</tr>
			<tr>
				<td>
					<p>24</p>
					<span>

					</span>
				</td>
				<td>
					<p>25</p>
					<span>

					</span>
				</td>
				<td>
					<p>26</p>
					<span>

					</span>
				</td>
				<td>
					<p>27</p>
					<span>
						<a href="javascript:void(0);"></a>
					</span>
				</td>
				<td>
					<p>28</p>
					<span>

					</span>
				</td>
				<td>
					<p>29</p>
					<span>
						<a href="javascript:void(0);"></a>
					</span>
				</td>
				<td>
					<p>30</p>
					<span></span>
				</td>
			</tr>
			<tr>
				<td>
					<p>31</p>
					<span></span>
				</td>
				<td>
					<p></p>
					<span></span>
				</td>
				<td>
					<p></p>
					<span></span>
				</td>
				<td>
					<p></p>
					<span></span>
				</td>
				<td>
					<p></p>
					<span></span>
				</td>
				<td>
					<p></p>
					<span></span>
				</td>
				<td>
					<p></p>
					<span></span>
				</td>
			</tr>
			</tbody>
		</table>
	</div>
</div>
```

  
  
  

## 동적 달력

위 html코드에서 thead와 tbody부분을 제거했다.  
restDaysWeekNumber를 통해서 주말과 평일을 나눠서 달력에 특별한 표시를 할수도 있다.  
해당 코드를 사용하기 위해서는 moment.js가 있어야한다.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.4/moment.min.js" integrity="sha512-CryKbMe7sjSCDPl18jtJI5DR5jtkUWxPXWaLCst6QjH8wxDexfRJic2WRmRXmstr2Y8SxDDWuBO6CQC6IE4KTA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script>
const createMonthTable = async (date) => {	
	let firstDate = new Date(date.getFullYear(), date.getMonth(), 1);
	let lastDate = new moment(firstDate).add(1, 'months').subtract(1, 'days');
	let currentDate = firstDate;
	$('#title-date').text(moment(firstDate).format("YYYY년 MM월"));
	$('#title-date').data("firstdate", firstDate);
	let table = $("#month-table");
	let calenderTable = $("<table id='month-table'></table>");
	calenderTable.empty();
	
	const today = moment();
	let tempCurrentDate;
	let daysNumber = 0;
	
	let theadTr = $("<thead></thead>");
	theadTr.appendTo(calenderTable);

	let headTr = $("<tr></tr>");
	for (let i = 0; i < 7; i++) {
		let th = $("<th>" + moment().day(i).format("ddd") + "</th>");
		headTr.append(th);
	}
	headTr.appendTo(theadTr);
	
	let restDaysWeekNumber = "60"; /* 정기휴일(일:0,월:1,화:2, ... ,금:5,토:6) */
	while (currentDate <= lastDate) {
		tempCurrentDate = new moment(currentDate);
		let daysTr = $("<tr></tr>");
		
		for (let i = 0; i < 7; i++) { // 여기서 i는 요일
			let td = $("<td></td>");
			
			if (restDaysWeekNumber.includes(i)) {
				td.addClass("blocked"); // 주말표시가 된 class를 추가할 수 있음
			}
			
			if (tempCurrentDate.day() == i && firstDate <= tempCurrentDate && tempCurrentDate <= lastDate) {
				let p = $("<p>"+tempCurrentDate.date()+"</p>");
				p.appendTo(td);
				
				let span = $("<span></span>");
				span.appendTo(td);
				
				tempCurrentDate.add(1, 'days');
			}
			
			td.appendTo(daysTr);
		}
		daysTr.appendTo(calenderTable);
		currentDate = new moment(tempCurrentDate);
	}
	
	let parent = table.parent();
	table.remove();
	calenderTable.appendTo(parent);
};
// 달력 이전달 이동
const makePreCalender = () => {
	preDateString = moment($('#title-date').data('firstdate')).add('-1','M').format("YYYY-MM-DD");
	createMonthTable(new Date(preDateString));
}
// 달력 다음달 이동
const makeNextCalender = () => {
	nextDateString = moment($('#title-date').data('firstdate')).add('1','M').format("YYYY-MM-DD");
	createMonthTable(new Date(nextDateString));
}

$(document).ready( () => {

	var data = createMonthTable(new Date());
	
});
</script>

<div>
	<div>
		<a href="javascript:makePreCalender();"><i class="fa fa-arrow-left" aria-hidden="true"></i>이전달</a>
		<p id="title-date">----년 -월</p>
		<a href="javascript:makeNextCalender();"><i class="fa fa-arrow-right" aria-hidden="true"></i>다음달</a>
	</div>
	<div>
		<table id="month-table">
			<thead>
			<tr>
				<th>일</th>
				<th>월</th>
				<th>화</th>
				<th>수</th>
				<th>목</th>
				<th>금</th>
				<th>토</th>
			</tr>
			</thead>
		</table>
	</div>
</div>
```

완성!

#[Moment.js](/tags/Moment-js/)
