<template>
  <div>
    <!-- 게시글 -->
    <article>
      <div class="d-flex align-items-center">
        <h1>{{ article.title }}</h1>
        <small v-show="isCorreted">(수정)</small>
      </div>
      <p>
        {{ article.content }}
      </p>
      <!-- 수정, 삭제 버튼 -->
      <div v-if="isAuthor">
        <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
          <button>Edit</button>
        </router-link>
        |
        <button @click="deleteArticle(articlePk)">Delete</button>
      </div>
      <!-- 좋아요 버튼 -->
      <!-- <div>
        <button @click="likeArticle(articlePk)">
          <i v-show="inLikeArticleList" class="material-icons like">favorite</i>
          <i v-show="!inLikeArticleList" class="material-icons no-like">heart_broken</i>
        </button> {{ likeCount }}
      </div> -->
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
      ...mapGetters(['isAuthor', 'article', 'currentUser']),
      likeCount() {
        return this.article.like_users?.length
      },
      // inLikeArticleList() { // 미리 계산하고 와야할 거 같은데 임시로
      //   let inLike = false;
      //   this.article.user_like.forEach(user => {
      //     if (user.pk === this.currentUser.pk) inLike = true;
      //   });
      //   return inLike;
      // },
      isCorreted() {
        if (this.article.created_at !== this.article.updated_at) return true;
        else return false;
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
        'addArticleView',
      ])
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
    mounted() {
      this.addArticleView(this.articlePk)
    }
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
