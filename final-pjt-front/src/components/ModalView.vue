<template>
   <transition name="modal">
   <div class="modal-mask d-flex justify-content-end align-items-end">
       <iframe id="video" :src="videoURL" frameborder="0"></iframe>
       <div class="">
       <button class="modal-body" @click="$emit('close')">
         그만보기
        </button>
        </div>
   </div>
  </transition>
</template>


<script>
// import YoutubeList from '@/components/YoutubeList.vue'
import axios from 'axios'

export default {
    name:'ModalView',
    props: {
        movieId: {
        type: Number,
        required: true,
        }
  },
    data(){
    return{
    youtubeVideos: {
    },
    }
  },

    computed: {

    videoURL: function () {
      return 'https://www.youtube.com/embed/' + this.youtubeVideos['key']
        
    },
  },
  created(){
    const API_KEY = '0c02eb6a6fc6a16f9de3ac6df5f9623b'
    const API_URL = `https://api.themoviedb.org/3/movie/${this.movieId}/videos?api_key=${API_KEY}`
    axios({
        method: 'get',
        url: API_URL,
        //   params: {
        //       api_key: API_KEY,
        //   }
    })
    .then((response) => (this.youtubeVideos = response.data.results[0]))
         
      }

  }
      

</script>


<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
    top: 50%;
    left: 50%;
    -webkit-transform: translate(-50%, -50%);
    -moz-transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    -o-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);;
  width: 70%;
  height: 70%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  align-content:center;
  transition: opacity .3s ease;
}

#video {
  position: absolute;
  width: 100%;
  height: 100%;
}



</style>