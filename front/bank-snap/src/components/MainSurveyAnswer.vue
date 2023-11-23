<!-- MainSurveyAnswer.vue -->
<template>
  <div class="container p-5">
    <div class="text-center">
      <h2 class="text-center">고객님의 저축성향은?</h2>
      <div class="card m-3">
        <div class="card-body p-5">

          <!-- 여기에 선택된 답변에 따른 결과를 표시하는 내용을 추가하세요 -->
          <h5>{{ result[0] }}</h5>
          <h3>{{ result[1] }}</h3>
          <br>
          <hr>
          <br>
          <div v-if="product">
          <h3>이런 상품을 추천합니다!</h3>
            <div v-for="p in product">
              <p class="lead">
                {{ p.name }}
                <a class="btn btn-outline-secondary" :href="p.url">정보 보러가기</a>
              </p>
            </div>
          </div>
        </div>
      </div>
      <RouterLink class="btn btn-secondary" :to="{ name: 'Survey' }">다시하기</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const selectedAnswers = ref([]);
const result = ref([])
const product = ref(null)
onMounted(() => {
  if (route.query.selectedAnswers) {
    selectedAnswers.value = route.query.selectedAnswers
    
    if (selectedAnswers.value <= 25) {
      result.value = ['손실은 절대 참을수 없어! 안전이 보장되어야 도전하는', '안정형']
      product.value = products.value[0]
    }else if (selectedAnswers.value <= 40) {
      result.value = ['안정적으로 수입을 쌓아가는','안정추구형']
      product.value = products.value[1]
    }else if (selectedAnswers.value <= 60) {
      result.value = ['위험을 최소화하면서 꾸준한 성장을 목표로!', '위험중립형']
      product.value = products.value[2]
    }else if (selectedAnswers.value <= 80) {
      result.value = ['고수익을 위해 높은 위험을 감수하는', '적극투자형']
      product.value = products.value[3]
    }else{
      result.value = ['모 아니면 도! 화끈하게 투자하는', '공격투자형']
      product.value = products.value[4]
    }

  }
})

const products = ref([
  [{name: '예금', url: '/deposit'}, {name:'적금', url: '/saving'}],
  [{name: '저축은행 상품', url: 'main'}],
  [{name: '외환 상품', url: '/exchange'}],
  [{name: '현물 상품', url: '/price'}],
  [{name: '주식', url: 'https://finance.naver.com/'}, {name: '선물', url: '/price'}]
])

</script>
  
<style scoped>
/* 필요한 스타일링을 추가하세요 */
</style>
  