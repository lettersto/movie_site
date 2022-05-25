<template>
  <nav class="navi">
    <div class="navi-list">
      <ul>
        <div class="navi-item">
          <div class="navi-brand">
            <h1>Movie</h1>
          </div>
          <li><router-link class="navi-link" :to="{ name: 'home' }">Home</router-link></li>
          <li><router-link class="navi-link" :to="{ name: 'community' }">Community</router-link></li>
          <li v-if="!isLoggedIn"><router-link class="navi-link" :to="{ name: 'signup' }">Signup</router-link></li>
          <li v-if="!isLoggedIn"><router-link class="navi-link" :to="{ name: 'login' }">Login</router-link></li>
          <li v-if="isLoggedIn"><router-link class="navi-link" :to="{ name: 'profile', params: { username } }">Profile</router-link></li>
          <li v-if="isLoggedIn"><router-link class="navi-link" :to="{ name: 'logout' }">Logout</router-link></li>
          <li v-if="showSearchBar">
            <div>
              <input 
                class="form-control me-2 px-1" type="search" 
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
          </li>
          <li>
            <button class="material-icons" @click="searchBtnToggle">
              search
            </button>
          </li>
        </div>
      </ul>
    </div>

  </nav>
  <!-- <nav class="navbar navbar-expand-lg navbar-light bg-light">
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
  </nav> -->
   
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
        filteredMovies: [],
        showSearchBar: false
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

      searchBtnToggle() {
        this.showSearchBar = !this.showSearchBar;
      }
    }

  }
</script>

<style scoped>
  *, 
  *:before, 
  *:after {
    padding: 0;
    margin: 0;  
  }

  nav {
    font-family: 'Poppins', sans-serif;
    max-width: 1350px;
  }

  .navi {
    background: #ffffff;
    z-index: 100;
    width: 90%;
    border: 1px solid #b8c5d657;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    border-radius: 30px;
    padding: 0 3%;
    box-sizing: border-box;
    position: fixed;
    top: 10px;
    left: 50%;
    transform: translateX(-50%);
    height: 80px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .navi-list {
    width: 100%;
  }

  .navi-list ul {
    /* display: flex;
    flex-direction: row;
    justify-content: space-around; */
    align-items: center;
    list-style: none;
    width: 100%;
    padding: 0;
  }

  .navi-item {
    display: flex;
    justify-content: space-around;
    align-items: center;
  }

  .navi-list ul li {
    margin: 0 10px;
  }

  .navi-list ul li .navi-link {
    position: relative;
    padding: 0 10px;
    font-size: 1rem;
    letter-spacing: 0.5px;
    text-decoration: none;
    color: #272d2da5;
    font-weight: bold;
    display: block;
  }

  .navi-list ul li .navi-link:hover {
    color: #272d2dde;
  }

  .navi-list ul li .navi-link::after {
    content: "";
    position: absolute;
    background-color: #272d2dde;
    height: 3px;
    width: 0;
    left: 0;
    bottom: -8px;
    transition: 0.3s;
  }

  .navi-list ul li .navi-link:hover::after {
    width: 100%;
  }

  .navi-list ul li button {
    background: linear-gradient(121.82deg, rgba(98, 122, 144, 0.664) 19.93%, #B8C5D6 102.22%);
    outline: none;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
    color: white;
    border-radius: 9px;
    cursor: pointer;
    transition: .4 ease;
  }

  .navi-list ul li button:hover {
    transform: translateY(-1.5px);
  }

  .navi-brand {
    cursor: pointer;
    font-size: 20px;
    font-weight: 700;
    background: linear-gradient(121.82deg, rgb(98, 122, 144) 19.93%, #B8C5D6 102.22%);
    -webkit-background-clip: text;
    color: transparent;
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
