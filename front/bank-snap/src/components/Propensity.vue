<script setup>
import { ref, onMounted } from 'vue'
import { useIndexStore } from '@/stores/index'
import axios from 'axios'
import { RouterLink } from 'vue-router'
const store = useIndexStore()
const username = ref(null)
const userId = ref(null)
const bank = ref(null)
const age = ref(-11)
const income = ref(-11)
const depositNow = ref(-11)
const depositType = ref('무')
onMounted(() => {
  axios({
  method: 'get',
  url: `${store.url}/user/propensity/`,
  headers: {
    Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      username.value = res.data.user_info.username
      userId.value =  res.data.user_info.id
      bank.value = res.data.bank_info.kor_co_nm
      age.value = res.data.age
      income.value = res.data.income
      depositNow.value = res.data.deposit_now
      depositType.value = res.data.deposit_type
    })
    .catch((err) => {
      console.log(err)
    })
})

</script>

<template>
  <div>
    <h1>{{ username }} 님의 정보 </h1>
    <div>
      <p>나이 : {{ age }}</p>
      <p>연봉 : {{ income }}</p>
      <p>선호 은행 : {{ bank }}</p>
      <p>보유 금액 : {{ depositNow }}</p>
      <p>투자 성향 : {{ depositType }}</p>
    </div>
  </div>
  <RouterLink v-if="userId" :to="{ name: 'PropensityUpdateView' }">정보 수정</RouterLink>

</template>
<style scoped>

</style>