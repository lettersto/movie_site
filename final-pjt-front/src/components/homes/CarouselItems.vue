<template>
  <Transition :name="transitionEffect">
    <div class="carousel-item" v-show="currentslide === index">
      <img :src="slide">
      {{currentslide}}
    </div>
  </Transition>
</template>

<script>
  export default {
    name: 'CarouselItems',
    props: {
      slide: String,
      index: Number,
      currentslide: Number,
      direction: String
    },
    computed: {
      transitionEffect() {
        return this.direction === "right" ? "slide-out" : "slide-in";
      }
    }
  }
</script>

<style scoped>
  .carousel-item {
    position: absolute;
    inset: 0;
  }

  .slide-in-enter-active,
  .slide-in-leave-active,
  .slide-out-enter-active,
  .slide-out-leave-active {
    transition: all 1s ease-in-out;
  }

  .slide-in-enter-from {
    transform: translateX(-100%);
  }

  .slide-in-leave-to {
    transform: translateX(100%);
  }

  .slide-out-enter-from {
    transform: translateX(100%);
  }

  .slide-out-leave-to {
    transform: translateX(-100%);
  }
</style>