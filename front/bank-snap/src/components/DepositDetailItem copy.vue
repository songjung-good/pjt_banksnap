<template>
    <div>
        <h1>상품</h1>
        {{ product }}
        <hr>
        <button @click="likeProduct">{{ likeButton }}</button>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { useIndexStore } from '@/stores/index'


const store = useIndexStore()
const route = useRoute()
const product = ref(null)
const likeButton = ref(null)
onMounted(() => {
    axios({
        method: 'get',
        url: `${store.url}/bank/product/detail/${route.params.id}/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res) =>{
        product.value = res.data.product
        if (res.data.is_liked){
            likeButton.value = '좋아요 취소'
        }else {
            likeButton.value = '좋아요'
        }

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
        if (res.data.is_liked){
            likeButton.value = '좋아요 취소'
        }else{
            likeButton.value = '좋아요'
        }

    })
    .catch((err) => {
        console.log(err)
    })

}

</script>

<style scoped>

</style>