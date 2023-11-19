<template>
    <div>
        <h3>작성 댓글</h3>
        <RouterLink 
            v-for="comment in comments" 
            :key="comment.id"
            :to="{ name: 'DetailView', params: { id: comment.article.id }}">
            <p>{{ comment.content }}</p>
        </RouterLink>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const props = defineProps({
    'comments': Object,
})
const comments = ref(props.comments)
</script>
