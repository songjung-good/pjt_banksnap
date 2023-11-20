<template>
  <div class="text-center">
    <main class="form-signin">
      <form @submit.prevent="login">
        <img class="mb-4" src="../assets/logo_nonbackgroound.png" alt="" width="80" height="57">
        <h1 class="h3 mb-3 fw-normal">로그인페이지</h1>
        <div class="form-floating">
          <input type="text" v-model.trim="username" class="form-control" id="floatingInput" placeholder="ID">
          <label for="floatingInput">아이디</label>
        </div>
        <div class="form-floating">
          <input type="password" v-model.trim="password" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">비밀번호</label>
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">로그인</button>
        <p class="mt-5 mb-3 text-muted">안녕하세요, 고객님!</p>
      </form>
      <div class="modal" tabindex="-1" role="dialog" :class="{ 'show': showErrorModal }">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">로그인 실패</h5>
              <button type="button" class="btn-close" @click="closeErrorModal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              로그인에 실패했습니다. 아이디와 비밀번호를 다시 확인해주세요.
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" @click="closeErrorModal">닫기</button>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div> 
</template>     
    
<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/index'

const store = useIndexStore()
const username = ref('')
const password = ref('')

const login = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  const loginResult = store.login(payload)

  if (!loginResult) {
    // 로그인 실패 시 모달을 표시
    showErrorModal.value = true
  }
}
const closeErrorModal = function () {
  // 모달을 닫을 때 호출
  showErrorModal.value = false
}

</script>

<style scoped>
/* Bootstrap styles */
@import '@/assets/css/bootstrap.min.css';

/* Additional styles */
@import '@/assets/css/signin.css';

.text-center {
  text-align: center;
}
</style>