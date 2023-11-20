<template>
  <div>
    <h1>정보 수정</h1>
    <form @submit.prevent="updatePropensity">
      <div>
        <p>나이 : <input type="number" v-model="age"></p>
        <p>연봉 : <input type="number" v-model="income"></p>
        <p>선호은행 : 
          <select v-model="bankName">
            <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>            
          </select>
        </p>
        <p>투자성향 : <input type="text" v-model="depositType"></p>
        <p>보유금액 : <input type="number" v-model="depositNow"></p>
      </div>
      <button type="submit">수정하기</button>
    </form>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { useIndexStore } from '@/stores/index'
import { useRoute, useRouter } from 'vue-router'

const store = useIndexStore()
const router = useRouter()
const route = useRoute()

const age = ref(null)
const income = ref(null)
const bankName = ref(null)
const depositNow = ref(null)
const depositType = ref(null)
const banks = ["우리은행", "한국스탠다드차타드은행", "대구은행", "부산은행", "광주은행", "제주은행", "전북은행", "경남은행", "중소기업은행", "한국산업은행", "국민은행", "신한은행", "농협은행주식회사", "하나은행", "주식회사 케이뱅크", "수협은행", "주식회사 카카오뱅크", "토스뱅크 주식회사"]

onMounted(() =>{
  axios({
  method: 'get',
  url: `${store.url}/user/propensity/`,
  headers: {
    Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      bankName.value = res.data.bank_info.kor_co_nm
      age.value = res.data.age
      income.value = res.data.income
      depositNow.value = res.data.deposit_now
      depositType.value = res.data.deposit_type
    })
    .catch((err) => {
      console.log(err)
    })
})


const updatePropensity = function () {
  axios({
    method: 'put',
    url: `${store.url}/user/propensity/`,
    data: {
      bank_name : bankName.value,
      age : age.value,
      income : income.value,
      deposit_now : depositNow.value,
      deposit_type : depositType.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.push({name: 'PropensityView'})
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>