<template>
  <div class="d-flex justify-content-between">
    <div class="leaderboard flex-grow-1 card">
    <div class="leaderboard_header card-title">
      <h3>
      <i class="material-icons">hotel_class</i>
      BEST RATING MOVIE
      </h3></div>
    <div class="leaderboard_content card-content">
    <ul>
      <li v-for="movie in movieRank" :key="movie.id">
        <div class="name">
        <router-link class="header"
        :to="{ name: 'movies', params: {moviePk: movie.id} }">
        {{ movie.title }}
        </router-link>
        <span class="stat">{{ movie.vote_average }}</span>
        </div>
      </li>
    </ul>
    </div>
    </div>
    <div class="leaderboard flex-grow-1 card">
      <div class="leaderboard_header card-title">
      <h3>
      <i class="material-icons">hotel_class</i>
      NEW MOVIE
      </h3></div>
      <div class="leaderboard_content card-content">
      <ul>
      <li v-for="movie in movieNewRank" :key="movie.id">
        <div class="name">
        <router-link class="header"
        :to="{ name: 'movies', params: {moviePk: movie.id} }">
        {{ movie.title }}
        </router-link>
        <br/>
        <span class="date">{{ movie.release_date }}</span>
        </div>
      </li>
      </ul>
      </div>
      </div>
    <div class="leaderboard flex-grow-1 card">
      <div class="leaderboard_header card-title">
      <h3>
      <i class="material-icons">hotel_class</i>
      HOT TOPIC
      </h3></div>
      <div class="leaderboard_content card-content">
    <ul>
      <li v-for="article in articleRank" :key="article.pk">
        <div class="name">
        <router-link class="header"
        :to="{ name: 'articleDetail', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
        </div>
      </li>
    </ul>
    </div>
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
      movieNewRank(){
        return _.orderBy(this.movies, 'release_date', 'desc').slice(0, 3)
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

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Montserrat:400,700");
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

body,
html {
  min-width: 100%;
  min-height: 100%;
  width: 100%;
  height: 100%;
  background: #f9f9f9;
  font-family: "Montserrat", sans-serif;
}
.leaderboard {
  max-width: 430px;
  position: relative;

}
.leaderboard .leaderboard_header {
  border-top-left-radius: 7px;
  border-top-right-radius: 7px;
  background: #c9ccd7;
  padding: 15px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 50px;
}

.leaderboard .leaderboard_header h3 {
  color: #0d132a;
  font-size: 16px;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 2px;
}

.leaderboard .leaderboard_content {
  background: #fff;
  padding: 10px;
}
.leaderboard .leaderboard_content ul {
  list-style: none;
  padding-left: 0;
  
  
}
.leaderboard .leaderboard_content ul li {
  cursor: pointer;
  background: #fefefe;
  padding: 10px 5px;
  border-radius: 5px;
  box-shadow: 0px 0px 10px 1px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: transform 0.1s ease-in-out;
  z-index: 4;
  width: 100%;
  height: 50px;
}
.leaderboard .leaderboard_content ul li:hover {
  z-index: 5;
  transform: scale(1.3);
  box-shadow: 0px 0px 16px 13px rgba(0, 0, 0, 0.1);
}
.leaderboard .leaderboard_content ul li:not(:last-child) {
  margin-bottom: 10px;
}

.leaderboard .leaderboard_content ul li .name span {
  vertical-align: middle;
  padding-left: 10px;
}
.leaderboard .leaderboard_content ul li .name .header {
  color: #979cb0;
  font-weight: 700;
  margin-right: 15px;
  vertical-align: middle;
  text-decoration: none;
  padding-left: 10px;
}
.leaderboard .leaderboard_content ul li .name span.stat {
  color: #35d8ac;
  font-weight: 700;
  font-size: 25px;
}
.leaderboard .leaderboard_content ul li .name span.date {
  color: #35d8ac;
  font-weight: 800;
  font-size: 12px;
  text-align: right;
}
</style>