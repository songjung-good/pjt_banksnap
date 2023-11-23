<template>
  <div class="text-center">
    <main class="form-signin">
      <form @submit.prevent="signUp">
        <img class="mb-4" src="../assets/logo_nonbackgroound.png" alt="" width="80" height="57">
        <h1 class="h3 mb-3 fw-normal">회원가입</h1>
        <div class="form-floating pb-2">
          <input type="text" v-model.trim="username" class="form-control" id="floatingInput" placeholder="ID">
          <label for="floatingInput">아이디</label>
        </div>
        <div class="form-floating">
          <input type="password" v-model.trim="password1" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">비밀번호</label>
        </div>
        <div class="form-floating">
          <input type="password" v-model.trim="password2" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">비밀번호확인</label>
        </div>
        <div class="form-floating pb-2">
          <input type="number" v-model.trim="age" class="form-control" id="floatingInput" placeholder="Age">
          <label for="floatingInput">나이</label>
        </div>
        <button class="w-100 btn btn-lg btn-outline-success" type="submit">Sign in</button>
        <p class="mt-5 mb-3 text-muted">뱅크스냅에 오신 것을 환영합니다!</p>
      </form>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/Index'

const store = useIndexStore()

const username = ref('')
const password1 = ref('')
const password2 = ref('')
const age = ref(null)

const signUp = function() {
  if (!username.value){
    alert("아이디를 입력해 주세요.")
  } else if (!password1.value || !password2.value){
    alert("비밀번호를 입력해 주세요.")
  } else if(password1.value !== password2.value){
    alert("비밀번호가 일치하지 않습니다.")
  } else if(!age.value){
    alert("나이를 입력해 주세요.")
  } else{

    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      age: age.value
    }
    store.signUp(payload)
  }
}

</script>

<style scoped>
/* Bootstrap styles */
@import '@/assets/css/bootstrap.min.css';

/* Additional styles */
@import '@/assets/css/signin.css';
</style>