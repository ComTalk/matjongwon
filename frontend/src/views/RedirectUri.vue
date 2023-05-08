<template>
  <h1>로그인 중입니다 ...</h1>
</template>

<script>
import axios from "axios";

export default {
  mounted() {
    if (this.$route.query.code) {
      this.kakao_login_with_backend(this.$route.query.code);
    }
  },
  data() {
    return {};
  },
  methods: {
    kakao_login_with_backend(authorization_code) {
      axios.get('/login/kakao_callback', {
        params : {
          'code' : authorization_code
        }
      }).then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });      
      this.$router.replace('/');
    }
  }
};
</script>
