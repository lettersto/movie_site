import Vue from 'vue'
import Vuex from 'vuex'
import movies from './modules/movies'
import community from './modules/community'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    movies, community
  }
})
