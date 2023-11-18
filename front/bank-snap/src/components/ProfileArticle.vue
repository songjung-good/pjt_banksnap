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
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const props = defineProps({
    'articles': Object,
})
console.log(props.articles)
const articles = ref(props.articles)
console.log(articles.value)
</script>
