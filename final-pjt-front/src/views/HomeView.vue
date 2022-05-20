<template>
  <div>
    <div class="container">
      <event-carossel class="row" />
      <ranking-chart class="row" />
      <weather-rec class="row" />
      <time-rec class="row" />
    </div>
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
      TimeRec
    }

  }
</script>

<style scoped>
  .container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100vh;
    
  }

  /* .row {
    background-color: rgb(197, 255, 255);
  } */


</style>
