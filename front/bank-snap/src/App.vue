
<script setup>
import MainNavbar from '@/components/MainNavbar.vue';
import MainSurvey from '@/components/MainSurvey.vue';
</script>

<template>
  <main class="center">
    <MainNavbar />
    <router-view />
    <MainSurvey />
  </main>
</template>

<style>
/* Bootstrap styles */
body {
  font-family: 'Nanum Gothic', sans-serif;
}
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