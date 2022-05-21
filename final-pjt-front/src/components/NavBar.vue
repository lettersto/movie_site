<template>
  <nav>
    <div class="container">
      <div class="nav-items-left">
        <!-- <div >
          <i class="material-icons">movie_filter</i>
          <span class="logo"> Cat's Movie</span>
        </div> -->
    
        <div class="nav-items-1">
          <router-link :to="{ name: 'home' }" class="nav-item mr">
            Home
          </router-link>
          <router-link :to="{ name: 'community' }" class="nav-item">
            Community
          </router-link>
        </div>
      </div>

      <search-bar />

      <div>
        <router-link v-if="!isLoggedIn" :to="{ name: 'signup' }" class="nav-item mr">
          Signup
        </router-link>
        <router-link v-if="!isLoggedIn" :to="{ name: 'login' }" class="nav-item">
          Login
        </router-link>
        <router-link v-if="isLoggedIn" :to="{ name: 'profile', params: { username: currentUser.username }}" class="nav-item mr">
          Profile
        </router-link>
        <router-link v-if="isLoggedIn" :to="{ name: 'logout' }" class="nav-item">
          Logout
        </router-link>
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
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
  },
  // username() {
  //   return this.currentUser.username ? this.currentUser.username : 'guest'
  // }
}
</script>

<style scoped>

  .container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }

  /* .logo {
    font-size: 1.5em;
    font-weight: bold;
  } */

  .nav-items-left {
    display: flex;
    flex-direction: row;
  }
  

  .nav-item {
    text-decoration: none;
    /* color: white; */
    color: black;
    font-size: 1.55em;
    font-weight: bold;
  }

  .nav-item:hover {
    color: rgb(164, 164, 164);
  }

  .mr {
    margin-right: 10px;
  }

  /* .nav-items-1 {
    padding: 0 .8em;
  } */


</style>