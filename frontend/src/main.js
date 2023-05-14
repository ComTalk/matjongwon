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
Vue.use(BootstrapVue)
Vue.config.productionTip = false

axios.defaults.baseURL = process.env.VUE_API_HOST;
Kakao.init("c5d2f854b236f050858192c2763f47f7"); // 초기화

/* eslint-disable no-new */
new Vue({
  render: h => h(App),
  store,
  router
}).$mount('#app')
