<template>
  <div>
    <h1>SignUp</h1>
    <form @submit.prevent="signUp">
      <p>아이디 : <input type="text" v-model.trim="username"></p>
      <p>비밀번호 확인 : <input type="password" v-model.trim="password1"></p>
      <p>비밀번호 확인 : <input type="password" v-model.trim="password2"></p>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/Index'

const store = useIndexStore()

const username = ref('')
const password1 = ref('')
const password2 = ref('')

const signUp = function() {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}

</script>

<style scoped>

</style>