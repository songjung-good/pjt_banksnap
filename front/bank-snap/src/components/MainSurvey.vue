<template>
  <div class="container">
    <h2 class="text-center">설문조사</h2>
    <div class="row">
      <div class="col-md-12">
        <div class="card">
          <div class="card-body">
            <div v-for="(question, index) in questions" :key="index">
              <h5 class="card-title">{{ question }}</h5>
              <p class="card-text">{{ question }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <button type="button" class="btn btn-primary" @click="submit">제출</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const questions = ref([
  '당신의 성별은?',
  '당신의 나이는?',
  '당신 질문은 물루는?',
  '당신의 취미는?',
  '당신의 직업은?',
]);

const answers = ref([]);

const submit = () => {
  // 답변 저장
  // 모달 창 닫기
};
</script>

<style scoped>
.card {
  margin-bottom: 20px;
}

.card-title {
  font-size: 20px;
}
</style>
