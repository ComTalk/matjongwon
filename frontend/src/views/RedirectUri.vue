<template>
  <h1>로그인 중입니다 ...</h1>
</template>

<script>
import axios from "axios";
import { mapActions } from "vuex";

export default {
  mounted() {
    console.log("카카오 콜백 프론트 사용자 정보");
    var user_info = {};
    user_info["user_id"] = this.$route.query.user_id;
    user_info["nickname"] = this.$route.query.nickname;
    user_info["profile_image"] = this.$route.query.profile_image;
    user_info["email"] = this.$route.query.email;
    user_info["age_range"] = this.$route.query.age_range;
    user_info["birthday"] = this.$route.query.birthday;
    user_info["access_token"] = this.$route.query.access_token;
    this.kakao_login_front(user_info);
  },
  data() {
    return {};
  },
  methods: {
    ...mapActions(["doLogin"]),

    kakao_login_front(user_info) {
      console.log(user_info.user_id);
      console.log(user_info.nickname);
      console.log(user_info.profile_image);
      console.log(user_info.email);
      console.log(user_info.age_range);
      console.log(user_info.birthday);
      console.log(user_info.access_token);

      localStorage.setItem("user_id", user_info.user_id);
      localStorage.setItem("nickname", user_info.nickname);
      localStorage.setItem(
        "profile_image",
        user_info.profile_image
      );
      localStorage.setItem("email", user_info.email);
      localStorage.setItem("age_range", user_info.age_range);
      localStorage.setItem("birthday", user_info.birthday);
      Kakao.Auth.setAccessToken(user_info.access_token);
      this.$router.push("/");
    }
  }
};
</script>
