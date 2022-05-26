<template>
  <div class="d-flex my-5">
    <div v-show="6 <= hour && hour < 14">
      <div class="row d-flex justify-content-around time-box">
        <h3 class="time-title">오늘 아침 피곤을 날려버릴 영화</h3>
        <div class="time-wrapper time-card col-md-8 col-lg-4" v-for="rec in morningRecommend" :key="rec.pk">
          <router-link class="time-link"
            :to="{ name: 'movies', params: { moviePk: rec.pk } }">
            <img :src="'https://image.tmdb.org/t/p/w500' + rec.poster_url" alt="...">
          </router-link>
        </div>
      </div>
    </div>
    <div v-show="14 <= hour && hour < 20">
      <div class="row d-flex justify-content-around time-box">
        <h3 class="time-title">나른한 오후 나를 흥미진진하게 할 영화</h3>
        <div class="time-wrapper time-card col-md-8 col-lg-4" v-for="rec in eveningRecommend" :key="rec.pk">
          <router-link class="time-link"
            :to="{ name: 'movies', params: { moviePk: rec.pk } }">
            <img :src="'https://image.tmdb.org/t/p/w500' + rec.poster_url" alt="...">
          </router-link>
        </div>
      </div>
    </div>
    <div v-show="20 <= hour && hour <= 24 || 0 <= hour && hour < 6">
      <div class="row d-flex justify-content-around time-box">
        <h3 class="time-title">오늘 저녁 나와 함께 할 영화</h3>
        <div class="time-wrapper time-card col-md-8 col-lg-4" v-for="rec in nightRecommend" :key="rec.pk">
          <router-link class="time-link"
            :to="{ name: 'movies', params: { moviePk: rec.pk } }">
            <img :src="'https://image.tmdb.org/t/p/w500' + rec.poster_url" alt="...">
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
    // movieURL() {
    //   return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_url
    // },  
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
    },
    
  }
}
</script>

<style scoped>

  @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');

  .time-title {
    /* position: absolute; */
    font-family: 'Nanum Pen Script', cursive;
    font-weight: bold;
    padding-bottom: 5px;
    margin-left: 3rem;
  }

  .time-wrapper {
    width: 90%;
  }

  @media (min-width: 992px) {
    .time-wrapper {
      width: 30% !important;
    }
    .time-title {
      margin-left: 6rem !important;
    }
  }

  @media (min-width: 768px) {
    .time-wrapper {
      width: 220px;
    }

    .time-title {
      margin-left: 3rem;
    }
  }

  .time-link {
    display: flex;
    justify-content: center;
  }

  .time-card img {
    width: 90%;
  }

</style>