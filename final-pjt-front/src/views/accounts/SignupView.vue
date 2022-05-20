<template>
  <div>
    <h1>SignUp</h1>
    <form>
      <div>
        <label for="username">아이디: </label>
        <input type="text" id="username" />
      </div>
      <div>
        <label for="password1">비밀번호: </label>
        <input type="password" id="password1" />
      </div>
      <div>
        <label for="password2">비밀번호 확인: </label>
        <input type="password" id="password2" />
      </div>
      <div>
        <label for="email">이메일: </label>
        <input type="email" id="email" />
      </div>
      <button>회원 가입</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
}
</script>

<style>

</style>