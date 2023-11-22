<template>
<div class="product-card">
    <h2>오늘의 경제 이슈</h2>
    <ul>
        <div v-for="news in newsList" :key="news.title">
        <a :href="news.link">
            <li v-html="news.title"></li>
        </a>
        </div>
    </ul>
</div>

<EconomyNewsVideo />
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router';
import axios from 'axios'

const router = useRouter()
const newsList = ref([])
const clientId = import.meta.env.VITE_clientId
const clientSecret = import.meta.env.VITE_clientSecret
const searchQuery = '경제' //'%EA%B8%88%EC%9C%B5'
const displayCount = 10
const startPage = 1
const sortOption = 'sim'
const searchURL = `/v1/search/news?query=${searchQuery}&display=${displayCount}&start=${startPage}&sort=${sortOption}`

onMounted(() => {
  axios.get(searchURL, {
    headers: {
      'X-Naver-Client-Id':clientId,
      'X-Naver-Client-Secret':clientSecret
    }
  })
    .then((response) => {
      newsList.value = response.data.items
    })
    .catch((error) => {
      console.error(error)
    })
})

    // 삼항연산자는 가독성을 위함 / 없어도 boolean값 반환
const imgIsEmpty = computed(() => {
    return newsList.value.length > 0 ? true : false
})
</script>

<style scoped>
  .product-card{
    border: 1px solid black;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }
</style>
