<template>
  <div>
    <b-navbar toggleable="sm" variant="light">
      <b-navbar-toggle target="sidebar-1" v-b-toggle.sidebar-1></b-navbar-toggle>

      <b-navbar-brand href="/">맛종원</b-navbar-brand>

      <b-navbar-nav class="ml-auto w-50">
        <b-nav-form class="mw-100" @submit.prevent="">
          <b-form-input class="mw-100" 
                        placeholder="검색" 
                        v-model="keyword"
                        @keydown="inputKeyDown">
          </b-form-input>
        </b-nav-form>
        <div v-if="suggestions.length" class="auto_suggestion">
        <div v-for="(suggestion, i) in suggestions" 
            :key="i" 
            @click="selectSuggestion(suggestion)" 
            class="auto_suggestion-item">
          <!-- 이미지를 불러와서 GPS 아이콘으로 표시. -->
          <b-img :src="require('@/assets/images/marker_place_on.png')" class="mr-2 gps-icon" alt="GPS Icon"></b-img>
          <!-- 제안된 장소의 이름을 표시. -->
          {{ suggestion.name }}
          <!-- 제안된 장소의 주소를 작은 글씨로 표시. -->
          <div class="small">{{ suggestion.address }}</div>
        </div>
      </div>
      </b-navbar-nav>
      
      <b-nav pills class="ml-auto">
        <b-nav-item size="sm" :active="gnb === 'map'"  @click="clickGnb('map')" href="/">지도</b-nav-item>
        <b-nav-item size="sm" :active="gnb === 'list'" @click="clickGnb('list')" href="/list">목록</b-nav-item>
      </b-nav>

      <!--b-navbar-nav class="ml-auto">
        <b-nav-item href="#">로그인</b-nav-item>
      </b-navbar-nav-->
      
      <b-sidebar id="sidebar-1" shadow>
        <div class="px-3 py-2">
          
        </div>
      </b-sidebar>
    </b-navbar>
  </div>
</template>
<script>

import {mapMutations, mapState} from 'vuex';
import placeService from '../service/place/placeService';

export default {
  data() {
    return {
      keyword: "",
      suggestions: [] // 검색어에 대한 제안 목록을 저장하는 배열
    }
  },
  computed: {
    ...mapState(['gnb']),
  },
  methods: {
    ...mapMutations(['setGnb', 'setPlaceQuery']),

    clickGnb(gnb) {
      this.setGnb(gnb);
    },

    inputKeyDown(e) {
      if (e.which === 13 || e.keyCode === 13) { // 엔터 키 입력시 검색 처리
        // this.setPlaceQuery(this.keyword);
        console.log("search word : " + this.keyword)
      }
    },
    selectSuggestion(suggestion) {
      // 사용자가 제안된 장소를 선택하면 검색창의 키워드를 해당 장소의 이름으로 설정.
      this.keyword = suggestion.name;
      // 선택 이후에는 제안 목록을 초기화.
      this.suggestions = [];
    },
  },
  watch: {
    // 사용자가 검색창에 입력하는 키워드를 관찰.
    keyword(value) {
      // 키워드가 있을 경우,
      if (value) {
        // 쿼리를 설정하고,
        let query = {
          query: value,
          page: 1
        }
  
        // 검색 서비스에 쿼리를 보냄.
        placeService.fetchPlaceList(query)
          .then(documents => {
            // 검색 결과를 받아서 제안 목록에 저장.
            this.suggestions = documents; // 전체 documents를 저장
          })
          .catch(err => {
            // 에러가 발생하면 콘솔에 로그를 출력.
            console.log(err);
          });
      } else {
        // 키워드가 없을 경우, 제안 목록을 초기화.
        this.suggestions = [];
      }
    }
  }
};
</script>
<style>
@media only screen and (max-width: 576px) {
  .navbar-brand {
    display: none !important;
  }
}

/* 제안 목록을 포함하는 컨테이너의 스타일을 정의. */
.auto_suggestion {
  border: 1px solid #ccc; /* 테두리 */
  border-radius: 4px; /* 모서리 둥글게 */
  position: absolute; /* 위치 고정 */
  z-index: 99; /* 다른 요소 위에 위치 */
  background-color: white; /* 배경색 */
  width: 100%; /* 너비 */
  top: 100%;  /* 위치: 검색창 아래 */
}

/* 각각의 제안 아이템의 스타일을 정의. */
.auto_suggestion-item {
  padding: 10px; /* 패딩 */
  cursor: pointer; /* 마우스 커서 모양 변경 */
  display: flex; /* 플렉스박스로 레이아웃 */
  align-items: center; /* 아이템들을 중앙 정렬 */
}

/* 제안 아이템의 주소 부분의 스타일을 정의. */
.auto_suggestion-item .small {
  font-size: 0.8rem; /* 글씨 크기 */
  color: #888; /* 글씨 색 */
  margin-left: 24px;  /* 왼쪽 여백 */
}

/* GPS 아이콘의 크기를 정의. */
.gps-icon {
  width: 16px; /* 너비 */
  height: 16px; /* 높이 */
  object-fit: contain; /* 이미지 크기 조정 */
}

/* 마우스 오버(호버) 시 제안 아이템의 배경색을 변경. */
.auto_suggestion-item:hover {
  background-color: #f0f0f0;
}

</style>
