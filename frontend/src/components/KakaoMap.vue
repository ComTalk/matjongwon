<template>
  <div id="kakaomap"></div>
</template>

<script>

import {mapState} from 'vuex';
import placeService from "../service/place/placeService";

// https://goodteacher.tistory.com/432
export default {
  name: "KakaoMap",
  data() {
    return {
      curPosition: null,
      kakaomap: null,
      stores: [],
      positions: [],
      markers: [],
      infowindows: [],
      markerOnImage: null,
      markerOffImage: null,
      query: "",
    };
  },
  computed: {
    ...mapState(['placeQuery']),
  },
  mounted() {
    let that = this;
    navigator.geolocation.getCurrentPosition(this.loadCurrentPosSuccess, this.loadKakaoMap);
    
    // 상단 검색창 입력값 변경 감시
    this.$store.subscribe((mutation, state) => {
      if (mutation.type === 'setPlaceQuery') {
        that.query = mutation.payload;
        that.fetchPlaceList()
          .then(() => that.redrawMarker);
      }
    })
  },
  methods: {
    loadCurrentPosSuccess(position) {
      this.curPosition = position;
      this.loadKakaoMap();
    },
    loadKakaoMap() {
      window.kakao && window.kakao.maps ? this.initMap() : this.addKakaoMapSdk();
    },
    initMap() {
      let that = this;
      const container = document.getElementById("kakaomap");
      const initLat = this.curPosition ? this.curPosition.coords.latitude : 37.498095;
      const initLng = this.curPosition ? this.curPosition.coords.longitude : 127.027610;
      const options = {
        center: new kakao.maps.LatLng(initLat, initLng, 16),
        level: 5,
        maxLevel: 7,
      };
      this.kakaomap = new kakao.maps.Map(container, options);
      // 지도 클릭 이벤트
      kakao.maps.event.addListener(this.kakaomap, 'click', function() {
        that.closeAllWindows();
      });
      // 지도 영역 변경 이벤트
      kakao.maps.event.addListener(this.kakaomap, 'dragend', function() {
        that.closeAllWindows();
        that.fetchPlaceList()
          .then(() => that.redrawMarker);
      });
      this.createMarkerImage();
      
      this.fetchPlaceList()
          .then(() => this.redrawMarker);
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
      // 부모 컴포넌트에 클릭 이벤트 전달
      that.$emit('clickMap');
    },
    createMarkerImage() {
      const imageOffSrc = require(`@/assets/images/marker_place_off.png`); 
      const imageOnSrc = require(`@/assets/images/marker_place_on.png`); 
      this.markerOffImage = new kakao.maps.MarkerImage(imageOffSrc, new kakao.maps.Size(16, 22));
      this.markerOnImage = new kakao.maps.MarkerImage(imageOnSrc, new kakao.maps.Size(32, 44));
    },
    markerClickHandler(marker, i) {
      this.closeAllWindows();
      marker.setImage(this.markerOnImage);
      this.infowindows[i].open(this.kakaomap, marker);

      // 부모 컴포넌트에 클릭된 상점 정보 전달
      this.$emit('clickMarker', this.stores[i]);
    },
    async fetchPlaceList() {
        try{
            let bounds = this.kakaomap.getBounds();
            let rect = [
              bounds.getSouthWest().getLng(),
              bounds.getSouthWest().getLat(),
              bounds.getNorthEast().getLng(),
              bounds.getNorthEast().getLat()
            ];

            let query = {
              query: this.query,
              size: 100,
              rect: rect.join(',')
            };
            this.stores = await placeService.fetchPlaceList(query);
            this.positions = [];
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

      // 지도에서 기존 마커 삭제
      this.markers.forEach((marker, i) => {
        marker.setMap(null);
        kakao.maps.event.addListener(marker, 'click', () => that.markerClickHandler(marker, i));
      });

      this.markers = [];
      this.infowindows = [];

      // 좌표기준으로 마커, 인포윈도우 생성
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
        kakao.maps.event.addListener(marker, 'click', () => that.markerClickHandler(marker, i));
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
