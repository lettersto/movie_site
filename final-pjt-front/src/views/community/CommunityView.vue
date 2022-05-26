<template>

  <div class="d-grid gap-5">
    <h1 class="text-center community-title">Community</h1>

    <div class="d-grid gap-3">
      <div class="d-flex justify-content-end">
        <div class="d-flex" style="max-width: 25em;">
          <!-- SearchBar -->
          <div>
            <input 
              class="form-control me-2" type="search" 
              placeholder="Search Article..." aria-label="Search"
              v-model="typedArticleName"
              autocomplete="off"
              @input="filterArticle"
              @keyup.enter="enterSearch"
            >
            <div class="article-searchbar-wrapper">
              <ul 
                v-if="filteredArticles.length !== 0 && typedArticleName"
                class="article-search-box"
              >
                <article-searched-items 
                  v-for="(article, idx) in filteredArticles.slice(0, 7)" 
                  :key="idx" :article=article
                />
              </ul>
            </div>
          </div>
        </div>
        <button class="btn btn-outline-secondary ms-2">
          <router-link :to="{ name: 'articleNew'}" class="article-new-btn">글쓰기</router-link>
        </button>
      </div>
      <article-hottopic :articles=articles :isStaff="true" class="mb-5" />
      <article-list :articles=articles :isStaff="false" class="article-list-box" />
    </div>
  </div>

</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import ArticleHottopic from '@/components/community/ArticleHottopic.vue'
  import ArticleList from '@/components/community/ArticleList.vue'
  import ArticleSearchedItems from '@/components/community/ArticleSearchedItems.vue'
  import _ from 'lodash'

  export default {
    name: 'CommunityView',
    components: {
      ArticleHottopic,
      ArticleList,
      ArticleSearchedItems
    },
    data() {
      return {
        typedArticleName: '',
        filteredArticles: [],
      }
    },
    computed: {
      ...mapGetters(['articles'])
    },
    methods: {
      ...mapActions(['fetchArticles']),

      filterArticle() {
        this.filteredArticles = [];
        this.filteredArticles = this.articles.filter(article => {
          return article.title.toLowerCase().startsWith(this.typedArticleName.toLowerCase());
        });
      },
      
      enterSearch() {
        if (!_.isEmpty(this.filteredArticles)) {
          let articleId = this.filteredArticles[0].pk;
          // console.log(this.filteredArticles[0])
          this.$router.push({ name: 'articleDetail', params: { articlePk: articleId }});
          // this.$router.go(this.$router.currentRoute);
          this.typedArticleName = "";
        }
      },

    },

    created() {
      this.fetchArticles()
    },

  }
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Grape+Nuts&display=swap');

  h1 {
    font-family: 'Grape Nuts', cursive;
    font-size: 3em;
    color: #272d2ddd;
    margin: 3em 0 2em 0;
  }
  
  .article-search-bar-wrapper {
    position: relative;
    width: 100%;
    z-index: 0;
  }

  .article-search-box {
    position: absolute;
    padding: 10px;
    border: 1px solid rgba(168, 194, 236, 0.566);
    border-radius: 5px;
    background-color: rgba(255, 255, 255, 0.826);
    z-index: 10;
  }

  .article-new-btn {
    text-decoration: none;
    color: rgba(0, 0, 0, 0.8);
  }

  .article-list-box {
    padding: 1rem .8rem 2.2rem .8rem;
    background-color: #ffffff;
    border: 1px solid #b8c5d657;
    border-radius: 5px;
    box-shadow: 5px 5px 15px rgba(75, 81, 94, 0.15);
  }

</style>
