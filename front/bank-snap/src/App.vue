<template>
  <header>
    <div class="center">
      <nav class="navbar navbar-expand-lg bg-#e3f2fd">
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
              <RouterLink class="nav-link" :to="{ name: 'DepositView' }">금리비교</RouterLink>
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
            <li class="nav-item" v-if="!isLogin">
              <RouterLink class="nav-link" :to="{ name: 'LoginView' }">Login</RouterLink>
            </li>
            <li class="nav-item" v-if="!isLogin">
              <RouterLink class="nav-link" :to="{ name: 'SignUpView' }">SignUp</RouterLink>
            </li>
            <li class="nav-item" v-if="isLogin">
              <RouterLink class="nav-link" :to="{ name: 'ProfileView', params:{id: user}}">MyPage</RouterLink>
            </li>
            <li class="nav-item" v-if="isLogin">
              <button @click="logout">Logout</button>
            </li>
          </ul>
        </div>
      </nav>
    </div>
  </header>
  <body class="center">
    <RouterView :key="$route.fullPath"/>  
  </body>
</template>

<script setup>
import { ref, computed } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useCounterStore  } from '@/stores/counter'

const router = useRouter()
const store = useCounterStore()

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

const activeTheme = ref('auto');

</script>


<style scoped>
.logo {
  cursor: pointer;
}
</style>

<style>
body {
    box-sizing: border-box;
    max-width: 1000px;
    margin: 0 auto;
  }
  @media screen and (min-width: 1024px) {
  .container {
    max-width: 1000px;
    margin: 0 auto;
  }
}
</style>
