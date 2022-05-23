<template>
    <form @submit.prevent="onSubmit" class="review-form">
    <label for="review">review: </label>
    <input type="text" id="review" v-model="content" required>
    <input type="Float" id="review" v-model="vote_rate" required>
    <button>Review</button> 
    </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewForm',
  data() {
    return {
      content: '',
      vote_rate: '',
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({ moviePk: this.movie.id, content: this.content, vote_rate: this.vote_rate})
      this.content = ''
      this.vote_rate = ''
    }
  }
}
</script>

<style>

</style>