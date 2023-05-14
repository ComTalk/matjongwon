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
        <b-nav-item v-b-toggle.sidebar-right-login v-if="!isLogin">로그인</b-nav-item>
        <b-nav-item v-b-toggle.sidebar-right-logout v-else>MY</b-nav-item>
        <b-sidebar id="sidebar-right-login" title="소셜로그인" right shadow>
          <div class="px-3 py-2">
            <p>로그인을 하시면 원하는 식당을 저장할 수 있어요.</p>
            <img src="../assets/images/naver_logo.png" width="60px" style="cursor:pointer" />
            <img
              src="../assets/images/kakao_logo.png"
              width="60px"
              style="cursor:pointer"
              @click="kakaoLogin()"
            />
            <img src="../assets/images/google_logo.png" width="60px" style="cursor:pointer" />
          </div>
        </b-sidebar>
        <b-sidebar id="sidebar-right-logout" title="프로필" right shadow>
          <div class="px-3 py-2">
            <p>내 정보</p>
            <div>
             <img :src='localStorageImageUrl' width="150px" class="center"/>
            </div>
            <p></p>
            <button @click="kakaoLogout()">로그아웃</button>
          </div>
        </b-sidebar>
      </b-nav>
    </b-navbar>
  </div>
</template>
<script>
import { mapMutations, mapState, mapActions } from "vuex";

export default {
  data() {
    return {
      keyword: ""
    };
  },
  computed: {
    ...mapState(["gnb", "stateLogin"]),

    isLogin() {
      if (localStorage.getItem("user_id")) return true;
      return false;
    },
    localStorageImageUrl() {
      const profile_image = localStorage.getItem('profile_image');
      return profile_image
    }
  },
  methods: {
    ...mapMutations(["setGnb", "setPlaceQuery", "setUserId"]),
    ...mapActions(["doLogin", "doLogout"]),

    clickGnb(gnb) {
      this.setGnb(gnb);
    },

    kakaoLogin() {
      const params = {
        redirectUri: "http://localhost:8000/oauth/kakao/authorize"
      };
      Kakao.Auth.authorize(params);
    },

    kakaoLogout() {
      if (!Kakao.Auth.getAccessToken()) {
        console.log("Not logged in.");
      } else {
        Kakao.Auth.logout(function() {
          alert("로그아웃 되었습니다.", Kakao.Auth.getAccessToken());
        });
        localStorage.clear();
        window.location.reload();
      }
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
