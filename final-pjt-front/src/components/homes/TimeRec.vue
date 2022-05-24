<template>
<div>
  <div v-show="6 <= hour & hour < 14">
  <h2>오늘 아침 피곤을 날려버릴 영화</h2>
  <div class="card-deck d-flex justify-content-around">
  <div class="col-sm-4 card" v-for="rec in morningRecommend" :key="rec.pk">
  <router-link 
  :to="{ name: 'movies', params: { moviePk: rec['pk'] } }">
  <img class="card-body" :src="'https://image.tmdb.org/t/p/w500' + rec['poster_url']" alt="...">
  </router-link>
  </div>
  </div>
  </div>
  <div v-show="14 <= hour & hour < 20">
  <h2>나른한 오후 나를 흥미진진하게 할 영화</h2>
  <div class="card-deck d-flex justify-content-around">
  <div class="col-sm-4 card" v-for="rec in eveningRecommend" :key="rec.pk">
  <router-link 
  :to="{ name: 'movies', params: { moviePk: rec['pk'] } }">
  <img class="card-body" :src="'https://image.tmdb.org/t/p/w500' + rec['poster_url']" alt="...">
  </router-link>
  </div>
  </div>
  </div>
  <div v-show="20 <= hour & hour < 6">
  <h2>오늘 저녁 나와 함께 할 영화</h2>
  <div class="card-deck d-flex justify-content-around">
  <div class="col-sm-4 card" v-for="rec in nightRecommend" :key="rec.pk">
  <router-link 
  :to="{ name: 'movies', params: { moviePk: rec['pk'] } }">
  <img class="card-body" :src="'https://image.tmdb.org/t/p/w500' + rec['poster_url']" alt="...">
  </router-link>
  </div>
  </div>
  </div>
  </div>
</template>

<script>
import dayjs from 'dayjs'
import { mapGetters } from 'vuex'
// import _ from 'lodash'

export default {
  name: 'TimeRec',
  data(){
    return{
      today: dayjs().format("YYYY-MM-DD HH:mm:ss"),
      hour:"",
    }
  },
  mounted(){
    this.dateSplit()
  },
  methods: {
    dateSplit(){
      this.hour = dayjs(this.today).hour()
    }
  },
  computed: {
      ...mapGetters(['movies',]),
      movieURL() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_url
      },  
      morningRecommend(){
        return [ {"pk": 629542, "poster_url": "/x6KSvale7iuxLhsrEfhYNoICyfK.jpg"},
        {"pk": 438695, "poster_url": "/xe8dVB2QiCxLWFV77V4dpZcOvYB.jpg"},
        {"pk": 678287, "poster_url": "/tvhX4QQnMyMjlFeShLCXovvbf0c.jpg"}
        ]
      },
      eveningRecommend(){
        return [ {"pk": 752623, "poster_url": "/8kZapNBZYGJu7AUbJVBDMmQgO1D.jpg"},
        {"pk": 639933, "poster_url": "/bfeM8NGWm1riLvvVxHDPLtWCRkF.jpg"},
        {"pk": 526896, "poster_url": "/8uiV88A5eB7PjMTtY6lQBUZ0Cpl.jpg"}
        ]
      },
      nightRecommend(){
        return [ {"pk": 453395, "poster_url": "/vL5ktZauR0fZMDOHKjakb1idhuU.jpg"},
        {"pk": 338953, "poster_url": "/uvQbXjMgC5weQepx4jLJJ60H3N0.jpg"},
        {"pk": 646385, "poster_url": "/j2lndg3r6pshxFJyDJZnn50EklS.jpg"}
        ]
      }
}
}
</script>

<style>
img {
  width: 100%;
  height: 500px;
}
</style>