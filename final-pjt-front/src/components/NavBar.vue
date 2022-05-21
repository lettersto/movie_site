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
        <search-bar type="search" aria-label="Search"/>
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
    username() {
      return this.currentUser.username ? this.currentUser.username : 'guest'
    }
  },

}
</script>

<style scoped>

  nav {
    font-family: 'Poppins', sans-serif;
  }

</style>
