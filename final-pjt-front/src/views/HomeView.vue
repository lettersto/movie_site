<template>
  <div>
    <event-carossel/>
    <!-- <div class="container">
      <event-carossel class="carousel">
        <slide-items v-for="(slide, index) in carouselSlides" :key="index">
          <div class="slide-info">
            {{slide}}
            <img :src=slide :alt="'img-' + index">
          </div>
        </slide-items>
        
      </event-carossel> -->
    <ranking-chart />
    <weather-rec />
    <time-rec />
    <!-- </div> -->
  </div>
</template>

<script>
  import EventCarossel from '@/components/homes/EventCarossel.vue'
  import RankingChart from '@/components/homes/RankingChart.vue'
  import WeatherRec from '@/components/homes/WeatherRec.vue'
  import TimeRec from '@/components/homes/TimeRec.vue'


  export default {
    name: 'HomeView',
    components: {
      EventCarossel,
      RankingChart,
      WeatherRec,
      TimeRec,
    },
    data() {
      return {

      }
    }

  }
</script>

<style scoped>


</style>
