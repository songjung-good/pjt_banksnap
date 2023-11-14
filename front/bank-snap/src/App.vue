<template>
  <header>
    <img alt="Pjt logo" class="logo" src="@/assets/exlogo.gif" width="125" height="125" />
    <div class="wrapper">
      <nav>
        <RouterLink :to="{ name: 'main' }">Home</RouterLink>
        <RouterLink :to="{ name: 'interestrate' }">금리비교</RouterLink>
        <RouterLink :to="{ name: 'exchangecalculator' }">환율계산기</RouterLink>
        <RouterLink :to="{ name: 'community' }">커뮤니티</RouterLink>
        <RouterLink :to="{ name: 'map' }">MAP</RouterLink>
        <!-- <RouterLink :to="{ name: 'user', params: {id: userId} } ">User</RouterLink> -->
        <!-- <RouterLink :to="{ name: 'login' } ">Login</RouterLink> -->
      </nav>
    </div>
  </header>

  <div>
    <h1>MAIN</h1>
      <RouterView />
  </div>

</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>

</style>