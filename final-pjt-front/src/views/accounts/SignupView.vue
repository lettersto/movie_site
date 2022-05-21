<template>
  <div class="login-box">
   
    <account-error-list v-if="authError" />

    <form @submit.prevent="signup(credentials)" @keyup.enter.prevent="signup(credentials)">
      <!-- ID input -->
      <div class="form-outline mb-4">
        <input 
          v-model="credentials.username"
          type="text" 
          id="username" class="form-control" 
          placeholder="아이디" required 
        />
      </div>

      <!-- Password input -->
      <div class="form-outline mb-4">
        <input 
          v-model="credentials.password1" type="password" 
          id="password1" class="form-control" 
          placeholder="비밀번호" required
        />
      </div>

      <div class="form-outline mb-4">
        <input 
          v-model="credentials.password2" type="password" 
          id="password2" class="form-control" 
          placeholder="비밀번호 확인" required
        />
      </div>

      <div class="d-flex flex-column justify-content-center align-items-center mb-4">
        <div class="col">
          <button 
            type="button" 
            class="btn btn-primary btn-block mb-4"
            @click.prevent="signup(credentials)">회원 가입</button>
        </div>
      </div>
    </form>
  </div>

  <!-- <div>
    <h1>SignUp</h1>

    <account-error-list v-if="authError" />

    <form @submit.prevent="signup(credentials)">
      <div>
        <label for="username">아이디: </label>
        <input v-model="credentials.username" type="text" id="username" required/>
      </div>
      <div>
        <label for="password1">비밀번호: </label>
        <input v-model="credentials.password1" type="password" id="password1" required/>
      </div>
      <div>
        <label for="password2">비밀번호 확인: </label>
        <input v-model="credentials.password2" type="password" id="password2" required/>
      </div>
      <button>회원 가입</button>
    </form>
  </div> -->
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/accounts/AccountErrorList.vue'


export default {
  name: 'SignupView',
  components: {
    AccountErrorList
  },
  data() {
    return {
      credentials: {
        username: '',
        password1: '',
        password2: ''
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['signup'])
  }
}
</script>

<style>

</style>