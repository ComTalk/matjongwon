<template>
  <div>
    <b-card-group>
        <StoreCard
                v-for="(item, i) in stores" :key="i"
                :name="item.name"
                :category="item.category"
                :address="item.address"
                :openingHours="item.opening_hours"
                :score_navermap="item.score_navermap"
                :score_kakaomap="item.score_kakaomap"
                :score_googlemap="item.score_googlemap"
                :menu="item.menu"
                :url="item.url"
                :reviews_navermap="item.reviews_navermap"
                :reviews_kakaomap="item.reviews_kakaomap"
                :reviews_googlemap="item.reviews_googlemap"
                :thumbnails="item.thumbnails"
                :description="item.description"
        >
        </StoreCard>
    </b-card-group>
    <infinite-loading @infinite="infiniteHandler" :identifier="infiniteId">
      <div slot="no-more"></div>
    </infinite-loading>
  </div>
</template>

<script>
import StoreCard from "../components/StoreCard";
import placeService from "../service/place/placeService";
import infiniteLoading from 'vue-infinite-loading';

export default {
  components: {
    StoreCard,
    infiniteLoading
  },
  data() {
    return {
      stores: [],
      page: 1,
      query: "",
      infiniteId: +new Date(),
    };
  },
  mounted() {
    let that = this;
    // 상단 검색창 입력값 변경 감시
    this.$store.subscribe((mutation, state) => {
      if (mutation.type === 'setPlaceQuery') {
        that.query = mutation.payload;
        that.stores = [];
        that.page = 1;
        that.infiniteId += 1;
      }
    });
  },
  methods: {
    async fetchPlaceList() {
      try{
        let query = {
          query: this.query,
          page: this.page
        }
        return await placeService.fetchPlaceList(query);
      } catch(e) {
        alert(e);
      }
    },
    async infiniteHandler($state) {
      console.log("test");
      let placeList = await this.fetchPlaceList();
      if (placeList.length) {
        this.page++;
        this.stores.push(...placeList);
        $state.loaded();
      } else {
        $state.complete();
       }
    },
  },
};
</script>
