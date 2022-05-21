<template>
  <div class="d-flex">
    <ranking-chart-item class="flex-grow-1" />
    <ranking-chart-item class="flex-grow-1" />
    <ranking-chart-item class="flex-grow-1" />
  </div>
</template>

<script>
import RankingChartItem from './RankingchartItem.vue'

  export default {
    name: 'RankingChart',
    components: {
      RankingChartItem
    }
  }
</script>

<style>

</style>