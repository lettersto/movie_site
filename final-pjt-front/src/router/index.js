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
import CommunityView from '@/views/community/CommunityView.vue'
import ArticleDetailView from '@/views/community/ArticleDetailView.vue'
import ArticleEditView from '@/views/community/ArticleEditView.vue'
import ArticleNewView from '@/views/community/ArticleNewView.vue'

// movies
import MovieView from '@/views/movies/MovieView.vue'
import MoviePeopleView from '@/views/movies/MoviePeopleView.vue'

// 404 Not Found
import NotFound404 from '@/views/NotFound404.vue'

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
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },

  // community
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/community/new',
    name: 'articleNew',
    component: ArticleNewView
  },
  {
    path: '/community/:articlePk',
    name: 'articleDetail',
    component: ArticleDetailView
  },
  {
    path: '/community/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView
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

  // 404
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// Navigation Guard 필요

export default router
