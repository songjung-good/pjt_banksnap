

<body>
<img src="header_photo.png" alt="배너 그림" />
</body>



[TOC]






# Bank Snap 🏦

💰 본 프로젝트는 **삼성 청년 SW 아카데미** 1학기 관통 프로젝트 결과물입니다

​	<br>	<br>



## **개요🌱**

- 금융상품정보 웹 애플리케이션
- 예적금상품조회, 금융상품추천, 환율계산, 은행 검색, 커뮤니티 기능을 제공
- 

​	<br>	<br>

## Team 😀

​	<br>	<br>



## 프로젝트 기간💞️

- 2023년 11월 14일 ~ 2023년 11월 24일 (11일)👋


  ### 일정

| 일시      | 진행내용                                                     | 특이사항                                                     | 비고                                                         |
| :-------- | ------------------------------------------------------------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 11/14(화) | 1. 카카오맵 api를 이용한 은행 위치 검색 기능 구현<br />2. 수출입은행 api를 통해 환율계산기능 구현<br />3. vue 컴포넌트 구성 <br />4. 프로젝트 레포 생성 | 1-1. XX+은행으로 검색하는 알고리즘(초기값 명지) <br />2-1. 환율계산기의 양방향 숫자 기입 기능의 문제<br />3-1 . 컴포넌트와 뷰의 기능의 차이에 대한 고찰<br />4-1. git desktop 이용 | 1-1-1. 필요시 변경예정<br />**1-1-2. 브라우저의 네비게이션 기능을 이용하라는 조언**<br />2-1-1. 한쪽에는 숫자를 기입, 다른쪽은 숫자 출력으로 기능 변경<br />3-1-1. (자료를 참고하자) |
| 11/15(수) | 1. 프로젝트 명, 프로젝트 로고 선정<br />2. 커뮤니티 페이지 구현(CRUD)<br />3. 회원가입, 로그인 기능 구현<br />4. 상단 바 네비게이션 구성 | <br />2-1. 커뮤니티의 게시글 수정 문제<br />3-1. 로그인기능구현 - 토큰을 통해 권한을 주는 동작이 정상작동을 하지 않았다<br /> | <br />2-1-1. 게시글 수정 후 페이지에 바로 적용이 안되어서 새로고침되게 만듦<br />3-1-1. 코드에 오타가 있었다. |
| 11/16(목) | 1. readme 초기안 작성<br />2. DB구조 설계<br />3. 금감원api를 통해 은행 상품 정보 불러오기<br />4. 메인페이지 내용 설정<br />5. 네비게이션바 상단 고정, 페이지 화면 범위 수정 | <br />2-1. 회원정보와 은행정보를 얼마나 나눠야할지 고민<br />2-2. 예적금 상품을 연결한 키 설정<br />3-1. 상품정보란 하위에 예금, 적금을 넣을 지 고민<br />4-1. 메인페이지에 경제관련 뉴스<br />5-1. app.vue에 전역범위로 body를 범위를 설정 | <br />2-1-1. 기본회원정보/ 추가회원정보(금융상품추천)/ 은행명/ 은행상품으로 구분<br />2-2-1. 상품키와 예치기간을 기준으로 연결<br />3-1-1. 예금 적금란을 따로 구분하여 금융상품 하위에 적용<br />4-1-1. 네이버검색 API 이용<br /> |
| 11/17(금) | 1. 메인페이지 naver api 통해 경제뉴스<br />2. user테이블 구조 수정<br />3. 은행상품데이터 출력<br />4. 환율계산기, 금리비교, 메인페이지 디자인 수정<br />5. 은행찾기 지역별 검색으로 수정<br /> | 1-1. api 요청에서 오류가 있었다.<br />1-2. 메인페이지 내용추가가 필요<br /><br />3-1. DB내용 재설정<br />3-2. 18시 이후 API서버 점검예정<br />4-1. 조금씩 나아지는 중<br />5-1. 지역데이터 json파일을 이용함 | 1-1-1. 코드리뷰 3시간만에 찾아낸 오류 : 두가지 코드 중 하나에 키 값이 누락되었다....<br /><br />1-2-1. 사진자료 등을 추가<br /><br />3-1-1. 은행상품 데이터에서 은행명은 외래키로 받아오는 것으로 변경<br />3-2-1. json파일로 데이터 저장하여 사용 |
| 11/18(토) | 1. 로그인 인증권한 수정 <br />2. 마이페이지 공부하기 <br />3. 금융상품 상세페이지 <br />4. bootstrap 템플릿 적용하기<br />5. 계산 파일 수정 | <br />2-1.  6주차 프로젝트 자료 참고<br />2-2. 작성게시글 및 댓글 확인<br />3-1. 상세페이지의 내용이 이해에 어렵게 구성되어있음<br />4-1.  UI 구현하는 작업<br />5-1. 시간을 금요일 날짜로 고정 시켜둠 | <br /><br /><br />4-1-1. 기능이 구현된 코드위에 디자인을 입히는 작업이 어려웠다.<br />5-1-1. 주말에는 환율자료를 받아오지못해서 조정이 필요했다. |
| 11/19(일) | 1. 관심상품 등록 기능 추가<br />2. 마이페이지 기능 구현<br />3. vuetify / bootstrapvue 적용 | 1-1. 버튼 누를 시에 마이페이지에 상품 추가<br /> 2-1. 마이페이지로 인해 메인페이지 로딩이 안됐어요 ㅠㅜㅠㅠㅠ<br />3-1. 적용 포기 | <br />2-1-1. 기존에 등록된 사용자 (가져올 데이터가 없거나) or 등록되지 않은 사용자<br />3-1-1. 이미 들어간 코드에 영향을 줌<br />3-1-2. 예시 코드가 vue2 혹은 typescript가 많고 이식시키는데 어러움을 느낌<br /> |
| 11/20(월) | 1. 개인정보 입력란 추가<br />2. 디버깅<br />3. 로그인, 회원가입 페이지 디자인 수정 | 1-1. 해당 입력 값을 통해 금융상품 추천 예정<br />2-1. 메인페이지가 보이지 않는 오류<br />2-2. 로그인이 되지 않는 오류<br />3-1. bootstrap을 적용 | 2-1-1. 마이페이지 기능이 추가되고 생겼었고 '로그인 시' 보이도록 수정<br />2-2-1. 마이페이지를 끄고 로그인 후 다시 작동을 시킨다.<br />2-2-2. HTML쪽 코드가 script의 코드보다 빠르게 진행되어 생기는 오류로 추측<br />2-2-3. 해당 오류는 life cycle 과 local에 입력데이터를 저장하는 방법 등으로 해결예정 |
| 11/21(화) | 1. 방향수정<br />2. 크롤링으로 금 / 유가 / 부동산 시세 받아오기<br />3. 게시판 정리 <br />4. 메인 페이지 정리 | 1-1. 기존에는 기능 구현에 힘썻다면 컨셉을 적용<br />2-1. 부동산은 네이버부동산을 이용하여 지도를 통해 주변 시세확인<br />2-2. 금/ 유가 크롤링해오기<br />3-1. 게시판 디자인 수정<br />4-1. 메인페이지의 뉴스를 옮김 | 1-1-1. 다양한 종류의 상품을 볼 수 있게 수정<br />1-1-2. 질문을 통해 상품 추천<br />2-1-1. 네이버 부동산 api가 있었는데 없어졌다.<br /><br />2-1-2. 부동산 포기<br />2-2-1. 크롤링을 막아둔 사이트가 많아서 다양한 시점을 보여주기 실패 |
| 11/22(수) | 1. 내 정보 창 수정<br />2. 추천상품 제공<br />3. 웹페이지 전체 디자인 수정<br />4. |                                                              |                                                              |
| 11/23(목) | 발표자료 구성                                                |                                                              |                                                              |
| 11/24(금) | 발표!!!!                                                     |                                                              |                                                              |

  <br><br>


