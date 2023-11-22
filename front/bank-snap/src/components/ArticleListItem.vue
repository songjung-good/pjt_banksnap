<template>
  <tr class="text-center">
    <td>{{ article.id }}</td>
    <td class="text-start">
      <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
      {{ article.title }}
      </RouterLink></td>
    <td>{{ createdAt }}</td>
    <td>{{ article.username }}</td>
  </tr>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import moment from 'moment'

const props = defineProps({
  article: Object
})
const createdAt = ref(moment(props.article.created_at).format('YYYY-MM-DD'))
</script>

<style scoped>
a {
    text-decoration: none;
    color: black;
}
</style>