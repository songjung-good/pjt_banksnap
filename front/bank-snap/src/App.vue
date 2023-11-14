<template>
  <div>
    <h1>MAIN</h1>
    <RouterLink :to="{ name: 'map' }">MAP</RouterLink>
    <RouterLink :to="{ name: 'test' }">TEST</RouterLink>
    <div>
      <RouterView />
    </div>
  </div>

</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>

</style>