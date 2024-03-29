// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from "./App.vue";
import router from "./router";
import BootstrapVue from 'bootstrap-vue'
import axios from "axios";
import store from './store';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import AxiosPlugin from 'vue-axios-cors';

Vue.use(AxiosPlugin);

axios.defaults.baseURL = process.env.VUE_API_HOST;

Vue.config.productionTip = false

Vue.use(BootstrapVue)

/* eslint-disable no-new */
new Vue({
  render: h => h(App),
  store,
  router
}).$mount('#app')