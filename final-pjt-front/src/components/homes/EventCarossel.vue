<template>
  <div class="carousel-wrapper my-4">
    <div class="carousel-container">
      <div id="carouselExampleFade" class="carousel slide carousel-fade carousel-content" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div v-for="(slide, index) in slides" :key="index" :class="index === 0 ? 'carousel-item active' : 'carousel-item'">
            <div class="container">
              <img class="d-block w-100" :src="slide" :alt="`image-${index}`" />
            </div>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>  
    </div>
  </div>

</template>

<script>
  export default {
    name: 'EventCarossel',
    data() {
      return {
          slides: [
            "https://images.unsplash.com/photo-1504701954957-2010ec3bcec1?ixlib=rb-1.2.1&raw_url=true&q=80&fm=jpg&crop=entropy&cs=tinysrgb&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774",
            "https://images.unsplash.com/photo-1542382156909-9ae37b3f56fd?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1243",
            "https://images.unsplash.com/photo-1606579331353-6454ed89ee3b?ixlib=rb-1.2.1&raw_url=true&q=80&fm=jpg&crop=entropy&cs=tinysrgb&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170",
            // "https://images.unsplash.com/photo-1507181280972-47966b705fd2?ixlib=rb-1.2.1&raw_url=true&q=80&fm=jpg&crop=entropy&cs=tinysrgb&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1332"
            // "https://images.unsplash.com/photo-1606579335925-ea67bcbd09c7?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170",
            // "https://images.unsplash.com/photo-1532568547949-a09f1afe4d1b?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870",
            // "https://images.unsplash.com/photo-1585951237318-9ea5e175b891?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870",
            // "https://images.unsplash.com/photo-1552417559-f62e53cba705?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870"
          ],
      }
    },
  }


</script>

<style scoped>


</style>