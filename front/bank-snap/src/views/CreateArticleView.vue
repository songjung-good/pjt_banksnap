<template>
  <div>
    <ArticleWrite
      :type="type"
      :id="articleId"
      />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useCounterStore } from '@/stores/counter'
import { useRouter, useRoute } from 'vue-router'
import ArticleWrite from '@/components/ArticleWrite.vue'

const route = useRoute()
const type = ref(route.query.type)
const articleId = ref(route.query.id)
console.log(articleId)
</script>

<style scoped>

</style>