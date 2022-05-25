<template>
  <div class="d-flex my-3" >
    <h3 class="weather-title">{{weatherRecSentence}}</h3>
    <weather-rec-item 
      v-for="movie in seletedWeatherMovie" :key="movie.id"
      :movie=movie
    />
  </div>
</template>

<script>
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
        seletedWeatherMovie: [],
        weatherRecSentence: ""
      }
    },

    computed: {
      ...mapGetters(['movies']),
    },

    methods:{
      ...mapActions(['fetchMovies']),
      onGeoSuccess(position) {
        const API_KEY = process.env.VUE_APP_WEATHER_API_KEY;

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
          this.weatherRecSentence = "☀️날씨가 맑아 기분 좋은 오늘의 영화"
        } else if (weather >= 801 && weather < 805) {
          this.currentGenreId1 = 10752
          this.currentGenreId2 = 10751
          this.currentGenreId3 = 10770
          this.weatherRecSentence = "☁️구름 껴 꿀꿀한 오늘의 영화"
        } else if (weather >= 700 && weather < 800) {
          this.currentGenreId1 = 9648
          this.currentGenreId2 = 99
          this.currentGenreId3 = 878
          this.weatherRecSentence = "🌪️흐린 날 스릴넘치는 영화"
        } else if (weather >= 600 && weather < 700) {
          this.currentGenreId1 = 10751
          this.currentGenreId2 = 10749
          this.currentGenreId3 = 18
          this.weatherRecSentence = "☃️눈오는 날 크리스마스를 기다리는 영화"
        } else if (weather >= 500 && weather < 600) {
          this.currentGenreId1 = 36
          this.currentGenreId2 = 10752
          this.currentGenreId3 = 80
          this.weatherRecSentence = "☔비오는 날 추적추적한 영화"
        } else if (weather >= 300 && weather < 400) {
          this.currentGenreId1 = 878
          this.currentGenreId2 = 14
          this.currentGenreId3 = 12
          this.weatherRecSentence = "🌂미묘한 날씨엔 미묘한 영화"
        } else if (weather >= 200 && weather < 300) {
          this.currentGenreId1 = 27
          this.currentGenreId2 = 37
          this.currentGenreId3 = 53
          this.weatherRecSentence = "⚡번개치는 날씨엔 번쩍번쩍한 영화"
        } else {
          this.currentGenreId1 = 35
          this.currentGenreId2 = 53
          this.currentGenreId3 = 16
          this.weatherRecSentence = "🎬 아무 이유 없이 보고싶은 영화"
        }
        // console.log(this.currentGenreId1)
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

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');


 .weather-title {
   font-family: 'Nanum Pen Script', cursive;
   font-weight: bold;
   padding-bottom: 5px;
   margin-left: 23px;
 }
</style>