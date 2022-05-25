<template>
  <div v-if="isMovieDetail" class="mt-5">
    <div class="movie-detail-wrapper container">
      <div class="movie-detail-container row">
        <div class="movie-detail-poster col-12 col-lg-6">
          <img :src="movieURL" alt="영화 포스터">
        </div>
        <div class="movie-detail-description col-12 col-lg-6">
          <ul class="movie-detail-list">
            <li class="movie-detail-title">
              <h3>{{ movie.title }} <span class="badge bg-secondary">{{ movie.vote_average }}</span></h3>
            </li>
            <li class="movie-detail-item">
              <span>개봉일: {{ movie.release_date }}</span>
            </li>
            <li class="movie-detail-item">
              <div v-for="director_list in movie.director" :key="director_list.id">
                감독: {{ director_list.name.slice(1, director_list.name.length-1) }}
              </div>
            </li>
            <li class="movie-detail-item">
              <div v-for="actor_list in movie.actor" :key="actor_list.id">
                배우: {{ actor_list.name.slice(1, actor_list.name.length-1) }}
              </div>
            </li>
            <li class="movie-detail-item">
              <p>{{ movie.overview.slice(0, 222) }}...</p>
            </li>
            <li>
              {{ isMovieDetail }}
              {{ movie.title }}
              <youtube-list v-if="isTitle" :title="movie.title" />
              </li>
          </ul>
        </div>
      </div>
    </div>
    <review-list :reviews="movie.reviews" class="mt-5"/>
    
  </div>


</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import ReviewList from '@/components/ReviewList.vue'
  import _ from 'lodash'
  import YoutubeList from '@/components/YoutubeList.vue'
  // import axios from 'axios'

  export default {
    name: 'MovieView.vue',
    components: {
      ReviewList,
      YoutubeList,
    },
    data() {
      return {
        moviePk: this.$route.params.moviePk,
      }
    },
    computed: {
      ...mapGetters(['movie', 'isTitle']),
      movieURL() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_url
      },
      isMovieDetail() {
        return !_.isEmpty(this.movie)
      },

    },
    methods: {
      ...mapActions([
        'fetchMovie',
      ])
    },
    created() {
      this.$store.commit('SET_MOVIE', null)
      this.fetchMovie(this.moviePk)
    },
  }
</script>

<style>
  .movie-detail-wrapper {
    margin: 0 auto;
    width: 90%;
    max-width: 860px;
   
  }

  .movie-detail-container {
    padding: 3em 2.5em;
    background-color: #ffffff;
    border-radius: 1.5em;
    border: 1px solid rgba(62, 62, 62, 0.1);
    box-shadow: 0 20px 40px rgba(125, 125, 125, 0.3);
  }

  .movie-detail-poster > img {
    max-width: 20rem;
    box-shadow: 10px 10px 10px rgba(125, 125, 125, 0.8);
  }

  .movie-detail-poster {
    display: flex;
    justify-content: center;
  }


  @media (max-width: 768px){
    .movie-detail-poster > img {
      max-width: 20rem;
    }
  }

  @media (max-width: 992px){
    .movie-detail-poster > img {
      max-width: 22rem;
    }
    .movie-detail-description {
      margin-top: 3em;
    }
  }

  .movie-detail-list {
    list-style: none;
    line-height: 1.8em;
    text-align: justify;
    padding: 0;
  }

  .movie-detail-title > h3 {
    font-weight: bold;
  }

  .movie-detail-title > h3 > span {
    font-weight: 400;
    font-size: 20px;
  }

  .movie-detail-item {
    margin-bottom: .8em;
  }

</style>