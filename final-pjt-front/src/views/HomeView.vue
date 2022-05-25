<template>
  <div>
    <event-carossel/>
    <ranking-chart />
    <!-- <weather-rec v-if="isMovie" /> -->
    <!-- <time-rec /> -->
  </div>
</template>

<script>
  import EventCarossel from '@/components/homes/EventCarossel.vue'
  import RankingChart from '@/components/homes/RankingChart.vue'
  // import WeatherRec from '@/components/homes/WeatherRec.vue'
  // import TimeRec from '@/components/homes/TimeRec.vue'
  import { mapGetters } from 'vuex'


  export default {
    name: 'HomeView',
    components: {
      EventCarossel,
      RankingChart,
      // WeatherRec,
      // TimeRec,
    },
    computed: {
      ...mapGetters(['isMovie'])
    }

  }
</script>

<style scoped>


</style>
