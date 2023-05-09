<template>
  <div>
    <div ref="googleLoginBtn"></div>
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
    }
  },
};
</script>
