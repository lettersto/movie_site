<template>
  <div>
    <h1>비밀번호 변경</h1>
    <account-error-list v-if="authError" />
    <form @submit.prevent="passwordChange(credentials)">
      <div>
        <label for="old_password">기존 비밀번호: </label>
        <input 
          v-model="credentials.old_password" 
          class="form-control" 
          type="password" id="old_password" required 
        />
      </div>
      <div>
        <label for="new_password1">새 비밀번호: </label>
        <input 
          v-model="credentials.new_password1" 
          class="form-control" type="password" 
          id="new_password1" required
        />
      </div>
      <div>
        <label for="new_password2">비밀번호 확인: </label>
        <input 
          v-model="credentials.new_password2" 
          class="form-control" type="password" 
          id="new_password2" required
        />
      </div>
      <button class="btn btn-outline-secondary">변경하기</button>
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
      ...mapActions(['passwordChange'])
    }
  }
</script>

<style>

</style>