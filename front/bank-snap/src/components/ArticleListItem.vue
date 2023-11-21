<template>
  <tr>
    <th>{{ article.id }}</th>
    <td>
      <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
      {{ article.title }}
      </RouterLink></td>
    <td>{{ article.created_at }}</td>
    <td>{{ article.user }}</td>
    
  </tr>
  <!-- 작성일자 / 작성자 serializer로 받아와야 함 -->
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>
