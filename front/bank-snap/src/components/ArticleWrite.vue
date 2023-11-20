<template>
  <div>
    <h1>{{ type }}</h1>
    <form @submit.prevent="writeArticle">
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
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { useIndexStore } from '@/stores/index'
import { useRoute, useRouter } from 'vue-router'
const props = defineProps({
  type: String,
  id: Number,
})

const store = useIndexStore()
const router = useRouter()
const route = useRoute()
const title = ref(null)
const content = ref(null)
const type = ref(null)

onMounted(() => {
  type.value = props.type
  if (type.value === 'modify'){
    axios({
    method: 'get',
    url: `${store.url}/articles/${props.id}/`
    })
      .then((res) => {
        title.value = res.data.title
        content.value = res.data.content
      })
      .catch((err) => {
        console.log(err)
      })
  }
})


const writeArticle = function() {
  if (type.value === 'modify'){
    updateArticle()
  } else if (type.value === 'create'){
    createArticle()
  }
}

console.log(`Token ${store.token}`)
const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.url}/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.push({ name: 'DetailView', params: { id: res.data.id } })
    })
    .catch((err) => {
      console.log(err)
    })
}

const updateArticle = function () {
  axios({
    method: 'put',
    url: `${store.url}/articles/${props.id}/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.push({ name: 'DetailView', params: { id: res.data.id } })
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style scoped>

</style>