const HOST = "http://localhost:8000/api/v1/"

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COMMUNITY = 'community/'

export default {
  accounts: {
    signup: () => HOST + ACCOUNTS + 'signup/',
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    user: () => HOST + ACCOUNTS + 'user/',
    passwordChange: () => HOST + ACCOUNTS + 'password/change/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username +'/',
    // passwordReset: () => HOST + ACCOUNTS + 'password/reset/'
    // passwordRestComfirm: () => HOST + ACCOUNTS + 'password/rest/confirm/'
  },

  movies: {
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    movieReviews: moviePk => HOST + MOVIES + `${moviePk}/` + 'reviews/',
    movieSearch: movieName => HOST + MOVIES + `${movieName}/`,
    personSearch: personPk => HOST + MOVIES + `${personPk}/`,
    weatherRec: () => HOST + MOVIES + 'weather-rec/',
    randomRec: () => HOST + MOVIES + 'random-rec/',
    rankingLike: () => HOST + MOVIES + 'ranking/like/',
    rankingNew: () => HOST + MOVIES + 'ranking/new/',
    rankingCom: () => HOST + MOVIES + 'ranking/community/'
  },

  community: {
    articles: () => HOST + COMMUNITY + '', 
    article: articlePk => HOST + COMMUNITY + `${articlePk}/`,
    likeArticle: articlePk => HOST + COMMUNITY + `${articlePk}/` + 'like/',
    comments: articlePk => HOST + COMMUNITY + `${articlePk}/` + 'comments/',
    comment: (articlePk, commentPk) => HOST + COMMUNITY + `${articlePk}/` + 'comments/' + `${commentPk}/`,
    articleSearch: articleTitle => HOST + COMMUNITY + `${articleTitle}/`,
    announce: () => HOST + COMMUNITY + 'announce/',
    hotTopic: () => HOST + COMMUNITY + 'hotTopic/'
  }
}