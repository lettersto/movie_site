<template>
  <div class="d-flex">
    <div class="flex-grow-1">
    <div>BEST RATING MOVIE</div>
    <ol>
      <li v-for="movie in movieRank" :key="movie.id">
        <router-link 
        :to="{ name: 'movies', params: {moviePk: movie.id} }">
        {{ movie.title }}
        </router-link>
        {{ movie.vote_average }}
      </li>
    </ol>
    </div>
    <div class="flex-grow-1">
      <div>NEW MOVIE</div>
      </div>
    <div class="flex-grow-1">
    <div>HOT TOPIC</div>  
    <ol>
      <li v-for="article in articleRank" :key="article.pk">
        <router-link 
        :to="{ name: 'articleDetail', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ol>
    </div>

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
      ...mapGetters(['movies', 'articles']),
      movieRank(){
        return _.orderBy(this.movies, 'vote_average', 'desc').slice(0, 3)
      },
      articleRank() {
        return _.orderBy(this.articles, ['like_count', 'view_count', 'comment_count'], ['desc', 'desc', 'desc']).slice(0, 3)
      }
    },
    methods: {
      ...mapActions(['fetchMovies', 'fetchArticles'])
    },
    created() {
      this.fetchMovies()
      this.fetchArticles()
    },
  }
</script>

<style>

</style>