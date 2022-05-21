<template>
  <div>
    <div class="focus-out" @click="modal=false"></div>
    <div class="serach-bar">
      <div class="search-box">
        <input 
          type="text" id="movie-search-input" 
          placeholder="영화 검색" 
          autocomplete="off"
          v-model="inputMovie"
          @input="filterMovie"
          @focus="modal=true"
        />
        <ul 
          v-if="filteredMovies.length !== 0 && modal && inputMovie"
          class="searched-list" 
        >
          <li 
            v-for="(movie, idx) in filteredMovies.slice(0, 10)" 
            :key="idx"
            @click="setInputValue(movie)"
            class="list-item"
          >
            {{ movie }}
          </li>
        </ul>
      </div>
      <!-- <button class="search-btn">
        <i class="material-icons">search</i>
      </button> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      inputMovie: "",
      modal: false,
      movies: [
        "The Marked Heart", "The Flash", "Heartstopper", "Encanto", "Bravo, My Life",
        "WandaVision", "Conversations with a Killer", "The King's Man", "Grey's Anatomy",
        "The Ice Age Adventures of Buck Wild", "Eternals", "No Exit", "All of Us Are Dead",
      ],
      filteredMovies: [],
    }
  },

  methods: {
    filterMovie() {
      this.filteredMovies = [];
      this.filteredMovies = this.movies.filter(movie => {
        return movie.toLowerCase().startsWith(this.inputMovie.toLowerCase());
      });
    },

    setInputValue(movie) {
      this.inputMovie = movie;
      this.modal = false;
    },
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
  /* width: 33%; */
  /* height: 100%; */
}


input[type="text"] {
  width: 100%;
  padding: 13px 13px;
  /* border: none; */
  border: 1px solid rgba(0, 0, 0, 0.3);
  outline: none;
  /* border-radius: 3px 3px 0 0; */
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

.list-item {
  width: 100%;
  background-color: #fffffffa;
  color: #00171F;
  padding: 0 13px 1em;
  font-size: 16px;
}

.search-btn {
  border: none;
  outline: none;
  width: 5em;
  color: #000f14d1;
  background-color: #fffffffa;
  cursor: pointer;
}

.search-btn:hover {
  background-color: #f4f4f4fa;
  color: #000f14;
}

</style>