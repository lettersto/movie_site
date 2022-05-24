<template>
  <!-- <div v-if="$store.state.youtubeVideos"> -->
    <iframe :src="videoURL" frameborder="0"></iframe>
    <!-- </div> -->
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'YoutubeListItem',
  props: {
    video: {
      type: Object,
      required: true
    },
  },
  computed: {
    ...mapGetters(['youtubeVideos']),
    videoURL: function () {
      const { videoId } = this.video.id
      console.log(videoId)
      return `https://www.youtube.com/embed/${videoId}`
    },
  }
}
</script>

<style>
</style>