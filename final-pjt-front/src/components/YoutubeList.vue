<template>
<div>
{{ this.title }}
  <ul class="youtube-list">
    <youtube-list-item
      v-for="video in youtubeVideos"
      :key="video.id.videoId"
      :video="video"/>
  </ul>
</div>
</template>

<script>
import YoutubeListItem from '@/components/YoutubeListItem.vue'
import axios from 'axios'

// import { mapGetters } from 'vuex'

export default {
  name: 'YoutubeList',
  components: {
    YoutubeListItem
  },
  props: {
    title: {
      type: String,
      // required: true
    }
  },
  data(){
    return{
    youtubeVideos: []
    }
  },
  computed:{
    movietitle(){
      return this.title
    },
    },

  // computed: {
  //   ...mapGetters([
  //     'youtubeVideos'
  //   ])
  // },
  created() {
    console.log(this.movietitle)
    const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
    const API_URL = 'https://www.googleapis.com/youtube/v3/search'
        axios({
          method: 'get',
          url: API_URL,
          params: {
            key: API_KEY,
            part: 'snippet',
            q: this.movietitle,
            type: 'video',
            maxResults: 1,
          }
        })
        .then(response =>  (this.youtubeVideos = response.data.items))
    
    // this.$store.dispatch('searchYoutube', this.title)
  },
}
</script>

<style>

</style>