
<script setup>
import { ref, onMounted, onBeforeMount } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import { useIndexStore } from '@/stores/index'


const store = useIndexStore()
const route = useRoute()
const product = ref(null)
const likeButton = ref(null)
const isData = ref(false)

onBeforeMount(() => {
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
            likeButton.value = '즐겨찾기 취소'
        }else {
            likeButton.value = '즐겨찾기'
        }
        isData.value = true
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
            likeButton.value = '즐겨찾기 취소'
        }else{
            likeButton.value = '즐겨찾기'
        }

    })
    .catch((err) => {
        console.log(err)
    })

}

</script>
<template>
    <div v-if="isData">
        <main>
            <h1 class="text-body-emphasis">💰{{ product.fin_prdt_nm }}💰</h1>
            <br>    
            <p class="fs-5 col-md-8">은행 명 : {{ product.kor_co_nm }}</p>
            <p class="fs-5 col-md-8">가입 대상 : {{ product.join_member }}</p>
            <p class="fs-5 col-md-8">가입 방법 : {{ product.join_way }}</p>
            <p class="fs-5 col-md-8">상품 정보</p>
            
            <div class="fs-6 col-md-8" v-html="product.etc_note.replace(/\n/g, '<br>')"></div>
            <br>
            <p class="fs-5 col-md-8">금리</p>
            <table class="table">
                <thead>
                <tr>
                    <th>구분</th>
                    <th>기간</th>
                    <th>금리</th>
                    <th>최고 금리</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="option in product.depositoption_set" :key="option.id">
                    <td>{{ option.intr_rate_type_nm }}</td>
                    <td>{{ option.save_trm }}개월</td>
                    <td>{{ option.intr_rate }}</td>
                    <td>{{ option.intr_rate2 }}</td>
                </tr>
                </tbody>
                </table>

            <button class="btn btn-primary btn-lg" @click="likeProduct">{{ likeButton }}</button>


        </main>
        
    </div>
</template>

<style scoped>

</style>