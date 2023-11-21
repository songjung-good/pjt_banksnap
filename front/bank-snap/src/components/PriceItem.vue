<template>
  <div>
    <h3>실시간 {{ item.name }} 시세</h3>
    <h5>{{ item.price }}</h5>
    <p>{{ item.before_price }}</p>
    <img :src="item.graph" alt="">
    <hr>
  </div>
</template>

<script setup>
const props = defineProps({
  item: Object,
})
console.log(props.item)
</script>

<style scoped>

</style>