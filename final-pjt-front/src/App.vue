<template>
  <div id="app" v-cloak>
    <nav-bar />
    <!-- <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav> -->
    <router-view/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import { mapActions } from 'vuex'

export default {
  name: 'App',
  components: {
    NavBar,
  },
  methods: {
    ...mapActions(['fetchCurrentUser'])
  },
  created() {
    this.fetchCurrentUser()
  }
}
</script>


<style>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR&family=Poppins&display=swap");
@import url("https://fonts.googleapis.com/icon?family=Material+Icons");

/* font-family: 'Noto Sans KR', sans-serif; */
/* font-family: 'Poppins', sans-serif; */

[v-cloak] {
  display: none;
}

*, *::before, *::after {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

/* body {
  margin: 1.5em 10%;
  
  background-color: #0a0a0af6;
  color: white;
} */

</style>
