<template>
  <div class="page-content page-container" id="page-content">
    <!-- {{ profile }} -->
    <div class="padding">
      <div class="row container d-flex justify-content-center">
        <div class="card user-card-full">
          <div class="row m-l-0 m-r-0">
            <div class="card-block">
              <h1 class="m-b-20 p-b-5 b-b-default f-w-600">{{ profile.username}}'s Information
                <router-link :to="{ name: 'passwordChange' }" v-if="sameUser">
                  <i class="material-icons password-change">edit</i>
                </router-link>
              </h1>
                <div class="row">
                  <div class="poster-box">
                    <p class="m-b-10 f-w-600" v-if="isLikeMovies">좋아하는 영화</p>
                    <div class="posters row">
                      <div class="col-12 col-lg-4" v-for="movie in likeMovies" :key="movie.movie.pk">
                        <router-link :to="{ name: 'movies' , params:{ moviePk: movie.movie.pk }}">
                          <img class="movie-poster-size" :src="'https://image.tmdb.org/t/p/w500' + movie.movie.poster_url" alt="">
                        </router-link>
                      </div>
                    </div>
                  </div>
                </div>
              <h6 class="m-b-20 m-t-40 p-b-5 b-b-default f-w-600">활동</h6>
              <div class="row">
                <div class="col-12 col-lg-6 profile-text-list">
                  <p class="m-b-10 f-w-600">작성한 글</p>
                  <div v-for="article in wroteArticles" :key="article.id">
                    <router-link class="link-text" :to="{ name: 'articleDetail' , params:{ articlePk: article.id }}">
                      <h6 class="text-muted f-w-400 link-text">{{ article.title }}</h6>
                    </router-link>
                  </div>
                </div>
                <div class="col-12 col-lg-6 profile-text-list">
                  <p class="m-b-10 f-w-600">좋아요 누른 게시글</p>
                    <div v-for="article in likeArticles" :key="article.id">
                      <router-link class="link-text" :to="{ name: 'articleDetail' , params:{ articlePk: article.id }}">
                        <h6 class="text-muted f-w-400">{{ article.title }}</h6>
                      </router-link>
                    </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import _ from 'lodash'

  export default {
    name: 'ProfileView',

    computed: {
      ...mapGetters(['profile', 'currentUser']),
      sameUser() {
        return this.currentUser.username === this.profile.username
      },
      
      isLikeMovies() {
        return !_.isEmpty(this.likeMovies);
      },

      likeMovies() {
        // const sortedMovie = _.orderBy(this.profile.reviews, ['updated_at'], ['desc'])
        // const uniqueMovie = _.uniqBy(this.profile.reviews, 'pk')
        // return _.orderBy(uniqueMovie, ['vote_rate', 'release_date'], ['desc', 'desc']).slice(0, 3);

        return _.orderBy(this.profile.reviews, ['vote_rate', 'release_date'], ['desc', 'desc']).slice(0, 3);
      },

      likeArticles() {
        if (this.isLikeMovies) {
          return this.profile.like_articles.slice(0, 5);
        } return []
      },

      wroteArticles() {
        if (this.isLikeMovies) {
          return this.profile.articles.slice(0, 5);
        } return []
      }
    },
    methods: {
      ...mapActions(['fetchProfile']),

    },
    created() {
      const payload = { username: this.$route.params.username }
      this.fetchProfile(payload)
    }

  }
</script>

<style scoped>
  body {
    background-color: #f9f9fa
  }

  .padding {
    padding: 3rem !important
  }

  .user-card-full {
    overflow: hidden;
  }

  .card {
    border-radius: 5px;
    -webkit-box-shadow: 0 1px 20px 0 rgba(69,90,100,0.08);
    box-shadow: 0 1px 20px 0 rgba(69,90,100,0.08);
    border: none;
    margin-bottom: 30px;
  }

  .m-r-0 {
    margin-right: 0px;
  }

  .m-l-0 {
    margin-left: 0px;
  }

  .user-card-full .user-profile {
    border-radius: 5px 0 0 5px;
  }

  .bg-c-lite-green {
    background: -webkit-gradient(linear, left top, right top, from(#f29263), to(#ee5a6f));
    background: linear-gradient(to right, #ee5a6f, #f29263);
  }

  .user-profile {
    padding: 20px 0;
  }

  .card-block {
    padding: 1.25rem;
  }

  .m-b-25 {
    margin-bottom: 25px;
  }

  .img-radius {
    border-radius: 5px;
  }


  
  h6 {
    font-size: 14px;
  }

  .card .card-block p {
    line-height: 25px;
  }

  @media only screen and (min-width: 1400px){
    p {
      font-size: 14px;
    }
  }

  .card-block {
    padding: 1.25rem;
  }

  .b-b-default {
    border-bottom: 1px solid #e0e0e0;
  }

  .m-b-20 {
    margin-bottom: 20px;
  }

  .p-b-5 {
    padding-bottom: 5px !important;
  }

  .card .card-block p {
    line-height: 25px;
  }

  .m-b-10 {
    margin-bottom: 10px;
  }

  .text-muted {
    color: #919aa3 !important;
  }

  .f-w-600 {
    font-weight: 600;
  }

  .m-b-20 {
    margin-bottom: 20px;
  }

  .m-t-40 {
    margin-top: 20px;
  }

  .p-b-5 {
    padding-bottom: 5px !important;
  }

  .m-b-10 {
    margin-bottom: 10px;
  }

  .m-t-40 {
    margin-top: 20px;
  }

  .user-card-full .social-link li {
    display: inline-block;
  }

  .user-card-full .social-link li a {
    font-size: 20px;
    margin: 0 10px 0 0;
    -webkit-transition: all 0.3s ease-in-out;
    transition: all 0.3s ease-in-out;
  }

  .poster-box {
    display: flex;
    flex-direction: column;
  }

  .posters {
    display: flex;
    justify-content: space-between;
  }

  @media (max-width: 992px) {
    .posters {
      justify-content: center;
    }
    .profile-text-list {
      text-align: center;
      margin-bottom: 1em;
    }
  }

  .link-text {
    text-decoration: none;
  } 

  .password-change {
    color:#5d6369;
  }

  .movie-poster-size {
    width: 100%;
    max-height: 480px; 
    /* 추가부분 */
  }



</style>