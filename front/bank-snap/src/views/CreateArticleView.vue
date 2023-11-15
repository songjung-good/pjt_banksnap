<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div>
        <label for="title">제목 : </label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용</label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const router = useRouter()
const title = ref(null)
const content = ref(null)

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.url}/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    // hearders: {
    //   Authorization: `Token ${store.token}`
    // }
  })
    .then((res) => {
      console.log(res)
      router.push({ name: 'community' })
    })
}


</script>

<style scoped>

</style>