<template>
  <div>
    <article-hottopic-item 
      v-for="article in articles" :key="article.pk"
      :article=article :isStaff=isStaff />
  </div>
</template>

<script>
  import ArticleHottopicItem from './ArticleHottopicItem.vue'

  export default {
    name: 'ArticleHottopic',
    props: {
      articles: Array,
      isStaff: Boolean
    },
    components: { 
      ArticleHottopicItem, 
    },
  }
</script>

<style scoped>


</style>