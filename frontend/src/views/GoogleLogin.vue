<template>
  <div>
    <div ref="googleLoginBtn"></div>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
import jwtDecode from "jwt-decode";

export default {
  mounted() {
    if (!sessionStorage.getItem("idToken")) {
    this.loadGsiLibrary()
      .then(() => {
        const gClientId = "client_id";
        window.google.accounts.id.initialize({
          client_id: gClientId,
          callback: this.handleCredentialResponse,
          auto_select: true,
        });
        google.accounts.id.prompt();
        window.google.accounts.id.renderButton(this.$refs.googleLoginBtn, {
          text: "signin_with",
          size: "large",
          width: "366",
          theme: "outline",
          logo_alignment: "left",
        });
      })
      .catch((error) => {
        console.error("Failed to load Google Identity Services library", error);
      });
    }
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
    async handleCredentialResponse(response) {
      // console.log(response.credential);
      // Put your backend code in here

      const idToken = response.credential;
      console.log("ID Token: " + idToken);

      // Store the ID token in localStorage
      sessionStorage.setItem('idToken', idToken);

      const responsePayload = jwtDecode(idToken);

      console.log("ID: " + responsePayload.sub);
      console.log('Full Name: ' + responsePayload.name);
      console.log('Given Name: ' + responsePayload.given_name);
      console.log('Family Name: ' + responsePayload.family_name);
      console.log("Image URL: " + responsePayload.picture);
      console.log("Email: " + responsePayload.email);
    },
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
  },
};
</script>
