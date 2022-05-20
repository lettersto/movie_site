# Movie Website Project

### ✨ 프로젝트 개요

- **프로젝트명** : 
- **팀원** : 문유주, 정혜령
- **시작일** : 2022.05.20. (금)
- **완료일** :
- **기술 스택**



### ✨ 프로젝트 목표 

1. 영화 데이터 기반 추천 웹 사이트 구성
2. 날씨와 장르에 기반한 영화 추천 알고리즘 구성
3. 사이트 내 커뮤니티 서비스 구성



### ✨ 프로젝트 컨셉 & 주요 기능

1. ㅇㅇ



---

### ✨ 프로젝트 일정표 & 진행 상황

| 번호 | 기능/목표                                           | 담당자 | 시작일 | 종료일 | 비고 |
| ---- | --------------------------------------------------- | ------ | ------ | ------ | ---- |
| 1    | 프로젝트 컨셉 및 시나리오 구상                      | 공통   | 5/20   | 5/20   |      |
| 2    | DB 설계                                             | 공통   | 5/20   | 5/20   |      |
| 3    | URL 설계                                            | 공통   | 5/20   | 5/20   |      |
| 4    | Software 구조 설계 (vue component)                  | 공통   | 5/20   | 5/20   |      |
| 5    | Django & Vue 프로젝트 생성 및 기본 연결 설정 + CORS | 공통   | 5/20   | 5/20   |      |
| 6    | Django 모델 작성                                    | 공통   | 5/20   |        |      |
| 7    | Django Admin 관리자 생성 및 등록                    |        |        |        |      |
| 8    | Django serializer 작성                              | 1      |        |        |      |
| 9    | Django views.py 작성 (알고리즘 제외)                |        |        |        |      |
| 10   | 추천 알고리즘 개발                                  |        |        |        |      |
| 11   | 개발용 테스트 데이터 생성 + POSTMAN으로 API 테스트  |        |        |        |      |
| 12   | Django Authentication & Authorization 기능 구현     | 2      |        |        |      |
| 13   | Vue Home component 생성 (template 위주)             |        |        |        |      |
| 14   | Vue Community component 생성 (template 위주)        |        |        |        |      |
| 15   | Vue 나머지 Component 생성  (template 위주)          |        |        |        |      |
| 16   | Vue router 작성                                     |        |        |        |      |
| 17   | Vue Vuex store 작성 및 component와 연결             |        |        |        |      |
| 18   | 사이트 html, css 디자인                             |        |        |        |      |
| 19   | 발표 준비                                           |        |        |        |      |



---

### ✨ 프로젝트 초기 설계

1. **DB 설계 - ERD**

2. **URL - API 주소**

   - HOST = `http://127.0.0.1:8000/api/v1/`

   | 번호        | url                                              | 기능                 |
   | ----------- | ------------------------------------------------ | -------------------- |
   | \<accounts> |                                                  |                      |
   | 1           | admin/                                           | 관리자 페이지 렌더링 |
   | 2           | accounts/password/reset/                         |                      |
   | 3           | accounts/password/rest/confirm/                  |                      |
   | 4           | accounts/login/                                  | 로그인 기능          |
   | 5           | accounts/logout/                                 | 로그아웃 기능        |
   | 6           | accounts/user/                                   | 개인 정보 조회       |
   | 7           | accounts/password/change                         | 비밀번호 변경        |
   | 8           | accounts/signup/                                 | 회원가입 기능        |
   | \<movies>   |                                                  |                      |
   | 1           | movies/\<int:movie_pk>/                          |                      |
   | 2           | movies/\<int:movie_pk>/reviews/                  |                      |
   | 3           | movies/\<int:movie_pk>/reviews/\<int:review_pk>/ |                      |
   | 13          | movies/\<str:movie_name>/                        |                      |
   | 14          |                                                  |                      |
   | 15          |                                                  |                      |
   | 16          |                                                  |                      |
   | 17          |                                                  |                      |
   | 18          |                                                  |                      |

   

3. Software 구조

---

### ✨ 프로젝트 구현

