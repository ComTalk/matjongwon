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
  display: flex;
  align-items: center;
  justify-content: center;
  width: 300px;
  height: 50px;
  background-color: white;
  color: black;
  border-radius: 2px;
  border: 2px solid #ccc; /* Set border color to light grey */
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  position: relative;
  left: calc(50% - 200px);
  right: calc(50% - 200px);
  margin-bottom: 10px;
}
</style>