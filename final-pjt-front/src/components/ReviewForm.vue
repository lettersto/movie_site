<template>
  <form @submit.prevent="onSubmit" class="review-form" @keyup.enter="onSubmit" >

    <div class="d-flex mb-3">
      <label for="ReviewArea" class="form-label">Review</label>
      <div class="star-widget-container">
        <div class="star-widget">
          <input type="radio" v-model="vote_rate" name="rate" id="rate-5" value="5">
          <label for="rate-5" class="material-icons">star</label>
          <input type="radio" v-model="vote_rate" name="rate" id="rate-4" value="4">
          <label for="rate-4" class="material-icons">star</label>
          <input type="radio" v-model="vote_rate" name="rate" id="rate-3" value="3">
          <label for="rate-3" class="material-icons">star</label>
          <input type="radio" v-model="vote_rate" name="rate" id="rate-2" value="2">
          <label for="rate-2" class="material-icons">star</label>
          <input type="radio" v-model="vote_rate" name="rate" id="rate-1" value="1">
          <label for="rate-1" class="material-icons">star</label>
        </div>
      </div>
    </div>
    <div class="input-group">
      <textarea class="form-control" id="ReviewArea" v-model="content" rows="3"></textarea>
      <button class="btn btn-outline-secondary">Review</button> 
    </div>

    <!-- <div>평점
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1" v-model="vote_rate" value="1">
        <label class="form-check-label" for="inlineRadio1">1</label>
      </div>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" v-model="vote_rate" value="2">
        <label class="form-check-label" for="inlineRadio2">2</label>
      </div>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" v-model="vote_rate" value="3">
        <label class="form-check-label" for="inlineRadio3">3</label>
      </div>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" v-model="vote_rate" value="4">
        <label class="form-check-label" for="inlineRadio4">4</label>
      </div>
      <div class="form-check form-check-inline">
        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" v-model="vote_rate" value="5">
        <label class="form-check-label" for="inlineRadio5">5</label>
      </div>
      <button class="btn btn-secondary">리뷰등록</button> 
    </div> -->
    
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

<style scoped>
  label {
    margin: 0;
  }

  .star-widget-container {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 120px;
    /* background-color: #ffffff; */
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

  textarea {
    resize: none;
  }

</style>