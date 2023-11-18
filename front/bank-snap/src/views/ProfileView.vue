<template>
  <div>
    <h1>{{ username }} 님의 Profile</h1>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'
const store = useCounterStore()
const route = useRoute()

const username = ref('')

onMounted(() => {
  axios({
      method: 'get',
      url: `${store.url}/user/profile/${route.params.id}`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) =>{
        username.value = res.data.username
      })
      .catch((err) => {
        console.log(err)
      })
})

</script>

<style scoped>

</style>