<template>
  <div id="app">
      <router-view name="header"></router-view>
      <main>
          <router-view/>
      </main>
      <router-view name="footer"></router-view>
  </div>
</template>
<script>
export default {
  created() {
    console.log(process.env);
  }
}
</script>
