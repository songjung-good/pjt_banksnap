<template>
  <div>

    <form @submit.prevent="createComment">
      <div class="input-group">
        <span class="input-group-text">댓글</span>
        <textarea class="form-control" aria-label="With textarea" v-model.trim="content"></textarea>
        <input type="submit" value="댓글 작성" class="btn btn-outline-secondary">
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/index'
import { useRouter } from 'vue-router'
import axios from 'axios'


const store = useIndexStore()
const content = ref(null)
const router = useRouter()
const props = defineProps({
  articleId: String,
})

// console.log(`Token ${store.token}`)
const createComment = function () {
  axios({
    method: 'post',
    url: `${store.url}/articles/comments/${props.articleId}/`,
    data: {
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res)
      // router.push({ name: 'DetailView', params: { id: props.articleId }})
      router.go()
    })
    .catch((err) => {
      console.log(err)
    })
}



</script>

<style scoped>

</style>