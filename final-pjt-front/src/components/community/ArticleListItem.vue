<template>
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
      <small>{{ dateDiff }}</small>
    </div>
  </router-link>
</template>

<script>
  export default {
    name: 'ArticleListItem',
    props: {
      article: Object
    },
    data() {
      return {
        dateDiff:'0초 전'
      }
    },
    methods: {
      getDateDifference() {
        let currentDate = Date.now();
        const createdDate = new Date(this.article.created_at);
        const milliSeconds = Math.abs(createdDate - currentDate);
        const seconds = milliSeconds / 1000;
        
        if (seconds < 60) return `${Math.trunc(seconds)}초 전`;

        const minutes = seconds / 60;

        if (minutes < 60) return `${Math.trunc(minutes)}분 전`

        const hours = minutes / 60;

        if (hours < 24) return `${Math.trunc(hours)}시간 전`

        const days = hours / 24;

        if (days < 31) return `${Math.trunc(days)}일 전`;
        
        return `오래전`
      },
    },
    mounted() {
      setInterval(() => {
        this.dateDiff = this.getDateDifference()
      }, 1000);
    }
  }
</script>

<style>

</style>