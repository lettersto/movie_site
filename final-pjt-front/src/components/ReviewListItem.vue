<template>
  <tr>
    <td class="text-center align-middle"><router-link :to="{ name: 'profile', params: { username: review.user.username } }">
      {{ review.user.username }}
    </router-link> </td>
    <td class="text-center align-middle">
      {{ payload.content }}
    </td>
    <td class="text-center align-middle">
      {{ payload.voterate }}
    </td>
    <td class="text-center align-middle">
      <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button @click="onUpdate" class="btn btn-default">
        <i class="material-icons like">update</i></button> |
      <button @click="switchIsEditing" class="btn btn-default">
        <i class="material-icons like">cancel</i>
      </button>
    </span>
    <span v-if="currentUser.username === review.user.username && !isEditing">
      <button @click="switchIsEditing" class="btn btn-default">
        <i class="material-icons like">edit</i>
        </button> |
      <button @click="deleteReview(payload)" class="btn btn-default">
        <i class="material-icons like">delete</i>
      </button>
    </span>
    </td>
  </tr>
  
  <!-- <li class="list-group-item">
    <router-link :to="{ name: 'profile', params: { username: review.user.username } }">
      {{ review.user.username }}
    </router-link>: 
    
    <span v-if="!isEditing">{{ payload.content }}
      <br/>
       평점: {{ payload.voterate }} </span>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button @click="onUpdate" class="btn btn-default">
        <i class="material-icons like">update</i></button> |
      <button @click="switchIsEditing" class="btn btn-default">
        <i class="material-icons like">cancel</i>
      </button>
    </span>
    <span v-if="currentUser.username === review.user.username && !isEditing">
      <button @click="switchIsEditing" class="btn btn-default">
        <i class="material-icons like">edit</i>
        </button> |
      <button @click="deleteReview(payload)" class="btn btn-default">
        <i class="material-icons like">delete</i>
      </button>
    </span>
  </li> -->
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