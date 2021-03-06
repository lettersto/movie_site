<template>
  <div>
    <!-- 게시글 -->
    <div class="article-detail-wrapper">
      <div class="article-detail-container">
      <p v-if="isArticle" class="article-detail-user"> {{ article.user.username }}</p>
      <button class="btn btn-default article-detail-close-btn" @click="onClose">
        <i class="material-icons close-btn">close</i>
      </button>
        <div class="article-detail-header">
          <div class="article-detail-title">
            <h2>{{ article.title }}</h2>
            <small class="article-detail-author"></small>
          </div>
          <div class="article-detail-title-info">
            <small>조회수: {{ articleHits }}</small>
            <small>{{ createdDate }}<span v-show="isCorreted">({{ updatedDate }} 수정)</span></small>
          </div>
        </div>
        <div class="article-detail-body">
          <p class="article-detail-body-content">{{ article.content }}</p>
        </div>
        <div class="article-detail-footer">
          <div class="article-detail-footer-btns">
            <router-link v-if="isAuthor" :to="{ name: 'articleEdit', params: { articlePk } }">
              <button class="btn btn-default">
                <i class="material-icons">edit</i>
              </button>
            </router-link>
            <button  v-if="isAuthor" @click="deleteArticle(articlePk)" class="btn btn-default">
              <i class="material-icons">delete</i>
            </button>
            <button @click="likeArticle(articlePk)" class="btn btn-default">
              <i v-show="inLikeArticleList" class="material-icons like">favorite</i>
              <i v-show="!inLikeArticleList" class="material-icons no-like">heart_broken</i>
            </button> 
          </div>
        </div>
      </div>
    </div>

    <br />
    
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
      // 생성일
      createdDate() {
        if (this.isArticle) {
          const index = this.article.created_at.indexOf('T');
          return this.article.created_at.slice(0, index);
        } else return '';
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
          hitsCount = this.article.article_views.length;
        }
        return hitsCount;
      },
    },
    methods: {
      ...mapActions([
        'fetchArticle','likeArticle',
        'deleteArticle','addArticleView',
      ]),

      onClose() {
        this.$router.push({name: 'community'})
      },
    },
    created() {
      this.fetchArticle(this.articlePk)
      this.addArticleView(this.articlePk)
    },
  }

</script>

<style scoped>

  .article-detail-wrapper {
    margin-top: 3em;
    width: 100%;
  }

  .article-detail-container {
    position: relative;
    background-color: #ffffff;
    padding: 2.8em 2.8em 5em 2.8em;
    min-height: 30vmin;
    border-radius: 8px;
    box-shadow: 0 10px 30px rgba(30, 21, 49, 0.2);
  }

  .article-detail-user {
    position: absolute;
    margin-left: .5em;
    margin-top: -.3em;
    color: rgb(32, 32, 32);
  }

  .article-detail-title {
    display: flex;
    flex-direction: row;
    align-items: baseline;
  }

  .article-detail-header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    height: 5em;
    padding: 0 5px 0 3px;
    border-bottom: 2px solid rgba(0, 0, 0, 0.329);
  }

  .article-detail-title > h2 {
    margin: 0;
  }

  .article-detail-author {
    display: flex;
    justify-content: baseline;
    font-size: 1em;
    margin-left: .5em;
  }

  .article-detail-title-info {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    color: gray;
  }

  .article-detail-body {
    padding: 1.3em .35em 1em .35em;
    text-align: justify;
  }

  .article-detail-footer {
    position: relative;
  }

  .article-detail-footer-btns {
    position: absolute;
    display: flex;
    justify-content: center;
    right: 1px;
  }

  .article-detail-close-btn {
    position: absolute;
    right: 2.1em;
    top: 1.6em;
  }

  .close-btn {
    font-size: 1.3em;
    color: rgb(82, 82, 82)
  }

  .close-btn:hover {
    color: rgb(29, 29, 29)
  }


  .like {
    color: #F02D3A;
  }

  .no-like {
    color: #273043;
  }

  .article-detail-content {
    text-align: justify;
  }



</style>
