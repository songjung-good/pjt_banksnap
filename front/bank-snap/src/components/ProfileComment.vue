<template>
        <div class="card">
            <div class="card-header text-center">
                <h5>작성 댓글</h5>
            </div>
            <div class="card-body">
                <p class="card-text text-start">
                    <RouterLink 
                        v-for="comment in comments" 
                        :key="comment.id"
                        :to="{ name: 'DetailView', params: { id: comment.article }}">
                        <p>{{ comment.content }}</p>
                    </RouterLink>
                </p>
            </div>
            
        </div>
        
</template>

<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/index'

const store = useIndexStore()

const props = defineProps({
    'comments': Object,
})
const comments = ref(props.comments)
</script>
