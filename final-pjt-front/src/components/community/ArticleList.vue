<template>
  <div>
    <article-list-item
      v-for="article in paginatedData" :key="article.pk"
      :article=article :isStaff=isStaff
    />
    <div class="btn-cover">
      <button :disabled="pageNum === 0" @click="prevPage" class="page-btn">
        이전
      </button>
      <span class="page-count">{{ pageNum + 1 }} / {{ pageCount }} 페이지</span>
      <button :disabled="pageNum >= pageCount - 1" @click="nextPage" class="page-btn">
        다음
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
        default: 10
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
  margin-top: 1.5rem;
  text-align: center;
}
.btn-cover .page-btn {
  width: 5rem;
  height: 2rem;
  letter-spacing: 0.5px;
}
.btn-cover .page-count {
  padding: 0 1rem;
}
</style>