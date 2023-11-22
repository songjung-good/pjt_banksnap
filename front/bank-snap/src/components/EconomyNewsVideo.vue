<script setup>  
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from "axios"

const apiKey = import.meta.env.VITE_VIDEO_API_KEY;
const router = useRouter()
const videos = ref([])
const searchURL = 'https://www.googleapis.com/youtube/v3/search?'
const searchTerm = '경제'

const params = {
        key: apiKey,
        part: 'snippet',
        q: searchTerm,
        maxResults: 6 ,
        order: 'date',
        type: 'video',
        safeSearch: "moderate",
    }
const start = () => {
  axios.get(searchURL, { params })
  .then((response) => { 
    videos.value = response.data.items
    for(var i=0; i<videos.value.length; i++){
      videos.value[i]['url'] = "https://www.youtube.com/watch?v=" + response.data.items[i].id.videoId
    }
  }).catch((error) => {
    console.error(error)
  })
}

onMounted(() => {
    start(); // 컴포넌트가 마운트되면 start 함수 실행
})

</script>

<template>
  <div class="card p-5 m-5">
    <h3>오늘의 경제 영상</h3>
    <div class="card-body">
      <div class="container">
        
        <div v-if="videos.length > 0" class="row justify-content-center row-cols-1 row-cols-m-3 g-3">
          
          <div v-for="video in videos" class="card mt-3 mb-3 mx-3" style="width: 18rem;">
            <a :href="video.url">
              <img :src="video.snippet.thumbnails.high.url" alt="" class="card-img-top">
              <div class="card-body">
                <h5 class="card-title" v-html="video.snippet.title"></h5>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
a{
  color: black;
  text-decoration: none;
}
</style>