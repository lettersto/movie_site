<template>
  <div class="about-wrapper">
    <div class="about-container">
      <h1 class="about-title">About Us</h1>
      <pre>
        영화란 무엇일까요?

        영화 속에는 우리 일상 생활의 많은 모습이 담겨있습니다.
        때로는 우리의 내면을 비추는 거울이 되기도 합니다.
        그렇기에 영화는 어떤 인물과 세계의 반영이자, 그림자이자, 혼입니다.

        저희는 사이트를 이용하는 모든 분들이
        영화의 인물과 함께 기뻐하고, 슬퍼하고, 때로는 화내며
        혼연일체로 즐기셨으면 하는 바람을 담아 만들었습니다.

        언제나 우리 사이트를 이용해 주시는 분들께
        감사 인사를 드립니다.

        문유주, 정혜령
      </pre>
    </div>

  </div>
</template>

<script>
  export default {
    name: 'AboutView',
  }
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Homemade+Apple&family=Nanum+Myeongjo&display=swap');

  * {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }

  .about-wrapper {
    /* position: relative; */
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 10.5rem;
  }

  .about-title {
    font-family: 'Homemade Apple', cursive;
    font-size: 4rem;
    font-weight: bold;
    margin-bottom: 2.5rem;
  }

  .about-container {
    background: none;
    /* width: 700px; */
    height: 400px;
    text-align: center;
  }

  .about-container pre {
    font-family: 'Nanum Myeongjo', serif;
    font-weight: 600;
    font-size: 1em;
    margin-right: 2em;
  }

</style>