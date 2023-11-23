<template>
  <div>
    <table class="table">
  <thead>
    <tr class="text-center">
      <th scope="col">번호</th>
      <th scope="col">제목</th>
      <th scope="col">작성일자</th>
      <th scope="col">작성자</th>
    </tr>
  </thead>
  <tbody>
    <ArticleListItem 
    v-for="article in store.articles"
    :key="article.id"
    :article="article"
    />
  </tbody>
  </table>
  </div>
</template>

<script setup>
import { useIndexStore } from '@/stores/index'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useIndexStore()

</script>
