<template>
  <div>
    <button class="carousel-control left" @click="$emit('prev')">Prev</button>
    <button class="carousel-control right" @click="$emit('next')">Next</button>
    aafjsdlfjslajfl
  </div>
</template>

<script>
export default {
  name: 'CarouselControl',
  emits: {
    prev: String,
    next: String
  }

}
</script>

<style scoped>

  .carousel-control {
    background-color: rgba(0, 0, 0, .5);
    border: none;
    display: inline-block;
    position: absoulute;
    height: 50px;
    width: 70px;
    top: calc(50% -25px);
    color: #f3f3f3;
    cursor: pointer;
  }

  .left {
    left: 0;
  }

  .right {
    right: 0;
  }

</style>