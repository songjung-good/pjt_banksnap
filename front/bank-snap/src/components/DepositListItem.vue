<template>
  <tr class="border-top">
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
  </tr>
  <RouterLink :to="{ name: 'ProductDetailView', params:{id: product.id}}">자세히 보기</RouterLink>
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