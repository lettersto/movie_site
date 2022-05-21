<template>
  <div>
    <h1>Community</h1>

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
    <!-- <h1>Community</h1>
    <router-link 
      :to="{ name: 'articleNew'}">new
    </router-link>
    <ul>
      <li v-for="article in articles" :key="article.pk">
        {{ article.user.username }} : 
        <router-link 
          :to="{ name: 'articleDetail', params: {articlePk: article.pk} }">
          {{ article.title }}
        </router-link>
        =>
        ({{ article.comment_count }}) | +{{ article.like_count }}
      </li>
    </ul> -->
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

<style>

</style>
