<template>
  <div>
    <div class="err-box" v-for="(errors, field) in authError" :key="field">
      <ul>
        <li v-for="(error, idx) in errors" :key="idx">
          * {{ error }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['authError'])
    }
  }
</script>

<style scoped>

  .err-box {
    width: 80%;
    margin-left: 10%;
  }

  ul {
    padding: 0;
    margin: 0;
    list-style: none;
    text-align: center;
    color: #5d6d82;
  }
  
</style>