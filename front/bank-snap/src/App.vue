

<script setup>
import { ref, computed } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useIndexStore  } from '@/stores/index'

const router = useRouter()
const store = useIndexStore()

const user = ref(null)
user.value = store.user
const isLogin = computed(()=>{
  return store.isLogin
})
console.log(isLogin)
const logout = ref(store.logout)
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

<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-light" data-bs-theme="light">
      <div class="center container-fluid">
        <a class="navbar-brand" href="#">
          <img alt="Pjt logo" class="logo" src="@/assets/logo_nonbackgroound.png" height="50" @click="goHome" />
        </a>
        <button class="navbar-toggler" type="button" @click="toggleNavbar">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" :class="{ 'show': isNavbarOpen }" @click="closeNavbar">
          <ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'main' }">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'test' }">장선생님의 영혼</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'DepositView' }">금리비교</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'exchangecalculator' }">환율계산기</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'map' }">MAP</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'community' }">커뮤니티</RouterLink>
            </li>
            <li class="nav-item" v-if="isLogin">
              <RouterLink class="nav-link" :to="{ name: 'ProfileView', params:{id: user}}">MyPage</RouterLink>
            </li>
            <div>              
              <!-- <button type="button" class="btn btn-outline-primary me-2" v-if="!isLogin"> -->
                <RouterLink v-if="!isLogin" class="btn btn-primary me-2" :to="{ name: 'LoginView' }" >Login</RouterLink>
              <!-- </button> -->
              <button type="button" class="btn btn-outline-primary me-2" @click="logout" v-if="isLogin">
                Logout
              </button>
              <!-- <button type="button" class=""> -->
                <RouterLink class="btn btn-primary me-2" :to="{ name: 'SignUpView' }">SignUp</RouterLink>
                <!-- </button> -->
              </div>
            </ul>
        </div>
      </div>
    </nav>
  </header>
  <body class="center">
    <RouterView :key="$route.fullPath"/>  
  </body>
</template>

<style scoped>
.logo {
  cursor: pointer;
}
</style>

<style>
.center {
    box-sizing: border-box;
    max-width: 1280px;
    margin: 0 auto;
  }
  @media screen and (min-width: 1024px) {
  .container {
    max-width: 1000px;
    margin: 0 auto;
  }
}
</style>
