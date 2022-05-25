<template>
  <div>
    <div class="chart-wrapper row mb-4">
      <!-- Best Rating -->
      <div class="chart-container col-md-8 col-lg-4">
        <h3 class="chart-title title-box">BEST RATING</h3>
        <div class="chart-box" v-for="movie in movieRank" :key="movie.id">
          <router-link class="chart-link"
            :to="{ name: 'movies', params: {moviePk: movie.id} }">
            <div class="chart-content">
              <div class="chart-text">
                <h6 class="chart-title">{{ movie.title }}</h6>
              </div>
              <div class="chart-icon">{{ movie.vote_average }}</div>
            </div>
          </router-link>
        </div>
      </div>
      <!-- New Movie -->
      <div class="chart-container col-md-8 col-lg-4">
        <h3 class="chart-title title-box">NEW MOVIE</h3>
        <div class="chart-box" v-for="movie in movieNewRank" :key="movie.id">
          <router-link class="chart-link"
            :to="{ name: 'movies', params: {moviePk: movie.id} }">
            <div class="chart-content">
              <div class="chart-text">
                <h6 class="chart-title">{{ movie.title }}</h6>
              </div>
            </div>
          </router-link>
            <!-- <div class="chart-icon">{{ movie.release_date }}</div> -->
        </div>
      </div>
      <div class="chart-container col-md-8 col-lg-4">
        <h3 class="chart-title title-box">HOT TOPIC</h3>
        <div class="chart-box" v-for="article in articleRank" :key="article.pk">
          <router-link class="chart-link"
            :to="{ name: 'articleDetail', params: { articlePk: article.pk } }">
            <div class="chart-content">
              <div class="chart-text">
                <h6 class="chart-title">{{ article.title }}</h6>
              </div>
              <div class="chart-icon">{{ article.like_count }}</div>
            </div>
          </router-link>
        </div>
      </div>
    </div>

    <!-- <hr> -->
    <!-- 구분선 -->

    <!-- <div class="d-flex justify-content-between">
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
  </div> -->

  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import _ from 'lodash'

  export default {
    name: 'RankingChart',
    computed: {
      ...mapGetters(['movies', 'articles']),
      movieRank(){
        return _.orderBy(this.movies, 'vote_average', 'desc').slice(0, 5)
      },
      movieNewRank(){
        return _.orderBy(this.movies, 'release_date', 'desc').slice(0, 5)
      },
      articleRank() {
        return _.orderBy(this.articles, ['like_count', 'view_count', 'comment_count'], ['desc', 'desc', 'desc']).slice(0, 5)
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
  @import url('https://fonts.googleapis.com/css2?family=Montserrat&family=Noto+Sans+KR&display=swap');

  * {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: "Montserrat", sans-serif;
  }

  .chart-wrapper {
    display: flex;
    justify-content: space-around;
  }

  .chart-container {
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 5px;
    padding: 10px;
    width: 90%;
    color: #272D2D;
  }

  @media (min-width: 992px) {
    .chart-container {
      width: 33% !important;
    }
  }

  @media (min-width: 768px) {
    .chart-container {
      width: 230px;
    }
  }

  .chart-content {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-left: 1em;
    width: 90%;
  }

  .chart-title {
    margin-top: 2.5px;
    font-weight: bold;
  }

  .title-box {
    text-align: center;
  }

  .chart-container .chart-box {
    position: relative;
    /* height: 40px; */
    height: auto;
    max-height: 50px;
    width: 100%;
    padding: 5px 0;
    background: rgb(255, 255, 255);
    cursor: pointer;
    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(84, 84, 84, 0.1);
    border-radius: 5px;
    transition: 0.3s;
  }

  .chart-container .chart-box:hover {
    transform: scale(1.01);
    color:#f9fcfe;
  }

  .chart-container .chart-box::before {
    content: "";
    position: absolute;
    width: 6px;
    height: 100%;
    bottom: -.1px;
    left: -.5px;
    background: #B8C5D6;
    transition: 0.3s ease-in-out;
  }

  .chart-container .chart-box:hover::before {
    width: 100%;
  }

  .chart-container .chart-box .chart-content {
    position: relative;
    display: flex;
    align-items: center;
    height: 100%;
  }

  .chart-container .chart-box .chart-content .chart-icon {
    padding: 1px 8px;
    font-size: 16px;
    font-weight: bold;
    color: #f9fcfe;
    background-color: #B8C5D6;
    border-radius: 7px;
  }

  .chart-link {
    text-decoration: none;
    color: #272D2D;
  }



  /* body,
  html {
    min-width: 100%;
    min-height: 100%;
    width: 100%;
    height: 100%;
    background: #f9f9f9;
    font-family: "Montserrat", sans-serif;
  } */
  /* .leaderboard {
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
  } */
</style>