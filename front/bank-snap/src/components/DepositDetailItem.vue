<template>
    <div>
        <h1>상품</h1>
    </div>
    <!-- 정보 수정 필요 -->
    <p> {{ product }}</p>
    <button @click="likeProduct">좋아요</button>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'


const store = useCounterStore()
const route = useRoute()
const product = ref(null)

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.url}/bank/product/detail/${route.params.id}/`,

    })
    .then((res) =>{
        console.log(product)
        product.value = res.data

    })
    .catch((err) => {
        console.log(err)
    })
})

const likeProduct = function() {
    axios({
        method: 'post',
        url: `${store.url}/bank/product/like/${route.params.id}/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res) =>{
        console.log(res.data)
        // 좋아요 버튼 처리해야함!
    })
    .catch((err) => {
        console.log(err)
    })

}

</script>

<style scoped>

</style>