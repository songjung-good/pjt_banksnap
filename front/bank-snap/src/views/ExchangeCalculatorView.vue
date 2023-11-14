<template>
    <div>
      <h1>Calculator</h1>
      <div>
        <h3>환율계산</h3>
        <div>
          <select v-model="selectedCur1">
            <option v-for="data in dataList" :value="data.cur_nm">{{ data.cur_nm }}</option>            
          </select>
          <input type="number" v-model="exchangeMoney1">
        </div>
        <div>     
          <select v-model="selectedCur2">
            <option v-for="data in dataList" :value="data.cur_nm">{{ data.cur_nm }}</option>            
          </select>
          <input type="number" v-model="exchangeMoney2" readonly>
        </div>
  
      </div>
  
  
  
      <div>
        <h3>환율 표</h3>
        <table>
          <tr>
            <th>국가</th>
            <th>송금 받을 때</th>
            <th>송금 보낼 때</th>
            <th>매매 기준율</th>
          </tr>
          <tr v-for="data in dataList">
            <td>{{ data.cur_nm }}</td>
            <td>{{ data.ttb }}</td>
            <td>{{ data.tts }}</td>
            <td>{{ data.deal_bas_r }}</td>
          </tr>
        </table>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { ref, onMounted, watch } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  
  
  const selectedCur1 = ref('미국 달러')
  const selectedCur2 = ref('한국 원')
  
  const exchangeMoney1 = ref(0)
  const exchangeMoney2 = ref(0)
  
  
  const dataList = ref([])
  const store = useCounterStore()
  
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
  </style>