<template>
  <div class="weather-wrapper col-md-8 col-lg-4">
    <div class="weather-container">
      <div class="weather-card-box">
        <div class="weather-card">
          <router-link class="weather-link" :to="{ name: 'movies', params: { moviePk: movie.id } }">
            <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_url" alt="...">
          </router-link>
        </div>
      </div>
    </div>  
    <!-- <div>
      <div class="card">
      <router-link :to="{ name: 'movies', params: { moviePk: movie.id } }" class="nav-link">
        <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_url" class="card-img" alt="...">
      </router-link>
      </div>
    </div> -->
  </div>
</template>

<script>
  export default {
    name: 'WeatherRecItem',
    props: {
      movie: Object
    }
  }
</script>

<style scoped>

  .weather-wrapper {
    width: 90%;
  }

  @media (min-width: 992px) {
    .weather-wrapper {
      width: 33% !important;
    }
  }

  @media (min-width: 768px) {
    .weather-wrapper {
      width: 230px;
    }
  }

  .weather-link {
    display: flex;
    justify-content: center;
  }

  .weather-card img {
    width: 90%;
  }

</style>