<template>
  <div>
    <PriceItem 
    v-for="item in items"
    :key="item.name"
    :item="item"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useIndexStore } from '@/stores/index'
import axios from 'axios'
import PriceItem from '@/components/PriceItem.vue'

const store = useIndexStore()
const items = ref([])
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
    })
    .catch((err) => {
      console.log(err)
    })
})
</script>

<style scoped>

</style>