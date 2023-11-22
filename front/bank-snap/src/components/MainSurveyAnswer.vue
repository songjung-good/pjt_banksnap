<!-- MainSurveyAnswer.vue -->
<template>
    <div class="container">
      <h2 class="text-center">선택된 답변 결과</h2>
      <div>
        <!-- 여기에 선택된 답변에 따른 결과를 표시하는 내용을 추가하세요 -->
        <p>선택된 답변: {{ selectedAnswers.join(', ') }}</p>
      </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const selectedAnswers = ref([]);
onMounted(() => {
  // 페이지가 로드될 때 라우터에서 전달된 params를 확인하여 selectedAnswers 업데이트
  const route = useRoute();
  if (route.query.selectedAnswers) {
    selectedAnswers.value = route.query.selectedAnswers;
    console.log(selectedAnswers.value)
  }
});
</script>
  
<style scoped>
/* 필요한 스타일링을 추가하세요 */
</style>
  