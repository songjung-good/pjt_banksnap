<template>
  <div>
    <h1>TEST PAGE</h1>
    <select v-model="selectLocal1">
      <option v-for="local1 in localType1"
        :value="local1">{{ local1 }}
      </option>            
    </select>
    <select v-model="selectLocal2">
      <option v-for="local2 in localType2"
        :value="local2">{{ local2 }}
      </option>            
    </select>
    <select v-model="selectLocal3">
      <option v-for="local3 in localType3"
        :value="local3">{{ local3 }}
      </option>            
    </select>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, watch, computed } from 'vue'
import { useIndexStore } from '@/stores/index'

import local from "@/assets/local.json"

const selectLocal1 = ref(Object.keys(local)[0])
const selectLocal2 = ref(Object.keys(local[selectLocal1.value])[0])
const selectLocal3 = ref(local[selectLocal1.value][selectLocal2.value][0])

const localType1 = ref(Object.keys(local))
const localType2 = computed(() => {
  return Object.keys(local[selectLocal1.value])
})
const localType3 = computed(() => {
  return local[selectLocal1.value][selectLocal2.value]
})

watch(selectLocal1, () => {
  selectLocal2.value = Object.keys(local[selectLocal1.value])[0]
})
watch(selectLocal2, () => {
  selectLocal3.value = local[selectLocal1.value][selectLocal2.value][0]
})

</script>

<style scoped>

</style>