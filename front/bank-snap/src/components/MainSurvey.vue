<!-- MainSurvey.vue -->
<template>
  <div class="container p-3">
    <h2 class="text-center p-3">당신의 투자성향은?</h2>
    <div class="row">
      <div class="col-md-12">
        <div class="card">
          <div class="card-body">
            <div v-for="(question, index) in questions" :key="index">
              <h5 class="card-title">{{ question.title }}</h5>
              <div class="form-check" v-for="(answer, answerIndex) in question.answers" :key="answerIndex">
                <input class="form-check-input" type="radio" :id="`question-${index}-answer-${answerIndex}`" v-model="selectedAnswers[index]" :value="((answerIndex+1) * question.score)">
                <label class="form-check-label" :for="`question-${index}-answer-${answerIndex}`">{{ answer }}</label>
              </div>
              <br>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12 text-center">
        <button type="button" class="btn btn-secondary" @click="submit">제출</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const questions = ref([
  { title: '고객님의 투자 자금의 투자 예정 기간은 얼마나 되시나요?', 
    answers: ['6개월 이내', '6개월 ~ 1년', '1년 ~ 2년', '2년 ~ 3년', '3년 이상'],
    score: 4
},
  { title: '평소 투자경험과 가장 가까운 것을 고르세요.', 
  answers: ['예적금/국채/지방채/보증채/MMF/CMA', '금융채/회사채(신용도 상)/채권형 펀드/ELS(원금보존추구형)', '회사채(신용도 중)/ELS(원금 일부 보장)/혼합형펀드', '회사채(신용도 하)/주식/ELS(원금 미보장)/주식형펀드(시장수익률 수준의 수익)', 'ELW/선물옵션/주식형펀드(시장수익률 이상 수익)/파생상품 펀드/주식신용거래'],
  score: 4

},
  { title: '금융상품 투자에 대한 고객님의 지식수준은 어느 정도입니까?', 
  answers: ['투자의사결정을 스스로 내려본 경험이 없다', '주식과 채권의 차이를 구별할 수 있다', '투자할 수 있는 대부분의 금융차이를 구분할 수 있다.', '투자대상 상품의 차이를 이해할 수 있다'],
  score: 5,
},
  { title: '현재 투자하고자 하는 자금은 전체 금융자산 중 어느 정도 비중 차지하나요?', 
  answers: ['40%이상', '30% ~ 40%', '20% ~ 30%', '10% ~ 20%', '10% 미만'],
  score: 4
},

  { title: '고객님께서 금융상품 투자 시 감내할 수 있는 손실은 어느 정도 되시나요?', 
  answers: ['손실을 원하지 않음(무조건 원금 보전)', '원금의 30%까지 손실은 감내할 수 있음', '원금의 50%까지 손실은 감내할 수 있음', '원금 100% 손실까지 감내할 수 있음'],
  score: 5
},
//   { title: '고객님의 수입은 어느정도인가요?', 
// answers: ['', '', ''] 
// },
//   { title: '고객님의 연령대는 어떻게 되나요?', 
// answers: ['19세 이하', '20 ~ 40세', '41 ~ 50세', '51 ~ 60세', '61세 이상'] 
// },
]);

const selectedAnswers = ref([NaN, NaN, NaN, NaN, NaN]);

const submit = () => {
  // 서버로 선택된 답변을 전송하는 로직 추가

  let sum = 0
  for (let i=0; i<selectedAnswers.value.length; i++){
    sum += selectedAnswers.value[i]
  }
  if (isNaN(sum)){
    console.log(sum)
    alert('모두 선택해 주세요.')
  }else{
    router.push({
      name: 'SurveyAnswer',
      query: { selectedAnswers: sum
      },
    });
  }
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
