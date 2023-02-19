// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from "./App.vue";
import router from "./router";
import BootstrapVue from 'bootstrap-vue'
import store from './store';
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import AxiosPlugin from 'vue-axios-cors';

Vue.use(AxiosPlugin);

axios.defaults.headers.common['Content-Type'] = 'application/x-www-form-urlencoded'
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
axios.defaults.baseURL = 'http://localhost:8000';

Vue.config.productionTip = false

Vue.use(BootstrapVue)

/* eslint-disable no-new */
new Vue({
  render: h => h(App),
  store,
  router
}).$mount('#app')