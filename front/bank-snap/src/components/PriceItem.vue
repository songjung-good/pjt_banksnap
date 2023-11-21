<template>
  <div>
    <h3>{{ item.name }} 현재 가격</h3>
    <p>{{ item.price }} 원</p>
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