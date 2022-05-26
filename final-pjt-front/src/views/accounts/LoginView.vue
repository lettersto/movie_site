<template>
  <div class="login-box">
    <h1>Login</h1>
    <account-error-list v-if="authError" class="login-err" />

    <form 
      @submit.prevent="onLoginSubmit(credentials)" 
      id="login-form"
    >
      <!-- ID input -->
      <div class="login-input-field">
        <input 
          v-model="credentials.username"
          type="text" 
          id="username"
          required 
        />
        <span></span>
        <label for="username">Username</label>
      </div>

      <!-- Password input -->
      <div class="login-input-field">
        <input 
          v-model="credentials.password" type="password" 
          id="password" 
          required
        />
        <i class="material-icons password-visibility" id="pass-vi" @click="visibilityToggle()">visibility</i>
        <span></span>
        <label for="password">Password</label>
      </div>

      <div class="pass">Forgot Password?</div>
        <input type="submit" value="Login">
        <div class="signup-link">
          Not a member? <router-link :to="{ name: 'signup' }" class="signup-text">Sign up</router-link>
        </div>

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
          username: "",
          password: ""
        },
        visbilityState: false,
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login']),
      onLoginSubmit(credentials) {
        this.login(credentials)
        this.credentials.username = "",
        this.credentials.password = ""
      },
      visibilityToggle() {
        if (this.visbilityState) {
          document.querySelector("#password").setAttribute("type", "password");
          document.querySelector("#pass-vi").innerText="visibility";
          this.visbilityState = false;
        } else {
          document.querySelector("#password").setAttribute("type", "text");
          document.querySelector("#pass-vi").innerText="visibility_off";
          this.visbilityState = true;
        }
      }
    },

    created() {
      this.$store.commit('SET_AUTH_ERROR', null)
    },
  }
  
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');

  .login-box {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 400px;
    background: #ffffff;
    border-radius: 10px;
    border: 1px solid rgba(192, 192, 192, 0.2);
    font-family: 'Noto Sans KR', sans-serif;
    color: #272d2ddc;
    box-shadow: 0 20px 40px rgba(192, 192, 192, 0.3);
  }

  .login-box h1 {
    text-align: center;
    padding: 20px 0 0 0;
  }

  .login-box #login-form {
    padding: 0 40px;
    box-sizing: border-box;
  }

  #login-form .login-input-field {
    position: relative;
    border-bottom: 2px solid #adadad;
    margin: 30px 0;
  }

  .login-input-field input {
    width: 100%;
    padding: 0 5px;
    height: 40px;
    font-size: 16px;
    border: none;
    background: none;
    outline: none;
  }

  .login-input-field label {
    position: absolute;
    top: 50%;
    left: 5px;
    color: #adadad;
    transform: translateY(-50%);
    pointer-events: none;
    font-size: 16px;
    transition: .5s;
  }

  .login-input-field span::before {
    content: '';
    position: absolute;
    background: #B8C5D6;
    top: 40px;
    left: 0;
    width: 0%;
    height: 2px;
    transition: .5s;
  }

  .login-input-field input:focus ~ label,
  .login-input-field input:valid ~ label {
    top: -5px;
    color: #B8C5D6;
  }

  .login-input-field input:focus ~ span::before,
  .login-input-field input:valid ~ span::before {
    width: 100%;
  }

  .pass {
    margin: -5px 0 20px 5px;
    color: #a6a6a6;
    cursor: pointer;
  }

  .pass:hover {
    text-decoration: underline;
  }

  input[type="submit"] {
    width: 100%;
    height: 50px;
    border: 1px solid;
    background: #B8C5D6;
    border-radius: 25px;
    font-size: 18px;
    color: #FFFFFF;
    font-weight: 700;
    cursor: pointer;
    outline: none;
  }

  input[type="submit"]:hover {
    border-color: #B8C5D6;
    transition: .5s;
  }

  .signup-link {
    margin: 30px 0;
    text-align: center;
    font-size: 16px;
    color: #666666;
  }

  .signup-link .signup-text {
    color: #B8C5D6;
    text-decoration: none;
  }

  .signup-link .signup-text:hover {
    text-decoration: underline;
  }

  .password-visibility {
    position: absolute;
    right: 10px;
    transform: translate(0, -40%);
    top: 50%;
    cursor: pointer;
    font-size: 20px;
    color: #a6a6a6;
  }



</style>