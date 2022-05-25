<template>
<div>
<!-- {{ this.title }} -->
<!-- {{ youtubeVideos }} -->
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
// import axios from 'axios'
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'YoutubeList',
  components: {
    YoutubeListItem
  },
  props: {
    title: {
      type: String,
      required: true,
    }
  },
  computed:{
    ...mapGetters(['youtubeVideos']),
    isMovietitle() {
        return !_.isEmpty(this.title)
      },
  
  },
  methods: {
      ...mapActions([
        'searchYoutube',
        
      ]),
  },
  created(){
    console.log(this.title)
    this.searchYoutube(this.title)
  },
  
  
}
</script>

<style>

</style>