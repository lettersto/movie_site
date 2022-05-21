<template>
    
  <div class="carousel">
    <div class="carousel-inner">
      <carousel-control @prev="prev" @next="next"/>
      <carousel-items 
        v-for="(slide, index) in slides" :key="`item-${index}`"
        :slide="slide" :currentslide="currentslide" :index="index"
        :direction="direction"
      />
    </div>
  </div>

</template>

<script>
import CarouselItems from '@/components/homes/CarouselItems.vue'
import CarouselControl from '@/components/homes/CarouselControl.vue'


export default {
  name: 'EventCarossel',
  components: {
    CarouselItems,
    CarouselControl
  },
  data() {
    return {
        currentslide: 0,
        slideinterval: null,
        direction: "right",
        slides: [
          "https://images.unsplash.com/photo-1585951237318-9ea5e175b891?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1032",
          "https://images.unsplash.com/photo-1585951237318-9ea5e175b891?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1032",
          "https://images.unsplash.com/photo-1552417559-f62e53cba705?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1032"
        ],
    }
  },
  methods: {
    setCurrentSlide(index) {
      this.currentslide = index; 
    },
    prev() {
      const index = this.currentslide > 0 ? this.currentslide - 1 : this.slides.length-1;
      this.setCurrentSlide(index);
      this.direction = "left";
    },
    next() {
      const index = this.currentslide < this.slides.length - 1 ? this.currentslide + 1 : 0;
      this.setCurrentSlide(index);
      this.direction = "right";
    }
  },
  mounted() {
    this.slideinterval = setInterval(() => {
      const index = this.currentslide < this.slides.length - 1 ? this.currentslide + 1 : 0;
      this.setCurrentSlide(index);
    }, 3000)
  },

  beforeUnmount() {
    clearInterval(this.slideInterval);
  }
}
</script>

<style scoped>

  .carousel {
    display: flex;
    justify-content: center;
  }

  .carousel-inner {
    position: relative;
    width: 900px;
    height: 400px;
    overflow: hidden;
  }

</style>