<template>
    <div>
        <h1>GITHUBLOGIN</h1>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  created() {
    const code = this.$route.query.code;
    if (code) {
        const Uri = 'http://localhost:8000/auth/github/token';
        const redirectUri = 'http://localhost:3000/login/callback/github';
        axios
        .post(Uri, { 
            code: code,
            clientId : process.env.GITHUB_CLIENT_ID,
            clientSecret: process.env.GITHUB_CLIENT_SECRET,
            redirectUri : redirectUri
        })
        .then((response) => {

            console.log(response.data);

            const { access_token } = response.data;

            // Send the access token to the parent window
            window.opener.postMessage({ access_token }, window.location.origin);
            // Close the current window
            window.close();

        })
        .catch((error) => {
            console.error("Error while exchanging GitHub code for access token:", error);
            // Redirect to a different route or show an error message if needed.
            this.$router.push("/login");
        });
    } else {
        // Redirect to a different route or show an error message if the code is missing.
        this.$router.push("/login");
    }
  },
};
</script>
