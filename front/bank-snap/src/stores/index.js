import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'


export const useIndexStore = defineStore('index', () => {
  const router = useRouter()
  const url = ref('http://127.0.0.1:8000')
  const articles = ref([])
  const token = ref(null)
  const user = ref(null)
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
        articles.value = []
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2, age } = payload
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
        return login({
          username: username,
          password: password1
        })

      })
      .then((res) => {
        createUserInfo(age)
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const createUserInfo = function (age) {
    axios({
      method: 'post',
      url: `${url.value}/user/propensity/`,
      data: {
        age: age,
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const login = function (payload) {
    const { username, password } = payload

    return axios({
      method: 'post',
      url: `${url.value}/accounts/login/`,
      data: {
        username,
        password
      }
    })  
      .then((res) => {
        user.value = username
        token.value = res.data.key
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
        alert('아이디와 비밀번호를 확인해 주세요.')
      })
  }
  const logout = function () {
    axios({
      method: 'post',
      url: `${url.value}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        user.value = null
        router.push({name: 'main'})
      })
      .catch((err) => {
        console.log(err)
      })
  }



  return { url, articles, getArticles, login, signUp, logout, token, isLogin, user }
}, { persist: true })
