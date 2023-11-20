<template>
  <div>
    <p>
      {{ comment.user }} : {{ comment.content }}
      <button @click="deleteComment">댓글 삭제</button>
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import axios from 'axios'

const store = useCounterStore()
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