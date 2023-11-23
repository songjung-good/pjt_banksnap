<!-- MainSurveyAnswer.vue -->
<template>
  <div class="container p-5">
    <div class="text-center">
      <h2 class="text-center">고객님의 투자성향은?</h2>
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
            <!-- <div v-for="p in product"> -->
              <!-- <div class="container">
                <div class="row "> -->

                  <div class="row">
                    <div class="col d-flex justify-content-center p-5" v-for="p in product" >
                      <div class="card h-100" style="width: 18rem;">
                        <img :src="p.img" class="card-img-top" alt="...">
                        <div class="card-body">
                          <h5 class="card-title">{{ p.name }}</h5>
                          <p class="card-text">{{ p.content }}</p>
                      <a class="btn btn-outline-secondary" :href="p.url">{{ p.name }}정보 보러가기</a>
                    </div>
                  <!-- </div>
                  </div> -->
                  </div>
                </div>
              </div>

              <!-- <p class="lead">
                {{ p.name }}
                <a class="btn btn-outline-secondary" :href="p.url">정보 보러가기</a>
              </p> -->



            <!-- </div> -->
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
  [
    {name: '예금', url: '/deposit', img: 'src/assets/deposit_2.jpg', content: '이자가 낮은 대신 입금/출금/송금이 자유로운 상품'},
    {name:'적금', url: '/saving', img: 'src/assets/deposit.jpg', content: '자금을 일정 기간동안 약정된 금리로 예치해 두는 상품'}
  ],
  [
    {name: '저축은행 상품', url: '/savingBank', img: 'src/assets/deposit.jpg', content: '일반 예/적금 보다 조금 더 높은 수익을 기대할 수 있는 상품'}
  ],
  [
    {name: '외환 상품', url: '/exchange', img: 'src/assets/money.png', content: '다른 국가의 통화나 외국 환율을 기반으로 하는 투자 상품'}
  ],
  [
    {name: '현물 상품', url: '/price', img: 'src/assets/gold.jpg', content: '물리적으로 보유하는 금, 은과 같은 상품에 투자하여 시장 가격 변동으로 이익을 얻을 수 있는 상품'}
  ],
  [
    {name: '주식', url: 'https://finance.naver.com/', img: 'src/assets/stock.jpg', content: '위험을 감내하더라도 높은 수준의 투자 수익을 얻을 수 있는 상품'}, 
    {name: '선물', url: '/price', img: 'src/assets/coffee.jpg', content: ' 미래의 특정 시점에 특정 가격으로 상품을 매매하는 투자'}
  ]
])

</script>
  
<style scoped>
img {
  height: 250px;
  object-fit: cover;  
}
</style>
  