<template>
  <div>
    <h1>Login</h1>
    <form>
      <div>
        <label for="username">아이디: </label>
        <input type="text" id="username" required />
      </div>
      <div>
        <label for="password">비밀번호: </label>
        <input type="password" id="password" required />
      </div>

      <button>로그인</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
}
</script>

<style>

</style>