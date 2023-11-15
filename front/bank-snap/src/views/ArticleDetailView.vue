<template>
  <div>
    <h1>Detail</h1>
    <div v-if="article">
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <p>작성일 : {{ article.created_at }}</p>
      <p>수정일 : {{ article.updated_at }}</p>
    </div>

    <button @click="deleteArticle">글 삭제</button>
    <RouterLink 
      :to="{name: 'CreateArticleView', query: { type: 'modify', id: $route.params.id }}">
      수정
    </RouterLink>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter, RouterLink } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.url}/articles/${route.params.id}/`
  })
    .then((res) => {
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

const deleteArticle = function() {
  axios({
    method: 'delete',
    url: `${store.url}/articles/${article.value.id}/`,
    // headers: {

    // }
  })
    .then((res) => {
      router.push({ name: 'community' })
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style>

</style>
