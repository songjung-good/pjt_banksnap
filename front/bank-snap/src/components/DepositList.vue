<template>
  <div>
    <table class="table">
      <thead>

        <tr class="table-info">
          <th>상품 코드</th>
          <th>은행명</th>
          <th>상품명</th>
          <th>기타</th>
        </tr>
      </thead>
      <tbody>
        <DepositListItem
        v-for="product in products"
        :key="product.id"
        :product="product"
        />
      </tbody>
    </table>
    
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useIndexStore } from '@/stores/index'
import DepositListItem from '@/components/DepositListItem.vue'


const props = defineProps({
  type: String,
})
const store = useIndexStore()
const products = ref(null)
const options = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.url}/bank/product/${props.type}/`,
    
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

</style>