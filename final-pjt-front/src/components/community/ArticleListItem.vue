<template>
  <div v-if="article.user.is_staff === isStaff">
    <div class="article-list-wrapper">
      <router-link
        :to="{ name: 'articleDetail', params: {articlePk: article.pk} }"
        class="article-list-link" aria-current="true"
      >
        <div class="d-flex w-100 justify-content-between">
          <h5 class="mb-1">{{ article.title }}</h5>
          <div>
            <small>
              <span class="material-icons article-icons">
                visibility
              </span> {{ article.view_count }}
            </small> |
            <small>
              <span class="material-icons article-icons">
                favorite
              </span> {{ article.like_count }}
            </small> |
            <small>
              <span class="material-icons article-icons">
                chat
              </span> {{ article.comment_count }}
            </small>
          </div>
        </div>
        <div class="d-flex justify-content-between">
          <small>{{ article.user.username }}</small>
          <small>{{ dateDiff }}</small>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'ArticleListItem',
    props: {
      article: Object,
      isStaff: Boolean
    },
    data() {
      return {
        dateDiff:'0초 전',
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

<style scoped>
  .article-icons {
    font-size: 1.4em; 
  }

  .article-list-wrapper {
    background-color: #ffffff;
    margin-bottom: .3rem;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #b8c5d657;
    box-shadow: 5px 0px 10px rgba(75, 81, 94, 0.1);
    transition: .2s;
  }

  .article-list-wrapper:hover {
    transform: translateY(-2px);
  }

  .article-list-link {
    text-decoration: none;
    color: #272d2da5;
    font-weight: bold;
  }


</style>