<template>
  <ul class="youtube-list">
    <youtube-list-item
      v-for="video in youtubeVideos"
      :key="video.id.videoId"
      :video="video"/>
  </ul>
</template>

<script>
import YoutubeListItem from '@/components/YoutubeListItem.vue'
import axios from 'axios'

// import { mapGetters } from 'vuex'

export default {
  name: 'YoutubeList',
  data(){
    return{
    youtubeVideos: [],
    }
  },
  props: {
    title: {
      type: String,
      required: true
    }
  },
  components: {
    YoutubeListItem
  },
  // computed: {
  //   ...mapGetters([
  //     'youtubeVideos'
  //   ])
  // },
  created() {
    console.log(this.title)
    const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
    const API_URL = 'https://www.googleapis.com/youtube/v3/search'
        axios({
          method: 'get',
          url: API_URL,
          params: {
            key: API_KEY,
            part: 'snippet',
            q: this.title,
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