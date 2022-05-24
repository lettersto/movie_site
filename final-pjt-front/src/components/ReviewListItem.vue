<template>
  <div>
    <div class="review-container">
    <div class="review-card">
      <router-link :to="{ name: 'profile', params: { username: review.user.username } }"
        class="review-link">
        <p class="review-author">{{ payload.voterate }} {{ review.user.username }}</p>
      </router-link>
      <p class="review-content">{{ review.content }}</p>
      <div class="review-footer" v-if="currentUser.username === review.user.username">
        <div v-if="!isEditing">
          <button @click="switchIsEditing" class="review-btn">
            <i class="material-icons">edit</i>
          </button>
          <button @click="deleteReview(payload)" class="review-btn">
            <i class="material-icons">delete</i>
          </button>
        </div>
        <div v-if="isEditing" class="review-edit-box">
          <input type="text" v-model="payload.content" class="review-input">
          <button @click="onUpdateClick" class="review-btn">
            <i class="material-icons">update</i>
          </button>
          <button @click="switchIsEditing" class="review-btn">
            <i class="material-icons">edit_off</i>
          </button>
        </div>
      </div>
    </div>
    {{ review }}
  </div>
  <div class="star-widget-container">
    <div class="star-widget">
      <input type="radio" name="rate-5" id="rate" value="5">
      <label for="rate-5" class="material-icons">star</label>
      <input type="radio" name="rate-4" id="rate" value="4">
      <label for="rate-4" class="material-icons">star</label>
      <input type="radio" name="rate-3" id="rate" value="3">
      <label for="rate-3" class="material-icons">star</label>
      <input type="radio" name="rate-2" id="rate" value="2">
      <label for="rate-2" class="material-icons">star</label>
      <input type="radio" name="rate-1" id="rate" value="1">
      <label for="rate-1" class="material-icons">star</label>
    </div>
  </div>

    <!-- <tr>
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
    </tr> -->
  </div>
  
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
        vote_rate: this.review.vote_rate
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
    onUpdateClick() {
      // console.log(this.payload)
      this.updateReview(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
  *, 
  *::before, 
  *::after {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }

  .review-container {
    position: relative;
    padding: 0 5px;
    margin-bottom: 1em;
    transition: .3s;
  }

  .review-container:hover {
    transform: scale(1);
    padding: 0;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  }

  .review-card {
    padding: 20px;
    background-color: #ffffff;
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 0.5rem;
    line-height: 1.7em;
    text-align: justify;
    
  }

  .review-footer {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
  }

  .review-btn {
    background: none;
    border: none;
    padding: 0 5px;
    margin-top: 4px;
  }

  .review-link {
    text-decoration: none;
  }

  .review-author {
    color: gray;
  }


  .review-author:hover {
    color: black;
    cursor: pointer;
    text-decoration: underline;
  }

  .review-edit-box {
    display: flex;
    flex-direction: row;
    justify-content: center;
    text-align: center;
  }

  .review-input {
    outline: none;
    border: 1px solid rgba(0, 0, 0, 0.2);
    border-radius: 5px;
    padding: 0 10px;
  }

  .star-widget-container {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 400px;
    background-color: #ffffff;
    padding: 20px 30px;
    border: 1px solid #444;
  }

  .star-widget-container .star-widget input {
    display: none;
  }

  .star-widget label {
    font-size: 20px;
    color: #444;
    padding: 1px;
    float: right;
    transition: all 0.2s ease;
  }

  input:not(:checked) ~ label:hover, 
  input:not(:checked) ~ label:hover ~ label {
    color: #fd4;
  }

  /* input:checked ~ label {

  } */


</style>