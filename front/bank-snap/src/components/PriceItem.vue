<template>
  <div class="card p-5">
    <div class="card-body d-flex flex-wrap">
      <div class="p-2 flex-grow-1">

        <h3>실시간 {{ item.name }} 시세</h3>
        <h5>{{ item.price }}</h5>
        <p>{{ item.before_price }}</p>
      </div>
      <div class="p-2 flex-fill">

        <img :src="item.graph" alt="graph">
      </div>
      
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  item: Object,
})
</script>

<style scoped>

</style>