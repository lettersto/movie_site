<template>
  <div id="app" v-cloak>
    <nav-bar />
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

  body {
    margin-bottom: 5em;
  }

</style>
