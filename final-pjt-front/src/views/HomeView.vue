<template>
  <div>
    <event-carossel/>
    <ranking-chart />
    <weather-rec />
    <time-rec />
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
