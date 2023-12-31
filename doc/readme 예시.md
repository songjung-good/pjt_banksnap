# Bank Snap

🔔 본 프로젝트는 **삼성 청년 SW 아카데미** 1학기 관통 프로젝트 결과물입니다

- 👀 I’m interested in Game
- 🌱 I’m currently learning Python
- 💞️ I’m looking to collaborate on smart people
- 📫 How to reach me add proflie

<br><br>



## **개요**

- 금융상품정보 웹 애플리케이션
- 예적금상품조회, 금융상품추천, 환율계산, 은행 검색, 커뮤니티 기능을 제공

<br><br>

## 프로젝트 기간

- 2023년 11월 14일 ~ 2023년 11월 24일 (11일)👋

<br>

<br>

## 기술 스택

<p align="center">
  <img src="https://img.shields.io/badge/API-Kakao_Map-yellow?style=flat&logo=kakao&logoColor=white"> 
  <img src="https://img.shields.io/badge/API-한국수출입은행-darkblue?style=flat">
  <img src="https://img.shields.io/badge/API-금융감독원-skyblue?style=flat">
  <img src="https://img.shields.io/badge/Library-BootstrapVue-violet?style=flat&logo=bootstrap-vue&logoColor=white"> 
  <img src="https://img.shields.io/badge/Library-Bootstrap5-purple?style=flat&logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/Language-Python-007396?style=flat&logo=python&logoColor=white"> 
  <img src="https://img.shields.io/badge/Language-JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=white"> 
  <img src="https://img.shields.io/badge/Database-Sqlite-darkgreen?style=flat&logo=sqlite&logoColor=white"> 
  <img src="https://img.shields.io/badge/Framework-Vue-D22128?style=flat&logo=vue.js&logoColor=white"> 

</p>

###### <br><br>

## 팀원

<table>
  <thead>
    <tr>
      <th>이름</th>
      <th>역할</th>
      <th>구현 기능</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">박대언</td>
      <td rowspan="2">팀장</td>
      <td>Front-End 전반</td>
    </tr>
    <tr>
      <td>Back-End (Rest API 설계, SQL/Spring 디버깅, 이미지 업로드, 매물 조회 게시판 카테고리/키워드 검색 등 필요 API 추가, DB 테이블 수정 등)</td>
    </tr>
    <tr>
      <td rowspan="2">강소현</td>
      <td rowspan="2">팀원</td>
      <td>Back-End 전반</td>
    </tr>
    <tr>
      <td>Front-End (메인 페이지 검색창 수정 및 매물 조회 게시판 디자인)</td>
    </tr>
  </tbody>
</table>

<br><br>

## **DataBase 설계**

![db설계](./assets/db설계.png)

<br><br>

## 주요 기능

![기능정의서](./assets/기능정의서.png)

<br><br>

## 실행 화면

### 🔗 메인 페이지 - 뉴스 API

![03_메인페이지_뉴스API](./assets/03_메인페이지_뉴스API.gif)

✅ 네이버 뉴스API를 활용하여 부동관 관련 뉴스 리스트로 표시

<br><br>

### 🔗 메인 페이지 - 키워드 검색

![03_메인페이지_키워드검색_1](./assets/03_메인페이지_키워드검색_1.gif)

![03_메인페이지_키워드검색_2](./assets/03_메인페이지_키워드검색_2.gif)

✅ 동, 건물명 중 검색 키워드 일부 혹은 전체 검색하면 관련 건물을 마커로 표시

<br><br>

---

### 🔗 회원가입

![01_1_회원가입](./assets/01_1_회원가입.gif)

✅ 회원 분류 (일반 회원 / 기업 회원) 2가지, 아이디 중복체크, 비밀번호 이중 체크

✅ 비밀번호, 비밀번호 확인이 같지 않으면 비밀번호가 일치하지 않음을 표시

<br><br>

### **🔗 비밀번호 찾기**

![01_2_비밀번호_찾기](./assets/01_2_비밀번호_찾기.gif)

✅ Commons Email을 활용한 회원 인증을 걸친 후, 임시 비밀번호를 사용자 이메일로 전송

<br><br>

---

### 🔗 공지사항

![공지사항](./실행화면/공지사항.gif)
✅ 공지사항 리스트, 글 조회, 작성, 수정, 삭제

<br><br>

---

### **🔗 매물 검색 - 동 검색**

![02_1_매물_동검색](./assets/02_1_매물_동검색.gif)

✅ 지도는 카카오 MAP API 사용

✅ 시, 구/군, 동 선택하면 그 지역에 존재하는 건물 마커로 표시

<br><br>

### **🔗 매물 검색 - 키워드 검색**

![02_1_매물_키워드검색_1](./assets/02_1_매물_키워드검색_1.gif)

![02_1_매물_키워드검색_2](./assets/02_1_매물_키워드검색_2.gif)

✅ 동, 건물명 중 검색 키워드 일부 혹은 전체 검색하면 관련 건물을 마커로 표시

<br><br>

### **🔗 관심 건물 - 북마크**

