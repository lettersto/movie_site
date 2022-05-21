<template>
  <div>
    <!-- v-for로 여러 개 생성하기 -->
    <comment-list-item class="list-group"/>
    <comment-form/>
  </div>
</template>

<script>
  import CommentListItem from './CommentListItem.vue'
  import CommentForm from './CommentForm.vue'

  export default {
    name: 'CommentList',
    components: {
      CommentListItem,
      CommentForm
    }
  }
</script>

<style>

</style>