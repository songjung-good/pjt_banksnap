import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useCounterStore = defineStore('counter', () => {
  const url = ref('http://127.0.0.1:8000')
  const articles = ref([])

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${url.value}/articles/`,
      // headers: {
      //   Authorization: `Token ${token.value}`
      // }
    })
      .then((res) =>{
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  return { url, articles, getArticles }
})
