<template>
  <div>
    <h1>{{ profile.username }}'s Profile</h1>
    <router-link :to="{ name: 'passwordChange' }" v-if="sameUser">
      비밀번호 변경
    </router-link>

    <p v-if="profile.email">email: {{ profile.email }}</p>
    <hr>
    <!-- 좋아요 -->
    <p>좋아요 누른 게시글</p>
    <hr>
    <div v-for="article in profile.like_articles" :key="article.id">
    <!-- <div v-if="profile.like_articles.length !== 0"> -->
      <router-link :to="{ name: 'articleDetail' , params:{ articlePk: article.id }}">
        {{ article.title }}
      </router-link>
    </div>
    <!-- 쓴 게시글 -->
    <!-- <div v-if="profile.articles.length !== 0"> -->
    <hr>
    <div>
      <p>{{ profile.username }}님이 작성한 글</p>
      <hr>
      <div v-for="article in profile.articles" :key="article.id">
        <router-link :to="{ name: 'articleDetail' , params:{ articlePk: article.id }}">
          <p>{{ article.title }}</p>
        </router-link>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile', 'currentUser']),
    sameUser() {
      return this.currentUser.username === this.profile.username
    }
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  }

}
</script>

<style>

</style>