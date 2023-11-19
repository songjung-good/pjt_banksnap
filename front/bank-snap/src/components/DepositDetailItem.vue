<template>
    <div>
        <h1>상품</h1>
    </div>
    <!-- <tr class="border-top">
        <td>{{ product.fin_prdt_cd }}</td>
        <td>{{ product.kor_co_nm }}</td>
        <td>{{ product.etc_note }}</td>
        <td>{{ product.join_way }}</td>
    </tr>
    <tr>
        <td colspan="4">
        <table class="option-table">
            <tr>
            <th>타입</th>
            <th>가입 기간</th>
            <th>이율</th>
            <th>최대 이율</th>
            </tr>
            <DepositOptionItem
            v-for="option in options"
            :key="option.id"
            :option="option" 
            />
        </table>
        </td>
    </tr> -->
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
        // headers: {
        //   Authorization: `Token ${store.token}`
        // }
    })
    .then((res) =>{
        console.log(product)
        product.value = res.data
    })
    .catch((err) => {
        console.log(err)
    })
})
</script>

<style scoped>

</style>