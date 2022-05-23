<template>
  <div>
    <!-- 영화 포스터란 -->
    <div class="card mb-3">
      <div class="row g-0">
        <div class="col-md-4">
          <img :src="movieURL" class="img-fluid rounded-start" alt="...">
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }} <span class="badge bg-secondary">평점</span></h5>
            <p class="card-text">개봉일: {{ movie.release_date }}</p>
            <div class="card-text">감독:
              <div v-for="director_list in movie.director" :key="director_list.id">
                {{ director_list.name }}
              </div>
            </div>
            <div class="card-text">배우: 
              <div v-for="actor_list in movie.actor" :key="actor_list.id">
                {{ actor_list.name }}
              </div>
            </div>
            <p class="card-text">{{ movie.overview }}
            </p>
            <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
          </div>
        </div>
      </div>
    </div>
    <hr>

    <!-- 댓글란 -->
    <review-list :reviews="movie.reviews"/>
    
  </div>


</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import ReviewList from '@/components/ReviewList.vue'


  export default {
    name: 'MovieView.vue',
    components: {
      ReviewList
    },
    data() {
      return {
        moviePk: this.$route.params.moviePk,
      }
    },
    computed: {
      ...mapGetters(['movie']),
      movieURL() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_url
    }
    },
    methods: {
      ...mapActions([
        'fetchMovie',
      ])
    },
    created() {
      this.fetchMovie(this.moviePk)
    },
  }
</script>

<style>

</style>