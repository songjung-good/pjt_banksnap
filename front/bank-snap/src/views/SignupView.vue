<template>
  <div>
    <h1>SignUp</h1>
    <form @submit.prevent="signUp">

    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

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