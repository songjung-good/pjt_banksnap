<template>
  <div class="text-center">
    <main class="form-signin">
      <form @submit.prevent="login">
        <img class="mb-4" src="../assets/brand/bootstrap-logo.svg" alt="" width="72" height="57">
        <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

        <div class="form-floating">
          <input type="text" v-model.trim="username" class="form-control" id="floatingInput" placeholder="ID">
          <label for="floatingInput">ID</label>
        </div>
        <div class="form-floating">
          <input type="password" v-model.trim="password" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">Password</label>
        </div>

        <div class="checkbox mb-3">
          <label>
            <input v-model="rememberMe" type="checkbox" value="remember-me"> Remember me
          </label>
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
        <p class="mt-5 mb-3 text-muted">Welcome! BankSnap</p>
      </form>
    </main>
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
    username: username.value,
    password: password.value
  }
  store.login(payload)
}

</script>

<style scoped>

</style>