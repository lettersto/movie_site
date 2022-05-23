<template>
  
  <li class="review-list-item">
    <router-link :to="{ name: 'profile', params: { username: review.user.username } }">
      {{ review.user.username }}
    </router-link>: 
    
    <span v-if="!isEditing">{{ payload.content }} / 평점: {{ payload.voterate }}</span>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>
    <span v-if="currentUser.username === review.user.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteReview(payload)">Delete</button>
    </span>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewListItem',
  props: { review: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie,
        reviewPk: this.review.pk,
        content: this.review.content,
        voterate: this.review.vote_rate
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
    
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
</style>