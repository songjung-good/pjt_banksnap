
<script setup>
import MainNavbar from '@/components/MainNavbar.vue';
import MainSurvey from '@/components/MainSurvey.vue';
import { ref } from 'vue';

const isSurveyModalOpen = ref(false);

const openSurveyModal = () => {
  isSurveyModalOpen.value = true;
};

const closeSurveyModal = () => {
  isSurveyModalOpen.value = false;
};
</script>

<template>
  <main class="center">
    <MainNavbar />
    <router-view />
    <MainSurvey v-if="isSurveyModalOpen" @close="closeSurveyModal" />
  </main>

  <div>
    <!-- 버튼 클릭 시 모달 띄우기 -->
    <button type="button" class="btn btn-primary" @click="openSurveyModal">Start Survey</button>
    <!-- 설문조사 모달 -->
  </div>
</template>

<style>
/* Bootstrap styles */
@import '@/assets/css/bootstrap.min.css';

.center {
    box-sizing: border-box;
    max-width: 1280px;
    margin: 0 auto;
  }
  @media screen {
  .container {
    max-width: 1280px;
    margin: 0 auto;
  }
}
</style>
