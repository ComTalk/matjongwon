<template>
  <div>
    <b-card no-body class="overflow-hidden" style="max-width: 540px;" :href="url">
      <b-carousel class="rounded-0"
          controls
          indicators
          :interval="0"
      >
        <b-carousel-slide
          v-for="(item, i) in getThumbnails" :key="i"
          :img-src="item"
        >
        </b-carousel-slide>
      </b-carousel>
      <b-card-body @click="goUrl">
        <b-card-title>
          {{ name }}
          <like-button />
        </b-card-title>
        <b-card-sub-title>
          {{ category }}
          <b-img :width="20" :height="20" :src="require(`@/assets/images/kakaomap_icon.png`)" v-if="score_kakaomap"></b-img><span>{{ score_kakaomap }}</span>
          <b-img :width="20" :height="20" :src="require(`@/assets/images/navermap_icon.png`)" v-if="score_navermap"></b-img><span>{{ score_navermap }}</span>
          <b-img :width="20" :height="20" :src="require(`@/assets/images/googlemap_icon.png`)" v-if="score_googlemap"></b-img><span>{{ score_googlemap }}</span>
        </b-card-sub-title>
      </b-card-body>
    </b-card>
  </div>
</template>

<script>
import LikeButton from "./LikeButton.vue"

export default {
  name: "StoreSummaryCard",
  components: {
    LikeButton
  },
  props: {
    name: {type: String},
    category: {type: String},
    address: {type: String},
    openingHours: {type: String},
    score_navermap: {type: String},
    score_kakaomap: {type: String},
    score_googlemap: {type: String},
    thumbnails: {type: String},
    url: {type: String},
  },
  computed: {
    getThumbnails() { 
      return this.thumbnails.split(",");
    }
  },
  methods: {
    goUrl() {
      if(this.url)
        window.open(this.url, '_blank');
    }
  }
}
</script>

<style>
</style>