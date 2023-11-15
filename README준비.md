# pjt









# 프로젝트 계획안

# 회의안

## 회의 주제

1. 프로젝트 주제 선정
   1. 금융프로젝트 VS 영화프로젝트
   2. 해당 프로젝트의 선정 이유
      1. 기획배경 작성
   3. 구현하고싶은 기능
      1. 목표설정
2. 프로젝트 계획 수립
   1. 역할 분배
   2. 기술스택, 개발환경 설정
   3. 프로젝트 일정설정

## 회의 내용

1. 금융프로젝트 선정
   1. 부산 내의 금융권에 어필 가능한 프로젝트
   2. 이전 기수들과는 차별점이 있는 프로젝트
   3. 구현
2. 구현하고 싶은 기능
   1. 기본적인 기능 + 외부적인 기능(사이트 광고, 이벤트적인 부분)
   2. 기본적 기능에 구체화된 기능(내용적인 디테일, 출석, 커뮤니티 등)
3. 역할 분배
   1. 지민아 미안해 내가 할 수 있는게 없어
   2. 그래도 열심히 해볼게 뭐가 필요하니?
   3. 잘해보자 화이팅
4. 기술 스택, 개발환경
   1. 운영체제 : window 10
   2. front : Vue.js 3, BootStrap5, JavaScript,
   3. back : Django3.2 , MySQL
   4. 기타 : python 3.9 , nodw.js 18.
5. 프로젝트 일정
   1. 11월 3일 ~ 11월 10일 : 프로젝트에 대한 기안 작성 및 기술스택 익히기
   2. 11월 11일 ~ 11월 21일 : 필수 기능 구현 및 기본 형태 구현
   3. 11월 22일 ~ : 추가 기능 및 디버깅







# 참고자료

# 참고 자료 및 참고 사이트

### 프로젝트 자료



### API

- 한국수출입은행 (koreaexim.go.kr)
  - https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=AUTHKEY1234567890&searchdate=20180102&data=AP01
  - 일일 호출 가능 횟수를 1000회로 제한 (1000회 이상 호출 시 result:4 반환, 데이터 미제공)
- Kakao 지도 Web API 가이드
  - 카카오맵은 마지막에 해야할듯 왜캐 어렵지?
- 오픈 API 소개 | 오픈API개요 | 오픈API | 금융감독원 금융상품통합비교공시 금융상품한눈에 (fss.or.kr)
  - https://fss.or.kr/finlife/finlifeapi/depositProductsSearch.xml?auth={인증키}&topFinGrpNo=020000&pageNo=1





# 시작 전 참고사이트

## 설명

- 이전 기수 프로젝트
  - [6기 프로젝트 공공데이터](https://github.com/ksh103/HappyHouse)
  - [비전공 6기](https://sostl.tistory.com/78)
- 이상적인 웹페이지
  - [마이뱅크](https://www.mibank.me/index.php)
  - [bank of hope](https://www.bankofhope.com/ko/hope-stories/take-your-banking-online)
- 웹페이지 템플릿
  - [start bootstrap](https://startbootstrap.com/?showAngular=false&showPro=false)
- 웹페이지 제작 도움글
  - [10분 웹페이지](https://brunch.co.kr/@llun/15)
  - [GPT로 웹페이지 만들기]([]())
- 웹페이지 배포
  - [netlify 1](https://penguingoon.tistory.com/260)
  - [코딩애플](https://codingapple.com/unit/react-build-deploy-github-pages/)
  - [git](https://brunch.co.kr/@everiwon/42)







# 페이지 인터페이스 구성

# 페이지의 모습은 어떻게 만들어질까요?

## 주요 모습

- 목표:
  - 메인페이지
    - carousel?
  - 프로필 페이지 → 회원 커스텀 페이지, 금융상품추천 알고리즘
    - allauth & dj-rest-auth
  - 예적금 금리 비교 페이지
  - 환율계산기 페이지
  - 근처 은행 검색
  - 커뮤니티

## 추가할 모습

- 목표가 아닌 항목:
  - 핵심 프로덕트 UI 변경 권장
  - 프로덕트 로드맵 변경 권장
- 다음 단계:
  - 연구팀의 인터뷰 10개 모두 보기
  - 인사이트 작성, Slack으로 공유





# 구현할 기능

## 필수구성요소

- 목표:
  - 예금 & 적금 금리 비교 (금감원 API)
  - 신혼 여행을 위한 환율 계산기 (한국수출입은행 환율 정보 API)
  - 내 집 주변 은행 검색 ( 카카오맵API)
  - 나에게 맞는 상품 추천
    - 아이디어가 필요

## 추가할 기능

- 목표가 아닌 항목:
  - (추가될 예정입니다 아마더..)

### 기능구현 아이디어 및 코드