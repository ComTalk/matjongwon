<template>
  <div>
    <button class="button" @click="loginWithGoogle">
      <img class="image" src="https://1000logos.net/wp-content/uploads/2016/11/New-Google-Logo-497x500.jpg" alt="Google Logo" width="20" height="20" />
      Login with Google
    </button>
  </div>
</template>

<script>
import jwtDecode from "jwt-decode";

export default {
  mounted() {
    this.loadGsiLibrary()
      .then(() => {
        const gClientId = process.env.GOOGLE_CLIENT_ID;
        window.google.accounts.id.initialize({
          client_id: gClientId,
          callback: this.handleCredentialResponse,
          auto_select: true,
        });
      })
      .catch((error) => {
        console.error("Failed to load Google Identity Services library", error);
      });
  },
  methods: {
    async loadGsiLibrary() {
      return new Promise((resolve, reject) => {
        const script = document.createElement("script");
        script.src = "https://accounts.google.com/gsi/client";
        script.async = true;
        script.defer = true;
        script.onload = () => {
          resolve();
        };
        script.onerror = () => {
          reject(new Error("Failed to load Google Identity Services library"));
        };
        document.body.appendChild(script);
      });
    },
    async loginWithGoogle() {
      window.google.accounts.id.prompt();
    },
    async handleCredentialResponse(response) {
      const idToken = response.credential;
      console.log("ID Token: " + idToken);

      // Store the ID token in sessionStorage
      sessionStorage.setItem('idToken', idToken);

      const responsePayload = jwtDecode(idToken);

      console.log("ID: " + responsePayload.sub);
      console.log('Full Name: ' + responsePayload.name);
      console.log('Given Name: ' + responsePayload.given_name);
      console.log('Family Name: ' + responsePayload.family_name);
      console.log("Image URL: " + responsePayload.picture);
      console.log("Email: " + responsePayload.email);
    }
  },
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
  border: 2px solid #ccc; /* Set border color to light grey */
  border-radius: 2px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  position: relative;
  left: calc(50% - 200px);
  right: calc(50% - 200px);
  margin-top: 10px;
  margin-bottom: 10px;
}

.image {
  width: 20px;
  height: 20px;
  margin-right: 10px;
}

.button:hover {
  background-color: #f5f5f5;
}
</style>
