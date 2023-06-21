<template>
  <div class="like-button">
    <img :src="getImageSrc" alt="like" @click.stop="handleClick" class="like-img"/>
  </div>
</template>
<script>
import likeService from "../service/like/likeService";

export default {
  name: "like-button",
  props: {
    storeId: String,
    isLike: Boolean
  },
  computed: {
    getImageSrc() {
      if (this.isLike)
        return require(`@/assets/images/like_on.png`);
      return require(`@/assets/images/like_off.png`);
    },
  },
  methods: {
    handleClick() {
      let param = {
        "storeId": this.storeId,
        "like": !this.isLike
      };
      likeService.like(param);
      this.isLike = !this.isLike;
    }
  }
};

</script>
<style>
.like-button {
  width: 40px;
  height: 40px;
  float: right;
}
.like-img {
  width: 100%;
  height: 100%;
}
</style>