<template>
  <div>
    <b-navbar toggleable="sm" variant="light">
      <b-navbar-toggle target="sidebar-1" v-b-toggle.sidebar-1></b-navbar-toggle>

      <b-navbar-brand href="/">맛종원</b-navbar-brand>

      <b-navbar-nav class="ml-auto w-50">
        <b-nav-form class="mw-100" @submit.prevent>
          <b-form-input class="mw-100" placeholder="검색" v-model="keyword" @keydown="inputKeyDown"></b-form-input>
        </b-nav-form>
      </b-navbar-nav>

      <b-nav pills class="ml-auto">
        <b-nav-item size="sm" :active="gnb === 'map'" @click="clickGnb('map')" href="/">지도</b-nav-item>
        <b-nav-item size="sm" :active="gnb === 'list'" @click="clickGnb('list')" href="/list">목록</b-nav-item>
        <b-nav-item v-b-toggle.sidebar-right>로그인</b-nav-item>
        <b-sidebar id="sidebar-right" title="소셜로그인" right shadow>
          <div class="px-3 py-2">
            <p>
              로그인을 하시면 원하는 식당을 저장할 수 있어요. 
            </p>
            <img src="../assets/images/naver_logo.png" width="60px"/>
            <img src="../assets/images/kakao_logo.png" width="60px" @click="kakaoLogin()"/>
            <img src="../assets/images/google_logo.png" width="60px"/>
          </div>
        </b-sidebar>
      </b-nav>

      <b-sidebar id="sidebar-1" shadow>
        <div class="px-3 py-2"></div>
      </b-sidebar>
    </b-navbar>
  </div>
</template>
<script>
import { mapMutations, mapState } from "vuex";

export default {
  data() {
    return {
      keyword: ""
    };
  },
  computed: {
    ...mapState(["gnb"])
  },
  methods: {
    ...mapMutations(["setGnb", "setPlaceQuery"]),

    clickGnb(gnb) {
      this.setGnb(gnb);
    },

    kakaoLogin() {
      const params = {
        redirectUri: "http://localhost:8080/oauth/kakao/callback"
      };
      Kakao.Auth.authorize(params);
    },

    inputKeyDown(e) {
      if (e.which === 13 || e.keyCode === 13) {
        // 엔터 키 입력시 검색 처리
        this.setPlaceQuery(this.keyword);
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
</style>
