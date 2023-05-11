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
          <b-img :src="require('@/assets/images/marker_place_on.png')" class="mr-2 gps-icon" alt="GPS Icon"></b-img>
          {{ suggestion.name }}
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
      suggestions: []
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
      this.keyword = suggestion.name;
      this.suggestions = [];
    },
  },
  watch: {
    keyword(value) {
    if (value) {
      let query = {
        query: value,
        page: 1
      }

      placeService.fetchPlaceList(query)
        .then(documents => {
          this.suggestions = documents; // use the whole document for the suggestion
        })
        .catch(err => {
          console.log(err);
        });
    } else {
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

.auto_suggestion {
  border: 1px solid #ccc;
  border-radius: 4px;
  position: absolute;
  z-index: 99;
  background-color: white;
  width: 100%;
  top: 100%; 
}

.auto_suggestion-item {
  padding: 10px;
  cursor: pointer;
  display: flex;
  align-items: center;
}

.auto_suggestion-item .small {
  font-size: 0.8rem;
  color: #888;
  margin-left: 24px; 
}

.gps-icon {
  width: 16px;
  height: 16px;
  object-fit: contain;
}

.auto_suggestion-item:hover {
  background-color: #f0f0f0;
}

</style>
