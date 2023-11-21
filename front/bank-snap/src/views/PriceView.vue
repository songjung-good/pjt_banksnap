<template>
  <div>
    <h1>실시간 시세</h1>
    <RouterLink :to="{ name: 'EstateView' }">부동산</RouterLink>
    <Price />
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import Price from '@/components/Price.vue'


</script>

<style scoped>

</style> 