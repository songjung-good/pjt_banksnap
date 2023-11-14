import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const url = ref('http://127.0.0.1:8000')
  return { url }
})
