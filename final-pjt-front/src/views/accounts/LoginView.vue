<template>
  <div>
    <h1>Login</h1>

    <account-error-list v-if="authError" />

    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">아이디: </label>
        <input v-model="credentials.username" type="text" id="username" required />
      </div>
      <div>
        <label for="password">비밀번호: </label>
        <input v-model="credentials.password" type="password" id="password" required />
      </div>

      <button>로그인</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/accounts/AccountErrorList.vue'


export default {
  name: 'LoginView',
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: '',
        password: ''
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['login'])
  }
}
</script>

<style>

</style>