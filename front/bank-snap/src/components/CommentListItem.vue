<template>
  <div>
    <p>{{ comment.user }} : {{ comment.content }}</p>
  </div>
</template>

<script setup>

const props = defineProps({
  comment: Object,
})
</script>

<style scoped>

</style>