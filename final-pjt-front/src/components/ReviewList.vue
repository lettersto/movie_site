<template>
  <div class="review-list">
    <!-- <ul class="list-group">
      <review-list-item 
        v-for="review in reviews" 
        :review="review" 
        :key="review.pk">
      </review-list-item>
    </ul> -->
    <table class="table">
     <thead>
    <tr>
      <th scope="col" class="text-center">작성자</th>
      <th scope="col" class="text-center">콘텐츠</th>
      <th scope="col" class="text-center">평점</th>
      <th scope="col" class="text-center">수정 및 삭제</th>
    </tr>
  </thead>
  <tbody>
      <review-list-item 
        v-for="review in reviews" 
        :review="review" 
        :key="review.pk">
      </review-list-item>
  </tbody>
  </table>

    <review-form></review-form>
  </div>
</template>

<script>
import ReviewForm from '@/components/ReviewForm.vue'
import ReviewListItem from '@/components/ReviewListItem.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ReviewList',
  components: { ReviewForm, ReviewListItem },
  props: { reviews: Array },
}
</script>

<style>
</style>