![02_2_관심매물_북마크](./assets/02_2_관심매물_북마크.gif)

✅ 관심 건물 북마크 표시 후 마이페이지에서 확인

<br><br>

### **🔗 관심 건물 - 북마크 해제**

![02_2_관심매물_북마크_해제](./assets/02_2_관심매물_북마크_해제.gif)

✅ 마이페이지에서 관심 건물 북마크 해제 (실거래가 페이지에서도 해제 가능)

<br><br>

### **🔗 리뷰 등록**

![02_3_리뷰_등록](./assets/02_3_리뷰_등록.gif)

✅ 실거주자는 건물에 대한 리뷰 작성이 가능

✅ 교통요건, 거주환경, 주변환경, 총 추천점수, 리뷰 내용 작성

<br><br>

### **🔗 리뷰 확인**

![02_3_리뷰_확인](./assets/02_3_리뷰_확인.gif)

✅ 마이페이지에서 리뷰 삭제

<br><br>

### **🔗 리뷰 삭제**

![02_3_리뷰_삭제](./assets/02_3_리뷰_삭제.gif)

<br><br>

### **🔗 관심 매물 - 북마크**

![02_4_관심_매물_북마크](./assets/02_4_관심_매물_북마크.gif)

✅ 관심 매물 북마크 표시 후 마이페이지에서 확인

<br><br>

### **🔗 관심 매물 - 북마크 해제**

![02_4_관심_매물_북마크_해제](./assets/02_4_관심_매물_북마크_해제.gif)

✅ 마이페이지에서 관심 매물 북마크 해제 (실거래가 페이지에서도 해제 가능)

<br><br>

----

### **🔗 기업회원 - 로그인**

![04_1_기업회원_로그인](./assets/04_1_기업회원_로그인.gif)

✅ 기업 회원 로그인

✅ 일반 회원, 기업 회원 데이터베이스 분리

<br><br>

### **🔗 매물 목록**

![04_2_매물_목록](./assets/04_2_매물_목록.gif)

✅ 등록된 매물 카드 형식으로 조회

<br><br>

### **🔗 매물 조회 - 거래 유형**

![04_3_매물_거래유형_](./assets/04_3_매물_거래유형_.gif)✅ 거래 유형(매매 / 전세 / 월세) 으로 분류

<br><br>

### **🔗 매물 검색 - 건물명**

![04_4_매물_검색_1_](./assets/04_4_매물_검색_1_.gif)

✅ 건물명(키워드 일부 혹은 전체) 검색을 통해 매물 조회

<br><br>

### **🔗 매물 검색 - 작성자**

![04_4_매물_검색_2_](./assets/04_4_매물_검색_2_.gif)

✅ 작성자(키워드 일부 혹은 전체) 검색을 통해 매물 조회

<br><br>

### **🔗 매물 검색 - 평 수**

![04_4_매물_검색_3_](./assets/04_4_매물_검색_3_.gif)

✅ 평 수 검색을 통해 관련 매물 조회

<br><br>

### **🔗 매물 등록**

![04_5_매물_등록_1](./assets/04_5_매물_등록_1.gif)

![04_5_매물_등록_2](./assets/04_5_매물_등록_2.gif)

✅ 매물 등록(건물 정보, 거래 종류, 실거래가, 해당 층, 면적(평 수), 방향, 관리비, 방, 욕실, 매물 특징, 매물 설정, 매물 이미지)

<br><br>

### **🔗 매물 삭제**

![04_6_매물_삭제](./assets/04_6_매물_삭제.gif)

✅ 등록된 매물 삭제

<br><br>

### **🔗 매물 이미지 확인**

![04_7_매물_이미지_확인](./assets/04_7_매물_이미지_확인.gif)

✅ 등록된 매물 이미지 확인 및 다운로드

<br><br>

----

### **🔗 마이페이지**

![05_1_마이페이지_1](./assets/05_1_마이페이지_1.gif)

✅ 마이페이지 화면

<br><br>

### **🔗 마이페이지 - 친구 관심 매물 확인**

![05_2_마이페이지_친구_관심매물](./assets/05_2_마이페이지_친구_관심매물.gif)

✅ 마이페이지를 통해 팔로워한 친구 관심 매물 확인

<br><br>

### **🔗 마이페이지 - 프로필 이미지 변경**

![05_2_마이페이지_프로필_이미지_변경](./assets/05_2_마이페이지_프로필_이미지_변경.gif)

✅ 마이페이지에서 사용자 프로필 이미지 변경

<br><br>

### **🔗 마이페이지 - 친구 등록**

![05_3_마이페이지_친구_등록](./assets/05_3_마이페이지_친구_등록.gif)

✅ 마이페이지에서 친구 추가를 통해 친구를 팔로잉 할 수 있음

<br><br>

### **🔗 마이페이지 - 친구 삭제**

![05_4_마이페이지_친구_삭제](./assets/05_4_마이페이지_친구_삭제.gif)

✅ 마이페이지에서 나를 팔로워 하는 친구를 삭제할 수 있음