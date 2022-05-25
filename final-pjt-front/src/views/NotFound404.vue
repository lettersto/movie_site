<template>
  <div class="not-found-err-container">
    <div class="not-found-err">
      <h1>404</h1>
      <h3>Page Not Found</h3>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'NotFound404',

  }
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Antonio:wght@700&display=swap');

  .not-found-err {
    font-family: 'Antonio', sans-serif;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 12em;
    letter-spacing: .8em;
    /* transform: translate(-50%, -50%); */
  }

  .not-found-err h1 {
    font-size: 10em;
  }

  .not-found-err h3 {
    font-size: 2.3em;
    margin-left: 15px;
  }
  
</style>