<script setup>
import { RouterLink } from 'vue-router'
import { computed } from 'vue'
import { useIndexStore } from '@/stores/index'
import Propensity from "@/components/Propensity.vue"

const store = useIndexStore()
const user = computed(() => {
  return store.user
})

</script>
<template>
  <div class="text-center p-5">
    <img class="mb-4" src="../assets/logo_nonbackgroound.png" alt="" width="80" height="57">
    <ul class="nav nav-tabs">
      <li class="nav-item">

          <RouterLink :to="{ name: 'ProfileView' , params:{id: user}}" class="nav-link">프로필</RouterLink>
      </li>
      <li class="nav-item">
          <p class="nav-link active" aria-current="page">내 금융정보</p>
      </li>
  </ul>
    <Propensity />
  </div>
</template>



<style scoped>
.nav-link {
  color: rgb(173, 173, 173);
}
</style>