<template>
        <div class="card">
            <div class="card-header text-center">
                <h5>작성 게시글</h5>
            </div>
            <div class="card-body">
                <p class="card-text text-start">
                    <RouterLink 
                        v-for="article in articles" 
                        :key="article.id"
                        :to="{ name: 'DetailView', params: { id: article.id }}">
                        <p>{{ article.title }}</p>
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
    'articles': Object,
})
const articles = ref(props.articles)
</script>
