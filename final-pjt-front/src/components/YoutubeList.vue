<!--
<template>
<div>
{{ this.title }}
{{ youtubeVideos }}
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

import { mapGetters } from 'vuex'

export default {
  name: 'YoutubeList',
  components: {
    YoutubeListItem
  },
  props: {
    title: {
      type: String,
      required: true
    }
  },
  computed:{
    ...mapGetters(['youtubeVideos']),
  },
  updated(){
    this.$store.dispatch('searchYoutube')
  }
  
}
</script>

<style>

</style>
-->