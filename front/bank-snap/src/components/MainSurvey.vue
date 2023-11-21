<!-- SurveyModal.vue -->
<template>
    <div class="modal fade" id="surveyModal" tabindex="-1" aria-labelledby="surveyModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="surveyModalLabel">Survey</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div v-if="currentQuestionIndex < questions.length">
              <h2>{{ questions[currentQuestionIndex].question }}</h2>
              <div v-for="(option, index) in questions[currentQuestionIndex].options" :key="index">
                <input type="radio" :id="`option-${index}`" :value="index" v-model="selectedOption" />
                <label :for="`option-${index}`">{{ option }}</label>
              </div>
            </div>
            <div v-else>
              <h2>Survey Result</h2>
              <p>You submitted: {{ selectedAnswers }}</p>
              <p>Explanation: {{ questions[currentQuestionIndex - 1].explanation }}</p>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" @click="nextQuestion">Next</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  const questions = [
    {
      question: "Question 1",
      options: ["Option A", "Option B", "Option C"],
      explanation: "Explanation for Question 1",
    },
    {
      question: "Question 2",
      options: ["Option X", "Option Y", "Option Z"],
      explanation: "Explanation for Question 2",
    },
    {
      question: "Question 3",
      options: ["Option P", "Option Q", "Option R"],
      explanation: "Explanation for Question 3",
    },
  ];
  
  let currentQuestionIndex = 0;
  let selectedOption = null;
  const selectedAnswers = [];
  
  const nextQuestion = () => {
    if (selectedOption !== null) {
      selectedAnswers.push(questions[currentQuestionIndex].options[selectedOption]);
      currentQuestionIndex++;
      selectedOption = null;
    }
  };
  </script>
  
  <style scoped>
  /* Add your custom styles here */
  @import '@/assets/css/bootstrap.min.css';
  </style>