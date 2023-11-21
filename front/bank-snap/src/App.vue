
<script setup>

</script>

<template>
  <main class="center">
    <router-view />
  </main>
</template>

<style>
/* Bootstrap styles */
@import '@/assets/css/bootstrap.min.css';

.center {
    box-sizing: border-box;
    max-width: 1280px;
    margin: 0 auto;
  }
  @media screen {
  .container {
    max-width: 1280px;
    margin: 0 auto;
  }
}
</style>
