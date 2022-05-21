<template>
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
  <router-link
    :to="{ name: 'articleDetail', params: {articlePk: article.pk} }"
    class="list-group-item list-group-item-action" aria-current="true"
  >
    <div class="d-flex w-100 justify-content-between">
      <h5 class="mb-1">{{ article.title }}</h5>
      <div>
        <small>
          <span class="material-icons">
            visibility
          </span> 30
        </small> |
        <small>
          <span class="material-icons">
            favorite
          </span> {{ article.like_count }}
        </small> |
        <small>
          <span class="material-icons">
            chat
          </span> {{ article.comment_count }}
        </small>
      </div>
    </div>
    <p class="mb-1">Some placeholder content in a paragraph.</p>
    <div class="d-flex justify-content-between">
      <small>작성자</small>
      <small>3 days ago</small>
    </div>
  </router-link>
</template>

<script>
  export default {
    name: 'ArticleListItem',
    props: {
      article: Object
    }
  }
</script>

<style>

</style>