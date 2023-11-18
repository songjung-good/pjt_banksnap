<template>
  <div>
    <h1>{{ username }} 님의 Profile</h1>
    <ProfileArticle />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

import ProfileArticle from '@/components/ProfileArticle.vue'
const store = useCounterStore()
const route = useRoute()

const username = ref('')
const articles = ref([])

onMounted(() => {
  axios({
      method: 'get',
      url: `${store.url}/user/profile/${route.params.id}`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) =>{
        console.log(res.data)
        username.value = res.data.user.username
        articles.value = res.data.articles
      })
      .catch((err) => {
        console.log(err)
      })
})

</script>

<style scoped>

</style>