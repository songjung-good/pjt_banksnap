<template>
    <div class="p-2">
      <h1>외환상품</h1>
      <br>
      <div>
        <h3>환율 계산하기</h3>
        <div class="rounded-pill bg-light input-container">
          <div class="container">
            보유화폐 : 
            <select v-model="selectedCur1">
              <option v-for="data in dataList" :value="data.cur_nm"> {{ data.cur_nm }}</option>            
            </select>
            <input class="" type="number" v-model="exchangeMoney1">
          </div>
          ▶️
          <div class="container">
            기준화폐 :
            <select v-model="selectedCur2">
              <option v-for="data in dataList" :value="data.cur_nm">{{ data.cur_nm }}</option>            
            </select>
            <input type="number" v-model="exchangeMoney2" readonly>
          </div>
        </div>
      </div>
      <br>
      <div>

      <h3>환율 표</h3>
      <table class="table table-hover">
        <thead>
          <tr class="table-info">
            <th scope="col">국가</th>
            <th scope="col">송금 받을 때</th>
            <th scope="col">송금 보낼 때</th>
            <th scope="col">매매 기준율</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="data in dataList">
            <td>{{ data.cur_nm }}</td>
            <td>{{ data.ttb }}</td>
            <td>{{ data.tts }}</td>
            <td>{{ data.deal_bas_r }}</td>
          </tr>
        </tbody>
      </table>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { ref, onMounted, watch } from 'vue'
  import { useIndexStore } from '@/stores/index'
  
  
  const selectedCur1 = ref('미국 달러')
  const selectedCur2 = ref('한국 원')
  
  const exchangeMoney1 = ref(0)
  const exchangeMoney2 = ref(0)
  
  
  const dataList = ref([])
  const store = useIndexStore()
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.url}/bank/exchange/`
    })
      .then((res) => {
        dataList.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  })
  const cur1 = ref(null)
  const cur2 = ref(null)
  
  const exchange = function() {
    cur1.value = dataList.value.find(data => data.cur_nm === selectedCur1.value)
    cur2.value = dataList.value.find(data => data.cur_nm === selectedCur2.value)
    const deal = Number(cur1.value.deal_bas_r.replace(/,/g, '')) / Number(cur2.value.deal_bas_r.replace(/,/g, ''))
    exchangeMoney2.value = Number(exchangeMoney1.value) * deal
  }
  
  
  
  watch([exchangeMoney1, selectedCur1, selectedCur2], () => {
      exchange()
  })
  
  </script>
  
  <style scoped>
  tr, th, td {
    border-bottom: 1px solid black;
    padding: 3px;
  }

  .input-container {
  display: flex;
  gap: 10px; /* 좌우 간격을 조절할 값 (원하는 간격으로 조절) */
  justify-content: space-around; /* 입력 요소들을 동일한 간격으로 배치 */
  align-items: center; /* 세로 중앙 정렬을 위한 설정 */
}
  </style>