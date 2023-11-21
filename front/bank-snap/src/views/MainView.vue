<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router';
import axios from 'axios'

const router = useRouter()
const newsList = ref([])
const clientId = import.meta.env.VITE_clientId
const clientSecret = import.meta.env.VITE_clientSecret
const searchQuery = '금융' //'%EA%B8%88%EC%9C%B5'
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

<template>
  
  <div class="d-flex h-100 text-center text-white bg-dark">
    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
      <header class="mb-auto">
        <div>
          <h3 class="float-md-start mb-0">Cover</h3>
          <nav class="nav nav-masthead justify-content-center float-md-end">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
            <a class="nav-link" href="#">Features</a>
            <a class="nav-link" href="#">Contact</a>
          </nav>
        </div>
      </header>

      <main class="px-3">
        <h1>Cover your page.</h1>
        <p class="lead">Cover is a one-page template for building simple and beautiful home pages. Download, edit the text, and add your own fullscreen background photo to make it your own.</p>
        <p class="lead">
          <a href="#" class="btn btn-lg btn-secondary fw-bold border-white bg-white">Learn more</a>
        </p>
      </main>
    </div>
  </div>

  
  <div class="product-card">
    <h3 >오늘의 경제 이슈</h3>
    <ul>
      <div v-for="news in newsList" :key="news.title">
        <a :href="news.link">
          <li v-html="news.title"></li>
        </a>
      </div>
    </ul>
  </div>

</template>

<style scoped>
  .product-card{
    border: 1px solid black;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }

  .product-card IMG{
    width: 200px;
    height: 200px;
    object-fit: fill;
  }
  .bd-placeholder-img { 
    font-size: 1.125rem;
    text-anchor: middle;
    -webkit-user-select: none;
    -moz-user-select: none;
    user-select: none;
  }

  @media (min-width: 768px) {
    .bd-placeholder-img-lg {
      font-size: 3.5rem;
    }
  }

</style>
