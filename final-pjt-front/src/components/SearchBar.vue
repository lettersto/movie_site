<template>
  <li @click="onClick(movie.id)" class="movie-searched-list-items">
    {{ movie.title }}
  </li>
</template>

<script>
export default {
  name: 'SearchBar',

  props: {
      movie: Object
  },
  methods: {
      onClick(movieId) {
        this.$router.push({ name: 'movies', params: { moviePk: movieId}})

      }
    }

}
</script>

<style scoped>

  .focus-out {
    position: absolute;
    z-index: -1;
    inset: 0;
  }

  .serach-bar {
    display: flex;
  }

  .search-box {
    position: relative;
    width: 30vw;
  }


  input[type="text"] {
    width: 100%;
    padding: 13px 13px;
    border: 1px solid rgba(0, 0, 0, 0.3);
    outline: none;
    background-color: #fffffffa;
    font-size: 16px;
    z-index: 10;
  }

  li:hover {
    cursor: pointer;
    color: #000000;
    font-weight: bold;
  }

  ul {
    list-style: none;
    position: absolute;
    width: 100%;
  }

  .list-items {
    width: 100%;
    background-color: #fffffffa;
    color: #00171F;
    padding: 0 13px 1em;
    font-size: 16px;
  }

  .list-items:hover {
    cursor: pointer;
    color: #000000;
    font-weight: bold;
  }

  .movie-searched-list-items {
    list-style: none;
    cursor: pointer;
  }

  .movie-searched-list-items:hover {
    font-weight: bold;
  }


</style>