<template>
  <div v-if="article.user.is_staff === isStaff">
    <router-link
      :to="{ name: 'articleDetail', params: {articlePk: article.pk} }"
      class="list-group-item list-group-item-action" aria-current="true"
    >
      <div class="d-flex w-100 justify-content-between">
        <h5 class="mb-1">⭐ {{ article.title }}</h5>
        <div>
          <small>
            <span class="badge bg-secondary">{{ article.view_count }}</span> 
          </small>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
  export default {
    name: 'ArticleHottopicItem',
    props: {
      article: Object,
      isStaff: Boolean
    },
  }
    
</script>

<style scoped>
  .article-icons {
    font-size: 1.5em; 
  }
</style>