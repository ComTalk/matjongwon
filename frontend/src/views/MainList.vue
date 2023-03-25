<template>
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
</template>

<script>
import StoreCard from "../components/StoreCard";
import placeService from "../service/place/placeService";

export default {
  components: {
    StoreCard,
  },
  methods: {
    async fetchPlaceList() {
        try{
            this.stores = await placeService.fetchPlaceList();
        } catch(e) {
            alert(e);
        }
    },
  },
  mounted() {
    this.fetchPlaceList();
  },
  data() {
    return {
      stores: [],
    };
  },
};
</script>
