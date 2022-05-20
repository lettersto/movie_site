import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'

// accounts
import SignupView from '@/views/accounts/SignupView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import PasswordView from '@/views/accounts/PasswordView.vue'
import AccountsUserView from '@/views/accounts/AccountsUserView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'

// community
import CommunityView from '@/views/communities/CommunityView.vue'

// movies
import MovieView from '@/views/movies/MovieView.vue'
import MoviePeopleView from '@/views/movies/MoviePeopleView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  // Accounts
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/password',
    name: 'password',
    component: PasswordView
  },
  {
    path: '/user',
    name: 'user',
    component: AccountsUserView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },

  // community
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },

  // movies
  {
    path: '/movies/:moviePk',
    name: 'movies',
    component: MovieView
  },
  {
    path: '/movies/:personPK',
    name: 'moviepeople',
    component: MoviePeopleView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
