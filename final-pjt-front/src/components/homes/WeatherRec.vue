<template>
  <div class="d-flex" >
    <weather-rec-item 
      v-for="movie in seletedWeatherMovie" :key="movie.id"
      :movie=movie
    />
    <hr>
  </div>
</template>

<script>
  // import _ from 'lodash'
  import WeatherRecItem from './WeatherRecItem.vue'
  import { mapGetters, mapActions } from 'vuex'

  export default {
    name: 'WeatherRec',
    components: {
      WeatherRecItem,
    },
    data() {
      return {
        currentWeatherId: 800,
        currentGenreId1: 10749,
        currentGenreId2: 12,
        currentGenreId3: 28,
        seletedWeatherMovie: []
      }
    },

    computed: {
      ...mapGetters(['movies']),
    },

    methods:{
      ...mapActions(['fetchMovies']),
      onGeoSuccess(position) {
        const API_KEY = "1862d1c4967555764bdeddf84816fa1d";
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        // console.log(latitude, longitude);
        const url = `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&appid=${API_KEY}&units=metric`
        fetch(url) // request & promise
          .then(res => res.json())
          .then(data => {
            // const cityName = data.name;
            const weather = data.weather[0].main;
            this.currentWeatherId = Number(weather);
            // console.log(data)
            // console.log(cityName, weather)
        })
      },
      onGeoError() {
        confirm("위치 정보가 있으면 더 좋은 추천 서비스를 제공 가능합니다. 그래도 끄시겠습니까?");
      },

      selectGenreBasedOnWeather(weather) {
        if (weather === 800) {
          this.currentGenreId1 = 10749
          this.currentGenreId2 = 12
          this.currentGenreId3 = 28
        } else if (weather >= 801 && weather < 805) {
          this.currentGenreId1 = 10752
          this.currentGenreId2 = 10751
          this.currentGenreId3 = 10770
        } else if (weather >= 700 && weather < 800) {
          this.currentGenreId1 = 9648
          this.currentGenreId2 = 99
          this.currentGenreId3 = 878
        } else if (weather >= 600 && weather < 700) {
          this.currentGenreId1 = 10751
          this.currentGenreId2 = 10749
          this.currentGenreId3 = 18
        } else if (weather >= 500 && weather < 600) {
          this.currentGenreId1 = 36
          this.currentGenreId2 = 10752
          this.currentGenreId3 = 80
        } else if (weather >= 300 && weather < 400) {
          this.currentGenreId1 = 878
          this.currentGenreId2 = 14
          this.currentGenreId3 = 12
        } else if (weather >= 200 && weather < 300) {
          this.currentGenreId1 = 27
          this.currentGenreId2 = 37
          this.currentGenreId3 = 53
        } else {
          this.currentGenreId1 = 35
          this.currentGenreId2 = 53
          this.currentGenreId3 = 16
        }
        console.log(this.currentGenreId1)
      },

      selectMovieBasedOnGenre(genreId1, genreId2, genreId3) {
        this.seletedWeatherMovie = this.movies.filter(movie => {
          return movie.genres.includes(genreId1) || movie.genres.includes(genreId2) || movie.genres.includes(genreId3)
        }).slice(0, 3)
      },

      setWeatherRecommendation() {
        navigator.geolocation.getCurrentPosition(this.onGeoSuccess, this.onGeoError);
        this.selectGenreBasedOnWeather(this.currentWeatherId)
        this.selectMovieBasedOnGenre(this.currentGenreId1, this.currentGenreId2, this.currentGenreId3)
      }
    },

    created() {
      this.fetchMovies()
      this.setWeatherRecommendation()
    }
  }

</script>

<style>

</style>