## 개발 환경 👀

<p align="center">
  <img src="https://img.shields.io/badge/API-Kakao_Map-yellow?style=flat&logo=kakao&logoColor=white"> 
  <img src="https://img.shields.io/badge/API-한국수출입은행-darkblue?style=flat">
  <img src="https://img.shields.io/badge/API-금융감독원-skyblue?style=flat">
  <img src="https://img.shields.io/badge/API-NAVER-lightgreen?style=flat&logo=naver">
  <img src="https://img.shields.io/badge/Language-Python-007396?style=flat&logo=python&logoColor=white"> 
  <img src="https://img.shields.io/badge/Language-JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=white"> 
  <img src="https://img.shields.io/badge/Database-Sqlite-green?style=flat&logo=sqlite&logoColor=white"> 
  <img src="https://img.shields.io/badge/Framework-django-darkgreen?style=flat&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/Framework-Vue-D22128?style=flat&logo=vue.js&logoColor=white">
  <img src="https://img.shields.io/badge/Library-Bootstrap-purple?style=flat&logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/Library-pinia-orange?style=flat&logo=pinia&logoColor=white">
</p>


```markdown
python: 3.9.13

JavaScript: es6++??

Sqlite: <- 플러그인으로 쓰는데??

Django: 4.2.7

djangorestframework: 3.14.0

Vite: 4.4.11 <-툴인데??

Vue: 4.4.0

bootstrap: 5.3.1

pinia: 2.1.7 

기술스택을 작성하는 법을 보고 수정을 하자
```



​	<br>	<br>	


## 협업 툴 👊

- Notion

- Mattermost

- github

  <br><br>



## ERD

![DB구조](doc\구조\DB.png)

  <br> <br>


## 주요기능



## ~~아키텍쳐 👨‍💻 수정이 필요합니다ㅠㅠ!~~ 

[![TechArchitecture](https://user-images.githubusercontent.com/53832553/154430527-09bd19d6-993f-4dc0-ae4f-5a5e77220055.png)](https://user-images.githubusercontent.com/53832553/154430527-09bd19d6-993f-4dc0-ae4f-5a5e77220055.png)

​	<br>	<br>
