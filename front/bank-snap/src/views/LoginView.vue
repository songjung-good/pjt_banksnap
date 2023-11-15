<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <p>아이디 : <input type="text" v-model.trim="username"></p>
      <p>비밀번호 : <input type="password" v-model.trim="password"></p>
      <input type="submit">
    </form>
  </div>
</template>     
    
<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref('')
const password = ref('')

const login = function () {
  const payload = {
    usename: username.value,
    password: password.value
  }
  store.login(payload)
}

</script>

<style scoped>

</style>