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

const start = () => {
    // console.log(params)
    axios.get(searchURL, { params })
    .then((response) => {
        console.log(response.data)
        products.value = response.data.items
    }).catch((error) => {
        console.error(error)
    })
}

const params = ref({
        key: 'AIzaSyCu6NZ13UapmgRPfQ7Up-wptjpNpCjqsdo',
        part: 'snippet',
        q: searchTerm.value,
        maxResults: 4,
        type: 'video',
        // videoDuration: 'long'
    })


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

</script>

<template>
    <div>
        <div class="video-list">
            <div v-for="product in products" :key="product.id" class="video-card">
                <img :src="product.snippet.thumbnails.medium.url" alt="썸네일" @click="goDetail(product)">
                <strong>{{ product.snippet.title }}</strong>
            </div>
        </div>
    </div>
</template>

<style scoped>
.video-card{
    border: 1px solid black;
    width: 255px;
}

.video-card IMG{
    width: 250px;
    height: 200px;
    object-fit: fill;
}

.video-list {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}
</style>
