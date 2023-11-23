<template>
  <tr class="border-top">
    <td>{{ product.fin_prdt_cd }}</td>
    <td>{{ product.kor_co_nm }}</td>
    <td>{{ product.fin_prdt_nm }}</td>
    <td>
      <RouterLink :to="{ name: 'ProductDetailView', params:{id: product.id}}">자세히 보기</RouterLink>
    </td>
      
  </tr>

</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import DepositOptionItem from '@/components/DepositOptionItem.vue'
const props = defineProps({
  product: Object,
})

const options = ref(props.product.depositoption_set)
</script>

<style scoped>
.option-table {
  width: 100%;
  text-align: center;

}
</style>