<template>
  <div class="p-3">

    
      <ul class="nav nav-tabs">
        <li class="nav-item">
          <div class="nav-link" :class="{ 'active': activeTab === 'gold' }" @click="itemClick('gold', 0)">금</div>
        </li>
        <li class="nav-item">
          <div class="nav-link" :class="{ 'active': activeTab === 'silver' }" @click="itemClick('silver', 1)">은</div>
        </li>
        <li class="nav-item">
          <div class="nav-link" :class="{ 'active': activeTab === 'oil' }" @click="itemClick('oil', 2)">가솔린</div>
        </li>
        <li class="nav-item">
          <div class="nav-link" :class="{ 'active': activeTab === 'gas' }" @click="itemClick('gas', 3)">천연가스</div>
        </li>

        <li class="nav-item">
          <div class="nav-link" :class="{ 'active': activeTab === 'coffee' }" @click="itemClick('coffee', 4)">커피</div>
        </li>
        <li class="nav-item">
          <div class="nav-link" :class="{ 'active': activeTab === 'corn' }" @click="itemClick('corn', 5)">옥수수</div>
        </li>

      </ul>
      <div v-if="item">
        <PriceItem :item="item" />
      </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useIndexStore } from '@/stores/index'
import axios from 'axios'
import PriceItem from '@/components/PriceItem.vue'

const store = useIndexStore()
const items = ref([])
const item = ref(null)
const activeTab = ref('gold')
onMounted(() => {
  axios({
  method: 'get',
  url: `${store.url}/bank/price/`,
  // headers: { 
  //   Authorization: `Token ${store.token}`
  //   }
  })
    .then((res) => {
      items.value = res.data
      item.value = items.value[0]
    })
    .catch((err) => {
      console.log(err)
    })
})

const itemClick = function(itemName, n){
  activeTab.value = itemName
  item.value = items.value[n]
}
</script>

<style scoped>
.nav-link {
  color: rgb(173, 173, 173);
}
</style>