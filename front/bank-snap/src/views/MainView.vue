<!-- MainView.vue -->
<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const showModal = () => {
  router.push('/survey')
}

</script>

<template>
  <div class="d-flex h-100 text-center text-black bg-light">
    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
      <header class="mb-auto">
        <!-- <div>
          <h3 class="float-md-start mb-0">Cover</h3>
          <nav class="nav nav-masthead justify-content-center float-md-end">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
            <a class="nav-link" href="#">Features</a>
            <a class="nav-link" href="#">Contact</a>
          </nav>
        </div> -->
      </header>

      <main class="px-3">
        <h1>당신의 자산을 투자하세요.</h1>
        <p class="lead">가치있는 자산을 만들어, 고객의 오늘을 즐겁게. 당신이 직접 만들어 가는 가치 다양한 상품 확인하고 여러분의 자산을 투자하세요</p>
        <p class="lead">
          <a href="#" class="btn btn-lg btn-secondary fw-bold border-white bg-gray" @click="showModal">시작하세요</a>
        </p>
      </main>
    </div>
  </div>

</template>

<style scoped>

</style>
