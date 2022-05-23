<template>
  <div>
    <comment-list-item
      v-for="comment in comments"
      :comment="comment"
      :key="comment.pk" />
    <comment-form />
    <!-- <table class="table">
     <thead>
    <tr>
      <th scope="col" class="text-center">작성자</th>
      <th scope="col" class="text-center">댓글</th>
      <th scope="col" class="text-center">수정 및 삭제</th>
    </tr>
  </thead>
  <tbody>
    <comment-list-item
      v-for="comment in comments"
      :comment="comment"
      :key="comment.pk" />
  </tbody>
  </table>
    <comment-form/> -->
  </div>
</template>

<script>
  import CommentListItem from './CommentListItem.vue'
  import CommentForm from './CommentForm.vue'


export default {
  name: 'CommentList',
  components: { 
    CommentForm, 
    CommentListItem 
  },
  props: { comments: Array },
}
</script>

<style>

</style>