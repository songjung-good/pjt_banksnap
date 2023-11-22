
<script setup>
import { ref, computed } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useIndexStore } from '@/stores/index'

const router = useRouter()
const store = useIndexStore()

const user = computed(() => {
  return store.user
})
const isLogin = computed(()=>{
  return store.isLogin
})
// console.log(isLogin)

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
    <nav class="navbar navbar-expand-lg bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">
          <img alt="Pjt logo" class="logo" src="@/assets/logo_nonbackgroound.png" height="50" @click="goHome" />
        </a>
        <button class="navbar-toggler bg-light" type="button" @click="toggleNavbar">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="navbar-collapse collapse" :class="{ 'show': isNavbarOpen }" @click="closeNavbar">
          <ul class="navbar-nav nav-tabs ms-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'main' }">
                🏡메인
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'community' }">
                📢커뮤니티
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'PriceView' }">
                👑현물 상품
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'DepositView' }">
                🐷저축성 상품
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'ExchangeCalculator' }">
                💹외환 상품
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'EconomyNews' }">
                📰경제뉴스
              </RouterLink>
            </li>
            <li class="nav-item" v-if="user">
              <RouterLink v-if="isLogin" class="nav-link" :to="{ name: 'ProfileView', params:{id: user}}">
                ⚙️내 정보
              </RouterLink>
            </li>
            <li>              
              <RouterLink v-if="!isLogin" class="nav-link" :to="{ name: 'LoginView' }" >
                🔑로그인
              </RouterLink>
            </li>
            <li>
              <a type="button" class="nav-link" @click="logout" v-if="isLogin">
                🔑로그아웃
              </a>
            </li>
            <li>
              <RouterLink v-if="!isLogin" class="nav-link" :to="{ name: 'SignUpView' }">
                🖋️회원가입
              </RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<style scoped>
@import '@/assets/css/bootstrap.min.css';
.logo {
  cursor: pointer;
}
.input-container {
  display: flex;
  gap: 10px; /* 좌우 간격을 조절할 값 (원하는 간격으로 조절) */
  justify-content: space-around; /* 입력 요소들을 동일한 간격으로 배치 */
  align-items: center; /* 세로 중앙 정렬을 위한 설정 */
}
.nav-link{
  color: white;
}
.nav-link:hover{
  color: rgb(187, 187, 187);
}
</style>

