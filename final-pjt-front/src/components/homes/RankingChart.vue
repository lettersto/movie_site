<template>
  <div>
      <ol>
        <li v-for="movie in movieRank" :key="movie.id">
          <router-link 
          :to="{ name: 'movies', params: {moviePk: movie.id} }">
          {{ movie.title }}
          </router-link>
          {{ movie.vote_average }}
        </li>
      </ol>  
  <!-- <div class="d-flex">
    <ranking-chart-item class="flex-grow-1" />
    <ranking-chart-item class="flex-grow-1" />
    <ranking-chart-item class="flex-grow-1" />
  </div> -->
</div>
</template>

<script>
// import RankingChartItem from './RankingchartItem.vue'
import { mapActions, mapGetters } from 'vuex'
import _ from 'lodash'

  export default {
    name: 'RankingChart',
    components: {
      // RankingChartItem
    },
    computed: {
      ...mapGetters(['movies']),
      movieRank(){
        return _.orderBy(this.movies, 'vote_average', 'desc').slice(0, 3)
      }
    },
    methods: {
      ...mapActions(['fetchMovies'])
    },
    created() {
      this.fetchMovies()
    },
  }
</script>

<style>

</style>