<template>
  <div>
    <div class="review-container">
    <div class="review-card">
      <div class="review-title">
        <div>
          <router-link :to="{ name: 'profile', params: { username: review.user.username } }"
            class="review-link">
            {{ stars[payload.vote_rate] }}
            <p class="review-author"> {{ review.user.username }}</p>
          </router-link>
        </div>
        <div class="review-date">
          {{ createdDate }} 
          <small v-if="review.created_at !== review.updated_at">
            ({{ updatedDate }} 수정)
          </small>
        </div>
      </div>
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
          <div class="star-widget-container">
            <div class="star-widget">
              <input type="radio" v-model="payload.vote_rate" name="rate" id="rate-5" value="5">
              <label for="rate-5" class="material-icons">star</label>
              <input type="radio" v-model="payload.vote_rate" name="rate" id="rate-4" value="4">
              <label for="rate-4" class="material-icons">star</label>
              <input type="radio" v-model="payload.vote_rate" name="rate" id="rate-3" value="3">
              <label for="rate-3" class="material-icons">star</label>
              <input type="radio" v-model="payload.vote_rate" name="rate" id="rate-2" value="2">
              <label for="rate-2" class="material-icons">star</label>
              <input type="radio" v-model="payload.vote_rate" name="rate" id="rate-1" value="1">
              <label for="rate-1" class="material-icons">star</label>
            </div>
          </div>
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
      stars: [
        '', '⭐', '⭐⭐', '⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'
      ]
    }
  },
  computed: {
    ...mapGetters(['currentUser']),

    createdDate() {
        const index = this.review.created_at.indexOf('T');
        return this.review.created_at.slice(0, index);
    },
    
    updatedDate() {
      const index = this.review.updated_at.indexOf('T');
      return this.review.updated_at.slice(0, index);
    },
    
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdateClick() {
      // console.log(this.payload)
      const starWidgets = document.querySelector(".star-widget label")
      this.updateReview(this.payload)
      this.isEditing = false
      starWidgets.style.color = "#444"
    },

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

  .review-title {
    display: flex;
    justify-content: space-between;
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
    margin-left: 5px;
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
    width: 120px;
    background-color: #ffffff;
    padding:0;
    /* border: 1px solid #444; */
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
    cursor: pointer;
  }

  input:not(:checked) ~ label:hover, 
  input:not(:checked) ~ label:hover ~ label {
    color: rgb(255, 212, 21);
  }

  input:checked ~ label {
    color: rgb(255, 212, 21);
  }

  input#rate-5:checked ~ label {
    color: #fe7;
    text-shadow: 0 0 20px rgb(250, 255, 193);
  }

  .review-date {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    color: gray;
    margin-right: 5px;
  }


  /* input:checked ~ label {

  } */


</style>