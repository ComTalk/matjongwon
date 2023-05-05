# matjongwon
맛집 종합원

## Scrapers

이 브랜치는 네이버, 카카오, 트립어드바이저 그리고 구글 맵 등의 데이터를 크롤링 하기 위해서 생성하였다.
크롤링한 데이터는 [data](https://github.com/ComTalk/matjongwon/tree/scrapers/data)에 json 파일로 저장되며,
json format 은 [여기](https://github.com/ComTalk/matjongwon/wiki/json-format) 에서 확인 가능하다.

### Prerequisite

* Python 3.7+
* Selenium 3.141.0
* Webdriver_manager 3.8.3
* urllib3 1.26.9
* requests 2.28.0

### Description

* kakaomap_scraper.py : Selenium을 사용하여 강남구 맛집 데이터를 카카오맵에서 크롤링. 데이터는 data/kakaomap_contents.json 에 저장
* naver_scaper.py : 네이버맵 API를 이용하여 강남구 맛집 데이터를 받아온 뒤, Selenium을 사용하여 네이버맵에서 크롤링. 데이터는 data/naver_contents.json 에 저장
* search_googlemap.py : 네이버와 카카오맵의 통합된 데이터를 읽어서 이 데이터를 토대로 selenium을 사용하여 구글맵에서 크롤링. 구글맵에 통합된 데이터의 자료가 있을 경우 구글맵 데이터를 기존의 데이터에 추가함. 추가로 경도 및 위도 정보 추가. 데이터는 data/final_contents.json 에 저장.
* search_kakaomap.py : 네이버 맵의 크롤링 데이터를 카카오맵에서 검색하여 네이버 맵 데이터가 카카오맵에 있을 경우 데이터를 통합. 데이터는 data/combine_contents.json 에 저장
* tripadvisor_scraper.py : selenium을 사용하여 강남구 맛집 데이터를 트립어드바이저에서 크롤링. 데이터는 data/tripadvisor_contents.json 

최종 데이터는 data/final_contents.json 이다.