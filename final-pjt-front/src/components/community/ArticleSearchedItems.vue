<template>
  <li @click="onClick(article.pk)" class="article-searched-list-items">
    {{ article.title }}
  </li>
</template>

<script>
  export default {
    name: 'ArticleSearchedItems',
    props: {
      article: Object
    },
    methods: {
      onClick(articleId) {
        this.$router.push({ name: 'articleDetail', params: { articlePk: articleId}})
      }
    }
  }
</script>

<style scoped>
  .article-searched-list-items {
    list-style: none;
    cursor: pointer;
  }
  .article-searched-list-items:hover {
    font-weight: bold;
  }
</style>