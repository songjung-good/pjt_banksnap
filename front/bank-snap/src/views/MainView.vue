
<script setup>
// import { ref, computed, onMounted } from 'vue'
// import { useRouter } from 'vue-router';
// import axios from 'axios'

// const router = useRouter()
// const specialImages = ref([])

// const clientId = '2KPHeGdbQvNEOM1Aly4d'
// const clientSecret = 'w194LdQlzo'
// const searchQuery = '금융'
// const displayCount = 10
// const startPage = 1
// const sortOption = 'sim'
// const searchURL = `https://openapi.naver.com/v1/search/news.json?query=${searchQuery}&display=${displayCount}&start=${startPage}&sort=${sortOption}`

// onMounted(() => {
//   axios.get(searchURL, {
//     headers: {
//       'X-Naver-Client-Id': clientId,
//       'X-Naver-Client-Secret': clientSecret
//     }
//   })
//     .then((response) => {
//       news.value = response.data.items
//     })
//     .catch((error) => {
//       console.error(error)
//     })
// })

// axios.get(searchURL)
//     .then((response) => {
//         // console.log(response.data)
//         news.value = response.data
//     }).catch((error) => {
//         console.error(error)
//     })

//     // 삼항연산자는 가독성을 위함 / 없어도 boolean값 반환
// const imgIsEmpty = computed(() => {
//     return specialImages.value.length > 0 ? true : false
// })


</script>

<template>
  <div>
    <h1>메인 페이지</h1>

  </div>
</template>

<style scoped>

</style>

<style>

.product-card{
    border: 1px solid black;
    width: 205px;
}

.product-card IMG{
    width: 200px;
    height: 200px;
    object-fit: fill;
}

.product-list {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}
</style>
