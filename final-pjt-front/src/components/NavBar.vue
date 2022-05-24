<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">로고위치</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
           <li class="nav-item">
            <router-link :to="{ name: 'home' }" class="nav-link">
              Home
            </router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'community' }" class="nav-link">
              Community
            </router-link>
          </li>
          <li class="nav-item">
            <router-link v-if="!isLoggedIn" :to="{ name: 'signup' }" class="nav-link">
              Signup
            </router-link>
          </li>
          <li class="nav-item">
            <router-link v-if="!isLoggedIn" :to="{ name: 'login' }" class="nav-link">
              Login
            </router-link>
          </li>
          <li>
            <router-link v-if="isLoggedIn" :to="{ name: 'profile', params: { username } }" class="nav-link">
              Profile
            </router-link>            
          </li>
          <li class="nav-item">
            <router-link v-if="isLoggedIn" :to="{ name: 'logout' }" class="nav-link">
              Logout
            </router-link>
          </li>
          <li class="nav-item">
          </li>
        </ul>
        <div>
            <input 
              class="form-control me-2" type="search" 
              placeholder="Search Movie..." aria-label="Search"
              v-model="typedMovieName"
              autocomplete="off"
              @input="filterMovie"
            >
            <div class="movie-searchbar-wrapper">
              <ul 
                v-if="filteredMovies.length !== 0 && typedMovieName"
                class="movie-search-box"
              >
                <search-bar 
                  v-for="(movie, idx) in filteredMovies.slice(0, 7)" 
                  :key="idx" :movie=movie
                />
                </ul>
              </div>
              </div>
      </div>
    </div>
  </nav>
   
</template>

<script>
import SearchBar from './SearchBar.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  components: {
    SearchBar,
  },
  data() {
      return {
        typedMovieName: '',
        filteredMovies: []
      }
    },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser', 'movies']),
    username() {
      return this.currentUser.username ? this.currentUser.username : 'guest'
    }
  },
  methods:{
    filterMovie() {
        this.filteredMovies = [];
        this.filteredMovies = this.movies.filter(movie => {
        return movie.title.toLowerCase().startsWith(this.typedMovieName.toLowerCase());
      })
      },
  }

}
</script>

<style scoped>

  nav {
    font-family: 'Poppins', sans-serif;
  }

  .movie-searchbar-wrapper {
    position: relative;
    width: 100%;
    z-index: 0;
  }

  .movie-search-box {
    position: absolute;
    padding: 10px;
    border: 1px solid rgba(168, 194, 236, 0.566);
    border-radius: 5px;
    background-color: rgba(255, 255, 255, 0.826);
    z-index: 10;
  }
</style>
