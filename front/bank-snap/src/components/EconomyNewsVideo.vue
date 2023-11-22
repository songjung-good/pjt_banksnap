<script setup>
import { defineStore } from 'pinia'
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from "axios"

const apiKey = process.env.VITE_VIDEO_API_KEY;
const router = useRouter()
const products = ref([])
const searchURL = 'https://www.googleapis.com/youtube/v3/search?'
const searchTerm = '경제'

const params = {
        key: apiKey,
        part: ['snippet'],
        q: searchTerm,
        maxResults: 8,
        order: 'date',
        type: ['video'],
        safeSearch: "moderate",
    }

const start = () => {
  axios.get(searchURL, { params })
  .then((response) => {
    console.log(response.data)
    products.value = response.data.items
  }).catch((error) => {
    console.error(error)
  })
}


const goDetail = (video) => {
    router.push({
        name: 'videodetail',
        params: {
            video: video.id.videoId
        },
        state: {
            data: params,
        },
    })
}

const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString('ko-KR', options);
};

onMounted(() => {
    start(); // 컴포넌트가 마운트되면 start 함수 실행
})

</script>

<template>
  <div>
    <div class="video-list">
      <div v-for="product in products" :key="product.id" class="video-card">
        <img :src="product.snippet.thumbnails.medium.url" alt="썸네일" @click="goDetail(product)">
        <strong>{{ product.snippet.title }}</strong>
        <p>{{ formatDate(product.snippet.publishedAt) }}</p>
        <p>{{ product.snippet.description }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.video-card{
    border: 1px solid black;
    width: 255px;
    margin-bottom: 20px;
}

.video-card img {
  width: 100%;
  height: auto;
}

.video-card strong {
  display: block;
  margin-top: 10px;
  font-size: 16px;
}

.video-card p {
  font-size: 14px;
  margin-top: 5px;
}
</style>




