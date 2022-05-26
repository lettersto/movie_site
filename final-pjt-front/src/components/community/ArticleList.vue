<template>
  <div>
    <article-list-item
      v-for="article in paginatedData" :key="article.pk"
      :article=article :isStaff=isStaff 
    />
    <div class="btn-cover">
      <button :disabled="pageNum === 0" @click="prevPage" 
        class="page-btn material-icons">
        arrow_left
      </button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }}</span>
      <button :disabled="pageNum >= pageCount - 1" @click="nextPage" 
        class="page-btn material-icons">
        arrow_right
      </button>
    </div>
  </div>
</template>

<script>
  import ArticleListItem from './ArticleListItem.vue'

  export default {
    name: 'ArticleList',
    components: {
      ArticleListItem
    },
    data () {
    return {
      pageNum: 0
    }
    },
    props: {
      articles: Array,
      isStaff: Boolean,
      pageSize: {
        type: Number,
        required: false,
        default: 8
    }
    },
  methods: {
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    }
  },
  computed: {
    pageCount () {
      let listLeng = this.articles.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;

      return page;
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.articles.slice(start, end);
    }
  }
}
</script>

<style scoped>
  .btn-cover {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 2em;
    text-align: center;
    color: #272d2ddd;
  }
  .btn-cover .page-btn {
    background: none;
    border: none;
    outline: none;
    font-size: 3em;
    color: #272d2ddd;
  }

  .btn-cover .page-btn:disabled {
    color: #464b4b7c;
  }

  .btn-cover .page-count {
    padding: 0;
  }
</style>