<template>
    <div>
        <h3>작성 게시글</h3>
        <RouterLink 
            v-for="article in articles" 
            :key="article.id"
            :to="{ name: 'DetailView', params: { id: article.id }}">
            <p>{{ article.title }}</p>
        </RouterLink>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/index'

const store = useIndexStore()

const props = defineProps({
    'articles': Object,
})
const articles = ref(props.articles)
</script>
