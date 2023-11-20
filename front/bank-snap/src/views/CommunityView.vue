
<template>

    <div>
        <h1>Community</h1>
        <span v-if="isLogin">
            <RouterLink :to="{ name: 'CreateArticleView', query:{ type: 'create' }}">글 쓰기</RouterLink>
        </span>
        <ArticleList />
    </div>
    

</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()
const isLogin = store.isLogin
onMounted(() => {
    store.getArticles()
})

</script>

<style scoped>

</style>
