<template>
 <div>
  <div class="modal modal-dialog-centered modal-dialog-scrollable" tabindex="-1" role="dialog" id="modalChoice">
   <div class="modal-content">
    <div class="modal-header">
     <h5 class="modal-title">설문조사</h5>
     <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
    </div>
    <div class="modal-body">
     <div v-for="(question, index) in questions" :key="index">
      <p style="width: calc(100% - 20px); height: 200px;">{{ question }}</p>
      </div>
    </div>
    <div class="modal-footer">
     <button type="button" class="btn btn-primary" @click="submit">제출</button>
    </div>
   </div>
  </div>
 </div>
</template>
    
  <script setup>
  import { ref } from 'vue';
  
  const questions = ref([
    '당신의 성별은?',
    '당신의 나이는?',
    '당신의 관심사는?',
    '당신의 취미는?',
    '당신의 직업은?',
  ]);
  
  const answers = ref([]);
  
  const nextQuestion = () => {
    answers.push(questions.value[questions.value.length - 1] === '남자' ? 1 : 0);
    questions.value.pop();
  };
  
  const submit = () => {
    // 답변 저장
    // 모달 창 닫기
    document.getElementById('modalChoice').style.display = 'none';
  };
  </script>
  
  <style scoped>
  /* Add your custom styles here */
  @import '@/assets/css/bootstrap.min.css';
  .modal {
  width: 1280px;
}
  </style>
  