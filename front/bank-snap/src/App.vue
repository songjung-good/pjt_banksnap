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
  <!-- <footer class="center">
    <div class="dropdown position-fixed bottom-0 end-0 mb-3 me-3 bd-mode-toggle">
    <button class="btn btn-primary py-2 dropdown-toggle d-flex align-items-center"
      :id="bd-theme"
      type="button"
      aria-expanded="false"
      data-bs-toggle="dropdown"
      aria-label="Toggle theme (auto)">
      <svg class="bi my-1 theme-icon-active" width="1em" height="1em"><use :href="themeIconActive()"></use></svg>
      <span class="visually-hidden" id="bd-theme-text">Toggle theme</span>
    </button>
    <ul class="dropdown-menu dropdown-menu-end shadow" aria-labelledby="bd-theme-text">
      <li>
        <button type="button" class="dropdown-item d-flex align-items-center" @click="toggleTheme('light')" aria-pressed="false">
          <svg class="bi me-2 opacity-50 theme-icon" width="1em" height="1em"><use :href="themeIconInactive()"></use></svg>
          Light
          <svg class="bi ms-auto d-none" width="1em" height="1em"><use href="#check2"></use></svg>
        </button>
      </li>
      <li>
        <button type="button" class="dropdown-item d-flex align-items-center" @click="toggleTheme('dark')" aria-pressed="false">
          <svg class="bi me-2 opacity-50 theme-icon" width="1em" height="1em"><use :href="themeIconInactive()"></use></svg>
          Dark
          <svg class="bi ms-auto d-none" width="1em" height="1em"><use href="#check2"></use></svg>
        </button>
      </li>
      <li>
        <button type="button" class="dropdown-item d-flex align-items-center active" @click="toggleTheme('auto')" aria-pressed="true">
          <svg class="bi me-2 opacity-50 theme-icon" width="1em" height="1em"><use :href="themeIconActive()"></use></svg>
          Auto
          <svg class="bi ms-auto d-none" width="1em" height="1em"><use href="#check2"></use></svg>
        </button>
      </li>
    </ul>
  </div>
  </footer> -->
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useCounterStore  } from '@/stores/counter'

const router = useRouter()
const store = useCounterStore()

const user = ref(store.user)
const isLogin = ref(store.isLogin)
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

const toggleTheme = (theme) => {
  activeTheme.value = theme;
};

const themeClasses = () => {
  if (activeTheme.value === 'auto') {
    return 'theme-auto';
  } else if (activeTheme.value === 'light') {
    return 'theme-light';
  } else {
    return 'theme-dark';
  }
};

const themeIconActive = () => {
  if (activeTheme.value === 'auto') {
    return 'circle-half';
  } else if (activeTheme.value === 'light') {
    return 'sun-fill';
  } else {
    return 'moon-stars-fill';
  }
};

const themeIconInactive = () => {
  if (activeTheme.value === 'auto') {
    return 'sun-fill';
  } else if (activeTheme.value === 'light') {
    return 'moon-stars-fill';
  } else {
    return 'circle-half';
  }
};
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
