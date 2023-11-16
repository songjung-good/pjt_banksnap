<template>
  <header px-8>
    <nav class="navbar navbar-expand-lg">
      <div class="container px-8">
        <a class="navbar-brand" href="#">
          <img alt="Pjt logo" class="logo" src="@/assets/logo_nonbackgroound.png" height="50" @click="goHome" />
        </a>
        <button class="navbar-toggler" type="button" @click="toggleNavbar">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" :class="{ 'show': isNavbarOpen }" @click="closeNavbar">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'main' }">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'test' }">장선생님의 영혼</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'interestrate' }">금리비교</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'exchangecalculator' }">환율계산기</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'community' }">커뮤니티</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'map' }">MAP</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'LoginView' }">Login</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'SignUpView' }">SignUp</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <body>
    <RouterView :key="$route.fullPath"/>  
  </body>
  <footer>
    
  </footer>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()

const goHome = () => {
  router.push('/')
}
const isNavbarOpen = ref(false);

const toggleNavbar = () => {
  isNavbarOpen.value = !isNavbarOpen.value;
}

const closeNavbar = () => {
  isNavbarOpen.value = false;
}

</script>

<style scoped>
body {
  box-sizing: border-box;
}

nav {
  background-color: #e3f2fd;
  /* position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000; */
}

  .logo {
  cursor: pointer;
}

</style>