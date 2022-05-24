<template>
  <div>
    <div>
      <div class="card">
      <router-link :to="{ name: 'movies', params: { moviePk: movie.id } }" class="nav-link">
        <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_url" class="card-img" alt="...">
      </router-link>
      </div>
    </div>
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

<style>

</style>