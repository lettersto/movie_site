import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

// Home
import HomeView from '@/views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'

// accounts
import SignupView from '@/views/accounts/SignupView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import PasswordChangeView from '@/views/accounts/PasswordChangeView.vue'
// import AccountsUserView from '@/views/accounts/AccountsUserView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'

// community
import CommunityView from '@/views/community/CommunityView.vue'
import ArticleDetailView from '@/views/community/ArticleDetailView.vue'
import ArticleEditView from '@/views/community/ArticleEditView.vue'
import ArticleNewView from '@/views/community/ArticleNewView.vue'

// movies
import MovieView from '@/views/movies/MovieView.vue'
import ActorDetailView from '@/views/movies/ActorDetailView.vue'
import DirectorDetailView from '@/views/movies/DirectorDetailView.vue'

// 404 Not Found
import NotFound404 from '@/views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
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
    path: '/password/change',
    name: 'passwordChange',
    component: PasswordChangeView
  },
  // {
  //   path: '/user',
  //   name: 'user',
  //   component: AccountsUserView
  // },
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
    path: '/movies/actor/:actorPk',
    name: 'actorDetail',
    component: ActorDetailView
  },
  {
    path: '/movies/director/:directorPk',
    name: 'directorDetail',
    component: DirectorDetailView
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
// Navigation Guard

router.beforeEach((to, from, next) => {
  const { isLoggedIn } = store.getters

  const noAuthPages = ['login', 'signup']

  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('로그인이 필요합니다.')
    next({ name: 'login' })
  } else {
    next()
  }

  if (!isAuthRequired && isLoggedIn) {
    next({ name: 'community' })
  }
})

export default router
