<template>
  <div class="password-change-box">
    <h1>Change Password</h1>
    <account-error-list v-if="authError" />

    <form id="password-form"
      @submit.prevent="onSubmit(credentials)">

      <!-- old password -->
      <div class="password-input-field">
        <input 
          v-model="credentials.old_password" 
          type="password" id="old_password" required 
        />
        <span></span>
        <label for="old_password">Old Password </label>
      </div>

      <!-- new password -->
      <div class="password-input-field">
        <input 
          v-model="credentials.new_password1" 
          type="password" 
          id="new_password1" required
        />
        <span></span>
        <label for="new_password1">New Password</label>
      </div>

      <!-- password confirmation -->
      <div class="password-input-field">
        <input 
          v-model="credentials.new_password2" 
          type="password" 
          id="new_password2" required
        />
        <span></span>
        <label for="new_password2">Password Confirmation</label>
      </div>
      <div class="pass">
        <input type="submit" value="Change Password">
      </div>
    </form>
  </div>
</template>

<script>
  import AccountErrorList from '@/components/accounts/AccountErrorList.vue'
  import { mapGetters, mapActions } from 'vuex'
  
  export default {
  components: { AccountErrorList },
    name: 'PasswordChangeView',
    props: {
      AccountErrorList
    },
    data() {
      return {
        credentials: {
          old_password: "",
          new_password1: "",
          new_password2: ""
        }
      }
    },

    computed: {
      ...mapGetters(['authError'])
    },

    methods: {
      ...mapActions(['passwordChange']),
      onSubmit(credentials) {
        this.passwordChange(credentials)
        this.credentials.old_password = ""
        this.credentials.new_password1 = ""
        this.credentials.new_password2 = ""
      }
    },

    created() {
      this.$store.commit('SET_AUTH_ERROR', null)
    }
  }
</script>

<style scoped>
  .password-change-box {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 450px;
    background: #ffffff;
    border-radius: 10px;
    border: 1px solid rgba(192, 192, 192, 0.2);
    font-family: 'Noto Sans KR', sans-serif;
    color: #272d2ddc;
    box-shadow: 0 20px 40px rgba(192, 192, 192, 0.3);
  }

  .password-change-box h1 {
    text-align: center;
    padding: 30px 0 0 0;
  }

  .password-change-box #password-form {
    padding: 0 40px;
    box-sizing: border-box;
  }

  #password-form .password-input-field {
    position: relative;
    border-bottom: 2px solid #adadad;
    margin: 30px 0;
  }

  .password-input-field input {
    width: 100%;
    padding: 0 5px;
    height: 40px;
    font-size: 16px;
    border: none;
    background: none;
    outline: none;
  } 

  .password-input-field label {
    position: absolute;
    top: 50%;
    left: 5px;
    color: #adadad;
    transform: translateY(-50%);
    pointer-events: none;
    font-size: 16px;
    transition: .5s;
  }

  .password-input-field span::before {
    content: '';
    position: absolute;
    background: #B8C5D6;
    top: 40px;
    left: 0;
    width: 0%;
    height: 2px;
    transition: .5s;
  }

  .password-input-field input:focus ~ label,
  .password-input-field input:valid ~ label {
    top: -5px;
    color: #B8C5D6;
  }

  .password-input-field input:focus ~ span::before,
  .password-input-field input:valid ~ span::before {
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

</style>