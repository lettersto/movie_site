<template>
  <form @submit.prevent="onSubmit" class="article-form-wrapper mt-3">
    <div class="article-form-container">
      <button class="btn btn-default article-form-btn" @click="onClose">
        <i class="material-icons close-btn">close</i>
      </button>
      <input type="text" id="article-form-input"
        placeholder="write your title..." 
        v-model="newArticle.title"
      >
      <textarea 
        id="article-form-textarea" rows="9"
        placeholder="write your content..."
        v-model="newArticle.content"
      >
      </textarea>
      <button class="btn btn-default">
        <i class="material-icons article-form-btn">edit</i>
      </button>
    </div>
  </form>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },

      onClose() {
        this.$router.push({ name : 'community'})
      }
    },
  }
</script>

<style scoped>
  
  .article-form-wrapper {
    position: absolute;
    width: 90vmin;
    transform: translate(-50%, -50%);
    top: 50%;
    left: 50%;
  }

  .article-form-container {
    background-color: #ffffff;
    padding: 2.8em 2.8em 5em 2.8em;
    border-radius: 8px;
    box-shadow: 5px 20px 50px rgba(30, 21, 49, 0.3);
  }

  #article-form-input {
    width: 100%;
    height: 3em;
    font-size: 25px;
    margin-bottom: 1em;
    /* background-color: blue; */
    border: none;
    outline: none;
    border-bottom: 2px solid rgba(0, 0, 0, 0.329);
  }

  #article-form-textarea {
    width: 100%;
    border: none;
    resize: none;
    outline: none;
    font-size: 16px;
    line-height: 28px;
    color: #0e101a;
  }

  .article-form-btn {
    position: absolute;
    right: 2.8em;
    color: rgb(82, 82, 82);
  }

  .article-form-btn:hover {
    color: rgb(29, 29, 29);
  }

  .close-btn {
    font-size: 1.2em;
  }



</style>