<template>
    <form @submit.prevent="onSubmit" class="review-form">

    <div class="mb-3">
    <label for="ReviewArea" class="form-label">Review</label>
    <textarea class="form-control" id="ReviewArea" v-model="content" rows="3"></textarea>
    </div>
    <!-- <label for="review">review: </label>
    <input type="text" id="review" v-model="content" required> -->
    <!-- <p>평점
    <input type="range" min="0" max="5" step="0.5" list="tickmarks" id="review" v-model="vote_rate" required>
    </p>
    <datalist id="tickmarks">
    <option value="1" label="1"></option>
    <option value="2" label="2"></option>
    <option value="3" label="3"></option>
    <option value="4" label="4"></option>
    <option value="5" label="5"></option>
    </datalist> -->
  <div>평점
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
  </div>
    
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