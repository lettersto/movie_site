<!--
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
import { mapGetters } from 'vuex'

export default {
  name: 'YoutubeList',
  props: {
    title: {
      type: String,
      required: true
    }
  },
  components: {
    YoutubeListItem
  },
  computed: {
    ...mapGetters([
      'youtubeVideos'
    ])
  },
    created() {
    this.$store.dispatch('searchYoutube', this.title)
  },
}
</script>

<style>

</style>
-->