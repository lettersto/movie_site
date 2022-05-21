<template>
  <div>
    <!-- 영화 포스터란 -->
    <div class="card mb-3">
      <div class="row g-0">
        <div class="col-md-4">
          <img src="https://movie-phinf.pstatic.net/20220516_144/1652687286550mcE4G_JPEG/movie_image.jpg?type=m203_290_2" class="img-fluid rounded-start" alt="...">
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h5 class="card-title">Example heading <span class="badge bg-secondary">평점</span></h5>
            <p class="card-text">개봉일: </p>
            <p class="card-text">감독: </p>
            <p class="card-text">배우: </p>
            <p class="card-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis, iste laboriosam sint, nobis eaque atque veniam accusamus itaque expedita dignissimos eligendi cupiditate velit magnam dolor veritatis accusantium aliquid hic a quos doloremque. Tenetur illo culpa provident assumenda, consectetur accusamus nihil praesentium? Voluptatibus tempora quia quibusdam odio necessitatibus dolore commodi aut.</p>
            <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
          </div>
        </div>
      </div>
    </div>
    <hr>

    <!-- 댓글란 -->
    <comment-list />
    
  </div>


</template>

<script>
  import CommentList from '@/components/CommentList.vue'


  export default {
    name: 'MovieView.vue',
    components: {
      CommentList
    }
  }
</script>

<style>

</style>