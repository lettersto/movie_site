<template>
  <div>
    <label for="voteRange" class="form-label">Vote range</label>
    <input type="range" class="form-range" min="0" max="5" step="0.5" id="voteRange">
    <div class="mb-3">
      <label for="CommentArea" class="form-label">Comment</label>
      <textarea class="form-control" id="CommentArea" rows="3"></textarea>
    </div>

  </div>
</template>

<script>
export default {
  name: 'CommentForm',
}
</script>

<style>

</style>