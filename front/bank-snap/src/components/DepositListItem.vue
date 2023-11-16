<template>
  <tr>
    <td>{{ product.fin_prdt_cd }}</td>
    <td>{{ product.kor_co_nm }}</td>
    <td>{{ product.etc_note }}</td>
    <td>{{ product.join_way }}</td>
  </tr>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  product: Object,
})

</script>

<style scoped>

</style>