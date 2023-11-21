<template>
  <div>
    <h1>Detail</h1>
    <main class="flex-shrink-0">
    <div v-if="article">
        <div class="container">
          <h1 class="mt-5">제목 : {{ article.title }}</h1>
          <p class="text-end">작성일 : {{ article.created_at }} | 수정일 : {{ article.updated_at }}</p>
          <p class="lead">{{ article.content }}</p>
          <div class="text-end ">

            <div class="btn-group" role="group">
              <button @click="deleteArticle" class="btn btn-outline-secondary">삭제</button>
              <RouterLink class="btn btn-outline-secondary"
              :to="{name: 'CreateArticleView', query: { type: 'modify', id: $route.params.id }}">
              수정
              </RouterLink>
            </div>
          </div>
            <hr>
          </div>
        </div>
        <div class="container">

          <CommentList :article-id="$route.params.id" />
          <CommentWrite :article-id="$route.params.id"/>
        </div>
      </main>
      </div>
    </template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useIndexStore } from '@/stores/index'
import { useRoute, useRouter, RouterLink } from 'vue-router'
import CommentList from '@/components/CommentList.vue'
import CommentWrite from '@/components/CommentWrite.vue'
import moment from 'moment'

const store = useIndexStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const createdAt = ref(null)
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.url}/articles/${route.params.id}/`
  })
    .then((res) => {
      article.value = res.data
      article.value.created_at = moment(res.data.created_at).format('YYYY-MM-DD HH:mm:ss')
      article.value.updated_at = moment(res.data.updated_at).format('YYYY-MM-DD HH:mm:ss')
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
