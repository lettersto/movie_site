<template>
  <div class="review-list">
    <review-list-item 
      v-for="review in reviews" 
      :review="review" 
      :key="review.pk">
    </review-list-item>

    <review-form></review-form>
  </div>
</template>

<script>
  import ReviewForm from '@/components/ReviewForm.vue'
  import ReviewListItem from '@/components/ReviewListItem.vue'


  export default {
    name: 'ReviewList',
    components: { ReviewForm, ReviewListItem },
    props: { reviews: Array },
  }
</script>

<style>

</style>