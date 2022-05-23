<template>
  <div class="d-grid gap-5">
    <h1 class="text-center mt-5">Community</h1>

    <div class="d-grid gap-3">
      <div class="d-flex justify-content-end">
        <div class="d-flex" style="max-width: 25em;">
          <input class="form-control me-2" type="search" placeholder="Search Article..." aria-label="Search">
          <button class="btn btn-outline-success">Search</button>
        </div>
        <button class="btn btn-outline-success">
          <router-link :to="{ name: 'articleNew'}">글쓰기</router-link>
        </button>
      </div>
      <article-hottopic />
      <article-list :articles=articles />
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import ArticleHottopic from '@/components/community/ArticleHottopic.vue'
  import ArticleList from '@/components/community/ArticleList.vue'

  export default {
    name: 'CommunityView',
    components: {
      ArticleHottopic,
      ArticleList
    },
    computed: {
      ...mapGetters(['articles'])
    },
    methods: {
      ...mapActions(['fetchArticles'])
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Grape+Nuts&display=swap');

  h1 {
    font-family: 'Grape Nuts', cursive;
    font-size: 3em;
  }
</style>
