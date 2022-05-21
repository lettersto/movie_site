<template>
  <div class="login-box">
   
    <account-error-list v-if="authError" />

    <form @submit.prevent="login(credentials)" @keyup.enter.prevent="login(credentials)">
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
          v-model="credentials.password" type="password" 
          id="password" class="form-control" 
          placeholder="비밀번호" required
        />
      </div>

      <div class="d-flex flex-column justify-content-center align-items-center mb-4">
        <div class="col">
          <button 
            type="button" 
            class="btn btn-primary btn-block mb-4"
            @click.prevent="login(credentials)">Log in</button>
        </div>
      </div>
    </form>


    <div class="text-center">
      <a href="#!">Forgot password?</a>
      <p>Not a member? <a href="#!">Register</a></p>
      <p>or sign up with:</p>
      <button type="button" class="btn btn-link btn-floating mx-1">
        CONTINUE WITH GOOGLE
      </button>
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

</style>