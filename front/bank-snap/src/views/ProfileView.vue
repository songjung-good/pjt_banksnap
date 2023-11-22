<template>
  <div class="text-center p-5">
    <img class="mb-4" src="../assets/logo_nonbackgroound.png" alt="" width="80" height="57">
       
    <h1>{{ username }} 님의 Profile</h1>
    <template v-if="articles.length > 0">
      <ProfileArticle :articles="articles" />
    </template>
    <hr>
    <template v-if="comments.length > 0">
      <ProfileComment :comments="comments" />
    </template>
    <hr>
    <template v-if="products.length > 0">
      <ProfileProduct :products="products" />
    </template>
    
    <p>
      <RouterLink :to="{name: 'PropensityView'}" class="btn btn-secondary">내 금융 정보</RouterLink>
    </p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import { useIndexStore } from '@/stores/index'
import axios from 'axios'

import ProfileArticle from '@/components/ProfileArticle.vue'
import ProfileComment from '@/components/ProfileComment.vue'
import ProfileProduct from '@/components/ProfileProduct.vue'

const store = useIndexStore()
const route = useRoute()

const username = ref('')
const articles = ref([])
const comments = ref([])
const products = ref([])

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
        username.value = res.data.username
        articles.value = res.data.article_set
        comments.value = res.data.comment_set
        products.value = res.data.like_products
      })
      .catch((err) => {
        console.log(err)
      })
})

</script>

<style scoped>

</style>