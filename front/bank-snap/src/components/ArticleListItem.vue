<template>
  <div>
    <span>{{ article.id }} | </span>
    <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
      {{ article.title }}
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>
