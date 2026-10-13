---
title: "Springboot Excel파일 업로드 후 DB에 저장"
date: 2021-08-09 20:07:29
tags: []
categories:
  - Backend
  - Spring
---

<div class="notification is-tldr">
  <p class="tldr-title">💡 <strong>핵심 요약 (TL;DR)</strong></p>
  <p class="tldr-desc">Springboot Excel파일 업로드 후 DB에 저장의 동작 원리를 이해하고 실제 프로젝트에 적용하기 위한 실무 가이드다.
    스프링프로젝트에서 엑셀파일을 업로드 한 뒤 각 열을 DB 컬럼과 맞춰서 저장하는 기능을 구현해보자.</p>
</div>

<!-- more -->

스프링프로젝트에서 엑셀파일을 업로드 한 뒤 각 열을 DB 컬럼과 맞춰서 저장하는 기능을 구현해보자.

## 엑셀데이터 예시

아이디 | 비밀번호 | 사용자이름  
---|---|---  
sea | 1234 | 김바다  
sun | 5678 | 박태양  
wind | 1234 | 이바람  
  
3행 3열로 이루어진 데이터를 DB에 넣어보려고한다.

  
  
  

## pom.xml

먼저 dependency를 추가해야한다. [메이븐 레포지토리 사이트](https://mvnrepository.com/artifact/org.apache.poi/poi-ooxml)에서 원하는 버전과 프로젝트를 선택한다.

```xml
<dependency>
	<groupId>org.apache.poi</groupId>
	<artifactId>poi-ooxml</artifactId>
	<version>5.0.0</version>
</dependency>
```

  
  
  

## userController.java

```java
@RequestMapping(value = "/addExcel", method = RequestMethod.POST)
public ResponseEntity<? extends BasicResponse> addExcel(HttpServletRequest request,
		HttpServletResponse response, MultipartFile file) {

	return ResponseEntity.ok().body(service.insertExcel(file));
};
```

  
  
  

## userService.java

확장자 유효성 검사는 1안과 2안이 있는데 2안이 훨씬 좋다.  
그 이유는 이름만 xls, xlsx로 바꿀 수 있기때문이다 아예 contentType이 XLSX인 것을 확인하는 것이 좋다.

  1. FilenameUtils.getExtension(file.getOriginalFilename()).toLowerCase()로 한 뒤 xlsx이나 xls이 일치하는 지 확인
  2. file.getFile().getContentType()을 변수에 담아서 ConstContentType.XLSX과 일치하는 지 확인

  
  
  
아래는 userService안의 addExcel 메서드 소스 코드이다.  
BasicResponse클래스는 그냥 response클래스이므로 생략하고 mapper클래스도 생략한다.

로직 순서이다.

  1. 파라미터에 파일이 있는지 확인 -> 없으면 return 에러
  2. 확장자가 엑셀인지 확인 -> 아니면 return 에러
  3. 엑셀테이터를 가져와서 각 행마다 VO객체에 저장 -> list에 저장
  4. list를 DB에 insert

```java
@Autowired
ExcelUtil excelUtil;
	
public BasicResponse addExcel(MultipartFile file) {
	BasicResponse res = new BasicResponse();

	// 파일 존재하지 않는 경우
	if (file.isEmpty()) {
		res.setEmpty();
		res.setMessage("Excel 파일을 선택해주세요.");
		return res;
	}

	// 확장자 유효성 검사 -> 엑셀파일만 가능
	//1안: tring ext = fileUtil.getExtension(file.getOriginalFilename());
	//2안
	String contentType = file.getFile().getContentType();

	//1안: if (!ext.equals("xlsx") && !ext.equals("xls")) {
	//2안
	if(!contentType.equals(ConstContentType.XLSX)) {
		res.setEmpty();
		res.setMessage("Excel 파일을 선택해주세요.");
		return res;
	}

	List<UserVO> listUser = new ArrayList<UserVO>();

	// 엑셀의 셀데이터를 가져와서 VO에 담기
	List<Map<String, Object>> listMap = excelUtil.getListData(file, 1, 3);

	for (Map<String, Object> map : listMap) {
		UserVO userInfo = new UserVO();
	
		// 각 셀의 데이터를 VO에 set한다.
		userInfo.setUserId(map.get("1").toString());
		userInfo.setPassword(map.get("2").toString());
		userInfo.setUserName(map.get("3").toString());

		listUser.add(userInfo);
	}

	// 리스트에 담은 VO를 DB에 저장
	for (UserVO oneUser : listUser){
		userMapper.insertUser(oneUser);
	}
}
```

  * getListData(file, 1, 3)의 의미  
엑셀파일의 1번째 행부터 3번째 열까지의 데이터를 listMap에 담는다.  
0번째 행부터 하지 않는 이유는 보통 0번째행은 머리글행으로 제목이나 구분명칭을 작성하기 때문이다.  
3인 이유는 엑셀데이터에 3열이 있기때문이다.  
가지고 있는 엑셀데이터에 따라 변경하면 된다.

  
  
  

## ExcelUtil.java

제일 중요한 엑셀유틸객체이다.

getListData 메서드의 파라미터 정의

  * startRowNum : 시트 시작 행 번호이다. 시트 행은 0부터 시작한다.
  * columnLength : 시트 열의 총 개수

```java
@Component
public class ExcelUtil {
	
	// 각 셀의 데이터타입에 맞게 값 가져오기
	public String getCellValue(XSSFCell cell) {

		String value = "";
		
		if(cell == null){
			return value;
		}

		switch (cell.getCellType()) {
			case STRING:
				value = cell.getStringCellValue();
				break;
			case NUMERIC:
				value = (int) cell.getNumericCellValue() + "";
				break;
			default:
				break;
		}
		return value;
	}

	// 엑셀파일의 데이터 목록 가져오기 (파라미터들은 위에서 설명함)
	public List<Map<String, Object>> getListData(MultipartFile file, int startRowNum, int columnLength) {

		List<Map<String, Object>> excelList = new ArrayList<Map<String,Object>>();
		
		try {
			OPCPackage opcPackage = OPCPackage.open(file.getInputStream());

			@SuppressWarnings("resource")
			XSSFWorkbook workbook = new XSSFWorkbook(opcPackage);

			// 첫번째 시트
			XSSFSheet sheet = workbook.getSheetAt(0);
			
			int rowIndex = 0;
			int columnIndex = 0;

			// 첫번째 행(0)은 컬럼 명이기 때문에 두번째 행(1) 부터 검색
			for (rowIndex = startRowNum; rowIndex < sheet.getLastRowNum() + 1; rowIndex++) {
				XSSFRow row = sheet.getRow(rowIndex);

				// 빈 행은 Skip
				if (row.getCell(0) != null && !row.getCell(0).toString().isBlank()) {

					Map<String, Object> map = new HashMap<String, Object>();

					int cells = columnLength;

					for (columnIndex = 0; columnIndex <= cells; columnIndex++) {
						XSSFCell cell = row.getCell(columnIndex);
						map.put(String.valueOf(columnIndex), getCellValue(cell));
						logger.info(rowIndex + " 행 : " + columnIndex+ " 열 = " + getCellValue(cell));
					}
					
					excelList.add(map);
				}
			}

		} catch (InvalidFormatException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		return excelList;
	}
}
```

  
  
  

## 파일 업로드 사이즈 초과 에러

파일 사이즈를 초과해서 업로드할 수 있으므로 예외처리를 해준다.  
`@RestControllerAdvice`를 사용한 BadRequestHandler 클래스에서 예외처리를 해주었다.

```java
@RestControllerAdvice
public class BadRequestHandler {

	@ExceptionHandler({MaxUploadSizeExceededException.class})
	public ResponseEntity<? extends BasicResponse> uploadException(MaxUploadSizeExceededException exc, 
		      HttpServletRequest request,
		      HttpServletResponse response) {
		
		return ResponseEntity.status(HttpStatus.PAYLOAD_TOO_LARGE).body(new ErrorResponse(String.valueOf(HttpStatus.PAYLOAD_TOO_LARGE.value()), "파일 사이즈를 초과하였습니다. (10MB 이하의 파일을 선택해주세요.)"));
	}
}
```
