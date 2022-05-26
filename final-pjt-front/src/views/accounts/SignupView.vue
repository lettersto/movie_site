<template>
  <div class="signup-box">
    <h1>Signup</h1>
    <account-error-list v-if="authError" />

    <form 
      @submit.prevent="onSignupSubmit(credentials)" 
      id="signup-form"
    >
      <!-- ID input -->
      <div class="signup-input-field">
        <input 
          v-model="credentials.username"
          type="text" id="username" 
          required 
        />
        <span></span>
        <label for="username">Username</label>
      </div>

      <!-- Password input -->
      <div class="signup-input-field">
        <input 
          v-model="credentials.password1" type="password" 
          id="password1" required
        />
        <i class="material-icons password-visibility" id="pass-vi-1" @click="visibilityToggle(1)">visibility</i>
        <span></span>
        <label for="password1">Password</label>
      </div>

      <div class="signup-input-field">
        <input 
          v-model="credentials.password2" type="password" 
          id="password2" required
        />
        <i class="material-icons password-visibility" id="pass-vi-2" @click="visibilityToggle(2)">visibility</i>
        <span></span>
        <label for="password2">Password Confirmation</label>
      </div>

      <div class="pass">
        <input type="submit" value="Signup">
      </div>
    </form>
  </div>
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
          username: "",
          password1: "",
          password2: ""
        },
        visbilityState: false,
      }
    },

    computed: {
      ...mapGetters(['authError'])
    },

    methods: {
      ...mapActions(['signup']),
      onSignupSubmit(credent) {
        this.signup(credent)
        this.credentials.username = ""
        this.credentials.password1 = ""
        this.credentials.password2  = ""
      },
      visibilityToggle(num) {
        if (this.state) {
          document.querySelector(`#password${num}`).setAttribute("type", "password");
          document.querySelector(`#pass-vi-${num}`).innerText="visibility";
          this.state = false;
        } else {
          document.querySelector(`#password${num}`).setAttribute("type", "text");
          document.querySelector(`#pass-vi-${num}`).innerText="visibility_off";
          this.state = true;
        }
      }

    },

    created() {
      this.$store.commit('SET_AUTH_ERROR', null)
    }
  }
</script>

<style scoped>
  .signup-box {
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

  .signup-box h1 {
    text-align: center;
    padding: 20px 0 0 0;
  }

  .signup-box #signup-form {
    padding: 0 40px;
    box-sizing: border-box;
  }

  #signup-form .signup-input-field {
    position: relative;
    border-bottom: 2px solid #adadad;
    margin: 30px 0;
  }

  .signup-input-field input {
    width: 100%;
    padding: 0 5px;
    height: 40px;
    font-size: 16px;
    border: none;
    background: none;
    outline: none;
  } 

  .signup-input-field label {
    position: absolute;
    top: 50%;
    left: 5px;
    color: #adadad;
    transform: translateY(-50%);
    pointer-events: none;
    font-size: 16px;
    transition: .5s;
  }

  .signup-input-field span::before {
    content: '';
    position: absolute;
    background: #B8C5D6;
    top: 40px;
    left: 0;
    width: 0%;
    height: 2px;
    transition: .5s;
  }

  .signup-input-field input:focus ~ label,
  .signup-input-field input:valid ~ label {
    top: -5px;
    color: #B8C5D6;
  }

  .signup-input-field input:focus ~ span::before,
  .signup-input-field input:valid ~ span::before {
    width: 100%;
  }

  .pass {
    margin: -5px 0 20px 5px;
    color: #a6a6a6;
    cursor: pointer;
  }

  input[type="submit"] {
    width: 100%;
    height: 50px;
    margin: 10px 0 25px;
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