
<template>

    <div>
        <h1>Community</h1>
        
        <ArticleList />
        <div class="text-end" v-if="isLogin">
            <RouterLink class="btn btn-outline-secondary px-4 m-1" :to="{ name: 'CreateArticleView', query:{ type: 'create' }}">글 쓰기</RouterLink>
        </div>
    </div>
    

</template>

<script setup>
import { onMounted } from 'vue'
import { useIndexStore } from '@/stores/index'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useIndexStore()
const isLogin = store.isLogin
onMounted(() => {
    store.getArticles()
})

</script>

<style scoped>

</style>
