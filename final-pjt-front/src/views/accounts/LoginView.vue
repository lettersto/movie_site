<template>
  <div>
    <div class="form-container">      
      <h1>Login</h1>
      <account-error-list v-if="authError" />
      <form @submit.prevent="login(credentials)">

        <!-- <label for="username">아이디: </label> -->
        <input 
          v-model="credentials.username" type="text" 
          id="username" required
          placeholder="아이디"
        />
        <!-- <label for="password">비밀번호: </label> -->
        <input 
          v-model="credentials.password" type="password"
          id="password" required 
          placeholder="비밀번호"
        />
        <button>로그인</button>
      </form>
    </div>
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

<style scoped>
/* 
.form-container {
  display: flex;
  flex-direction: column;
  background-color: white;
  width: 25em;
  height: 25em;
  position: absolute;
  transform: translate(-50%, -50%);
  top: 50%;
  left: 50%;
  border-radius: 20px;
}

input {
  width: 85%;
  height: 38px;
  border-radius: 4px;
  border: 1px solid rgba(0, 0, 0, 0.3);
  outline: none;
  padding: 8px;
} */

</style>