<template>
  <div class="container">
    <h2 class="text-center">당신의 투자성향은?</h2>
    <div class="row">
      <div class="col-md-12">
        <div class="card">
          <div class="card-body">
            <div v-for="(question, index) in questions" :key="index">
              <h5 class="card-title">{{ question.title }}</h5>
              <div class="form-check" v-for="(answer, answerIndex) in question.answers" :key="answerIndex">
                <input class="form-check-input" type="radio" :id="`question-${index}-answer-${answerIndex}`" v-model="selectedAnswers[index]" :value="answer">
                <label class="form-check-label" :for="`question-${index}-answer-${answerIndex}`">{{ answer }}</label>
              </div>
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
  { title: '고객님의 연령대는 어떻게 되시나요?', answers: ['19세 이하', '20~59세', '60세 이상'] },
  { title: '고객님의 연소득은 어떻게 되시나요?', answers: ['5천만원 이하', '5천만원 ~ 7천만원', '7천만원 ~ 1억원', '1억원 이상'] },
  { title: '고객님께서 금융상품 투자 시 감내할 수 있는 손실은 어느 정도 되시나요?', 
    answers: ['손실을 원하지 않음(무조건 원금 보전)', '원금의 30%까지 손실은 감내할 수 있음', '원금의 50%까지 손실은 감내할 수 있음', '원금 100% 손실까지 감내할 수 있음'] 
  },
  { title: '고객님의 투자 자금의 투자 예정 기간은 얼마나 되시나요?', 
    answers: ['1년 미만', '1 ~ 3년', '3년 이상', '원금 100% 손실까지 감내할 수 있음'] 
  },
  { title: '고객님께서 금융상품을 투자하는 목적은?', answers: ['생활비', '주택마련', '채무상환', '자산증식'] },
]);

const selectedAnswers = ref([]);

const submit = () => {
  // 서버로 선택된 답변을 전송하는 로직 추가
  console.log('선택된 답변:', selectedAnswers.value);
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
