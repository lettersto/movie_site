<template>
  <div>
    <div class="comment-container">
      <div class="comment-card">
        <router-link :to="{ name: 'profile', params: { username: comment.user.username } }"
          class="comment-link">
          <p class="comment-author">{{ comment.user.username }}</p>
        </router-link>
        <p class="comment-content">{{ comment.content }}</p>
        <div class="comment-footer" v-if="currentUser.username === comment.user.username">
          <div v-if="!isEditing">
            <button @click="toggleEditingBtn" class="comment-btn">
              <i class="material-icons">edit</i>
            </button>
            <button @click="deleteComment(newComment)" class="comment-btn">
              <i class="material-icons">delete</i>
            </button>
          </div>
          <div v-if="isEditing" class="comment-edit-box">
            <input type="text" v-model="newComment.content" class="comment-input">
            <button @click="onUpdate" class="comment-btn">
              <i class="material-icons">update</i>
            </button>
            <button @click="toggleEditingBtn" class="comment-btn">
              <i class="material-icons">edit_off</i>
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- <tr>
      <td class="text-center align-middle">
        <router-link :to="{ name: 'profile', params: { username: comment.user.username } }"
          class="author">
          {{ comment.user.username }}
        </router-link> </td>
      <td class="text-center align-middle">
        {{ comment.content }}
      </td>
      <td class="text-center align-middle">
        <div v-if="currentUser.username === comment.user.username">
          <div v-if="!isEditing">
            <button @click="toggleEditingBtn" class="btn btn-default">
              <i class="material-icons">edit</i>
            </button>
            <button @click="deleteComment(newComment)" class="btn btn-default">
              <i class="material-icons">delete</i>
            </button>
          </div>
        </div>
        <div v-if="isEditing">
          <input type="text" v-model="newComment.content">
          <button @click="onUpdate" class="btn btn-default">
            <i class="material-icons">file_upload</i>
          </button>
          <button @click="toggleEditingBtn" class="btn btn-default">
            <i class="material-icons">edit_off</i>
          </button>
        </div>
      </td>
    </tr> -->

  </div>
</template>

<script>

  import { mapGetters, mapActions } from 'vuex'

  export default {
    name: 'CommentListItem',
    props: {
      comment: Object,
    },
    data() {
      return{
        isEditing: false,
        newComment: {
          articlePk: this.comment.article,
          commentPk: this.comment.pk,
          content: this.comment.content
        }
      }
    },
    computed: {
      ...mapGetters(['currentUser'])
    },
    methods: {
      ...mapActions(['updateComment', 'deleteComment']),
      toggleEditingBtn() {
        this.isEditing = !this.isEditing;
      },
      onUpdate() {
        this.updateComment(this.newComment);
        this.isEditing = false;
      },
    }
  }
</script>

<style scoped>
  *, 
  *::before, 
  *::after {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }

  .comment-container {
    position: relative;
    padding: 0 5px;
    margin-bottom: 1em;
    transition: .3s;
  }

  .comment-container:hover {
    transform: scale(1.05);
  }

  .comment-card {
    padding: 20px;
    background-color: #ffffff;
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 0.5rem;
    line-height: 1.7em;
    text-align: justify;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
  }

  .comment-footer {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
  }

  .comment-btn {
    background: none;
    border: none;
    padding: 0 5px;
    margin-top: 4px;
  }

  .comment-link {
    text-decoration: none;
  }

  .comment-author {
    color: gray;
  }


  .comment-author:hover {
    color: black;
    cursor: pointer;
    text-decoration: underline;
  }

  .comment-edit-box {
    display: flex;
    flex-direction: row;
    justify-content: center;
    text-align: center;
  }

  .comment-input {
    outline: none;
    border: 1px solid rgba(0, 0, 0, 0.2);
    border-radius: 5px;
    padding: 0 10px;
  }

  /* .comment-container::before {
    content: "";
    background-color: rgb(170, 170, 170);
    position: absolute;
    min-height: 100%;
    width: 1px;
    left: 10px;
  } */

  /* .author {
    text-decoration: none;
    color: black;
  }

  .author:hover {
    text-decoration: underline;
  } */
</style>