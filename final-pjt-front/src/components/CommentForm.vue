<template>
  <form @submit.prevent="onSubmit" @keyup.enter="onSubmit">

    <div>
      <div>
        <textarea v-model="content" class="form-control" 
          rows="3" placeholder="write some comments...">
        </textarea>
      </div>
      <div>
        <button class="btn btn-outline-secondary">등록</button> 
      </div>
    </div>
    
  </form>
</template>

<script>

  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'CommentForm',
    data() {
      return {
        content: ''
      }
    },
    computed: {
      ...mapGetters(['article'])
    },
    methods: {
      ...mapActions(['createComment']),
      onSubmit() {
        console.log(this.article)
        const comment = {
          articlePk: this.article.pk,
          content: this.content,
        }
        this.createComment(comment)
        this.content = ''
      }
    }
  }
</script>

<style scoped>
  textarea {
    resize: none;
  }
</style>