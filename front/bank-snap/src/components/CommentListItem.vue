<template>
  <div>
    <p>
      {{ comment.username }} : {{ comment.content }}
      <button v-if="comment.username === store.user" @click="deleteComment" class="btn btn-outline-secondary">댓글 삭제</button>
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/index'
import { useRouter } from 'vue-router'
import axios from 'axios'

const store = useIndexStore()
const router = useRouter()
const props = defineProps({
  comment: Object,
})

const deleteComment = function() {
  axios({
    method: 'delete',
    url: `${store.url}/articles/comment/delete/${props.comment.id}/`,
    // headers: {

    // }
  })
    .then((res) => {
      console.log(res.data)
      router.go()
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>