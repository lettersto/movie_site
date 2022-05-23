<template>
  <div>
    <article-list-item
      v-for="article in articles" :key="article.pk"
      :article=article :isStaff=isStaff
    />
  </div>
</template>

<script>
  import ArticleListItem from './ArticleListItem.vue'

  export default {
    name: 'ArticleList',
    components: {
      ArticleListItem
    },
    props: {
      articles: Array,
      isStaff: Boolean
    }
  }
</script>

<style>

</style>