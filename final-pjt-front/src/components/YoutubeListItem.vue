<!--
<template>
  <div v-if="$store.state.youtubeVideos">
    <iframe :src="videoUrl" frameborder="0"></iframe>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'YoutubeListItem',
  computed: {
    ...mapGetters(['youtubeVideos']),
    videoURL: function () {
      const { videoId } = this.youtubeVideos.id
      return `https://www.youtube.com/embed/${videoId}`
    },
  }
}
</script>

<style>
</style>
-->