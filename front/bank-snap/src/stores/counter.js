import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'


export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const url = ref('http://127.0.0.1:8000')
  const articles = ref([])
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${url.value}/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload
    axios({
      method: 'post',
      url: `${url.value}/accounts/signup/`,
      data: {
        username,
        password1,
        password2
      }
    })
      .then((res) => {
        // console.log(res)
        login({
          username: username,
          password: password1
        })
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const login = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${url.value}/accounts/login/`,
      data: {
        username,
        password
      }
    })
      .then((res) => {
        // console.log(res)
        token.value = res.data.key
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }



  return { url, articles, getArticles, login, signUp, token, isLogin }
}, { persist: true })
