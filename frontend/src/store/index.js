import Vue from 'vue';
import Vuex from 'vuex';


Vue.use(Vuex);

export default new Vuex.Store({
  // 글로벌 영역 상태값.
  state: {
     gnb: '', // 선택중인 GNB
     placeQuery: '', // 상단 검색창 검색어
     stateLogin: false, 
     user : null
  },

  mutations: {
    /**
     * GNB를 선택하는 메소드
     *
     * @param state 저장소
     * @param id 선택된 template type
     */
    setGnb(state, id) {
      state.gnb = id;
    },

    setPlaceQuery(state, placeQuery) {
      state.placeQuery = placeQuery;
    },

    setLogin(state, user) {
      state.stateLogin = true;
      state.user = user;
    },

    setLogout(state) {
      state.stateLogin = false; 
      state.user = null;
    }
  },
  actions : {
    doLogin({commit}, user) {
      commit ('setLogin', user);
    }, 
    doLogout({commit}) {
      commit ('setLogout');
    }
  },
  getters : {
    stateLogin : state => state.stateLogin,
    user : state => state.user
  }
});
