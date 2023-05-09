<template>
  <div>
    <!-- Your other template code here -->
    <GoogleLogin />
    <GithubLogin></GithubLogin>
    <button class="button" button @click="logout">Logout</button>
  </div>
</template>

<script>
import GoogleLogin from './GoogleLogin.vue';
import GithubLogin from './GithubLogin.vue';

export default {
  components: {
    GoogleLogin,
    GithubLogin
  },
  methods:{
    logout() {
    if (localStorage.getItem('idToken') || sessionStorage.getItem('idToken')) {
      localStorage.removeItem('idToken');
      sessionStorage.removeItem('idToken');
      
      // Call a function to reset the application state
      this.resetAppState();

      console.log("Logged out.");
    } else {
      console.log("No ID token found. User is not logged in.");
    }
  },
  resetAppState() {
    // Clear user-specific data (replace this with your own logic)
    // this.$store.commit('clearUserData');

    // Refresh the current page
    window.location.reload();
  },
  }
};
</script>

<style scoped>
    .button {
        list-style: none; width: 400px;
        margin: 0 !important;
        position: relative;
        left: calc(50% - 200px); right: calc(50% - 200px);
    }
</style>