<template>
  <div class="text-center p-5">
    <!-- <img class="m-3" src="../assets/logo_nonbackgroound.png" alt="" width="80" height="57"> -->
    <h1>정보 수정</h1>
    
    <form @submit.prevent="updatePropensity">
      <div class="card p-5 m-5">
        <div class="card-body">
          <div class="mb-3 row justify-content-center">
            <label for="age" class="col-sm-2 col-form-label">나이</label>
            <div class="col-sm-3">
              <input type="number" class="form-control" id="age" v-model="age">
            </div>
          </div>
          <div class="mb-3 row justify-content-center">
            <label for="income" class="col-sm-2 col-form-label">연봉</label>
            <div class="col-sm-3">
              <input type="number" class="form-control" id="income" v-model="income">
            </div>
          </div>
          <div class="mb-3 row justify-content-center">
            <label for="bank" class="col-sm-2 col-form-label">선호은행</label>
            <div class="col-sm-3">
              <select class="form-control" v-model="bankName" id="bank">
                <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>            
              </select>
            </div>
          </div>
          <div class="mb-3 row justify-content-center">
            <label for="type" class="col-sm-2 col-form-label">투자성향</label>
            <div class="col-sm-3">
              <select class="form-control" v-model="depositType" id="type">
                <option value="미선택">미선택</option>
                <option value="안정형">안정형</option>
                <option value="안정추구형">안정추구형</option>
                <option value="위험중립형">위험중립형</option>
                <option value="적극투자형">적극투자형</option>
                <option value="공격투자형">공격투자형</option>
              </select>
            </div>
          </div>
          <div class="mb-3 row justify-content-center">
            <label for="money" class="col-sm-2 col-form-label">보유 금액</label>
            <div class="col-sm-3">
              <input type="number" class="form-control" id="money" v-model="depositNow">
            </div>
          </div>
        </div>
      </div>
      <br>
        <button type="submit" class="btn btn-secondary">수정하기</button>
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
const banks = ["미선택", "우리은행", "한국스탠다드차타드은행", "대구은행", "부산은행", "광주은행", "제주은행", "전북은행", "경남은행", "중소기업은행", "한국산업은행", "국민은행", "신한은행", "농협은행주식회사", "하나은행", "주식회사 케이뱅크", "수협은행", "주식회사 카카오뱅크", "토스뱅크 주식회사"]

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