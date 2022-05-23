<template>
  <div v-if="isArticle">
    <!-- 게시글 -->
    <article>
      <div class="d-flex justify-content-between align-items-center mt-5">
        <div class="d-flex align-items-baseline">
          <h1>{{ article.title }}</h1>
          <p class="text-muted"> ({{ article.user.username }})</p>
        </div>
        <div class="d-flex flex-column justify-content-right">
          <small class="text-end text-muted">조회수: {{ articleHits }}</small>
          <small class="text-end text-muted" v-show="isCorreted">({{ updatedDate }} 수정)</small>
        </div>
      </div>
      <hr>
      <p>
        {{ article.content }}
      </p>
      <div class="d-flex justify-content-between">
        <!-- 좋아요 버튼 -->
        <div>
          <button @click="likeArticle(articlePk)">
            <i v-show="inLikeArticleList" class="material-icons like">favorite</i>
            <i v-show="!inLikeArticleList" class="material-icons no-like">heart_broken</i>
          </button> {{ likeCount }}
        </div>
        <!-- 수정, 삭제 버튼 -->
        <div v-if="isAuthor">
          <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
            <button>Edit</button>
          </router-link> |
          <button @click="deleteArticle(articlePk)">Delete</button>
        </div>
      </div>
    </article>
    
    <hr />
    
    <!-- Comment section -->
    <comment-list :comments="article.comments"></comment-list>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'

  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article', 'isArticle', 'currentUser']),
      // 좋아요 수
      likeCount() {
        return this.article.like_users?.length
      },
      // 좋아요 하트 토글
      inLikeArticleList() { 
        let inLike = false;
        if (this.article.user_like === undefined || this.article.user_like.length === 0) {
          return inLike;
        }
        this.article.user_like.forEach(user => {
          if (user.pk === this.currentUser.pk) inLike = true;
        });
        return inLike;
      },
      // 수정 여부
      isCorreted() {
        if (this.article.created_at !== this.article.updated_at) return true;
        else return false;
      },
      // 수정일
      updatedDate() {
        if (this.isArticle) {
          const index = this.article.updated_at.indexOf('T');
          return this.article.updated_at.slice(0, index);
        } else return '';
      },
      // 조회수
      articleHits() {
        let hitsCount = 0;
        if (this.isArticle) {
          return hitsCount;
        }
        hitsCount = this.article.article_views.length;
        return hitsCount
        // let hitsCount = 0;
        // if (this.article.article_views === undefined || this.article.article_views.length === 0) {
        //   return hitsCount;
        // }
        // hitsCount = this.article.article_views.length;
        // return hitsCount
      },
    },
    methods: {
      ...mapActions([
        'fetchArticle','likeArticle',
        'deleteArticle','addArticleView',
      ]),
    },
    created() {
      this.fetchArticle(this.articlePk)
      this.addArticleView(this.articlePk)
    },
  }

</script>

<style scoped>
  button {
    background: none;
    border: none;
    outline: none;
  }

  .like {
    color: #F02D3A;
  }

  .no-like {
    color: #273043;
  }

</style>
