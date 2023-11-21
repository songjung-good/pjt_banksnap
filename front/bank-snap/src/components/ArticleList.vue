<template>
  <div>
    <h3>Article List</h3>
    <table class="table">
  <thead>
    <tr>
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
