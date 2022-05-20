<template>
  <div>
    <h1>Community</h1>
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
    </ul>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
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
