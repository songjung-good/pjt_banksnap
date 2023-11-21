
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
              <RouterLink class="btn btn-outline-light nav-link" :to="{ name: 'main' }">
                🏡메인
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link btn btn-outline-light" :to="{ name: 'community' }">📢커뮤니티</RouterLink>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Dropdown</a>
              <ul class="dropdown-menu">
                <li>
                  <RouterLink class="dropdown-item btn btn-outline-light" :to="{ name: 'PriceView' }">📰투자 정보</RouterLink>
                </li>
                  <li>
                    <RouterLink class="dropdown-item btn btn-outline-light" :to="{ name: 'DepositView' }">🐷예적금 상품</RouterLink>
                  </li>
                  <li>
                    <RouterLink class="dropdown-item btn btn-outline-light" :to="{ name: 'ExchangeCalculator' }">💹환율계산기</RouterLink>
                  </li>
                </ul>
              </li>
              <li class="nav-item" v-if="isLogin">
              <RouterLink v-if="user" class="nav-link btn btn-outline-info" :to="{ name: 'ProfileView', params:{id: user}}">⚙️MyPage</RouterLink>
            </li>
            <li>              
              <RouterLink v-if="!isLogin" class="nav-link btn btn-outline-info" :to="{ name: 'LoginView' }" >🔑Login</RouterLink>
            </li>
            <li>
              <a type="button" class="nav-link btn btn-outline-info" @click="logout" v-if="isLogin">
                🔑Logout
              </a>
            </li>
            <li>
              <RouterLink class="nav-link btn btn-outline-info" :to="{ name: 'SignUpView' }">🖋️SignUp</RouterLink>
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
</style>

