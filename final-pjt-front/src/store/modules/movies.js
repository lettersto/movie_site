import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'

export default {
  state: {
    movies: [],
    movie: {},
    youtubeVideos: [],
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    youtubeVideos: state => state.youtubeVideos,
    isMovie: state => !_.isEmpty(state.movies),
    isTitle: state => !_.isEmpty(state.movie),
    },
  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIE_REVIEWS: (state, reviews) => (state.movie.reviews = reviews),
    SEARCH_VIDEOS: (state, youtubeVideos) => (state.youtubeVideos = youtubeVideos),
  },
  actions: {
    fetchMovies({ commit, getters }) {
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },

    fetchMovie({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
    createReview({ commit, getters }, { moviePk, content, vote_rate }) {
      const review = { content, vote_rate }

      axios({
        url: drf.movies.movieReviews(moviePk),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    updateReview({ commit, getters }, { moviePk, reviewPk, content, vote_rate }) {
      const review = { content, vote_rate }

      axios({
        url: drf.movies.movieReview(moviePk, reviewPk),
        method: 'put',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteReview({ commit, getters }, { moviePk, reviewPk }) {
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.movies.movieReview(moviePk, reviewPk),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_MOVIE_REVIEWS', res.data)
            })
            .catch(err => console.error(err.response))
        }
      },
    searchYoutube({ commit }, searchText) {
        const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
        const API_URL = 'https://www.googleapis.com/youtube/v3/search'
        axios({
          method: 'get',
          url: API_URL,
          params: {
            key: API_KEY,
            part: 'snippet',
            q: searchText,
            type: 'video',
            maxResults: 1,
          }
        })
        .then(response => {
          // console.log(response.data.items)
          commit('SEARCH_VIDEOS', response.data.items)
        })
      },
  },
}