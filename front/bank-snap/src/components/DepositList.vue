<template>
  <div>
    <table>
      <tr>
        <th>상품 코드</th>
        <th>은행명</th>
        <th>정보</th>
        <th>가입 방법</th>
      </tr>
      <DepositListItem
      v-for="product in products"
      :key="product.id"
      :product="product"
      />
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import DepositListItem from '@/components/DepositListItem.vue'

const props = defineProps({
  type: String,
})
const store = useCounterStore()
const products = ref(null)


onMounted(() => {
  axios({
    method: 'get',
    url: `${store.url}/bank/product/${props.type}/`,
    // headers: {
    //   Authorization: `Token ${store.token}`
    // }
  })
    .then((res) =>{
      products.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})


</script>

<style scoped>

</style>
<style>
  tr, th, td {
    border-bottom: 1px solid black;
    padding: 3px;
  }
</style>