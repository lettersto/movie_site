<template>
  <div>
    <event-carossel/>
    <ranking-chart />
    <weather-rec v-if="isMovie" class="row d-flex justify-content-center weather-box" />
    <time-rec class="row d-flex justify-content-center time-box" />
  </div>
</template>

<script>
  import EventCarossel from '@/components/homes/EventCarossel.vue'
  import RankingChart from '@/components/homes/RankingChart.vue'
  import WeatherRec from '@/components/homes/WeatherRec.vue'
  import TimeRec from '@/components/homes/TimeRec.vue'
  import { mapGetters } from 'vuex'


  export default {
    name: 'HomeView',
    components: {
      EventCarossel,
      RankingChart,
      WeatherRec,
      TimeRec,
    },
    computed: {
      ...mapGetters(['isMovie'])
    }

  }
</script>

<style scoped>

 .weather-box, .time-box {
  background-color: #ffffff;
  padding: 2em 8px;
  border: 1px solid rgba(84, 84, 84, 0.1);
  box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.1);
  border-radius: 20px;
 }

</style>
