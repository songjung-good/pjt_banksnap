<template>
  <div class="p-5">
    <h1>{{ type }}</h1>
    <form @submit.prevent="writeArticle">
      
      <div class="input-group">
        <span class="input-group-text">제목</span>
        <input type="text" v-model.trim="title" id="title" class="form-control">
      </div>
      <br>
      <div class="input-group">
        <span class="input-group-text">내용</span>
        <textarea v-model.trim="content" id="content" class="form-control" rows="10" aria-label="내용"></textarea>
      </div>
      <div class="text-end">

        <input class="btn btn-outline-secondary px-4 m-1" type="submit" value="작성">
      </div>
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