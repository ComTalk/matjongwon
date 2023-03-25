<template>
  <div id="kakaomap"></div>
</template>

<script>

import placeService from "../service/place/placeService";

// https://goodteacher.tistory.com/432
export default {
  name: "KakaoMap",
  data() {
    return {
      kakaomap: null,
      stores: [],
      positions: [],
      markers: [],
      infowindows: [],
      markerOnImage: null,
      markerOffImage: null
    };
  },
  mounted() {
    window.kakao && window.kakao.maps ? this.initMap() : this.addKakaoMapSdk();
    this.fetchPlaceList()
        .then(() => this.redrawMarker);
  },
  methods: {
    initMap() {
      let that = this;
      const container = document.getElementById("kakaomap");
      const options = {
        center: new kakao.maps.LatLng(37.498095, 127.027610, 16),
        level: 5,
      };
      this.kakaomap = new kakao.maps.Map(container, options);
      kakao.maps.event.addListener(this.kakaomap, 'click', function() {
        that.closeAllWindows();
      });
      this.createMarkerImage();
    },
    addKakaoMapSdk() {
      const script = document.createElement("script");
      script.src = "//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=a82e397860bdddf2149271fcc898e75a";
      script.onload = () => kakao.maps.load(this.initMap);
      document.head.appendChild(script);
    },
    closeAllWindows() {
      let that = this;
      this.infowindows.forEach((info, i) => {
        info.close();
        that.markers[i].setImage(that.markerOffImage);
      });
    },
    createMarkerImage() {
      const imageOffSrc = require(`@/assets/images/marker_place_off.png`); 
      const imageOnSrc = require(`@/assets/images/marker_place_on.png`); 
      this.markerOffImage = new kakao.maps.MarkerImage(imageOffSrc, new kakao.maps.Size(16, 22));
      this.markerOnImage = new kakao.maps.MarkerImage(imageOnSrc, new kakao.maps.Size(32, 44));
    },
    async fetchPlaceList() {
        try{
            this.stores = await placeService.fetchPlaceList();
            this.stores.forEach(store => {
              this.positions.push({
                title: store.name,
                latlng: new kakao.maps.LatLng(store.coordinates_latitude, store.coordinates_longitude)
              })
            });
        } catch(e) {
        }
    },
  },
  computed: {
    // https://apis.map.kakao.com/web/sample/basicMarker/
    redrawMarker() {
      let that = this;
      let kakaomap = this.kakaomap;

      this.positions.forEach(pos => {
        let marker = new kakao.maps.Marker({
          map: kakaomap,
          position: pos.latlng,
          title: pos.title, 
          image: that.markerOffImage,
        });

        let infowindow = new kakao.maps.InfoWindow({
          content: "<div style='padding:5px;'>" + pos.title + "</div>",
          position: pos.latlng,
          removable : true
        });

        this.markers.push(marker);
        this.infowindows.push(infowindow);
      });

      this.markers.forEach((marker, i) => {
        kakao.maps.event.addListener(marker, 'click', function() {
          that.closeAllWindows();
          marker.setImage(that.markerOnImage);
          that.infowindows[i].open(kakaomap, marker);
        });
      });
    },
  }
};
</script>
<style>
#kakaomap {
  width: 100%;
  height: 1000px;
}
</style>
