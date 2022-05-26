<template>
  <div v-if="article.user.is_staff === isStaff">
    <div class="hot-topic-wrapper">
      <router-link
        :to="{ name: 'articleDetail', params: {articlePk: article.pk} }"
        class="hot-topic-link" aria-current="true"
      >
        <div class="hot-topic-container">
          <div class="d-flex w-100 justify-content-between">
            <h5><i class="material-icons hot-topic-icon">movie_filter</i> {{ article.title }}</h5>
            <div>
              <small>
                <span class="badge bg-secondary me-2">{{ article.view_count }}</span> 
              </small>
            </div>
          </div>
        </div>
      </router-link>
    </div>
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

  .hot-topic-wrapper {
    background-color: #ffffff;
    margin-bottom: .3rem;
    border-radius: 10px;
    border: 1px solid #b8c5d657;
    box-shadow: 5px 5px 15px rgba(75, 81, 94, 0.15);
    transition: .2s;
  }

  .hot-topic-wrapper:hover {
    transform: translateY(-2px);
  }

  .hot-topic-container {
    padding: 8px 1rem;
    display: flex;
    justify-content: center;
  }

  .hot-topic-container {
    margin: 4px 0 0 0;
  }

  .hot-topic-link {
    text-decoration: none;
    color: #272d2da5;
    font-weight: bold;
  }

  .hot-topic-icon {
    color: rgba(77, 113, 146, 0.664);
  }

</style>