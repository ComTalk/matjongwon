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
      <b-card-body >
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
        <b-card-text>
          {{ getDescriptions }}
        </b-card-text>
        <a :href="reviews_navermap" class="card-link">네이버 리뷰</a>
        <a :href="reviews_kakaomap" class="card-link">카카오 리뷰</a>
        <a :href="reviews_googlemap" class="card-link">구글 리뷰</a>
      </b-card-body>
      <b-list-group flush>
        <b-list-group-item>{{ address }}</b-list-group-item>
        <b-list-group-item>{{ menu }}</b-list-group-item>
      </b-list-group>
    </b-card>
  </div>
</template>

<script>
import LikeButton from "./LikeButton.vue"

export default {
  name: "StoreCard",
  components: {
    LikeButton
  },
  props: {
    name: {type: String},
    category: {type: String},
    description: {type: String},
    address: {type: String},
    openingHours: {type: String},
    score_navermap: {type: String},
    score_kakaomap: {type: String},
    score_googlemap: {type: String},
    menu: {type: String},
    thumbnails: {type: String},
    url: {type: String},
    reviews_navermap: {type: String},
    reviews_kakaomap: {type: String},
    reviews_googlemap: {type: String},
  },
  computed: {
    getDescriptions() {
      if (this.description) {
        return this.description.substring(1,70) + "...";
      }
      return "";
    },
    getThumbnails() {
      return this.thumbnails.split(",");
    }
  },
  data() {
    return {
    };
  },
}
</script>

<style></style>