<template>
  <header>
    <img alt="Pjt logo" class="logo" src="@/assets/exlogo.gif" />
    <div class="wrapper">
      <nav>
        <RouterLink :to="{ name: 'test' }">TEST</RouterLink>
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
  <RouterView />
  
  <footer>

  </footer>

</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

header {
  display: flex;
  place-items: center;
  padding-right: calc(var(--section-gap) / 2);
}

</style>