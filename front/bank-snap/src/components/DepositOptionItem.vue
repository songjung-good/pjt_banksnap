<template>
    <tr>
      <td>{{ option.intr_rate_type_nm }}</td>
      <td>{{ option.save_trm }}</td>
      <td>{{ option.intr_rate }}</td>
      <td>{{ option.intr_rate2 }}</td>
    </tr>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  option: Object,
})

</script>

<style scoped>

</style>