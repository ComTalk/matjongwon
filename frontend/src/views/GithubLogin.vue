<!-- src/components/GithubLogin.vue -->
<template>
    <div>
        <button class="button" @click="loginWithGithub">
        <img class="image" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo" width="20" height="20" />
        Login with GitHub
        </button>
    </div>
</template>
  
  <script>
  import axios from 'axios';
  
  export default {
    methods: {
      async loginWithGithub() {
        const clientId = process.env.GITHUB_CLIENT_ID;
        const redirectUri = 'http://localhost:3000/login/callback/github';
        const scope = 'user'; // Request the 'user' scope for the logged-in user's profile information
  
        const authUrl = `https://github.com/login/oauth/authorize?client_id=${clientId}&redirect_uri=${encodeURIComponent(redirectUri)}&scope=${scope}`;
  
        // Open the GitHub OAuth login in a new window
        const authWindow = window.open(authUrl, 'githubAuth', 'width=600,height=600');

        window.addEventListener('message', (event) => {
            if (event.origin !== window.location.origin) return;
            
            // Close the GitHub OAuth login window
            authWindow.close();
            
            // Get the access token from the event data
            const { access_token } = event.data;

            // Save the access token in sessionStorage
            sessionStorage.setItem('idToken', access_token);

            // Fetch the GitHub profile information
            this.fetchGithubProfile(access_token);

        }, false);
      },
      async fetchGithubProfile(access_token) {
        const profileResponse = await axios.get('https://api.github.com/user', {
        headers: {
            'Authorization': `token ${access_token}`,
        },
        });
        // console.log('GitHub profile:', profileResponse.data);

        const profileData = profileResponse.data;

        // console.log(profileData)

        console.log("ID: " + profileData.id);
        console.log("Full Name: " + profileData.name);
        console.log("Login: " + profileData.login); // GitHub doesn't provide given_name and family_name; using login instead
        console.log("Avatar URL: " + profileData.avatar_url);
        console.log("Email: " + profileData.email);
    },
    },
  };
  </script>
  
  <style scoped>
.login-prompt {
  display: flex;
  justify-content: center;
  
}

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