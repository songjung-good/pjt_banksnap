<template>
  <tr class="border-top">
    <td>{{ product.fin_prdt_cd }}</td>
    <td>{{ product.kor_co_nm }}</td>
    <td>{{ product.etc_note }}</td>
    <td>{{ product.join_way }}</td>
  </tr>
    <table>
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
</template>

<script setup>
import { ref } from 'vue'
import DepositOptionItem from '@/components/DepositOptionItem.vue'
const props = defineProps({
  product: Object,
})

const options = ref(props.product.depositoption_set)
console.log(options.value)
</script>

<style scoped>

</style>