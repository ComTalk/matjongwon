<template>
  <div>
    <KakaoMap 
        @clickMarker="updateStoreCardData"
        @clickMap="resetCardData"
    >
    </KakaoMap>
    <div class="storeCard">
      <StoreSummaryCard v-if="selectedItem != null"
          :name="selectedItem.name"
          :category="selectedItem.category"
          :address="selectedItem.address"
          :openingHours="selectedItem.opening_hours"
          :score_navermap="selectedItem.score_navermap" 
          :score_kakaomap="selectedItem.score_kakaomap"
          :score_googlemap="selectedItem.score_googlemap"
          :menu="selectedItem.menu"
          :url="selectedItem.url"
          :reviews_navermap="selectedItem.reviews_navermap"
          :reviews_kakaomap="selectedItem.reviews_kakaomap"
          :reviews_googlemap="selectedItem.reviews_googlemap"
          :thumbnails="selectedItem.thumbnails"
          :description="selectedItem.description">
      </StoreSummaryCard>
    </div>
  </div>
</template>

<script>
import KakaoMap from "../components/KakaoMap";
import StoreSummaryCard from "../components/StoreSummaryCard";

export default {
  components: {
    KakaoMap,
    StoreSummaryCard
  },
  data() {
    return {
      selectedItem: null
    };
  },
  methods: {
    updateStoreCardData(item) {
      this.selectedItem = item;
    },
    resetCardData() {
      this.selectedItem = null;
    }
  }
};
</script>

<style>
.storeCard {
  position: fixed;
  bottom : 0;
  margin:20px;
  z-index: 100
}
</style>